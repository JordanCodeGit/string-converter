from tkinter import *
from tkinter import ttk

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

# set window title
root.title("String Converter by Jordan Ang.")

# set window size and position
root.geometry("1000x350+500+200")

# set window style
style = ttk.Style()
style.theme_use("clam")

# create input label
input_label = ttk.Label(root, text="Ujian Sekolah DP1 & DP3")
input_label.pack(pady=10)

# create input label
input_label = ttk.Label(root, text="Enter a string to convert:")
input_label.pack(pady=10)

# create input box
input_box = ttk.Entry(root, width=50, font=("Helvetica", 14))
input_box.pack()

# create option label
option_label = ttk.Label(root, text="Select a conversion option:")
option_label.pack(pady=10)

# create option menu
option_var = StringVar(root)
option_var.set("Select an option")
option_menu = ttk.OptionMenu(root, option_var, "Choose a language", "binary", "hexadecimal", "decimal", "octal", "ascii")
option_menu.config(width=20)
option_menu.pack()

# create convert button
convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.config(width=20)
convert_button.pack(pady=20)

# create output label
output_label = ttk.Label(root, text="Converted string:")
output_label.pack(pady=10)

# create output box
output_box = ttk.Entry(root, width=75, font=("Helvetica", 14))
output_box.pack()

# run the main loop
root.mainloop()
