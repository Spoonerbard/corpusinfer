import json
import re
from datetime import datetime
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


def save_word_counts(word_counts: dict[str, int], output_dir: Path) -> Path:
    """Save word counts to JSON using a filename that includes the date/time it was run.

    Args:
        word_counts: Mapping of word to its count.
        output_dir: Directory to write the JSON file into (created if missing).

    Returns:
        Path to the JSON file that was written.
    """
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = output_dir / f"shakespeare_word_counts_{timestamp}.json"

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(word_counts, file, indent=4)

    return output_path
