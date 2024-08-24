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
    
    root = tk.Tk()
    root.withdraw()
    
    
    file_path = filedialog.askopenfilename(title="Select a text file", filetypes=[("Text files", "*.txt")])
    
    if file_path:
        
        chars_to_remove = input("Enter the characters you want to remove separated by a comma: ")
        
        
        characters = [char.strip() for char in chars_to_remove.split(',')]
        
       
        remove_characters_from_file(file_path, characters)
        
        print("Characters removed successfully.")
    else:
        print("No file selected.")

if __name__ == "__main__":
    main()
