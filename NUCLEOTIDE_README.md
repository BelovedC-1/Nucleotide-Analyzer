# 🧬 Nucleotide Sequence Analyser

A Streamlit web app that analyses DNA and RNA nucleotide sequences and outputs detailed biological information.

## What it does

**If the input is DNA:**
- Transcribes the DNA to mRNA
- Derives the tRNA anticodon strand
- Translates to 3-letter amino acid sequence
- Outputs the 1-letter protein sequence

**If the input is RNA:**
- Outputs the complement strand
- Outputs the reverse complement strand

The app automatically detects whether the sequence is DNA or RNA based on the presence of T (DNA) or U (RNA).

## Example inputs

| Sequence | Type |
|----------|------|
| `ATGCTTGAA` | DNA |
| `AUGCUUGAA` | RNA |
| `GATTACAGGCTAA` | DNA |

## Run locally

```bash
pip install streamlit
streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

## Deploy on Streamlit Community Cloud

1. Push `app.py` and `requirements.txt` to a GitHub repo
2. Go to [share.streamlit.io](https://share.streamlit.io) and sign in with GitHub
3. Click **New app** → select your repo → set main file to `app.py` → **Deploy**

You'll get a live public URL in about a minute.

## Files

| File | Description |
|------|-------------|
| `app.py` | Main Streamlit application |
| `requirements.txt` | Python dependencies |
| `README.md` | This file |

## Requirements

- Python 3.8+
- streamlit >= 1.32.0
- No other external libraries needed — pure Python logic
