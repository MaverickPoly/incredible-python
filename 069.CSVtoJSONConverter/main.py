import csv
import json
import os.path


def convert(csv_file, json_file):
    if not os.path.exists(csv_file) or not os.path.exists(json_file):
        print("Invalid csv file or json file")

    try:
        fields = None
        data = []

        with open(csv_file, "r") as file:
            reader = csv.reader(file)
            for i, element in enumerate(reader):
                if i == 0:
                    fields = element
                else:
                    data.append({fields[i]: element[i] for i in range(len(element))})

        with open(json_file, "w") as file:
            json.dump(data, file)

        print("Successfully converter csv to json")
    except Exception as e:
        print(f"Error converting csv to json: {e}")


def main():
    csv_file = input("Enter the path for csv file: ")
    json_file = input("Enter the path for json file: ")

    convert(csv_file, json_file)


if __name__ == '__main__':
    main()
