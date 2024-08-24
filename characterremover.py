import tkinter as tk
from tkinter import filedialog

def remove_characters_from_file(file_path, characters):
    with open(file_path, 'r') as file:
        content = file.read()
    
    for char in characters:
        content = content.replace(char, "")
    
    with open(file_path, 'w') as file:
        file.write(content)

def main():
    # Create a Tkinter root window (it will remain hidden)
    root = tk.Tk()
    root.withdraw()
    
    # Ask the user to select a text file
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        # Ask the user to input the characters to remove
        chars_to_remove = input("Enter the characters you want to remove separated by a comma: ")
        
        # Split the input by commas to get a list of characters
        characters = [char.strip() for char in chars_to_remove.split(',')]
        
        # Remove the characters from the file
        remove_characters_from_file(file_path, characters)
        
        print("Characters removed successfully.")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
