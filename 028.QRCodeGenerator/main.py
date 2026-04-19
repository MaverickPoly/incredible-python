import qrcode
import argparse


def main():
    parser = argparse.ArgumentParser(description="QR Code Generator CLI")

    parser.add_argument("text", help="Text to generate qr code for")

    args = parser.parse_args()

    img = qrcode.make(args.text)
    img.save("qr_code.png")

    img.show()



if __name__ == '__main__':
    main()
