import os


DIR = "bulk_files/"

def main():
    files = {}
    for filename in os.listdir(DIR):
        extension = os.path.splitext(filename)[1].strip(".")
        if extension in files:
            files[extension].append(filename)
        else:
            files[extension] = [filename]

    count = 0
    for extension, filenames in files.items():
        os.makedirs(os.path.join(DIR, extension), exist_ok=True)

        for filename in filenames:
            source = DIR + filename
            destination = os.path.join(DIR, extension, filename)

            os.rename(source, destination)
            count += 1

    print(f"Total bulk_files moved: {count}")

if __name__ == '__main__':
    main()
