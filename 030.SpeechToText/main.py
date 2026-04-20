import speech_recognition


running = True
recognizer = speech_recognition.Recognizer()

while running:
    with speech_recognition.Microphone() as source:
        print("Listening...")
        audio_text = recognizer.listen(source)
        print(audio_text.sample_width)

        try:
            text = recognizer.recognize_google(audio_text)
            print(text)
        except Exception as e:
            print(e)
            print("Sorry, did not hear that!")
