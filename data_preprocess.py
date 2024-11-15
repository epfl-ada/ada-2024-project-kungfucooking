import json
from tqdm import tqdm

# Input and output file paths
input_file_path = 'project/yt_metadata_en.jsonl'
output_file_path = 'yt_metadata_filtered_"trump ".jsonl'

# Define keywords
keywords = [
    "trump ", 
    "45th president", 
]

# Count variables
total_count = 0
filtered_count = 0

# Function: Check if entry contains keywords
def contains_keywords(data):
    # Combine title, description, and tags into a single string, convert to lowercase
    text = f"{data.get('title', '')} {data.get('description', '')} {data.get('tags', '')}".lower()
    # Check if any keyword is present
    for keyword in keywords:
        if keyword in text:
            return keyword, True
    return None, False

# Start data cleaning
with open(input_file_path, "r") as infile, open(output_file_path, "w") as outfile:
    for line in tqdm(infile):
        total_count += 1  # Total entry count
        data = json.loads(line)
        keyword, contains = contains_keywords(data)
        # Check if entry contains keywords
        if contains:
            filtered_count += 1  # Filtered entry count
            data['description'] = ''
            data['keywords'] = keyword
            # Write entries that meet the criteria to the new file
            outfile.write(json.dumps(data) + "\n")

# Print the number of entries before and after
print(f"Original number of entries: {total_count}")
print(f"Number of entries containing keywords: {filtered_count}")
print(f"Filtered and generated new file: {output_file_path}")
