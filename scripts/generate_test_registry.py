#!/usr/bin/env python3
"""Generate TEST_REGISTRY.md from the tests/ directory."""

import ast
import os
from collections import OrderedDict

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTS_DIR = os.path.join(REPO_ROOT, "tests")
OUTPUT_PATH = os.path.join(REPO_ROOT, "TEST_REGISTRY.md")


def collect_tests():
    results = []
    for root, dirs, files in os.walk(TESTS_DIR):
        dirs.sort()
        for f in sorted(files):
            if not (f.startswith("test_") and f.endswith(".py")):
                continue
            path = os.path.join(root, f)
            rel = os.path.relpath(path, REPO_ROOT)
            with open(path) as fh:
                tree = ast.parse(fh.read(), path)
            classes = []
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef):
                    methods = [
                        n.name
                        for n in node.body
                        if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))
                        and n.name.startswith("test_")
                    ]
                    if methods:
                        classes.append((node.name, methods))
            if classes:
                file_total = sum(len(mlist) for _, mlist in classes)
                results.append((rel, classes, file_total))
    return results


def group_by_directory(results):
    groups = OrderedDict()
    for path, classes, ft in results:
        parts = path.split(os.sep)
        if len(parts) == 2:
            group = "(root)"
        else:
            group = os.sep.join(parts[1:-1])
        groups.setdefault(group, []).append((path, classes, ft))
    return groups


def build_tree(results):
    tree = {}
    for path, _, ft in results:
        parts = path.split(os.sep)
        node = tree
        for part in parts[:-1]:
            node = node.setdefault(part, {})
        node[parts[-1]] = ft

    lines = []

    def walk(node, prefix=""):
        entries = sorted(node.keys(), key=lambda k: (not isinstance(node[k], dict), k))
        for i, name in enumerate(entries):
            is_last = i == len(entries) - 1
            connector = "└── " if is_last else "├── "
            child = node[name]
            if isinstance(child, dict):
                lines.append(f"{prefix}{connector}{name}/")
                extension = "    " if is_last else "│   "
                walk(child, prefix + extension)
            else:
                lines.append(f"{prefix}{connector}{name} ({child} tests)")

    walk(tree)
    return lines


def render(results, groups):
    total_files = len(results)
    total_classes = sum(len(classes) for _, classes, _ in results)
    total_tests = sum(ft for _, _, ft in results)

    lines = []
    lines.append("# Test Registry")
    lines.append("")
    lines.append(
        "> Centralized index of all pydepgate tests. Auto-generated; do not edit by hand."
    )
    lines.append("> Run `python scripts/generate_test_registry.py` to regenerate.")
    lines.append("")
    lines.append(
        f"**{total_files}** test files | **{total_classes}** test classes | **{total_tests}** test cases"
    )
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Tree")
    lines.append("")
    lines.append("```")
    lines.extend(build_tree(results))
    lines.append("```")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Contents")
    lines.append("")
    for g in groups:
        label = g if g != "(root)" else "tests (root)"
        anchor = (
            label.replace("/", "")
            .replace("(", "")
            .replace(")", "")
            .replace(" ", "-")
            .lower()
        )
        gt = sum(ft for _, _, ft in groups[g])
        lines.append(f"- [{label}](#{anchor}) ({gt} tests)")
    lines.append("")
    lines.append("---")
    lines.append("")

    for g, items in groups.items():
        label = g if g != "(root)" else "tests (root)"
        gt = sum(ft for _, _, ft in items)
        lines.append(f"## {label}")
        lines.append("")
        lines.append(f"*{len(items)} files, {gt} tests*")
        lines.append("")

        for path, classes, ft in items:
            lines.append(f"### `{path}` ({ft} tests)")
            lines.append("")
            for cls_name, methods in classes:
                lines.append("<details>")
                lines.append(
                    f"<summary><code>{cls_name}</code> ({len(methods)} tests)</summary>"
                )
                lines.append("")
                for method_name in methods:
                    lines.append(f"- `{method_name}`")
                lines.append("")
                lines.append("</details>")
                lines.append("")

        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def main():
    results = collect_tests()
    groups = group_by_directory(results)
    content = render(results, groups)
    with open(OUTPUT_PATH, "w") as f:
        f.write(content)
    total_tests = sum(ft for _, _, ft in results)
    print(
        f"TEST_REGISTRY.md generated: {len(results)} files, {total_tests} tests"
    )


if __name__ == "__main__":
    main()
