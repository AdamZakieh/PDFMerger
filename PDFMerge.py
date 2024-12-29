import os
import re
from PyPDF2 import PdfMerger

def extract_numeric_key(filepath):
    """
    Extracts a list of integer values from the filename to ensure correct numeric sorting.
    Example: 'week10-slide2.pdf' -> [10, 2]
    """
    filename = os.path.basename(filepath)
    # Find *all* digit sequences in the filename.
    numbers = re.findall(r'\d+', filename)
    # Convert each digit sequence to an integer.
    return [int(num) for num in numbers]

def sort_files_numerically(files):
    """
    Sorts files by extracting all digits and sorting by those numeric values.
    """
    # Debugging: Show the numeric key for each file
    for f in files:
        print(f"File: {f} -> Keys: {extract_numeric_key(f)}")

    sorted_files = sorted(files, key=extract_numeric_key)
    print("Sorted files:", sorted_files)  # Debugging output
    return sorted_files

def merge_pdfs(pdf_list, output_filename):
    """
    Combines a list of PDF files into one.

    Args:
        pdf_list (list): Paths to PDF files.
        output_filename (str): The name of the merged output file.
    """
    merger = PdfMerger()
    for pdf in pdf_list:
        print(f"Adding {pdf}...")
        merger.append(pdf)
    print(f"Saving merged PDF as {output_filename}...")
    merger.write(output_filename)
    merger.close()
    print("All done!")

def main():
    print("=== Simple PDF Merger ===")
    folder = input("Enter the folder where your PDFs are stored: ").strip()
    output_file = input("Enter the name for the merged file (e.g., merged.pdf): ").strip()

    # Get all PDF files in the folder
    pdf_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    # Sort the files numerically
    pdf_files = sort_files_numerically(pdf_files)

    print(f"Found {len(pdf_files)} PDF file(s):")
    for pdf in pdf_files:
        print(f" - {pdf}")

    merge_pdfs(pdf_files, output_file)

if __name__ == "__main__":
    main()