print("TEXT COMPRESSION")

text = input("Enter text to compress: ")
if text == "":
    print("Compressed text: ")
    raise SystemExit

compressed = ""
current = text[0]
count = 1

for character in text[1:]:
    if character == current:
        count += 1
    else:
        compressed += current + str(count)
        current = character
        count = 1

compressed += current + str(count)
print("Compressed text:", compressed)
