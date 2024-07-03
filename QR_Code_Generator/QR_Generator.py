import qrcode as qrc
import tkinter as tk
from tkinter import ttk, colorchooser, messagebox
from PIL import Image, ImageTk
import unittest

def generate_qr():
    global img
    try:
        link = link_entry.get()
        if not link:
            raise ValueError("Missing Link")
    name = name_entry.get()
    version = int(version_slider.get())
    box_size = int(box_size_slider.get())
    border = int(border_slider.get())
    fill_color = fill_color_button.cget('bg')
    back_color = back_color_button.cget('bg')

    if not (1 <= version <= 40):
        messagebox.showerror("Invalid Version", "Version must be between 1 and 40.")
        return
    if not (1 <= box_size <= 50):
        messagebox.showerror("Invalid Box Size", "Box size must be between 1 and 50.")
        return
    if not (1 <= border <= 10):
        messagebox.showerror("Invalid Border Size", "Border size must be between 1 and 10.")
        return

    qr = qrc.QRCode(
        version=version,
        error_correction=qrc.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    preview_img = img.resize((200, 200))
    preview_img_tk = ImageTk.PhotoImage(preview_img)
    preview_label.config(image=preview_img_tk)
    preview_label.image = preview_img_tk

    except ValueError as ve:
        messagebox.showerror("Input Error: ", str(ve))
    except ValueError as e:
        messagebox.showerror("Error: ", str(e))

def save_qr():
     try:
        name = name_entry.get()
        if not name:
            raise ValueError("Please enter a name.")
        img.save(name + '.png')
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error", str(e))

def choose_fill_color():
    color_code = colorchooser.askcolor(title="Choose Fill Color")
    fill_color_button.config(bg=color_code[1])

def choose_back_color():
    color_code = colorchooser.askcolor(title="Choose Background Color")
    back_color_button.config(bg=color_code[1])

# Creation of main window
root = tk.Tk()
root.title("QR Code Generator")

# Link Input
tk.Label(root, text="Link: ").grid(row=0, column=0, padx=10, pady=5)
link_entry = tk.Entry(root, width=40)
link_entry.grid(row=0, column=1, padx=10, pady=5)

# Name Input
tk.Label(root, text="Name: ").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root, width=40)
name_entry.grid(row=1, column=1, padx=10, pady=5)

# Version Slider
tk.Label(root, text="Version: ").grid(row=2, column=0, padx=10, pady=5)
version_slider = tk.Scale(root, from_=1, to=40, orient='horizontal')
version_slider.set(20)
version_slider.grid(row=2, column=1, padx=10, pady=5)

# Box Size Slider
tk.Label(root, text="Box Size: ").grid(row=3, column=0, padx=10, pady=5)
box_size_slider = tk.Scale(root, from_=1, to=50, orient='horizontal')
box_size_slider.set(25)
box_size_slider.grid(row=3, column=1, padx=10, pady=5)

# Border Size Slider
tk.Label(root, text="Border Size: ").grid(row=4, column=0, padx=10, pady=5)
border_slider = tk.Scale(root, from_=1, to=10, orient='horizontal')
border_slider.set(5)
border_slider.grid(row=4, column=1, padx=10, pady=5)

# Fill Color Button
tk.Label(root, text="Fill Color:").grid(row=5, column=0, padx=10, pady=5)
fill_color_button = tk.Button(root, bg='black', width=20, command=choose_fill_color)
fill_color_button.grid(row=5, column=1, padx=10, pady=5)

# Background Color Button
tk.Label(root, text="Background Color:").grid(row=6, column=0, padx=10, pady=5)
back_color_button = tk.Button(root, bg='white', width=20, command=choose_back_color)
back_color_button.grid(row=6, column=1, padx=10, pady=5)

# Generate Button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.grid(row=7, column=0, columnspan=2, pady=10)

# Preview Label
preview_label = tk.Label(root)
preview_label.grid(row=8, column=0, columnspan=2, pady=10)

# Save Button
save_button = tk.Button(root, text="Save QR Code", command=save_qr)
save_button.grid(row=9, column=0, columnspan=2, pady=10)

root.mainloop()
