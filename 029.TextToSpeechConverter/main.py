import argparse
import pyttsx3 as tts


def main():
    engine = tts.init()

    parser = argparse.ArgumentParser(description="Text To Speech CLI")

    parser.add_argument("text", help="Text to speak")

    args = parser.parse_args()
    engine.say(args.text)
    engine.runAndWait()
    engine.save_to_file(args.text, "speech.mp3")
    engine.runAndWait()


if __name__ == '__main__':
    main()
