# AI Powered Location Survey Data Optimizer: Inspection Report Generator

This is a Python tool that reads Survey123 (ESRI's survey tool) like field inspection records, uses an LLM to clean up raw field notes into full sentences, generates location maps, and then produces a single formatted Word inspection report document.

This work is inspired by the workflow of taking quick field notes from inspectors and turning them into client ready documentation. This is a common pain point in environmental and infrastructure consulting industry.

From messy survey data to this in seconds:
<img width="640" height="531" alt="image" src="https://github.com/user-attachments/assets/f47093e1-bce6-4ec9-9dd4-e7e940cd52b5" />


## What it does?

For each inspection record in the input CSV:

1. **Reads** the raw note, location, inspector, photo reference
2. **Cleans the note** via OpenAI `gpt-4o-mini`. It preserves numbers, units, and abbreviations (DI, TP, etc.) exactly as written
3. **Generates a small location map** showing the site coordinates
4. **Composes a Word section** with metadata table, cleaned narrative, photo, map side by side
5. **Saves a single report** with one section per inspection

## Stack

- Python 3.13
- `openai` LLM API client (gpt-4o-mini)
- `python-docx` Word document generation
- `matplotlib` local map rendering
- `python-dotenv` secure API key handling
- `Pillow` image handling

## Project structure

```bash
project-d-report-gen/
├── data/
│   ├── inspections.csv     # input: Survey123 like records
│   └── photos/             # input: site photos
├── output/
│   ├── inspection\_report.docx   # final deliverable
│   └── maps/                    # auto generated location maps
├── seed\_data.py            # generates mirroring test data
└── generate\_report.py      # the main pipeline
```

## To run it:

```bash
# One time: install requirements (uses parent venv)
pip install openai python-docx matplotlib python-dotenv pillow

# Set up your API key in .env
echo "OPENAI_API_KEY=sk-..." > .env

# Generate test data (5 mirroring inspections and placeholder photos)
python seed_data.py

# Generate the report
python generate_report.py
```

## Example transformation

Raw field notes get converted to clean sentences while preserving all technical content such as:

| Raw note | Cleaned by gpt-4o-mini |
|---|---|
| Cracked DI Top | Cracked DI top. |
| Slopong tp the building | Sloping TP to the building. |
| Grading tp step not correct | The grading TP step is not correct. |
| Conduit ehposed at base, needs cover ASAP | Conduit exposed at base needs cover ASAP. |

## Possible extensions in future:

- Pull live records from an ArcGIS Online feature service using REST API
- Use ArcGIS Pro layouts via `arcpy.mp` for actual, production quality maps
- Add severity classification via a second LLM pass or fine tuned classifier, could use free version Qwen
- Email report directly to project manager/reviewer on completion
- Async batch processing for large submission sets

That's all.
