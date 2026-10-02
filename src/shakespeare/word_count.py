import json
import re
from pathlib import Path


def count_words_in_file(file_path: Path) -> dict[str, int]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path}")

    word_counts: dict[str, int] = {}
    with path.open("r", encoding="utf-8") as file:
        for line in file:
            # strip punctuation but keep apostrophes so contractions stay intact
            for word in re.findall(r"[a-z']+", line.lower()):
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1

    return dict(sorted(word_counts.items(), key=lambda kv: kv[1], reverse=True))


def write_word_counts(word_counts: dict[str, int], output_path: Path) -> None:
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(word_counts, f, indent=4)
