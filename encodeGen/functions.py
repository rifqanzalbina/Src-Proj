import string
from collections import deque
import tkinter as tk
from tkinter import messagebox, ttk
import pyperclip
import mysql.connector

history = []

# HELP
def help_command(language):
    if language == "Indonesian":
        help_text = "Teks bantuan dalam Bahasa Indonesia"
    else:
        help_text = "Help text in English"
    return help_text

# SHOWING HELP
def show_help(language_option):
    lang = language_option.get()
    help_text = help_command(lang)
    if lang == "Indonesia":   
        help_text = """
        Cara Menggunakan Aplikasi
        1. Masukkan teks yang ingin Anda enkripsi atau dekripsi.
        2. Masukkan Jumlah shift (default adalah 3).
        3. Klik 'Encode' untuk mengenkripsi teks, atau 'Decode' untuk mendekripsi teks.
        4. Teks hasil enkripsi atau dekripsi akan ditampilkan di Bawah.
        5. Anda dapat menyalin teks ke clipboard dengan Mengklik 'Copy to Clipboard'
    """
    else :
        help_text = """
        How To use Application 
        1. Enter the text you want to encrypt or decrypt.
        2. Enter the shift amount (default is 3).
        3. Click 'Encode' to encrypt the text, or 'Decode' to decrypt the text.
        4. The encrypted or decrypted text will be displayed below.
        5. You can copy the text to the clipboard by clicking 'Coopy to Clipboard'.
    """
    messagebox.showinfo("Bantuan / Help", help_text)

# COPY FUNCTIONS
def copy_to_clipboard(outputt_entry):
    text = outputt_entry.get("1.0", tk.END).strip()
    pyperclip.copy(text)

def copy_history(history_listbox):
    selected = history_listbox.curselection()  
    if selected:  
        text = history_listbox.get(selected[0]) 
    else:
        text = "\n".join(history_listbox.get(0, tk.END)) 
    pyperclip.copy(text)


# ENCIPHER
def caesar_encipher(text, shift=3):
    alphabet = string.ascii_lowercase
    alphabet_upper = string.ascii_uppercase
    rotated = deque(alphabet)
    rotated.rotate(-shift)
    rotated_upper = deque(alphabet_upper)
    rotated_upper.rotate(-shift)
    translation = str.maketrans(alphabet + alphabet_upper, "".join(rotated) + "".join(rotated_upper))
    return text.translate(translation)  

# DECIPHER
def caesar_decipher(text, shift=3):
    return caesar_encipher(text, -shift)



# ENCODE
def on_encode(text_entry, shift_entry, output_entry, history_listbox):
    shift = shift_entry.get()
    if not is_valid_shift(shift):
        tk.messagebox.showerror("Invalid Input", "Shift must be a number")
        return
    
    text = text_entry.get("1.0", tk.END).strip()
    encoded = caesar_encipher(text, int(shift))
    output_entry.config(state=tk.NORMAL) 
    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, encoded)
    output_entry.config(state=tk.DISABLED) 

    # HISTORY
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())

    # UPDATE HISTORY
    history.append(f"Encoded : {encoded}")
    update_history(history_listbox)


# DECODE
def on_decode(text_entry, shift_entry, output_entry, history_listbox):
    shift = shift_entry.get()
    if not is_valid_shift(shift):
        tk.messagebox.showerror("Invalid Input", "Shift must be a number")
        return
    
    text = text_entry.get("1.0", tk.END).strip()
    decoded = caesar_decipher(text, int(shift))
    output_entry.config(state=tk.NORMAL) 
    output_entry.delete("1.0", tk.END)
    output_entry.insert(tk.END, decoded)
    output_entry.config(state=tk.DISABLED)

    # HISTORY
    text = text_entry.get("1.0", tk.END).strip()
    shift = int(shift_entry.get())

    # UPDATE HISTORY
    history.append(f"Decoded : {decoded}" )
    update_history(history_listbox)



# HISTORY
def update_history(history_listbox):
    history_listbox.delete(0, tk.END)
    for item in history:
        history_listbox.insert(tk.END, item)

# VALID
def is_valid_shift(shift):
    try:
        int(shift)
        return True
    except ValueError:
        return False
    





