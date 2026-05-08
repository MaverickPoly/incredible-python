import csv
import json


def convert_json_to_csv(json_file, csv_file):
    try:
        with open(json_file, "r") as file:
            json_data: list[dict] = json.load(file)

        if len(json_data) == 0:
            return

        fields = list(json_data[0].keys())
        data = [list(data.values()) for data in json_data]

        print(fields)
        print(data)

        with open(csv_file, "w") as file:
            writer = csv.writer(file)

            writer.writerow(fields)
            writer.writerows(data)

        print("Successfully converter json to csv!")
    except Exception as e:
        print(f"Error converting json to csv: {e}")


def main():
    json_file = input("Enter the path of json file: ")
    csv_file = input("Enter the path of csv fil : ")

    convert_json_to_csv(json_file, csv_file)


if __name__ == '__main__':
    main()
