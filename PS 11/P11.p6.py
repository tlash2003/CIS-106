
def get_user_input():
    text = input("Enter a line of text: ")
    num_chars = int(input("Enter the number of characters per line: "))
    num_lines = int(input("Enter the number of lines to print: "))
    direction = input("Enter the scroll direction (left or right): ").lower()
    return text, num_chars, num_lines, direction

def scroll_text(text, num_chars, num_lines, direction):
    text = (text * ((num_chars // len(text)) + 1))[:num_chars]
    for _ in range(num_lines):
        print(text)
        if direction == "left":
            text = text[1:] + text[0]
        elif direction == "right":
            text = text[-1] + text[:-1]

#MAIN
text, num_chars, num_lines, direction = get_user_input()
scroll_text(text, num_chars, num_lines, direction)


