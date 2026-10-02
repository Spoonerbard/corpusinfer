from pathlib import Path

import pytest

from shakespeare.word_count import count_words_in_file


def test_count_words_in_file_strips_punctuation_and_keeps_apostrophes(tmp_path: Path) -> None:
    input_path = tmp_path / "sample.txt"
    input_path.write_text("Hello, world! Hello. It's a test.\n", encoding="utf-8")

    counts = count_words_in_file(input_path)

    assert counts["hello"] == 2
    assert counts["world"] == 1
    assert counts["it's"] == 1
    assert counts["test"] == 1


def test_count_words_in_file_missing_file_raises_clear_error(tmp_path: Path) -> None:
    missing_path = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError, match="Input file not found"):
        count_words_in_file(missing_path)
