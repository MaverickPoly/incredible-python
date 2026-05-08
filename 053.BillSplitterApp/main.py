def calculate_bill():
    try:
        bill = int(input("Enter the bill amount: "))
        tip_percent = int(input("Enter the tip percent: "))
        number_of_people = int(input("Enter the number of people: "))

        if any(map(lambda x: x <= 0, [bill, tip_percent, number_of_people])):
            print("Invalid input!")
            return

        tip_amount = bill * (tip_percent / 100)
        total_amount = bill + tip_amount
        price_per_person = total_amount / number_of_people

        print("------ Summary ------")
        print(f"Tip amount: {tip_amount}")
        print(f"Total amount: {total_amount}")
        print(f"Price per person: {price_per_person}")
    except ValueError as e:
        print(f"Error during processing: {e}")


if __name__ == '__main__':
    calculate_bill()
