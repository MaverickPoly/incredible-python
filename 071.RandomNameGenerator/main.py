import os

import dotenv
import requests


dotenv.load_dotenv()
URL = "https://api.api-ninjas.com/v1/babynames?gender=neutral"
API_KEY = os.getenv("API_NINJAS_API")


def main():
    try:
        api_header = {"X-Api-Key": API_KEY}
        params_girl = {"gender": "girl"}
        params_boy = {"gender": "boy"}

        response_girls = requests.get(URL, params=params_girl, headers=api_header)
        response_girls.raise_for_status()

        response_boys = requests.get(URL, params=params_boy, headers=api_header)
        response_boys.raise_for_status()

        girl_names = response_girls.json()
        boy_names = response_boys.json()

        size = len(girl_names)

        girl_names_modified = [f"{girl_names[i]} {girl_names[size//2+i]}" for i in range(size//2)]
        boy_names_modified = [f"{boy_names[i]} {boy_names[size//2+i]}" for i in range(size//2)]

        print("====== Girl Names ======")
        for girl_name in girl_names_modified:
            print(girl_name)

        print()
        print("====== Boy Names ======")
        for boy_name in boy_names_modified:
            print(boy_name)
    except Exception as e:
            print(f"Error fetching names: {e}")


if __name__ == '__main__':
    main()
