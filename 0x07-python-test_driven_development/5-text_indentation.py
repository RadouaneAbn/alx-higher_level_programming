
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    L = len(text)
    i = 0
    while i < L:
        if text[i] in [".", "?", ":"]:
            print(text[i] + "\n")
            if i + 1 < L and text[i + 1] == " ":
                i += 1
        else:
            print(text[i], end='')
        i += 1