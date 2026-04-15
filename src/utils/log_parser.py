from __future__ import annotations


def parse_statistics(log_content: str) -> tuple[int, list[tuple[str, int]]]:
    counts: dict[str, int] = {}

    for line in log_content.strip().splitlines():
        parts = line.split("] ", maxsplit=1)
        if len(parts) == 2:
            key = parts[1].strip()
            counts[key] = counts.get(key, 0) + 1

    total = sum(counts.values())
    sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)[:100]

    return total, sorted_counts