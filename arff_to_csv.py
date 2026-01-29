import os

path_to_file = r"C:\Users\Hp\Documents\dataset folders\autism\Autism_Data.arff"

def arff_to_csv(arff_path):
    csv_lines = []
    header = []
    data_section = False

    with open(arff_path, "r") as f:
        for line in f:
            line = line.strip()

            # Skip empty lines and comments
            if not line or line.startswith("%"):
                continue

            # Read attributes
            if line.lower().startswith("@attribute"):
                parts = line.split()
                attr_name = parts[1].strip("'\"")  # remove quotes
                header.append(attr_name)

            # Detect data section
            elif line.lower().startswith("@data"):
                csv_lines.append(",".join(header) + "\n")
                data_section = True

            # Read actual data
            elif data_section:
                csv_lines.append(line + "\n")

    return csv_lines


# Convert file
csv_content = arff_to_csv(path_to_file)

output_csv = path_to_file.replace(".arff", ".csv")
with open(output_csv, "w") as out:
    out.writelines(csv_content)

print("✅ CSV generated successfully:", output_csv)
print("Rows written:", len(csv_content) - 1)
