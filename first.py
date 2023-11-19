phrase = "abcde"
index = 0
while index < len(phrase):
    char = phrase[index]
    if char == 'd':
        index += 1  # must still iterate index to avoid infinite loop
        break  # end iterations if the character is 'd'
    print(char)
    index += 1
