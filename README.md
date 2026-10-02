# Shakespeare

## Description

A Python 3.12+ data processing project that counts word frequencies in a text file
(the Shakespeare corpus) and writes the results to JSON.

## Installation

1. Clone the repository and change into it.
2. Create the conda environment:

   ```bash
   conda env create -f environment.yml
   ```

   This creates the `shakespeare` environment with Python 3.12, pandas, numpy,
   jupyter, and ipykernel, and installs this package into it in editable mode
   (`pip -e .`).
3. Activate the environment:

   ```bash
   conda activate shakespeare
   ```

If the environment already exists and you just need to pick up code changes,
install the package manually instead:

```bash
pip install -e .
```

## Usage

Run the CLI from the activated `shakespeare` environment:

```bash
python -m shakespeare
```

By default this reads `data/shakespeare.txt` and writes the word counts to
`data/output/shakespeare_word_counts.json`.

Override the input file and/or output directory:

```bash
python -m shakespeare --input data/shakespeare.txt --output-dir data/output
```

See all available options:

```bash
python -m shakespeare --help
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
  CLI writes `shakespeare_word_counts.json` here.

The word-counting logic lives in `src/shakespeare/word_count.py`
(`count_words_in_file` and `write_word_counts`).

## Notebooks

- `notebooks/01_exploration.ipynb` — placeholder notebook for exploration.
- `src/notebook.ipynb` — the original exploratory notebook the CLI logic was
  ported from.

When using Jupyter, select the `shakespeare` kernel (installed via `ipykernel`
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

## License

MIT License.
