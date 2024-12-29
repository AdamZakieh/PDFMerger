import os
from PyPDF2 import PdfMerger


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
    folder = input("Enter the folder location wheree the PDFs are stored: ").strip()
    output_file = input("Enter the name for the merged file: ").strip()

    # Get all PDF files in the folder
    pdf_files = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith('.pdf')]

    if not pdf_files:
        print("No PDF files found in the specified folder.")
        return

    print(f"Found {len(pdf_files)} PDF file(s):")
    for pdf in pdf_files:
        print(f" - {pdf}")

    merge_pdfs(pdf_files, output_file)


if __name__ == "__main__":
    main()