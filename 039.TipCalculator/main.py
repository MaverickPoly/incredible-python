bill = float(input("Enter the total bill amount: "))

tip_percentage = int(input("Enter the tip percentage: "))

number_of_people = int(input("Enter the total number of people: "))


# Calculate tip total amount
tip_amount = bill * tip_percentage / 100

total_bill = bill + tip_percentage

amount_per_person = total_bill / number_of_people

print(f"Total bill: {total_bill}")
print(f"Bill per person: {amount_per_person}")
