import os
import argparse
from PyPDF2 import PdfReader


def search_text_in_pdfs(folder_path, search_text):
    """
    Search for a given text (English / Telugu) in all PDFs in a folder.

    Args:
        folder_path (str): Path to folder containing PDF files
        search_text (str): Text to search
    """
    if not os.path.exists(folder_path):
        print(f"❌ Folder not found: {folder_path}")
        return

    pdf_files = sorted([f for f in os.listdir(folder_path) if f.lower().endswith('.pdf')])
    if not pdf_files:
        print(f"⚠️ No PDFs found in {folder_path}")
        return

    print(f"📁 Searching in {len(pdf_files)} PDFs")
    print(f"🔍 Search Text: {search_text}")
    print("=" * 60)

    total_matches = 0
    files_with_matches = 0

    for pdf in pdf_files:
        pdf_path = os.path.join(folder_path, pdf)
        found_in_file = False

        try:
            reader = PdfReader(pdf_path)

            for page_num, page in enumerate(reader.pages, start=1):
                text = page.extract_text()
                if not text:
                    continue

                # For English: case-insensitive
                # For Telugu: casefold has no effect, safe to use
                if search_text.casefold() in text.casefold():
                    count = text.casefold().count(search_text.casefold())
                    total_matches += count
                    found_in_file = True
                    print(f"📄 {pdf} | Page {page_num} → {count} match(es)")

            if found_in_file:
                files_with_matches += 1

        except Exception as e:
            print(f"❌ Error reading {pdf}: {str(e)}")

    print("\n" + "=" * 60)
    print(f"✅ FILES WITH MATCHES : {files_with_matches}")
    print(f"✅ TOTAL MATCHES     : {total_matches}")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Search a word (English / Telugu) in all PDF files in a folder"
    )

    parser.add_argument(
        '--folder',
        required=True,
        help='Folder containing PDF files'
    )

    parser.add_argument(
        '--text',
        required=True,
        help='Text to search (English / Telugu)'
    )

    args = parser.parse_args()
    search_text_in_pdfs(args.folder, args.text)


if __name__ == "__main__":
    main()
