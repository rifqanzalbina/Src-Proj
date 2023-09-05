import pyqrcode
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
 
def generate_qr_code():
    data = entry.get()
    if data:
        qr = pyqrcode.create(data)
        qr_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if qr_file_path:
            qr.png(qr_file_path, scale=8)
            img = Image.open(qr_file_path)
            img = img.resize((300, 300), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            label_img.config(image=img)
            label_img.photo = img
            label_img.grid(column=0, row=3, columnspan=2, pady=20)
    else:
        messagebox.showwarning("Input Error", "Please enter some text or link")

window = tk.Tk()
window.title("QR Code Generator")
window.geometry("400x500")
window.configure(bg="blue")

label = tk.Label(window, text="Enter the text or link to generate QR code:", bg="blue", fg="white")
label.grid(column=0, row=0, columnspan=2, padx=10, pady=10)


entry = tk.Entry(window, width=40)
entry.grid(column=0, row=1, columnspan=2, padx=10, pady=10)

button = tk.Button(window, text="Generate QR Code", command=generate_qr_code, width=20)
button.grid(column=0, row=2, columnspan=2)

label_img = tk.Label(window, bg="blue")
label_img.grid(column=0, row=3, columnspan=2, pady=20)

window.mainloop()
