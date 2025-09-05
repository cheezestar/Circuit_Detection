from imutils import  paths
import os
import argparse 
import csv
import shutil

BASEPATH = os.path.dirname(os.path.abspath(__file__))

def main():

    #collects the file path to the csv files from the arg 
    parser = argparse.ArgumentParser(description="csv file locations")
    parser.add_argument("--file-dir", type=str, required=False, help="path to output directory")
    args = parser.parse_args()

    #joins the path to poin correctly
    file_path = os.path.join(BASEPATH, args.file_dir)
    rows = []

    #reads each csv file and appends the rows to a list
    for path in paths.list_files(file_path, validExts=(".csv")):
        with open(path, newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if row:
                    rows.append(row)
        os.remove(path)

    #writes the rows to a new csv file
    output_file = os.path.join(BASEPATH, "circuits" , "annotations", "combined_annotations.csv")

    with open(output_file, "w", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    print(f"[INFO] Wrote {len(rows)} rows to {output_file}")

if __name__ == "__main__":
    main()