import tkinter as tk
from tkinter import ttk
from functions import *

def change_theme(theme, app, text_entry, output_entry):
    color_scheme = themes.get(theme, themes['Default'])
    app.configure(bg=color_scheme['bg'])
    text_entry.configure(bg=color_scheme['text_bg'], fg=color_scheme['text_fg'])
    output_entry.configure(bg=color_scheme['text_bg'], fg=color_scheme['text_fg'])

themes = {
    'Default': {'bg': 'white', 'text_bg': 'white', 'text_fg': 'black'},
    'Dark': {'bg': 'black', 'text_bg': 'grey', 'text_fg': 'white'},
    'Green': {'bg': 'green', 'text_bg': 'green', 'text_fg' : 'white'}
}

