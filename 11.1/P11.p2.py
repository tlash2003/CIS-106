
def get_input():
    r = input("Enter a line of text: ")
    return r

def process_text(text):
   text = text.strip()
   text = ' '.join(text.split())
   return text

def reverse_text(text):
    return text[::-1]

def print_output(text):
    print(text)


#MAIN
user_input = get_input()
processed_text = process_text(user_input)
reversed_text = reverse_text(processed_text)
print_output(reversed_text)

