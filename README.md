# Exquisite Corpus

*Exquisite Corpus* is an experimental poetry generation tool built from found phrases transfigured into annotated corpora.
It is inspired by surrealist practices such as the Surrealist *[cadavre exquis](https://www.tate.org.uk/art/art-terms/c/cadavre-exquis-exquisite-corpse)* game, [psychography](https://en.wikipedia.org/wiki/Automatic_writing), and devotional indexing.

## About
I am an artist, computational linguist, and ontologist/semantic data modeler by day/night. My practice moves between corpus linguistics, semantics, and etymology (eg., *tradurre è tradire* while passing flake8). This project is one small study in poetic computation for others to stich, fork, lint, translate, and betray.

## Status
Functionality is in progress.
Current features: canonical corpus (e.g., `data/canon.csv`), CLI for previewing corpora, and appending new phrases.

## Corpus File Format
*Exquisite Corpus* works with **corpora** (i.e. corpus files) that enumerate found phrases and minimal metadata. Every corpus file **must** include the following columns:
| Column                 | Type   | Description                                                                 |
|------------------------|--------|-----------------------------------------------------------------------------|
| `phrase_idx`           | string    | Auto-incremented index of each phrase (1, 2, 3, …).                         |
| `phrase`               | string | Phrase text copied verbatim from a found source.                                     |
| `phrase_recorded_date` | string | Date the phrase was logged in `YYYY-MM-DD` format.                          |
| `phrase_reference_link`| string | Source URL where the phrase was found.    |

### Supported formats

- **CSV** (`.csv`) — comma separated values
- **TSV** (`.tsv`) — tab separated values
- **JSON** (`.json`) — an array of objects (one object per phrase)

The loader will **auto-detect** the format from the file extension. If your file has no or a wrong extension, use the CLI override `--format`.

### Examples

**CSV**
```csv
phrase_idx,phrase,phrase_recorded_date,phrase_reference_link
1,"to solemnly scatter",2024-07-12,https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
2,"The disposition of their bodies is the unglamorous but critical work of the government.",2024-07-12,https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
3,"Collection of indigent dead",2024-07-12, https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
```

**TSV**
```tsv
phrase_idx	phrase	phrase_recorded_date	phrase_reference_link
1	to solemnly scatter	2024-07-12	https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
2	The disposition of their bodies is the unglamorous but critical work of the government.	2024-07-12	https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
3	Collection of indigent dead	2024-07-12	https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/
```

**JSON**
```json
[
  {
    "phrase_idx": 1,
    "phrase": "to solemnly scatter",
    "phrase_recorded_date": "2024-07-12",
    "phrase_reference_link": "https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/"
  },
  {
    "phrase_idx": 2,
    "phrase": "The disposition of their bodies is the unglamorous but critical work of the government.",
    "phrase_recorded_date": "2024-07-12",
    "phrase_reference_link": "https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/"
  },
  {
    "phrase_idx": 3,
    "phrase": "Collection of indigent dead",
    "phrase_recorded_date": "2024-07-12",
    "phrase_reference_link": "https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/"
  }
]
```

### Canonical Corpus

This repository contains a **canonical corpus** (i.e. `data/canon.csv`). This file is an evolving archive and ritualized starting point for provocation, translation, testing, etc.

Other corpora may be added under `data/corpora/`, while `canon.csv` remains an authoritative corpus of the initial cantor/coder.

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/exquisite-corpus.git
cd exquisite-corpus
python -m venv venv
source venv/bin/activate   # On Windows use venv\Scripts\activate
pip install -e .
```

## Usage

After installation, you can use the `excorpus` command-line interface (CLI) to
work with files.

### Preview the first N rows of the canonical corpus
```bash
excorpus corpus head data/canon.csv --rows 3

# Force the format if the extension is missing or wrong
excorpus corpus head data/canon --format csv --rows 3
```

### Example outpt
```bash
[{'phrase_idx': 1, 'phrase': 'to solemnly scatter',
  'phrase_recorded_date': '2024-07-12',
  'phrase_reference_link': 'https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/'},
 {'phrase_idx': 2, 'phrase': 'The disposition of their bodies is the unglamorous but critical work of the government.',
  'phrase_recorded_date': '2024-07-12',
  'phrase_reference_link': 'https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/'},
 {'phrase_idx': 3, 'phrase': 'Collection of indigent dead',
  'phrase_recorded_date': '2024-07-12',
  'phrase_reference_link': 'https://sfstandard.com/2024/03/18/san-francisco-unclaimed-dead-ashes-scattering/'}]
```

### Appending to the canon
```bash
excorpus corpus append data/canon.csv data/new_phrases.csv --format csv
```

### Running linting and tests
Use [flake8](https://flake8.pycqa.org/) for linting and [pytest](https://pytest.org/) for tests:

```bash
flake8 src tests
pytest -q
```

### Pre-commit hooks

This repository uses [pre-commit](https://pre-commit.com/) to enforce
consistent style (trailing whitespace, end-of-file newline, flake8 checks, etc.).

Install pre-commit (once per machine):

```bash
pip install pre-commit
```

Set up the hooks in your local clone:
```bash
pre-commit install
```

Now, every time you run `git commit`, the hooks will automatically check and fix your code.
You can also run them manually on all files:
```bash
pre-commit run --all-files
```

## License
This project is licensed under the
[Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).
You may share and adapt the code with attribution, but **commercial use is not permitted**.
