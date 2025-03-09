import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

# Global variables
file_path = None  # Stores selected file path
dark_mode = True  # Default mode

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.webp;*.png;*.jpg;*.jpeg;*.ico")])
    if file_path:
        lbl_file.config(text=os.path.basename(file_path))

def convert_image(format_choice):
    global file_path
    if not file_path:
        messagebox.showerror("Error", "No file selected")
        return
    
    output_dir = filedialog.askdirectory(title="Choose Output Directory")
    if not output_dir:
        return
    
    formats = {"PNG": "png", "JPEG": "jpg", "WEBP": "webp", "ICO": "ico"}
    base_name = os.path.splitext(os.path.basename(file_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.{formats[format_choice]}")
    
    while os.path.exists(output_path):
        output_path = os.path.join(output_dir, f"{base_name}t.{formats[format_choice]}")
    
    try:
        img = Image.open(file_path)
        img = img.convert("RGBA")
        img.save(output_path, format_choice)
        messagebox.showinfo("Success", f"Converted and saved to: {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert: {e}")

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    bg_color = "#1E1E1E" if dark_mode else "#F0F0F0"
    fg_color = "white" if dark_mode else "black"
    button_bg = "#5865F2" if dark_mode else "#A0A0A0"
    format_button_bg = "#57F287" if dark_mode else "#4CAF50"
    
    root.configure(bg=bg_color)
    lbl_title.config(bg=bg_color, fg=fg_color)
    lbl_file.config(bg=bg_color, fg=fg_color)
    lbl_format.config(bg=bg_color, fg=fg_color)
    btn_theme.config(bg=button_bg, fg=fg_color)
    btn_select.config(bg=button_bg, fg=fg_color)
    for btn in frame_buttons.winfo_children():
        btn.config(bg=format_button_bg, fg="white", borderwidth=0, relief="flat", highlightthickness=0, 
                   padx=10, pady=8, bd=0, font=("Segoe UI", 12, "bold"), cursor="hand2", activebackground="#45D06A", 
                   activeforeground="white", border=0, highlightcolor=format_button_bg)

# GUI setup
root = tk.Tk()
root.title("Image Converter")
root.geometry("550x500")
root.configure(bg="#1E1E1E")
root.resizable(False, False)

# Style adjustments
lbl_title = tk.Label(root, text="Image Converter", font=("Segoe UI", 18, "bold"), fg="white", bg="#1E1E1E")
lbl_title.pack(pady=15)

btn_select = tk.Button(root, text="Choose Image File", command=select_file, bg="#5865F2", fg="white", font=("Segoe UI", 14, "bold"), 
                       relief="flat", borderwidth=0, highlightthickness=0, padx=20, pady=10, bd=0, 
                       cursor="hand2", activebackground="#4752C4", activeforeground="white", border=0)
btn_select.pack(pady=10)

lbl_file = tk.Label(root, text="No file selected", fg="white", bg="#1E1E1E", font=("Segoe UI", 10))
lbl_file.pack()

lbl_format = tk.Label(root, text="Output File Format", font=("Segoe UI", 12, "bold"), fg="white", bg="#1E1E1E")
lbl_format.pack(pady=10)

frame_buttons = tk.Frame(root, bg="#1E1E1E")
frame_buttons.pack(pady=10)

formats = ["PNG", "JPEG", "WEBP", "ICO"]
for fmt in formats:
    btn = tk.Button(frame_buttons, text=fmt, command=lambda f=fmt: convert_image(f), bg="#57F287", fg="white", font=("Segoe UI", 12, "bold"), 
                    width=10, relief="flat", borderwidth=0, highlightthickness=0, padx=10, pady=8, bd=0, cursor="hand2", 
                    activebackground="#45D06A", activeforeground="white", border=0)
    btn.pack(side=tk.LEFT, padx=8)

btn_theme = tk.Button(root, text="Toggle Dark Mode", command=toggle_theme, bg="#5865F2", fg="white", font=("Segoe UI", 12, "bold"), 
                      relief="flat", borderwidth=0, highlightthickness=0, padx=20, pady=10, bd=0, cursor="hand2", 
                      activebackground="#4752C4", activeforeground="white", border=0)
btn_theme.pack(pady=15)

root.mainloop()
