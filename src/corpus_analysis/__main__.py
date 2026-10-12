import argparse
from collections.abc import Sequence
from pathlib import Path

from corpus_analysis.word_count import count_words_in_file, save_word_counts

# repo root is two levels up from this file (src/corpus_analysis/__main__.py)
REPO_ROOT = Path(__file__).resolve().parents[2]


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="corpus analysis data processing")
    parser.add_argument(
        "--input",
        type=Path,
        default=REPO_ROOT / "data/input" / "complete_shakespeare.txt",
        help="path to the input text file",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "data" / "output",
        help="directory to write the word counts JSON to",
    )
    args = parser.parse_args(argv)

    if not args.input.exists():
        parser.error(f"Input file not found: {args.input}")

    word_counts = count_words_in_file(args.input)
    output_path = save_word_counts(word_counts, args.output_dir)
    print("Word counts have been written to:", output_path)


if __name__ == "__main__":
    main()
