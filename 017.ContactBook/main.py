import argparse
import sqlite3


DB = "sqlite.db"

def format_contact(contact: tuple) -> str:
    return f"{contact[0]}. {contact[1]}, {contact[2]} - {contact[3]}"


def init_db():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                phone TEXT,
                email TEXT
            )
        """)

def get_contacts():
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM contacts
        """)
        return cursor.fetchall()

def add_contact(username: str, phone: str, email: str):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO contacts (username, phone, email) VALUES (?, ?, ?)
        """, (username, phone, email))

def delete_contact(contact_id: int):
    with sqlite3.connect(DB) as conn:
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM contacts WHERE id=?
        """, (contact_id,))


def main():
    init_db()

    parser = argparse.ArgumentParser(description="Contact book CLI")

    subparsers = parser.add_subparsers(dest="command")

    get_parser = subparsers.add_parser("get")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--username", required=True, help="Contact's username")
    add_parser.add_argument("--phone", required=True, help="Contact's phone number")
    add_parser.add_argument("--email", required=True, help="Contact's email address")

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, help="Contact id to delete")

    args = parser.parse_args()

    match args.command:
        case "get":
            contacts = get_contacts()
            for contact in contacts:
                print(format_contact(contact))
        case "add":
            add_contact(args.username, args.phone, args.email)
            print("Added new contact successfully!")
        case "delete":
            delete_contact(args.id)
            print("Deleted contact successfully!")


if __name__ == '__main__':
    main()
