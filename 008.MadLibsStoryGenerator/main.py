def play_mad_libs():
    print("------ Welcome to the Mad Libs Generator! ---")
    print("Please provide the following words:\n")

    adj1 = input("Adjective: ")
    noun1 = input("Noun (Person/Place/Thing): ")
    verb1 = input("Verb (Present Tense): ")
    adj2 = input("Adjective: ")
    place = input("A Place: ")
    verb2 = input("Verb ending in 'ing': ")

    story = f"""
    Today was an incredibly {adj1} day!
    I decided to take my favourite {noun1} and {verb1} all the way to {place}.
    The weather was {adj2}, so I spent most of my time {verb2}.
    It was a day I'wll never forget!
    """

    print("\n---- Your story ----")
    print(story)


if __name__ == "__main__":
    play_mad_libs()
