BACKGROUND_COLOR = "#B1DDC6"

#---------------------------------------------Reading Csv files------------------------------------------------------------------
import pandas
import random

current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

def change_card():
    global flip_timer, current_card
    windows.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(word_text,text = current_card["French"],fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = windows.after(3000, func=flip_card)


def flip_card():
    current_card = random.choice(data_dict)
    canvas.itemconfig(title_text, text="English",fill="white")
    canvas.itemconfig(word_text, text=current_card["English"],fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("./data/words_to_learn.csv")
    change_card()


#---------------------------------------------UI Setup------------------------------------------------------------------
import tkinter
windows = tkinter.Tk()
windows.title("Flashy")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer = windows.after(3000, func=flip_card)

canvas = tkinter.Canvas(width=800,height=526)
card_front_img = tkinter.PhotoImage(file="./images/card_front.png")
card_back_img = tkinter.PhotoImage(file="./images/card_back.png")
card_background = canvas.create_image(400,264,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title_text = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
word_text = canvas.create_text(400,263,text="Word",font=("Arial",40,"italic"))
canvas.grid(row=0,column=0,columnspan=2)

right_image = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_image = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(image=wrong_image,highlightthickness=0,command=change_card)
wrong_button.grid(row=1,column=0)

change_card()

windows.mainloop()

#TODO: Solve the Error