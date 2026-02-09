from pathlib import Path
import docx

lecture_folder = Path("data/raw/lectures")
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "lectures_raw_text.txt"

all_text = ""

# Helper to extract week number from filename
def get_week_number(path):
    return int(path.name.split("Week")[1].split()[0])

# Loop through lecture files in week order
for lecture_file in sorted(lecture_folder.glob("*.docx"), key=get_week_number):
    print("Processing:", lecture_file.name)

    document = docx.Document(lecture_file)

    all_text = all_text + "\n\n"  # Space before each lecture
    all_text = all_text + "--- SOURCE: " + lecture_file.name + " ---\n\n"

    for paragraph in document.paragraphs:
        if paragraph.text.strip() != "":
            all_text = all_text + paragraph.text + "\n\n"

# Write extracted text to output file
output_file.write_text(all_text.strip(), encoding="utf-8")

print("Extraction complete. Output saved to:", output_file)