import string


def check_strength(psw: str):
    punctuation = string.punctuation

    includes_uppercase = False
    includes_lowercase = False
    includes_digits = False
    includes_punctuation = False

    for char in psw:
        if char.isupper():
            includes_uppercase = True
        elif char.islower():
            includes_lowercase = True
        elif char.isdigit():
            includes_digits = True
        elif char in punctuation:
            includes_punctuation = True

    requirements = []
    if not includes_uppercase: requirements.append("Missing uppercase")
    if not includes_lowercase: requirements.append("Missing lowercase")
    if not includes_digits: requirements.append("Missing digits")
    if not includes_punctuation: requirements.append("Missing punctuation")

    return requirements


if __name__ == '__main__':
    password = input("Enter password: ")
    result = check_strength(password)

    if len(result) == 0:
        print("Password is strong!")
    else:
        print("Password is weak!")
        for requirement in result:
            print(f"- {requirement}")
