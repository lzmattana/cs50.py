# - Hello :) > Hello 🙂
# - Goodbye :( > Goodbye 🙁
# - Hello :) Goodbye :( > Hello 🙂 Goodbye 🙁

text = input()
text = text.replace(":)", "🙂")
text = text.replace(":(", "🙁")
print(text)