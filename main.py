import tkinter as tk
from tkinter import filedialog, simpledialog
import subprocess
import os

def browse_file():
    filename = filedialog.askopenfilename()
    if filename:
        file_entry.delete(0, tk.END)
        file_entry.insert(0, filename)

def convert_to_exe():
    filepath = file_entry.get()
    if filepath:
        try:
            # Prompt user for destination folder
            dest_path = filedialog.askdirectory()
            if dest_path:
                # Create folder "Copyright by Ramishka" inside specified path
                dest_folder = os.path.join(dest_path, "Copyright by Ramishka")
                if not os.path.exists(dest_folder):
                    os.makedirs(dest_folder)
                
                # Display processing message
                result_label.config(text="Converting...")
                result_label.update()

                # Convert to .exe and move it to the specified folder
                subprocess.run(["pyinstaller", "--onefile", "--noconsole", filepath])
                exe_path = os.path.join("dist", os.path.basename(filepath).replace(".py", ".exe"))
                os.rename(exe_path, os.path.join(dest_folder, os.path.basename(exe_path)))

                result_label.config(text="Conversion successful!")
            else:
                result_label.config(text="Please select a destination folder.")
        except Exception as e:
            result_label.config(text=f"Error: {e}")
    else:
        result_label.config(text="Please select a file first.")

def reset():
    file_entry.delete(0, tk.END)
    result_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Python to Exe Converter")

# Create widgets
file_label = tk.Label(root, text="Select Python file:")
file_label.pack()

file_entry = tk.Entry(root, width=50)
file_entry.pack()

browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

convert_button = tk.Button(root, text="Convert to .exe", command=convert_to_exe)
convert_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
