#Made by Jordan Angkawijaya
#XII RPL 4
#Ujian Sekolah DP1 & DP3

#Import Library
import tkinter as tk
from tkinter import ttk
from tkinter import *

# Define the main font
main_font = ("Helvetica", 12)

# Define the ASCII conversion function
def ascii_conversion(string):
    ascii_values = []
    for char in string:
        ascii_values.append(ord(char))
    return ascii_values

# Define the base conversion functions
def convert_base(num, base):
    if base == 2:
        return bin(num)
    elif base == 8:
        return oct(num)
    elif base == 10:
        return str(num)
    elif base == 16:
        return hex(num)

# Define the base conversion function
def base_conversion(num, from_base, to_base):
    if from_base == 10:
        decimal_num = int(num)
    elif from_base == 2:
        decimal_num = int(num, 2)
    elif from_base == 8:
        decimal_num = int(num, 8)
    elif from_base == 16:
        decimal_num = int(num, 16)

    if to_base == 10:
        return str(decimal_num)
    else:
        return convert_base(decimal_num, to_base)

# Define the string to ASCII event handler
def handle_string_to_ascii():
    string = input_string.get()
    ascii_values = ascii_conversion(string)
    ascii_result.config(text="The ASCII values for the string are:\n" + ", ".join(str(value) for value in ascii_values), font=("Helvetica", 18))

# Define the base conversion event handler
def handle_base_conversion():
    num = input_num.get()
    from_base = int(from_base_var.get())
    to_base = int(to_base_var.get())
    converted_num = base_conversion(num, from_base, to_base)
    base_result.config(text="The converted number is: " + converted_num)

# Define the conversion function
def convert():
    input_str = input_box.get()
    option = option_var.get()

    # define the binary conversion function
    if option == 'binary':
        binary = ''.join(format(ord(c), '08b') for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, binary)

    # define the hexadecimal conversion function
    elif option == 'hexadecimal':
        hexadecimal = ''.join(hex(ord(c))[2:] for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, hexadecimal)

    # define the decimal conversion function
    elif option == 'decimal':
        decimal = ''.join(str(ord(c)) for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, decimal)

    # define the octal conversion function
    elif option == 'octal':
        octal = ''.join(oct(ord(c))[2:] for c in input_str)
        output_box.delete(0, END)
        output_box.insert(0, octal)

    # define the invalid option function
    else:
        output_box.delete(0, END)
        output_box.insert(0, "Invalid option selected.")

# Create the main window
root = tk.Tk()
root.title("Python Conversion by Jordan Ang.")
root.geometry("900x500")

# Define the notebook style
style = ttk.Style()
style.theme_use("default")
style.configure("TNotebook", background="white")
style.configure("TNotebook.Tab", background="gray", foreground="white", font=main_font)
style.map("TNotebook.Tab", background=[("selected", "black")])

# Create the notebook
notebook = ttk.Notebook(root)

### ----Create the ASCII conversion tab---- ###
ascii_tab = ttk.Frame(notebook)
notebook.add(ascii_tab, text="ASCII Conversion")
# Create the label for the string to convert
input_label = tk.Label(ascii_tab, text="Enter the string to convert to ASCII:", font=main_font)
input_label.pack(pady=10)
# Create the entry for the string to convert
input_string = tk.Entry(ascii_tab, font=main_font)
input_string.pack(padx=10)
# Create the button to convert the string
ascii_button = tk.Button(ascii_tab, text="Convert", font=main_font, command=handle_string_to_ascii)
ascii_button.pack(pady=10)
# Create the label for the result
ascii_result = tk.Label(ascii_tab, text="", font=main_font)
ascii_result.pack(pady=10)


### ----Create the base conversion tab---- ###
base_tab = ttk.Frame(notebook)
notebook.add(base_tab, text="Base Conversion")
# Create the label for the number to convert
num_label = tk.Label(base_tab, text="Enter the number to convert:", font=main_font)
num_label.pack(pady=10)
# Create the entry for the number to convert
input_num = tk.Entry(base_tab, font=main_font)
input_num.pack(padx=10, pady=10)
# Create the label for binary information
from_base_label = ttk.Label(base_tab, text="2: Binary", font=main_font)
from_base_label.pack(pady=1)
# Create the label for octal information
from_base_label = ttk.Label(base_tab, text="8: Octal", font=main_font)
from_base_label.pack(pady=1)
# Create the label for decimal information
from_base_label = ttk.Label(base_tab, text="10: Decimal", font=main_font)
from_base_label.pack(pady=1)
# Create the label for hexadecimal information
from_base_label = ttk.Label(base_tab, text="16: Hexadecimal", font=main_font)
from_base_label.pack(pady=1)
# Create the label for the base to convert from
from_base_label = tk.Label(base_tab, text="Enter the base of the number:", font=main_font)
from_base_label.pack(pady=10)
# Create the dropdown for the base to convert from
from_base_var = tk.StringVar(value="Pick...")
from_base_dropdown = tk.OptionMenu(base_tab, from_base_var, "2", "8", "10", "16")
from_base_dropdown.pack(padx=10)
# Create the label for the base to convert to
to_base_label = tk.Label(base_tab, text="Enter the base to convert to:", font=main_font)
to_base_label.pack(pady=10)
# Create the dropdown for the base to convert to
to_base_var = tk.StringVar(value="Pick...")
to_base_dropdown = tk.OptionMenu(base_tab, to_base_var, "2", "8", "10", "16")
to_base_dropdown.pack(padx=10)
# Create the button to convert the number
base_button = tk.Button(base_tab, text="Convert", command=handle_base_conversion, font=main_font)
base_button.pack(pady=10)
# Create the label for the result
base_result = tk.Label(base_tab, text="", font=("Helvetica", 20))
base_result.pack(pady=10)


### ----Create the string to base conversion tab---- ###
stringbase_tab = ttk.Frame(notebook)
notebook.add(stringbase_tab, text="String to Base Conversion")
# create input label
input_label = ttk.Label(stringbase_tab, text="Enter a string to convert:", font=main_font)
input_label.pack(pady=10)
# create input box
input_box = ttk.Entry(stringbase_tab, width=50, font=main_font)
input_box.pack()
# create option label
option_label = ttk.Label(stringbase_tab, text="Select a conversion option:", font=main_font)
option_label.pack(pady=10)
# create option menu
option_var = StringVar(stringbase_tab)
option_var.set("Select an option")
option_menu = ttk.OptionMenu(stringbase_tab, option_var, "Choose a number system", "binary", "hexadecimal", "decimal", "octal")
option_menu.config(width=30)
option_menu.pack()
# create convert button
convert_button = ttk.Button(stringbase_tab, text="Convert", command=convert)
convert_button.config(width=20)
convert_button.pack(pady=20)
# create output label
output_label = ttk.Label(stringbase_tab, text="Converted string:", font=main_font)
output_label.pack(pady=10)
# create output box
output_box = ttk.Entry(stringbase_tab, width=75, font=main_font)
output_box.pack()


# Create the notebook pack
notebook.pack(expand=True, fill="both")
root.mainloop()