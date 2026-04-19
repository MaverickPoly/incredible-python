import argparse
from PyPDF2 import PdfReader


def main():
    parser = argparse.ArgumentParser(description="PDF Text Extractor CLI")

    parser.add_argument("-f", "--filepath", required=True, help="Filepath of the pdf file.")

    args = parser.parse_args()

    try:
        reader = PdfReader(args.filepath)
        pages = reader.pages
        print("Extracted text:")
        for idx, page in enumerate(pages, start=1):
            print(f"\n---- Page {idx}:")
            print(page.extract_text())
    except FileNotFoundError:
        print("Invalid filepath!")


if __name__ == '__main__':
    main()
