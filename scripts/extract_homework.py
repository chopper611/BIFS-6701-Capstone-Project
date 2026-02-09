from pathlib import Path
import docx

homework_folder = Path("data/raw/homeworks")
output_folder = Path("data/processed")
output_folder.mkdir(parents=True, exist_ok=True)

output_file = output_folder / "homeworks_raw_text.txt"

all_text = ""

# Helper to extract homework number if present
def get_hw_number(path):
    return int(path.stem.split("HW")[1])

# Loop through homework files in order
for hw_file in sorted(homework_folder.glob("*.docx"), key=get_hw_number):
    print("Processing homework:", hw_file.name)

    document = docx.Document(hw_file)

    all_text = all_text + "\n\n"
    all_text = all_text + "--- SOURCE: " + hw_file.name + " ---\n\n"

    for paragraph in document.paragraphs:
        if paragraph.text.strip() != "":
            all_text = all_text + paragraph.text + "\n\n"

output_file.write_text(all_text.strip(), encoding="utf-8")

print("Homework extraction complete. Output saved to:", output_file)