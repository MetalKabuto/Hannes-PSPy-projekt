import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

#active_file används för att få sökvägen till filen man öppnar eller sparar som utanför funktionerna 'open_file' och 'save_file_as'
active_file = ""
def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if not filepath:
        return
    txt_edit.delete("1.0", tk.END)
    with open(filepath, mode="r", encoding="utf-8") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Simple Text Editor - {filepath}")
    global active_file
    active_file = filepath

def save_file():
    #om active_file har ett värde sparas texten i editorn till den sökvägen
    if active_file != "":
        with open(active_file, mode="w", encoding="utf-8") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)

def save_file_as():
    """Save the current file as a new file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
    if not filepath:
        return
    with open(filepath, mode="w", encoding="utf-8") as output_file:
        text = txt_edit.get("1.0", tk.END)
        output_file.write(text)
    window.title(f"Simple Text Editor - {filepath}")
    global active_file
    active_file = filepath

#select är oanvänd än så länge
def select():
    selected = txt_edit.selection_get()

def boldify():
    #taget från https://www.youtube.com/watch?v=X6zqePBPDVU , ändrat 'my_text' till 'txt_edit'
    """Makes highlighted text bold"""
    bold_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    bold_font.configure(weight="bold")
    txt_edit.tag_configure("bold", font=bold_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "bold" in current_tags:
        txt_edit.tag_remove("bold", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("bold", "sel.first", "sel.last")

def italify():
    #taget från https://www.youtube.com/watch?v=X6zqePBPDVU , ändrat 'my_text' till 'txt_edit'
    """Makes highlighted text italicised"""
    italic_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    italic_font.configure(slant="italic")
    txt_edit.tag_configure("italic", font=italic_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "italic" in current_tags:
        txt_edit.tag_remove("italic", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("italic", "sel.first", "sel.last")

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save", command=save_file)
btn_save_as = tk.Button(frm_buttons, text="Save As...", command=save_file_as)
btn_bold = tk.Button(frm_buttons, text="Bold", command=boldify)
btn_italic = tk.Button(frm_buttons, text="Italify", command=italify)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_bold.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_italic.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
