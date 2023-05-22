import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

#active_file används för att få sökvägen till filen man öppnar eller sparar utanför funktionerna 'open_file' och 'save_file_as'
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

#TODO: man kan endast ha fetstil eller kursiv, inte båda samtidigt!
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

def underline():
    #hittade underline = true här: #https://stackoverflow.com/questions/3655449/underline-text-in-tkinter-label-widget
    """Makes highlighted text underlined"""
    underline_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    underline_font.configure(underline=True)
    txt_edit.tag_configure("underline", font=underline_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "underline" in current_tags:
        txt_edit.tag_remove("underline", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("underline", "sel.first", "sel.last")

def bold_ital():
    """Makes highlighted text bold and italicised"""
    bold_ital_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    bold_ital_font.configure(weight="bold", slant="italic")
    txt_edit.tag_configure("bold_ital", font=bold_ital_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "bold_ital" in current_tags:
        txt_edit.tag_remove("bold_ital", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("bold_ital", "sel.first", "sel.last")

def bold_under():
    """Makes highlighted text bold and underscored"""
    bold_under_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    bold_under_font.configure(weight="bold", underline=True)
    txt_edit.tag_configure("bold_under", font=bold_under_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "bold_under" in current_tags:
        txt_edit.tag_remove("bold_under", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("bold_under", "sel.first", "sel.last")

def ital_under():
    """Makes highlighted text italicised and underscored"""
    ital_under_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    ital_under_font.configure(slant="italic", underline=True)
    txt_edit.tag_configure("ital_under", font=ital_under_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "ital_under" in current_tags:
        txt_edit.tag_remove("ital_under", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("ital_under", "sel.first", "sel.last")

def all_fx():
    """Makes highlighted text have all 3 effects"""
    all_fx_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    all_fx_font.configure(weight="bold", slant="italic", underline=True)
    txt_edit.tag_configure("all_fx", font=all_fx_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "all_fx" in current_tags:
        txt_edit.tag_remove("all_fx", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("all_fx", "sel.first", "sel.last")

def clear_fx():
    """Removes any applied effects to the highlighted text"""
    current_tags= txt_edit.tag_names("sel.first")
    if "bold" in current_tags:
        txt_edit.tag_remove("bold", "sel.first", "sel.last")
    if "italic" in current_tags:
        txt_edit.tag_remove("italic", "sel.first", "sel.last")
    if "underline" in current_tags:
        txt_edit.tag_remove("underline", "sel.first", "sel.last")
    if "bold_ital" in current_tags:
        txt_edit.tag_remove("bold_ital", "sel.first", "sel.last")
    if "bold_under" in current_tags:
        txt_edit.tag_remove("bold_under", "sel.first", "sel.last")
    if "ital_under" in current_tags:
        txt_edit.tag_remove("ital_under", "sel.first", "sel.last")
    if "all_fx" in current_tags:
        txt_edit.tag_remove("all_fx", "sel.first", "sel.last")
    
window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

test_text = "String för att testa grejer!"
txt_edit = tk.Text(window)
txt_edit.insert(1.0, test_text)
frm_buttons = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(frm_buttons, text="Open", command=open_file)
btn_save = tk.Button(frm_buttons, text="Save", command=save_file)
btn_save_as = tk.Button(frm_buttons, text="Save As...", command=save_file_as)
btn_bold = tk.Button(frm_buttons, text="Bold", command=boldify)
btn_italic = tk.Button(frm_buttons, text="Italify", command=italify)
btn_underline = tk.Button(frm_buttons, text="Underline", command=underline)
btn_bold_ital = tk.Button(frm_buttons, text="Bold+Ital", command=bold_ital)
btn_bold_under = tk.Button(frm_buttons, text="Bold+Under", command=bold_under)
btn_ital_under = tk.Button(frm_buttons, text="Ital+Under", command=ital_under)
btn_all_fx = tk.Button(frm_buttons, text="All", command=all_fx)
btn_clear_fx = tk.Button(frm_buttons, text="Clear FX", command=clear_fx)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_save_as.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_bold.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_italic.grid(row=4, column=0, sticky="ew", padx=5, pady=5)
btn_underline.grid(row=5, column=0, sticky="ew", padx=5, pady=5)
btn_bold_ital.grid(row=6, column=0, sticky="ew", padx=5, pady=5)
btn_bold_under.grid(row=7, column=0, sticky="ew", padx=5, pady=5)
btn_ital_under.grid(row=8, column=0, sticky="ew", padx=5, pady=5)
btn_all_fx.grid(row=9, column=0, sticky="ew", padx=5, pady=5)
btn_clear_fx.grid(row=10, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
