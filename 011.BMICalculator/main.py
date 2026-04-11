import argparse


def main():
    parser = argparse.ArgumentParser(description="BMI Calculator!")

    # Weight in kg
    parser.add_argument("-we", "--weight", type=float,
                        required=True, help="Your weight.")
    # Height in cm
    parser.add_argument("-he", "--height", type=float,
                        required=True, help="Your height.")

    args = parser.parse_args()

    bmi_result = (args.weight) / (args.height * args.height / (100 * 100))

    print(f"BMI result: {round(bmi_result, 1)}")
    if bmi_result < 20:
        print("Underweight")
    elif bmi_result < 25:
        print("Healthy")
    elif bmi_result < 30:
        print("Overweight")
    else:
        print("Obese")


if __name__ == "__main__":
    main()
