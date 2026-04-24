import argparse
from database import BooksDatabase, Book


def main():
    parser = argparse.ArgumentParser(description="Library Management System CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add new book")
    add_parser.add_argument("-t", "--title", required=True, help="Title of a book")
    add_parser.add_argument("-a", "--author", required=True, help="Author of a book")
    add_parser.add_argument("-r", "--rating", required=True, help="Rating of a book")

    get_parser = subparsers.add_parser("get", help="Get all books")

    delete_parser = subparsers.add_parser("delete", help="Delete a book")
    delete_parser.add_argument("id", help="Id of a book to delete")

    update_parser = subparsers.add_parser("update", help="Update a book")
    update_parser.add_argument("id", help="Id of a book to update")
    update_parser.add_argument("-t", "--title", required=True, help="Title of a book")
    update_parser.add_argument("-a", "--author", required=True, help="Author of a book")
    update_parser.add_argument("-r", "--rating", required=True, help="Rating of a book")

    args = parser.parse_args()
    books_database = BooksDatabase()

    print(args)

    match args.command:
        case "add":
            books_database.add_book(args.title, args.author, args.rating)
            print("Added book successfully!")
        case "get":
            books = books_database.get_books()
            print(f"====== {len(books)} Books ======")
            for book in books:
                print(f"{book.id}. {book.title} - {book.author} ({book.rating})")
        case "delete":
            rowcount = books_database.delete_book(args.id)
            if rowcount > 0:
                print("Deleted a book successfully!")
            else:
                print(f"Book with id {args.id} not found!")
        case "update":
            rowcount = books_database.update_book(args.id, args.title, args.author, args.rating)
            if rowcount > 0:
                print("Updated a book successfully!")
            else:
                print(f"Book with id {args.id} not found!")


if __name__ == '__main__':
    main()

