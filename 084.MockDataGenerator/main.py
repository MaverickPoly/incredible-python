import csv
import json
import random

from faker import Faker
from faker.config import AVAILABLE_LOCALES


STATE = "production"

if STATE == "testing":
    print(AVAILABLE_LOCALES)


class MockDataGenerator:
    def __init__(self, locale="en_US"):
        self.faker = Faker(locale)

    def generate_person(self):
        return {
            "id": self.faker.uuid4(),
            "first_name": self.faker.first_name(),
            "last_name": self.faker.last_name(),
            "email": self.faker.email(),
            "country": self.faker.country(),
            "username": self.faker.user_name(),
            "password": self.faker.password(),
            "date_of_birth": self.faker.date_of_birth(),
            "created_at": self.faker.date_time_this_decade(),
        }

    def generate_comment(self):
        return {
            "id": self.faker.uuid4(),
            "post_id": self.faker.uuid4(),
            "username": self.faker.user_name(),
            "content": self.faker.sentence(),
            "emoji": self.faker.emoji(),
            "likes": random.randint(0, 10000),
            "created_at": self.faker.date_time_this_decade(),
        }

    def generate_product(self):
        return {
            "id": self.faker.uuid4(),
            "name": self.faker.catch_phrase(),
            "description": self.faker.text(max_nb_chars=200),
            "price": random.randint(5, 9999),
            "category": self.faker.word(),
            "rating": round(random.uniform(1, 5), 1),
            "manufacturer": self.faker.company(),
            "created_date": self.faker.date_this_decade(),
            "is_available": self.faker.boolean(),
        }

    @staticmethod
    def save_to_csv(data: list[dict], filename: str):
        if not data:
            print("No data provided!")
            return

        field_names = data[0].keys()
        with open(filename, "w") as file:
            writer = csv.DictWriter(file, fieldnames=field_names)
            writer.writeheader()
            writer.writerows(data)
        print(f"Data saved to {filename}")

    @staticmethod
    def save_to_json(data: list[dict], filename: str):
        if not data:
            print("No data provided!")
            return

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, default=str, ensure_ascii=False)
        print(f"Data saved to {filename}")


def main():
    generator = MockDataGenerator("ru_RU")

    persons = [generator.generate_person() for _ in range(5)]
    comments = [generator.generate_comment() for _ in range(5)]
    products = [generator.generate_product() for _ in range(5)]

    print("======== Generating Persons ========")
    for person in persons:
        print(person)

    print("\n======== Generating Comments ========")
    for comment in comments:
        print(comment)

    print("\n======== Generating Products ========")
    for product in products:
        print(product)

    generator.save_to_csv(persons, "persons.csv")
    persons = [generator.generate_person() for _ in range(5)]
    generator.save_to_json(persons, "persons.json")


if __name__ == '__main__':
    main()
