import tkinter as tk
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename, asksaveasfilename

#active_file används för att få sökvägen till filen man öppnar eller sparar utanför funktionerna 'open_file' och 'save_file_as'
active_file = ""
#TODO: Gör en 'vill du spara först?' dialog om man redan har en fil öppen.
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
    return selected

#TODO: Gör de olika effekterna mer effektiva, istället för att ha en egen metod för varje variant.
#OBS: Om man lägger på en effekt före en font, så hamnar fonten 'ovanpå' effekt-taggen, och endast fonten syns.
#Gör därför font först, sen effekt.
#OBS2: Om man markerar flera rader med olika fonter och sedan lägger på en effekt, får alla rader samma font som den översta man valt.
def boldify():
    #taget från https://www.youtube.com/watch?v=X6zqePBPDVU , ändrat 'my_text' till 'txt_edit'
    """Makes highlighted text bold"""
    bold_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
    bold_font.configure(weight="bold")
    txt_edit.tag_configure("bold", font=bold_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "cascadia" in current_tags:
        if "cascadia_bold" in current_tags:
            txt_edit.tag_remove("cascadia_bold", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "bold")
            txt_edit.tag_configure("cascadia_bold", font=cascadia_font)
            txt_edit.tag_add("cascadia_bold", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_bold" in current_tags:
            txt_edit.tag_remove("consolas_bold", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "bold")
            txt_edit.tag_configure("consolas_bold", font=consolas_font)
            txt_edit.tag_add("consolas_bold", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_bold" in current_tags:
            txt_edit.tag_remove("courier_bold", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "bold")
            txt_edit.tag_configure("courier_bold", font=courier_font)
            txt_edit.tag_add("courier_bold", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_bold" in current_tags:
            txt_edit.tag_remove("lucida_bold", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "bold")
            txt_edit.tag_configure("lucida_bold", font=lucida_font)
            txt_edit.tag_add("lucida_bold", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_italic" in current_tags:
            txt_edit.tag_remove("cascadia_italic", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "italic")
            txt_edit.tag_configure("cascadia_italic", font=cascadia_font)
            txt_edit.tag_add("cascadia_italic", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_italic" in current_tags:
            txt_edit.tag_remove("consolas_italic", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "italic")
            txt_edit.tag_configure("consolas_italic", font=consolas_font)
            txt_edit.tag_add("consolas_italic", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_italic" in current_tags:
            txt_edit.tag_remove("courier_italic", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "italic")
            txt_edit.tag_configure("courier_italic", font=courier_font)
            txt_edit.tag_add("courier_italic", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_italic" in current_tags:
            txt_edit.tag_remove("lucida_italic", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "italic")
            txt_edit.tag_configure("lucida_italic", font=lucida_font)
            txt_edit.tag_add("lucida_italic", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_under" in current_tags:
            txt_edit.tag_remove("cascadia_under", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "underline")
            txt_edit.tag_configure("cascadia_under", font=cascadia_font)
            txt_edit.tag_add("cascadia_under", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_under" in current_tags:
            txt_edit.tag_remove("consolas_under", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "underline")
            txt_edit.tag_configure("consolas_under", font=consolas_font)
            txt_edit.tag_add("consolas_under", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_under" in current_tags:
            txt_edit.tag_remove("courier_under", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "underline")
            txt_edit.tag_configure("courier_under", font=courier_font)
            txt_edit.tag_add("courier_under", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_under" in current_tags:
            txt_edit.tag_remove("lucida_under", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "underline")
            txt_edit.tag_configure("lucida_under", font=lucida_font)
            txt_edit.tag_add("lucida_under", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_bold_ital" in current_tags:
            txt_edit.tag_remove("cascadia_bold_ital", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "bold", "italic")
            txt_edit.tag_configure("cascadia_bold_ital", font=cascadia_font)
            txt_edit.tag_add("cascadia_bold_ital", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_bold_ital" in current_tags:
            txt_edit.tag_remove("consolas_bold_ital", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "bold", "italic")
            txt_edit.tag_configure("consolas_bold_ital", font=consolas_font)
            txt_edit.tag_add("consolas_bold_ital", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_bold_ital" in current_tags:
            txt_edit.tag_remove("courier_bold_ital", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "bold", "italic")
            txt_edit.tag_configure("courier_bold_ital", font=courier_font)
            txt_edit.tag_add("courier_bold_ital", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_bold_ital" in current_tags:
            txt_edit.tag_remove("lucida_bold_ital", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "bold", "italic")
            txt_edit.tag_configure("lucida_bold_ital", font=lucida_font)
            txt_edit.tag_add("lucida_bold_ital", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_bold_under" in current_tags:
            txt_edit.tag_remove("cascadia_bold_under", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "bold", "underline")
            txt_edit.tag_configure("cascadia_bold_under", font=cascadia_font)
            txt_edit.tag_add("cascadia_bold_under", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_bold_under" in current_tags:
            txt_edit.tag_remove("consolas_bold_under", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "bold", "underline")
            txt_edit.tag_configure("consolas_bold_under", font=consolas_font)
            txt_edit.tag_add("consolas_bold_under", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_bold_under" in current_tags:
            txt_edit.tag_remove("courier_bold_under", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "bold", "underline")
            txt_edit.tag_configure("courier_bold_under", font=courier_font)
            txt_edit.tag_add("courier_bold_under", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_bold_under" in current_tags:
            txt_edit.tag_remove("lucida_bold_under", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "bold", "underline")
            txt_edit.tag_configure("lucida_bold_under", font=lucida_font)
            txt_edit.tag_add("lucida_bold_under", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_ital_under" in current_tags:
            txt_edit.tag_remove("cascadia_ital_under", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "italic", "underline")
            txt_edit.tag_configure("cascadia_ital_under", font=cascadia_font)
            txt_edit.tag_add("cascadia_ital_under", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_ital_under" in current_tags:
            txt_edit.tag_remove("consolas_ital_under", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "italic", "underline")
            txt_edit.tag_configure("consolas_ital_under", font=consolas_font)
            txt_edit.tag_add("consolas_ital_under", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_ital_under" in current_tags:
            txt_edit.tag_remove("courier_ital_under", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "italic", "underline")
            txt_edit.tag_configure("courier_ital_under", font=courier_font)
            txt_edit.tag_add("courier_ital_under", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_ital_under" in current_tags:
            txt_edit.tag_remove("lucida_ital_under", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "italic", "underline")
            txt_edit.tag_configure("lucida_ital_under", font=lucida_font)
            txt_edit.tag_add("lucida_ital_under", "sel.first", "sel.last")
    else:
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
    if "cascadia" in current_tags:
        if "cascadia_all_fx" in current_tags:
            txt_edit.tag_remove("cascadia_all_fx", "sel.first", "sel.last")
        else:
            cascadia_font = ("Cascadia Code", 11, "bold", "italic", "underline")
            txt_edit.tag_configure("cascadia_all_fx", font=cascadia_font)
            txt_edit.tag_add("cascadia_all_fx", "sel.first", "sel.last")
    elif "consolas" in current_tags:
        if "consolas_all_fx" in current_tags:
            txt_edit.tag_remove("consolas_all_fx", "sel.first", "sel.last")
        else:
            consolas_font = ("Consolas", 11, "bold", "italic", "underline")
            txt_edit.tag_configure("consolas_all_fx", font=consolas_font)
            txt_edit.tag_add("consolas_all_fx", "sel.first", "sel.last")
    elif "courier" in current_tags:
        if "courier_all_fx" in current_tags:
            txt_edit.tag_remove("courier_all_fx", "sel.first", "sel.last")
        else:
            courier_font = ("Courier", 11, "bold", "italic", "underline")
            txt_edit.tag_configure("courier_all_fx", font=courier_font)
            txt_edit.tag_add("courier_all_fx", "sel.first", "sel.last")
    elif "lucida" in current_tags:
        if "lucida_all_fx" in current_tags:
            txt_edit.tag_remove("lucida_all_fx", "sel.first", "sel.last")
        else:
            lucida_font = ("Lucida Console", 11, "bold", "italic", "underline")
            txt_edit.tag_configure("lucida_all_fx", font=lucida_font)
            txt_edit.tag_add("lucida_all_fx", "sel.first", "sel.last")
    else:
        if "all_fx" in current_tags:
            txt_edit.tag_remove("all_fx", "sel.first", "sel.last")
        else:
            txt_edit.tag_add("all_fx", "sel.first", "sel.last")

def clear_fx():
    """Removes any applied effects to the highlighted text"""
    current_tags= txt_edit.tag_names("sel.first")
    if "default" not in current_tags:
        txt_edit.tag_remove("bold", "sel.first", "sel.last")
        txt_edit.tag_remove("italic", "sel.first", "sel.last")
        txt_edit.tag_remove("underline", "sel.first", "sel.last")
        txt_edit.tag_remove("bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_under", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("cascadia_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_all_fx", "sel.first", "sel.last")

def cascadia():
    """Changes highlighted text to 'Cascadia Code' font"""
    cascadia_font = ("Cascadia Code", 11)
    txt_edit.tag_configure("cascadia", font=cascadia_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "cascadia" in current_tags:
        txt_edit.tag_remove("cascadia", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("cascadia", "sel.first", "sel.last")

def consolas():
    """Changes highlighted text to 'Consolas' font"""
    consolas_font = ("Consolas", 11)
    txt_edit.tag_configure("consolas", font=consolas_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "consolas" in current_tags:
        txt_edit.tag_remove("consolas", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("consolas", "sel.first", "sel.last")

def courier():
    """Changes highlighted text to 'Courier' font"""
    courier_font = ("Courier", 11)
    txt_edit.tag_configure("courier", font=courier_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "courier" in current_tags:
        txt_edit.tag_remove("courier", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("courier", "sel.first", "sel.last")

def lucida():
    """Changes highlighted text to 'Lucida Console' font"""
    lucida_font = ("Lucida Console", 11)
    txt_edit.tag_configure("lucida", font=lucida_font)
    current_tags= txt_edit.tag_names("sel.first")
    if "lucida" in current_tags:
        txt_edit.tag_remove("lucida", "sel.first", "sel.last")
    else:
        txt_edit.tag_add("lucida", "sel.first", "sel.last")

def clear_font():
    current_tags= txt_edit.tag_names("sel.first")
    """Removes any applied fonts to the highlighted text"""
    txt_edit.tag_remove("cascadia", "sel.first", "sel.last")
    txt_edit.tag_remove("consolas", "sel.first", "sel.last")
    txt_edit.tag_remove("courier", "sel.first", "sel.last")
    txt_edit.tag_remove("lucida", "sel.first", "sel.last")
    if "cascadia_bold" in current_tags or "consolas_bold" in current_tags or "courier_bold" in current_tags or "lucida_bold" in current_tags:
        txt_edit.tag_remove("cascadia_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold", "sel.first", "sel.last")
        bold_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        bold_font.configure(weight="bold")
        txt_edit.tag_configure("bold", font=bold_font)
        txt_edit.tag_add("bold", "sel.first", "sel.last")
    elif "cascadia_italic" in current_tags or "consolas_italic" in current_tags or "courier_italic" in current_tags or "lucida_italic" in current_tags:
        txt_edit.tag_remove("cascadia_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_italic", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_italic", "sel.first", "sel.last")
        italic_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        italic_font.configure(slant="italic")
        txt_edit.tag_configure("italic", font=italic_font)
        txt_edit.tag_add("italic", "sel.first", "sel.last")
    elif "cascadia_under" in current_tags or "consolas_under" in current_tags or "courier_under" in current_tags or "lucida_under" in current_tags:
        txt_edit.tag_remove("cascadia_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_under", "sel.first", "sel.last")
        underline_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        underline_font.configure(underline=True)
        txt_edit.tag_configure("underline", font=underline_font)
        txt_edit.tag_add("underline", "sel.first", "sel.last")
    elif "cascadia_bold_ital" in current_tags or "consolas_bold_ital" in current_tags or "courier_bold_ital" in current_tags or "lucida_bold_ital" in current_tags:
        txt_edit.tag_remove("cascadia_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold_ital", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold_ital", "sel.first", "sel.last")
        bold_ital_font.configure(weight="bold", slant="italic")
        txt_edit.tag_configure("bold_ital", font=bold_ital_font)
        current_tags= txt_edit.tag_names("sel.first")
        txt_edit.tag_add("bold_ital", "sel.first", "sel.last")
    elif "cascadia_bold_under" in current_tags or "consolas_bold_under" in current_tags or "courier_bold_under" in current_tags or "lucida_bold_under" in current_tags:
        txt_edit.tag_remove("cascadia_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_bold_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_bold_under", "sel.first", "sel.last")
        bold_under_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        bold_under_font.configure(weight="bold", underline=True)
        txt_edit.tag_configure("bold_under", font=bold_under_font)
        txt_edit.tag_add("bold_under", "sel.first", "sel.last")
    elif "cascadia_ital_under" in current_tags or "consolas_ital_under" in current_tags or "courier_ital_under" in current_tags or "lucida_ital_under" in current_tags:
        txt_edit.tag_remove("cascadia_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_ital_under", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_ital_under", "sel.first", "sel.last")
        ital_under_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        ital_under_font.configure(slant="italic", underline=True)
        txt_edit.tag_configure("ital_under", font=ital_under_font)
        txt_edit.tag_add("ital_under", "sel.first", "sel.last")
    elif "cascadia_all_fx" in current_tags or "consolas_all_fx" in current_tags or "courier_all_fx" in current_tags or "lucida_all_fx" in current_tags:
        txt_edit.tag_remove("cascadia_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("consolas_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("courier_all_fx", "sel.first", "sel.last")
        txt_edit.tag_remove("lucida_all_fx", "sel.first", "sel.last")
        all_fx_font = tkFont.Font(txt_edit, txt_edit.cget("font"))
        all_fx_font.configure(weight="bold", slant="italic", underline=True)
        txt_edit.tag_configure("all_fx", font=all_fx_font)
        txt_edit.tag_add("all_fx", "sel.first", "sel.last")

def about():
    about_window = tk.Tk()
    about_window.title("About")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)
    about_txt = tk.Text(about_window)
    about_txt.grid(row=0, column=1, sticky="nsew")
    hjälp_text = """Beskrivning av programmets funktioner:\n
Open - Öppnar en .txt fil.
Save - Sparar den nuvarande filen.
Save as - Sparar texten till en annan fil.

OBS För effekter och fonter: Välj en font först, sedan effekt!
OBS2: För att lägga på flera effekter samtidigt, använd de designerade knapparna

Boldify - Gör markerad text fetstil.
Italify - Gör markerad text kursiv.
Underline - Gör markerad text understrykt
Bold + Ital ~ All FX - Lägger på flera effekter på markerad text.
Clear FX - Tar bort alla effekter från markerad text.
Cascadia ~ Lucida - Ändrar till respektiv font på markerad text.
Clear Font - Tar bort ändrade fonter.
About - Visar detta fönster.
"""
    about_txt.insert(1.0, hjälp_text)

window = tk.Tk()
window.title("Simple Text Editor")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

#lista med monospace fonts: https://en.wikipedia.org/wiki/List_of_monospaced_typefaces

test_text = "String för att testa grejer!\n"
#monospace font hittad i första svaret här: https://stackoverflow.com/questions/48731746/how-to-set-a-tkinter-widget-to-a-monospaced-platform-independent-font
default_font = ("TkFixedFont", 11)
txt_edit = tk.Text(window, font=(default_font))
default_font = ("TkFixedFont", 20)
txt_edit.tag_configure("default", font=default_font)
txt_edit.insert(1.0, test_text)
txt_edit.insert(2.0, test_text)
txt_edit.insert(3.0, test_text)
txt_edit.insert(4.0, test_text)

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
btn_cascadia = tk.Button(frm_buttons, text="Cascadia", command=cascadia)
btn_consolas = tk.Button(frm_buttons, text="Consolas", command=consolas)
btn_courier = tk.Button(frm_buttons, text="Courier", command=courier)
btn_lucida = tk.Button(frm_buttons, text="Lucida", command=lucida)
btn_clear_font = tk.Button(frm_buttons, text="Clear Font", command=clear_font)
btn_about = tk.Button(frm_buttons, text="About", command=about)

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
btn_cascadia.grid(row=11, column=0, sticky="ew", padx=5, pady=5)
btn_consolas.grid(row=12, column=0, sticky="ew", padx=5, pady=5)
btn_courier.grid(row=13, column=0, sticky="ew", padx=5, pady=5)
btn_lucida.grid(row=14, column=0, sticky="ew", padx=5, pady=5)
btn_clear_font.grid(row=15, column=0, sticky="ew", padx=5, pady=5)
btn_about.grid(row=16, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
