import tkinter as tk
import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox, colorchooser, font

class PyNotepad:

    def __init__(self, root):
        self.root = root
        self.root.title("PyNotepad")

        self.current_font = 'Arial'
        self.current_size = 12
        self.current_color = 'black'

        # List Color
        self.colors = ['black','blue','gray','brown']
        self.color_index = 0

        # Text area
        self.textarea = tk.Text(self.root, wrap='word', undo=True, font=(self.current_font, self.current_size))
        self.textarea.pack(expand=1, fill='both')
        self.textarea.bind('<Key>', self.change_color_on_type)

        # Menu bar
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # File menu
        self.file_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)

        # Edit menu
        self.edit_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.textarea.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.textarea.edit_redo)
        self.edit_menu.add_command(label="Cut", command=self.cut_text)
        self.edit_menu.add_command(label="Copy", command=self.copy_text)
        self.edit_menu.add_command(label="Paste", command=self.paste_text)
        self.edit_menu.add_command(label="Search", command=self.search_text)

        # View menu
        self.view_menu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label="View", menu=self.view_menu)
        self.view_menu.add_command(label="Dark Mode", command=self.dark_mode)
        self.view_menu.add_command(label="Light Mode", command=self.light_mode)
        self.view_menu.add_command(label="Choose Font Color", command=self.choose_color)
        self.view_menu.add_command(label="Choose Font", command=self.choose_font)

        # Auto-save feature every 10 seconds
        self.root.after(10000, self.auto_save)

        

    def new_file(self):
        self.textarea.delete(1.0, tk.END)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, 'r') as file:
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.INSERT, file.read())

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"),
                                                            ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.textarea.get(1.0, tk.END))

    def auto_save(self):
        # For simplicity, we're saving to a default location and filename
        with open("autosave.txt", 'w') as file:
            file.write(self.textarea.get(1.0, tk.END))
        self.root.after(10000, self.auto_save)

    def cut_text(self):
        self.textarea.event_generate(("<<Cut>>"))

    def copy_text(self):
        self.textarea.event_generate(("<<Copy>>"))

    def paste_text(self):
        self.textarea.event_generate(("<<Paste>>"))

    def search_text(self):
        find_string = simpledialog.askstring("Find...", "Enter text")
        text = self.textarea.get(1.0, tk.END)

        occurrences = text.upper().count(find_string.upper())

        if text.upper().count(find_string.upper()) > 0:
            label = messagebox.showinfo("Results", f"'{find_string}' found {occurrences} times in the document.")
        else:
            label = messagebox.showinfo("Results", f"'{find_string}' not found in the document.")

    def dark_mode(self):
        self.textarea.config(bg="black", fg="white")

    def light_mode(self):
        self.textarea.config(bg="white", fg="black")

    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.textarea.config(fg=color)

    def choose_font(self, root):
        chosen_font = font.askfont(root)
        if chosen_font:
            self.textarea.config(font=(chosen_font['family'], chosen_font['size']))

    def change_color_on_type(self, event):
        """
        Change the color of the character being typed.
        """
        # Increment the color index
        self.color_index += 1
        if self.color_index >= len(self.colors):
            self.color_index = 0

        # Change the color of the last character typed
        self.textarea.tag_add("color", "insert -1c", "insert")
        self.textarea.tag_config("color", foreground=self.colors[self.color_index])

    

