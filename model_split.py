import os
import pandas as pd

BASE_DIR = r"C:\Users\Hp\Documents\dataset folders\autism"
splits = ["train", "val", "test"]

for split in splits:
    split_dir = os.path.join(BASE_DIR, split)

    if not os.path.exists(split_dir):
        raise FileNotFoundError(f"❌ Folder not found: {split_dir}")

    data = {}

    for feature in os.listdir(split_dir):
        feature_dir = os.path.join(split_dir, feature)

        if not os.path.isdir(feature_dir):
            continue

        files = os.listdir(feature_dir)
        if len(files) != 1:
            raise ValueError(f"⚠ {feature_dir} should contain exactly ONE file")

        file_path = os.path.join(feature_dir, files[0])

        col_data_
