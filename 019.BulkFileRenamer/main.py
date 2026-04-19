import os

DIR = "./files/"


def main():
    for index, filename in enumerate(os.listdir(DIR)):
        extension = os.path.splitext(filename)[1]
        new_file = f"hii_{index}{extension}"

        print(filename)
        print(extension)

        source = DIR + filename
        destination = DIR + new_file

        os.rename(source, destination)


if __name__ == '__main__':
    main()
