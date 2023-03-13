from tkinter import *

def convert():
    input_str = input_box.get()
    option = option_var.get()
    if option == 'binary':
        binary = ''.join(format(ord(c), '08b') for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, binary)
    elif option == 'hexadecimal':
        hexadecimal = ''.join(hex(ord(c))[2:] for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, hexadecimal)
    elif option == 'decimal':
        decimal = ''.join(str(ord(c)) for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, decimal)
    elif option == 'octal':
        octal = ''.join(oct(ord(c))[2:] for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, octal)
    elif option == 'ascii':
        ascii_code = ''.join(str(ord(c)) + ' ' for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, ascii_code)
    else:
        output_box.delete(0, END)
        output_box.insert(0, "Invalid option selected.")

root = Tk()

input_label = Label(root, text="Enter a string to convert:")
input_label.pack()

input_box = Entry(root)
input_box.pack()

option_var = StringVar(root)
option_var.set("Select an option")

option_menu = OptionMenu(root, option_var, "binary", "hexadecimal", "decimal", "octal", "ascii")
option_menu.pack()

convert_button = Button(root, text="Convert", command=convert)
convert_button.pack()

output_label = Label(root, text="Converted string:")
output_label.pack()

output_box = Entry(root, width=200)
output_box.pack()

root.mainloop()
