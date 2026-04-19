from PIL import Image
import argparse


def main():
     parser = argparse.ArgumentParser(description="Image Resizer")

     parser.add_argument("-i", "--image", required=True, help="Image path")

     parser.add_argument("width", type=int, help="Image width")
     parser.add_argument("height", type=int, help="Image height")

     args = parser.parse_args()

     img = Image.open(args.image)
     print("Initial size:")
     print(img.width, img.height)

     img = img.resize((args.width, args.height), Image.Resampling.LANCZOS)
     img.save(args.image)


if __name__ == '__main__':
    main()
