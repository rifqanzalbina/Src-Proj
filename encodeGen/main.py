import tkinter as tk
from tkinter import simpledialog, messagebox
import functions 
import theme 
from PIL import Image,  ImageTk
from tkinter import ttk
from theme import change_theme

# APP
app = tk.Tk()
app.title("Encoder App")
app.wm_iconbitmap('img/encode.ico')

# FRAME
frame = tk.Frame(app)
frame.grid(row=1, column=0, padx=20, pady=20, sticky='nsew')

top_frame = tk.Frame(app)
top_frame.grid(row=0, column=0, sticky="ew")

# LABEL
text_label = tk.Label(frame, text="Enter your text:")
text_label.grid(row=0, column=0, sticky=tk.W, pady=5)

# TEXT ENTRY
text_entry = tk.Text(frame, height=4, width=50, wrap=tk.WORD)
text_entry.grid(row=1, column=0, columnspan=2, pady=5)

# SHIFT LABEL
shift_label = tk.Label(frame, text="Shift (default is 3):")
shift_label.grid(row=2, column=0, sticky=tk.W, pady=5)

# SHIFT ENTRY
shift_entry = tk.Entry(frame, width=5)
shift_entry.grid(row=2, column=1, sticky=tk.W, pady=5)
shift_entry.insert(tk.END, "3")

# ENCODE 
encode_button = tk.Button(frame, text="Encode", command=lambda: functions.on_encode(text_entry, shift_entry, output_entry, history_listbox))
encode_button.grid(row=3, column=0, pady=5)

# DECODE
decode_button = tk.Button(frame, text="Decode", command=lambda: functions.on_decode(text_entry, shift_entry, output_entry, history_listbox))
decode_button.grid(row=3, column=1, pady=5)

# OUTPUT LABEL
output_label = tk.Label(frame, text="Output:")
output_label.grid(row=4, column=0, sticky=tk.W, pady=5)

# OUTPUT ENTRY
output_entry = tk.Text(frame, height=4, width=50, wrap=tk.WORD, state=tk.DISABLED, bg="white")
output_entry.grid(row=5, column=0, columnspan=2, pady=5)

# COPY BUTTON
copy_button = tk.Button(frame, text="Copy to Clipboard", command=lambda: functions.copy_to_clipboard(output_entry))
copy_button.grid(row=6, column=0, columnspan=1, pady=4)

copy_history_button = tk.Button(frame, text="Copy History", command=lambda: functions.copy_history(history_listbox))
copy_history_button.grid(row=9, column=0, columnspan=2, pady=5)

# HISTORY LISTBOX
history_listbox = tk.Listbox(frame)
history_listbox.grid(row=8, column=0, columnspan=2, pady=5)

# THEME 
theme_option = ttk.Combobox(frame, values=list(theme.themes.keys()))
theme_option.grid(row=6, column=1, columnspan=2, pady=5)
theme_option.set('Default')
theme_option.bind("<<ComboboxSelected>>", lambda e: change_theme(theme_option.get()))

# HELP BUTTON
help_button = tk.Button(top_frame, text="Help", command=lambda: functions.show_help(language_option))
help_button.grid(row=0, column=0, sticky="w") 

#LANGUAGE OPTION
language_option = ttk.Combobox(top_frame, values=["English"])
language_option.grid(row=0, column=1, sticky="e")  
language_option.set("English")

# RUNNING APP
app.mainloop()
