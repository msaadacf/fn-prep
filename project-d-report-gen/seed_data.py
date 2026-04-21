"""
Seed script: It is creating a mock Survey123 like inspections CSV
and creating placeholder photo files to test the report generator.
"""
import csv
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

DATA_DIR = Path("data")
PHOTOS_DIR = DATA_DIR / "photos"
PHOTOS_DIR.mkdir(parents=True, exist_ok=True)

# Fake inspection records — Lafayette, LA area
inspections = [
    {
        "id": 94,
        "creator": "Alice Mouton",
        "creation_date": "2026-04-15",
        "lat": 30.2241,
        "lon": -92.0198,
        "notes": "Cracked DI Top",
        "photo": "site_94.jpg",
    },
    {
        "id": 95,
        "creator": "Bob Hebert",
        "creation_date": "2026-04-15",
        "lat": 30.2305,
        "lon": -92.0254,
        "notes": "DI top cracked on edge",
        "photo": "site_95.jpg",
    },
    {
        "id": 96,
        "creator": "Alice Mouton",
        "creation_date": "2026-04-16",
        "lat": 30.2189,
        "lon": -92.0142,
        "notes": "Slopong tp the building",
        "photo": "site_96.jpg",
    },
    {
        "id": 97,
        "creator": "Coy LeBlanc",
        "creation_date": "2026-04-16",
        "lat": 30.2350,
        "lon": -92.0301,
        "notes": "Grading tp step not correct",
        "photo": "site_97.jpg",
    },
    {
        "id": 98,
        "creator": "Bob Hebert",
        "creation_date": "2026-04-17",
        "lat": 30.2260,
        "lon": -92.0220,
        "notes": "Conduit ehposed at base, needs cover ASAP",
        "photo": "site_98.jpg",
    },
]

# Writing the CSV now
csv_path = DATA_DIR / "inspections.csv"
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=inspections[0].keys())
    writer.writeheader()
    writer.writerows(inspections)
print(f"Wrote {csv_path} with {len(inspections)} rows")

# Generating the placeholder images in JPG format (just colored rectangles with text)
colors = ["#A8DADC", "#F1FAEE", "#E63946", "#457B9D", "#1D3557"]
for record, color in zip(inspections, colors):
    img = Image.new("RGB", (640, 480), color)
    draw = ImageDraw.Draw(img)
    text = f"Site {record['id']}\nField photo placeholder"
    draw.text((20, 20), text, fill="white")
    photo_path = PHOTOS_DIR / record["photo"]
    img.save(photo_path, "JPEG")
    print(f"Wrote {photo_path}")

print("\nDone. Data is all ready.")