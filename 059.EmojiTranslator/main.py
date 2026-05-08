import emoji


print("Enter your text with aliases for your emojis...")
text = input()
final_text = emoji.emojize(text)

print(final_text)
