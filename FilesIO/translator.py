from translate import Translator

translator = Translator(to_lang="ja")

try:
    with open("./test.txt", "r") as f:
        text = f.read()
        translation = translator.translate(text)
        print(translation)

        with open("./test-ja.txt", "w") as f2:
            f2.write(translation)

except FileNotFoundError as e:
    print("Check your file path.")
