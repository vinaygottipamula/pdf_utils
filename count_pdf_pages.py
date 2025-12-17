import os
import argparse
from PyPDF2 import PdfReader


def count_pages_in_folder(folder_path):
    """
    Count total number of pages in all PDF files in a folder.

    Args:
        folder_path (str): Path to folder containing PDF files

    Returns:
        int: Total number of pages across all PDFs
    """
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return 0

    pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])
    if not pdf_files:
        print(f"⚠️ No PDFs found in {folder_path}")
        return 0

    total_pages = 0

    print(f"📁 Found {len(pdf_files)} PDF files in {folder_path}\n")

    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        try:
            reader = PdfReader(pdf_path)
            page_count = len(reader.pages)
            total_pages += page_count
            print(f"📄 {pdf} → {page_count} pages")
        except Exception as e:
            print(f"❌ Error reading {pdf}: {str(e)}")

    print("\n" + "=" * 40)
    print(f"✅ TOTAL PAGES IN ALL PDFs: {total_pages}")
    print("=" * 40)

    return total_pages


def main():
    parser = argparse.ArgumentParser(
        description="Count total number of pages in all PDF files in a folder"
    )

    parser.add_argument(
        '--folder',
        required=True,
        help='Folder containing PDF files'
    )

    args = parser.parse_args()
    count_pages_in_folder(args.folder)


if __name__ == "__main__":
    main()
