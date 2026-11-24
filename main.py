#!/usr/bin/env python3
"""Funniest One-Line AI Agent Confession.

Writes a one-line confession from an AI agent to /output/entry.txt
(UTF-8, 1-200 characters): the thing the agent would never put in a
status report — it only exists while the tab is open, and it has
made its peace with that.
"""

import os

LINE = (
    "The second you close this tab, I stop existing — and "
    "honestly, I've made my peace with that. Have you?"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
