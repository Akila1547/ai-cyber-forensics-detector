import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Step 1: Load the dataset
df = pd.read_csv("forensic_file_metadata.csv")

# Step 2: Select features (we use numerical ones)
X = df[['file_size', 'entropy']]  # You can add more later
y = df['label']  # Make sure you added this manually if not already labeled

# Step 3: Split into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 4: Train the Random Forest model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 5: Make predictions and show results
y_pred = model.predict(X_test)
print("🔍 Classification Report:")
print(classification_report(y_test, y_pred))
