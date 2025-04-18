
import os
import mimetypes
import pandas as pd
import datetime
import math

# Folder containing files to scan
DATASET_DIR = "dataset"

# Function to calculate entropy of a file
def calculate_entropy(file_path):
    try:
        with open(file_path, 'rb') as f:
            byte_arr = f.read()
        if len(byte_arr) == 0:
            return 0
        freq_list = [float(byte_arr.count(b)) / len(byte_arr) for b in range(256)]
        entropy = -sum([p * math.log2(p) for p in freq_list if p > 0])
        return round(entropy, 4)
    except:
        return 0

# Extract metadata from each file
data = []
for folder, _, files in os.walk(DATASET_DIR):
    for file in files:
        path = os.path.join(folder, file)
        size = os.path.getsize(path)
        mime = mimetypes.guess_type(path)[0]
        entropy = calculate_entropy(path)
        accessed = datetime.datetime.fromtimestamp(os.path.getatime(path))
        data.append([file, size, mime, entropy, accessed])

# Save to CSV
df = pd.DataFrame(data, columns=['file_name', 'file_size', 'mime_type', 'entropy', 'accessed_time'])
df.to_csv("forensic_file_metadata.csv", index=False)
print("Metadata saved to forensic_file_metadata.csv")
