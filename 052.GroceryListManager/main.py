import argparse
import json


FILENAME = "data.json"

def add_grocery(title, quantity, price):
    data = load_groceries()
    new_data = {"title": title, "quantity": quantity, "price": price}
    data.append(new_data)
    with open(FILENAME, "w") as file:
        json.dump(data, file)


def load_groceries():
    with open(FILENAME, "r") as file:
        json_data = json.load(file)
        return json_data


def main():
    parser = argparse.ArgumentParser(description="Grocery List Manager CLI")

    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    load_parser = subparsers.add_parser("load")

    add_parser.add_argument("title", help="Title of a grocery item")
    add_parser.add_argument("quantity", type=int, help="Quantity of a grocery item")
    add_parser.add_argument("price", type=float, help="Price of a grocery item")

    args = parser.parse_args()

    if args.command == "add":
        add_grocery(args.title, args.quantity, args.price)
        print("New grocery added!")
    elif args.command == "load":
        groceries = load_groceries()
        print("====== Groceries ======")
        total_price = 0
        for grocery in groceries:
            price = grocery["quantity"] * grocery["price"]
            total_price += price
            print(f'{grocery["title"]}: {grocery["quantity"]} X ${grocery["price"]} = ${price}')

        print(f"Total price: ${total_price}")


if __name__ == '__main__':
    main()
