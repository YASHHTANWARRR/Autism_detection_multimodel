import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Load dataset
csv_path = r"C:\Users\Hp\Documents\dataset folders\autism\Autism_Data.csv"
df = pd.read_csv(csv_path)

# Target column
target_col = "Class/ASD"

# Encode categorical columns
for col in df.select_dtypes(include=["object"]).columns:
    df[col] = LabelEncoder().fit_transform(df[col])

# Split features and labels
X = df.drop(columns=[target_col])
y = df[target_col]

# Train / Val / Test split
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, stratify=y, random_state=42
)

X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42
)

print("Train:", X_train.shape)
print("Val:", X_val.shape)
print("Test:", X_test.shape)
