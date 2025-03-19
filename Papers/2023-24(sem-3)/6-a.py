number_to_text=["zero","one","two","three","four","five","six","seven","eight","nine"]
def update_text(text):
    text_list = list(text)
    for i in range(len(text)):
        if text_list[i].isdigit():
            digit = int(text_list[i])
            text_list[i] = number_to_text[digit] + " "
        result = ''.join(text_list)
        return ''.join(result.split())

with open("mint.txt","r") as file:
    content = file.read()

new_text = update_text(content)

with open("mint.txt","w") as file:
    file.write(new_text)