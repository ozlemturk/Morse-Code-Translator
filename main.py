from tkinter import *

#Colors and font settings

#-------------------------
GRAY = "#71797E"
DARK_GRAY = "#36454F"
FONT_NAME = "Inter"

#Mors alphabet dictionary
#-------------------------

MORSE_CODE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",
    "E": ".",     "F": "..-.",  "G": "--.",   "H": "....",
    "I": "..",    "J": ".---",  "K": "-.-",   "L": ".-..",
    "M": "--",    "N": "-.",    "O": "---",   "P": ".--.",
    "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",
    "Y": "-.--",  "Z": "--..",

    "0": "-----", "1": ".----", "2": "..---", "3": "...--",
    "4": "....-", "5": ".....", "6": "-....", "7": "--...",
    "8": "---..", "9": "----.",

    ".": ".-.-.-", ",": "--..--", "?": "..--..", "/": "-..-.",
    "@": ".--.-."
}

#Reverse dictionary for decoding Morse Code
MORSE_CODE_REVERSE = {value: key for key, value in MORSE_CODE.items()}

# -----------------------------
# Functions
# -----------------------------
def text_to_mors():
    """Takes text from the left box and converts it into Morse code"""

    # "1.0" means starting from the very first character
    # END means until the last character in the text box

    text_entry_get = text_entry.get("1.0",END).upper()
    result = []

    for i in text_entry_get:
        if i == " ":
            result.append("/") # Space is converted to "/"
        elif i in MORSE_CODE:
            result.append(MORSE_CODE[i])
    translate_str = "".join(result)
    print(translate_str)
    mors_entry.delete("1.0",END)
    mors_entry.insert("1.0",translate_str)

def mors_to_text():
    """Takes Morse code from the right box and converts it into text"""

    # strip() removes extra spaces from start and end
    mors_entry_get = mors_entry.get("1.0", END).strip()
    # Split Morse code by "/" to separate words
    word = mors_entry_get.split(" / ")# Split by space to get each letter
    translate = []
    for i in word:
        letters = i.split()
        decoded = [MORSE_CODE_REVERSE.get(letter,"?") for letter in letters]
        translate.append("".join(decoded))
    translate_str = "".join(translate)
    text_entry.delete("1.0",END)
    text_entry.insert("1.0",translate_str)
    print(translate_str)


# -----------------------------
# Tkinter GUI Design
# -----------------------------

window = Tk()
window.title("Mors Alphabet")
window.config(padx=100, pady=50, bg = GRAY)
#bg background

# Vertical separator line in the middle

separator = Frame(window, bg="white", width=2, height=300)
separator.grid(column=1, row=1, rowspan=3)


# Labels

text_label =Label(text="Text", font=(FONT_NAME, 25, "normal"), fg="white")
text_label.grid(column=0,row=0)

mors_label = Label(text="Mors Code", font=(FONT_NAME, 25, "normal"),  fg="white")
mors_label.grid(column=2,row=0)

# Text boxes

text_entry = Text(window, width=30, height=10, font=("Arial", 12))
text_entry.grid(column=0,row = 1, rowspan=3)

mors_entry = Text(window, width=30, height=10, font=("Arial", 12))
mors_entry.grid(column=2,row=1,rowspan=3)

# Buttons

text_button = Button(text = "translate", highlightbackground=GRAY, bg=DARK_GRAY, fg=DARK_GRAY, command=text_to_mors)
text_button.grid(column=0,row=4)

mors_button = Button(text = "translate", highlightbackground=GRAY, bg=DARK_GRAY, fg=DARK_GRAY, command=mors_to_text)
mors_button.grid(column=2,row=4)





# Decorative canvas (empty space in the middle bottom)

canvas = Canvas(window,width= 100, height=112, bg = GRAY, highlightthickness=0)
canvas.grid(column=1, row= 4)


window.mainloop()


# -----------------------------
# README (GitHub'a yüklerken kullan)
# -----------------------------
"""
# Morse Code Translator

Bu program, yazdığın İngilizce metni Mors alfabesine çevirir ve Mors alfabini tekrar metne dönüştürür.

## Nasıl Çalıştırılır

1. Python yüklü olmalı (Python 3.x önerilir)
2. Bu dosyayı çalıştır:
   python main.py
3. Açılan pencerede:
   - Sol kutuya yazı yazıp "translate" butonuna bas → sağ kutuda Mors kodu görünür
   - Sağ kutuya Mors kodu yazıp "translate" butonuna bas → sol kutuda metin görünür

## Desteklenen Karakterler

- Harfler: A-Z
- Sayılar: 0-9
- Noktalama: . , ? / @
- Boşluk → `/` olarak çevrilir
- Bilinmeyen karakter → `?` olarak gösterilir
"""
