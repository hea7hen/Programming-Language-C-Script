import basic

while True:
    text = input("basic> ")
    if text == "quit":
        break
    result, error = basic.run(text)
    if error:
        print(error.as_string())
    else:
        print(result)

