from tkinter import *
import pandas as pd
from pandas import DataFrame
import random


BACKGROUND_COLOR = "#B1DDC6"

#------------------------Flash_cards------------------------------------------
words = pd.read_csv("data/french_words.csv")
#convets the csv file into a dataframe(convert the DataFrame into a list of dictionaries)
data = words.to_dict(orient="records")
french_words = []
random_words = []

for item in data:
    #getting hold of the french keyword
    french_word = item["French"]
    french_words.append(french_word)

for item in data:
    pass


def random_french():
    global current_word, title_text, french_text  # Declare the variable as global if you want to access it elsewhere

    canvas.delete(title_text)

    current_word = random.choice(data)  # Select a random item from data
    random_french_word = current_word["French"] # Get the French word
    french_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    title_text = canvas.create_text(400, 263, text=random_french_word, font=("Arial", 60, "bold"))
    canvas.delete(french_text)


def english_words():
    global current_word,french_text,title_text
    current_word = random.choice(data)
    french_text = canvas.create_text(400, 150, text="English", font=("Arial", 40, "italic"))
    title_text = canvas.create_text(400, 263, text=current_word, font=("Arial", 60, "bold"))

def random_french():
    global current_word # Declare the variable as global if you want to access it elsewhere
    current_word = random.choice(data)  # Select a random item from data
    random_french_word = current_word["French"] # Get the French word
    canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
    canvas.create_text(400, 263, text=random_french_word, font=("Arial", 60, "bold"))




#------------------------UI_SETUP------------------------------------------

#for the window

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#for the canvas, canvas allows you to layer things on top of eachother

canvas = Canvas(width=800, height=526)

#front image
front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=front_image)

#back image
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=back_image)
canvas.itemconfig(canvas_image, image=back_image)


french_text = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
title_text = canvas.create_text(400, 263, text="Title", font=("Arial", 60, "bold"))

canvas.config(background=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

#creating buttons with images

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=random_french)
right_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=random_french)
wrong_button.grid(column=0, row=1)


window.mainloop()