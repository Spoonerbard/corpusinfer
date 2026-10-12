import json
import re
from pathlib import Path

import pytest

from shakespeare.word_count import count_words_in_file, save_word_counts



    
# Counts words correctly
def test_single_word(tmp_path):
    file = tmp_path / "single.txt"
    file.write_text("hello")

    result = count_words_in_file(file)

    assert result == {"hello": 1}

# Counts repeated words correctly
def test_repeated_words(tmp_path):
    file = tmp_path / "repeated.txt"
    file.write_text("hello hello hello")

    result = count_words_in_file(file)

    assert result == {"hello": 3}

# Handles empty files
def test_empty_file_returns_empty_dict(tmp_path):
    file = tmp_path / "empty.txt"
    file.write_text("")

    result = count_words_in_file(file)

    assert result == {}

# Raises an error for missing files
def test_missing_file_raises_error(tmp_path):
    file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError):
        count_words_in_file(file)
        
# Produces output sorted by descending frequency

def test_output_sorted_by_descending_frequency(tmp_path):
    file = tmp_path / "frequency.txt"
    file.write_text("apple banana apple cherry banana apple")

    result = count_words_in_file(file)

    sorted_result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
    assert sorted_result == {"apple": 3, "banana": 2, "cherry": 1}

# Writes valid JSON
def test_writes_valid_json(tmp_path):
    import json

    file = tmp_path / "json.txt"
    file.write_text("apple banana apple")

    result = count_words_in_file(file)

    json_str = json.dumps(result)
    parsed = json.loads(json_str)
    assert parsed == result

# save_word_counts writes the data to a timestamped file and returns its path
def test_save_word_counts_writes_json_and_returns_path(tmp_path):
    word_counts = {"apple": 3, "banana": 2, "cherry": 1}

    output_path = save_word_counts(word_counts, tmp_path)

    assert output_path.exists()
    assert re.fullmatch(r"shakespeare_word_counts_\d{8}_\d{6}\.json", output_path.name)
    assert json.loads(output_path.read_text(encoding="utf-8")) == word_counts

# save_word_counts creates the output directory if it does not exist
def test_save_word_counts_creates_output_dir(tmp_path):
    output_dir = tmp_path / "nested" / "output"

    output_path = save_word_counts({"hello": 1}, output_dir)

    assert output_dir.exists()
    assert output_path.parent == output_dir