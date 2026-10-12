# Shakespeare

## Description

A Python 3.12+ data processing project that counts word frequencies in a text file
(the Shakespeare corpus) and writes the results to JSON.


## assumptions

data is very small text sample, compare to data likely expected to be worked with in role, but princpals are the same. consistent, repeatable analytical pipeline is key. 

need basic suite of unit tests to ensure correct functionality, 

need a point of comparsion

compare to a version of the shakespeare corpus found on github as when trying to test teh validate of the counts returned, there was a mismatch between the two, likely reason is editorial changes between different versions, so not suitable. kept it as a point of comparsion for benchmarking. 




## design decisions

use copilot to test out different methods and approaches to find the most optimal solution, create a notebook file using ipython to benchmark different solution. likely best candidate is counter from collections module, as this implementation uses CPython dict data type. rather than slower bytecode. 

to perform effective benchmarking, I want to split out the function that saves the sorted dictionary from the function that counts. more modular design, more ATOMIC design. let's me test more benchmark options, not concerned about file write times. counting and sorting are where the memory will be taking a hit. 

## Installation

1. Clone the repository and change into it.
2. Create the conda environment:

   ```bash
   conda env create -f environment.yml
   ```

   This creates the `corpus_analysis` environment with Python 3.12, pandas, numpy,
   jupyter, and ipykernel, and installs this package into it in editable mode
   (`pip -e .`).
3. Activate the environment:

   ```bash
   conda activate corpus_analysis
   ```

If the environment already exists and you just need to pick up code changes,
install the package manually instead:

```bash
pip install -e .
```

## Usage

Run the CLI from the activated `corpus_analysis` environment:

```bash
python -m corpus_analysis
```

By default this reads `data/shakespeare.txt` and writes the word counts to
`data/output/shakespeare_word_counts_<timestamp>.json`, where `<timestamp>`
is the date/time the command was run (`YYYYMMDD_HHMMSS`), so each run
produces a new file rather than overwriting the previous one.

Override the input file and/or output directory:

```bash
python -m corpus_analysis --input data/shakespeare.txt --output-dir data/output
```

See all available options:

```bash
python -m corpus_analysis --help
```

## Validation

Run the small test suite for the word-count logic:

```bash
pytest -q
```

This keeps the verification focused on the real behavior of the package without
adding heavy tooling or broad coverage.

## Data

- `data/shakespeare.txt` — default input text file.
- `data/output/` — generated output directory (contents are gitignored); the
  CLI writes a timestamped `shakespeare_word_counts_<timestamp>.json` file
  here on each run.

The word-counting logic lives in `src/corpus_analysis/word_count.py`
(`count_words_in_file` and `save_word_counts`).

## Notebooks

- `notebooks/01_exploration.ipynb` — placeholder notebook for exploration.
- `src/notebook.ipynb` — the original exploratory notebook the CLI logic was
  ported from.

When using Jupyter, select the `corpus_analysis` kernel (installed via `ipykernel`
in the conda environment).

## Project Structure

```
src/shakespeare/      # package: __main__.py (CLI entry), word_count.py (logic)
src/notebook.ipynb    # exploratory notebook
data/                 # input data and generated output
notebooks/            # placeholder notebook
environment.yml       # conda environment definition
pyproject.toml        # project metadata and build config
```

## Next Steps 
- Would be interesting to implement in Rust, as likely performance benefits but need to work on using Rust skills.
- look at patterns of word usage

## License

MIT License.
