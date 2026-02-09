from pathlib import Path
import json

# Input and output locations
input_file = Path("data/processed/homeworks_raw_text.txt")
output_file = Path("outputs/chunks_homework.json")
output_file.parent.mkdir(parents=True, exist_ok=True)

chunk_size = 500
overlap = 100

chunks = []
chunk_id = 0

# Function to split text into overlapping chunks
def split_into_chunks(text, source):
    global chunk_id

    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]

        chunks.append({
            "chunk_id": chunk_id,
            "source": source,
            "text": chunk
        })

        chunk_id = chunk_id + 1
        start = start + chunk_size - overlap

# Read the extracted lecture text
text = input_file.read_text(encoding="utf-8")
lines = text.splitlines()

current_source = ""
current_text = ""

# Loop through lines and separate by source
for line in lines:
    if line.startswith("--- SOURCE:"):
        # Chunk previous lecture before moving on
        if current_text != "":
            split_into_chunks(current_text, current_source)

        # Set new source
        current_source = line.replace("--- SOURCE:", "").replace("---", "").strip()
        current_text = ""

    else:
        current_text = current_text + line + " "

# Chunk the final lecture
if current_text != "":
    split_into_chunks(current_text, current_source)

# Write chunks to JSON file
with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(chunks, outfile, indent=2)

print("Chunking complete. Total chunks created:", len(chunks))
print("Output saved to:", output_file)