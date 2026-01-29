import pandas as pd
import numpy as np

from sklearn.model_selection import StratifiedKFold, cross_val_score
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC

# -----------------------------
# 1. Load dataset
# -----------------------------
csv_path = r"C:\Users\Hp\Documents\dataset folders\autism\Autism_Data.csv"
df = pd.read_csv(csv_path)

# -----------------------------
# 2. Encode categorical columns
# -----------------------------
categorical_cols = df.select_dtypes(include=["object"]).columns
for col in categorical_cols:
    df[col] = LabelEncoder().fit_transform(df[col])

# -----------------------------
# 3. Split features & label
# -----------------------------
X = df.drop("Class", axis=1)
y = df["Class"]

# -----------------------------
# 4. ML Pipeline
# -----------------------------
pipeline = Pipeline([
    ("feature_selection", SelectKBest(score_func=f_classif, k=8)),
    ("scaler", StandardScaler()),
    ("svm", SVC(kernel="rbf", C=10, gamma="scale"))
])

# -----------------------------
# 5. K-Fold Cross Validation
# -----------------------------
kfold = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

cv_scores = cross_val_score(
    pipeline,
    X,
    y,
    cv=kfold,
    scoring="accuracy"
)

# -----------------------------
# 6. Results
# -----------------------------
print("Cross-validation accuracies:", cv_scores)
print("Mean Accuracy:", cv_scores.mean())
print("Standard Deviation:", cv_scores.std())
