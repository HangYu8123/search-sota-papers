#!/usr/bin/env python3
"""Install or package Find SOTA Papers for Claude and ChatGPT/Codex.

The source skill follows the open Agent Skills format. Claude consumes the skill
folder directly (or as a ZIP), Codex can discover the same folder from
``.agents/skills``, and ChatGPT installs the skill through a plugin marketplace.

Examples:
    python install.py --target all
    python install.py --target claude-code --scope project
    python install.py --target codex --scope user
    python install.py --target chatgpt
    python install.py --target packages
    python install.py --dry-run
"""

import argparse
import json
import os
import shutil
import sys
import tempfile
import zipfile


SKILL_NAME = "find-sota-papers"
PLUGIN_NAME = SKILL_NAME
HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_SRC = os.path.join(HERE, "skills", SKILL_NAME)
MANIFEST_SRC = os.path.join(HERE, ".codex-plugin", "plugin.json")
DIST_DIR = os.path.join(HERE, "dist")

# target -> (label, user-scope path parts, project-scope path parts)
SKILL_TARGETS = {
    "claude-code": (
        "Claude Code",
        ("~", ".claude", "skills"),
        (".claude", "skills"),
    ),
    "codex": (
        "Codex",
        ("~", ".agents", "skills"),
        (".agents", "skills"),
    ),
}


def validate_sources():
    required = [os.path.join(SKILL_SRC, "SKILL.md"), MANIFEST_SRC]
    missing = [path for path in required if not os.path.isfile(path)]
    if missing:
        sys.exit("error: missing required source file(s):\n  " + "\n  ".join(missing))


def resolve_skill_dest(target, scope, project_dir):
    _, user_parts, project_parts = SKILL_TARGETS[target]
    if scope == "user":
        base = os.path.expanduser(user_parts[0])
        return os.path.join(base, *user_parts[1:], SKILL_NAME)
    return os.path.join(os.path.abspath(project_dir), *project_parts, SKILL_NAME)


def replace_tree(src, dest, dry_run):
    """Replace one exact destination directory with a fresh source copy."""
    if dry_run:
        print("    would install -> {}".format(dest))
        return
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.isdir(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest)
    print("    installed -> {}".format(dest))


def plugin_files():
    """Yield (absolute source, plugin-relative path) pairs."""
    yield MANIFEST_SRC, os.path.join(".codex-plugin", "plugin.json")
    for root, dirs, files in os.walk(SKILL_SRC):
        dirs.sort()
        files.sort()
        for filename in files:
            source = os.path.join(root, filename)
            skill_relative = os.path.relpath(source, SKILL_SRC)
            relative = os.path.join("skills", SKILL_NAME, skill_relative)
            yield source, relative


def install_chatgpt_plugin(dry_run):
    """Install the plugin and merge it into the personal ChatGPT marketplace."""
    plugin_dest = os.path.join(os.path.expanduser("~"), "plugins", PLUGIN_NAME)
    marketplace_path = os.path.join(
        os.path.expanduser("~"), ".agents", "plugins", "marketplace.json"
    )

    if dry_run:
        print("    would install plugin -> {}".format(plugin_dest))
        print("    would update marketplace -> {}".format(marketplace_path))
        return

    parent = os.path.dirname(plugin_dest)
    os.makedirs(parent, exist_ok=True)
    staged = tempfile.mkdtemp(prefix=PLUGIN_NAME + "-", dir=parent)
    try:
        for source, relative in plugin_files():
            destination = os.path.join(staged, relative)
            os.makedirs(os.path.dirname(destination), exist_ok=True)
            shutil.copy2(source, destination)
        if os.path.isdir(plugin_dest):
            shutil.rmtree(plugin_dest)
        os.replace(staged, plugin_dest)
        staged = None
    finally:
        if staged and os.path.isdir(staged):
            shutil.rmtree(staged)

    if os.path.exists(marketplace_path):
        try:
            with open(marketplace_path, "r", encoding="utf-8") as handle:
                marketplace = json.load(handle)
        except (OSError, ValueError) as exc:
            sys.exit("error: cannot safely update {}: {}".format(marketplace_path, exc))
        if not isinstance(marketplace, dict) or not isinstance(
            marketplace.get("plugins"), list
        ):
            sys.exit("error: {} is not a valid plugin marketplace".format(marketplace_path))
    else:
        marketplace = {
            "name": "personal",
            "interface": {"displayName": "Personal"},
            "plugins": [],
        }

    entry = {
        "name": PLUGIN_NAME,
        "source": {"source": "local", "path": "./plugins/{}".format(PLUGIN_NAME)},
        "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
        "category": "Productivity",
    }
    for index, existing in enumerate(marketplace["plugins"]):
        if isinstance(existing, dict) and existing.get("name") == PLUGIN_NAME:
            marketplace["plugins"][index] = entry
            break
    else:
        marketplace["plugins"].append(entry)

    os.makedirs(os.path.dirname(marketplace_path), exist_ok=True)
    fd, temporary_path = tempfile.mkstemp(
        prefix="marketplace-", suffix=".json", dir=os.path.dirname(marketplace_path)
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(marketplace, handle, indent=2)
            handle.write("\n")
        os.replace(temporary_path, marketplace_path)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)

    print("    installed plugin -> {}".format(plugin_dest))
    print("    updated marketplace -> {}".format(marketplace_path))


def write_skill_zip(output_path):
    """Build Claude's upload ZIP with the skill folder at the archive root."""
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        for root, dirs, files in os.walk(SKILL_SRC):
            dirs.sort()
            files.sort()
            for filename in files:
                source = os.path.join(root, filename)
                relative = os.path.relpath(source, os.path.dirname(SKILL_SRC))
                archive.write(source, relative.replace(os.sep, "/"))


def marketplace_document():
    return {
        "name": "find-sota-papers",
        "interface": {"displayName": "Find SOTA Papers"},
        "plugins": [
            {
                "name": PLUGIN_NAME,
                "source": {
                    "source": "local",
                    "path": "./plugins/{}".format(PLUGIN_NAME),
                },
                "policy": {
                    "installation": "AVAILABLE",
                    "authentication": "ON_INSTALL",
                },
                "category": "Productivity",
            }
        ],
    }


def write_chatgpt_zip(output_path):
    """Build a self-contained marketplace ZIP for ChatGPT/Codex."""
    archive_root = "find-sota-papers-chatgpt"
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as archive:
        marketplace_name = archive_root + "/.agents/plugins/marketplace.json"
        marketplace_json = json.dumps(marketplace_document(), indent=2) + "\n"
        archive.writestr(marketplace_name, marketplace_json)
        plugin_root = archive_root + "/plugins/" + PLUGIN_NAME
        for source, relative in plugin_files():
            archive_name = plugin_root + "/" + relative.replace(os.sep, "/")
            archive.write(source, archive_name)


def build_packages(kind, dry_run):
    outputs = []
    if kind in ("claude", "both"):
        outputs.append(("Claude skill", os.path.join(DIST_DIR, SKILL_NAME + "-claude.zip"), write_skill_zip))
    if kind in ("chatgpt", "both"):
        outputs.append(("ChatGPT plugin marketplace", os.path.join(DIST_DIR, SKILL_NAME + "-chatgpt.zip"), write_chatgpt_zip))

    for label, output_path, builder in outputs:
        if dry_run:
            print("    would build {} -> {}".format(label, output_path))
            continue
        os.makedirs(DIST_DIR, exist_ok=True)
        builder(output_path)
        print("    built {} -> {}".format(label, output_path))


def main():
    parser = argparse.ArgumentParser(
        description="Install Find SOTA Papers for Claude and ChatGPT/Codex."
    )
    parser.add_argument(
        "--target",
        choices=[
            "claude-code",
            "codex",
            "chatgpt",
            "claude-zip",
            "chatgpt-zip",
            "packages",
            "zip",
            "all",
        ],
        default="all",
        help=(
            "Installation surface. 'zip' is a backward-compatible alias for "
            "'claude-zip'; 'packages' builds both distributable ZIPs."
        ),
    )
    parser.add_argument(
        "--scope",
        choices=["user", "project"],
        default="user",
        help="Scope for Claude Code or Codex filesystem installation.",
    )
    parser.add_argument(
        "--project-dir",
        default=os.getcwd(),
        help="Project root for --scope project (default: current directory).",
    )
    parser.add_argument(
        "--legacy-codex",
        action="store_true",
        help="Also install the bare skill to ~/.codex/skills for older Codex builds.",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Show actions without changing files."
    )
    args = parser.parse_args()

    validate_sources()
    target = "claude-zip" if args.target == "zip" else args.target
    print("Installing '{}'{}\n".format(SKILL_NAME, " (dry run)" if args.dry_run else ""))

    filesystem_targets = []
    if target == "all":
        filesystem_targets = ["claude-code", "codex"]
    elif target in SKILL_TARGETS:
        filesystem_targets = [target]

    for skill_target in filesystem_targets:
        print("  {} [{} scope]:".format(SKILL_TARGETS[skill_target][0], args.scope))
        destination = resolve_skill_dest(skill_target, args.scope, args.project_dir)
        replace_tree(SKILL_SRC, destination, args.dry_run)
        print()

    if target in ("chatgpt", "all"):
        print("  ChatGPT plugin [personal marketplace]:")
        install_chatgpt_plugin(args.dry_run)
        print()

    package_kind = None
    if target == "claude-zip":
        package_kind = "claude"
    elif target == "chatgpt-zip":
        package_kind = "chatgpt"
    elif target in ("packages", "all"):
        package_kind = "both"
    if package_kind:
        print("  Distributable packages:")
        build_packages(package_kind, args.dry_run)
        print()

    if args.legacy_codex:
        print("  Codex legacy path:")
        legacy = os.path.join(os.path.expanduser("~"), ".codex", "skills", SKILL_NAME)
        replace_tree(SKILL_SRC, legacy, args.dry_run)
        print()

    print("Done. Restart the relevant app or begin a new agent session.")


if __name__ == "__main__":
    main()
