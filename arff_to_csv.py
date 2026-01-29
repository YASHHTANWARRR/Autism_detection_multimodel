import os

path_to_file = r'C:\Users\Hp\Documents\dataset folders\autism\Autism_Data.arff'

def toCsv(content):
    data = False
    header = ""
    newContent = []

    for line in content:
        line = line.strip()
        if not data:
            if line.lower().startswith("@attribute"):
                parts = line.split()
                columnName = parts[1]
                header += columnName + ","
            elif line.lower().startswith("@data"):
                data = True
                header = header[:-1] + "\n"
                newContent.append(header)
        else:
            if line and not line.startswith("%"):
                newContent.append(line + "\n")

    return newContent


with open(path_to_file, "r") as inFile:
    content = inFile.readlines()
    name, _ = os.path.splitext(path_to_file)
    new = toCsv(content)

with open(name + ".csv", "w") as outFile:
    outFile.writelines(new)

print("ARFF → CSV conversion complete")
