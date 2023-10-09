from tkinter import *
import pandas
import random
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_dict.html

BACKGROUND_COLOR = "#B1DDC6"

# global variable
current_card = {}
flip_timer = None

try:
    data = pandas.read_csv("Python Bootcamp\Tkiner\Flash_Card_Project\data\\words_to_learn.csv")
    
# words_to_learn does not exist
except FileNotFoundError:
    original_data = pandas.read_csv("Python Bootcamp\Tkiner\Flash_Card_Project\data\\french_words.csv")
    to_learn = original_data.to_dict(orient = "records")
else:
    to_learn = data.to_dict(orient = "records")

def next_card():
    global current_card, flip_timer

    # cancel the execution of a delayed command
    window.after_cancel(flip_timer)
    # get current card
    current_card = random.choice(to_learn)
    # config title using "French"
    canvas.itemconfig(card_title, text = "French", fill = "black")
    # config word using French text
    canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
    # config card background using front image
    canvas.itemconfig(card_background, image = card_front_img)
    # flip card on the window every 3000 ms
    window.after(3000, func = flip_card)

# flip card to English part
def flip_card():

    # configure card title as English and fill canvas with white
    canvas.itemconfig(card_title, text = "English", fill = "white")
    # configure card word as English text
    canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
    # config background image to background image
    canvas.itemconfig(card_background, image = card_back_img)

# remove current card from the to_learn list
def is_known():

    # remove current card from to_learn dictionary
    to_learn.remove(current_card)

    # save updated to_learn dictionary
    data = pandas.DataFrame(to_learn)
    data.to_csv("Python Bootcamp\Tkiner\Flash_Card_Project\data\words_to_learn.csv", index = False)

    next_card()

# set up window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)

# flip card on the window every 3000 ms
flip_timer = window.after(3000, func = flip_card)

# set up canvas
canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = "Python Bootcamp/Tkiner/Flash_Card_Project/images/card_front.png")

# set up card back image
card_back_img = PhotoImage(file = "Python Bootcamp\Tkiner\Flash_Card_Project\images\card_back.png")
# set up card front image
card_front_img = PhotoImage(file = "Python Bootcamp\Tkiner\Flash_Card_Project\images\card_front.png")

# set up card front ground
card_background = canvas.create_image(400, 263, image = card_front_img)

# set up title
card_title = canvas.create_text(400, 150, font = ("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, font = ("Ariel", 60, "bold"))

# set up color
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row = 0, column = 0)

# set up wrong mark button
cross_image = PhotoImage(file = "Python Bootcamp\Tkiner\Flash_Card_Project\images\wrong.png")
unknown_button = Button(image = cross_image, highlightthickness=0, command = next_card)
unknown_button.grid(row = 1, column = 0)

# set up check mark button 
check_image = PhotoImage(file = "Python Bootcamp\Tkiner\Flash_Card_Project\images\\right.png")
known_button = Button(image = check_image, highlightthickness=0, command = is_known)
known_button.grid(row = 1, column = 1)

# display both title and word on the screen
next_card()

if __name__ == "__main__":
    window.mainloop()