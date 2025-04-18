# ai-cyber-forensics-detector
AI-based system to detect suspicious or disguised files for digital forensics
# 🔍 AI-Powered Suspicious File Detection (Cyber Forensics)

This project uses AI to detect disguised or suspicious files (e.g., ZIP files pretending to be images or malware embedded in renamed PDFs). It's designed for digital forensics applications to support the early detection of potential cyber threats during evidence analysis.

---

## 📁 Dataset

A synthetic dataset was created with the following metadata features:
- `file_name`
- `file_size`
- `mime_type`
- `entropy` (measures randomness; higher entropy often means compressed or encrypted data)
- `accessed_time`
- `label` (1 = suspicious, 0 = safe)

---

## ⚙️ How It Works

### 1. **Feature Selection**
The model uses:
- `file_size`
- `entropy`

These features were found to be effective in distinguishing between normal and disguised files.

### 2. **Model Used**
A **Random Forest Classifier** was used for its reliability and accuracy on structured data.

### 3. **Training & Evaluation**
Run the following script to train the model:

```bash
python train_model.py
