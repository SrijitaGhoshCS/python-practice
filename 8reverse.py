#Reverse a text in python using loop
text = "Hello World"
reversed_text = ""

for i in range(len(text) - 1, -1, -1):
    reversed_text += text[i]

print("Original:", text)
print("Reversed:", reversed_text)
