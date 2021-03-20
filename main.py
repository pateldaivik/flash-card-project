BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import  random
current_card={}
to_learn={}
try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    orignal_data = pandas.read_csv('data/french_words.csv')
    to_learn = orignal_data.to_dict(orient='records')
else:
    to_learn = data.to_dict(orient='records')

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title,text='French',fill='black')
    canvas.itemconfig(card_word,text=current_card['French'],fill='black')
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000,func=flip_card)
def flip_card():
    canvas.itemconfig(card_title,text='English',fill='white')
    canvas.itemconfig(card_word, text=current_card['English'],fill='white')
    canvas.itemconfig(card_background,image=card_back)

def is_known():
    to_learn.remove(current_card)
    next_card()
    data =pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv',index=False)


window = Tk()
window.title('Flashy')
window.config(bg=BACKGROUND_COLOR,padx=20,pady=20)
flip_timer = window.after(3000,func=flip_card)
card_front = PhotoImage(file='./images/card_front.png')
card_back = PhotoImage(file='./images/card_back.png')
canvas = Canvas(width=800,height=526)
card_background=canvas.create_image(400,263,image=card_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
card_title= canvas.create_text(400,150,text='Title',font=('Arial',40,'italic'))
card_word =canvas.create_text(400,263,text='Word',font=('Arial',60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

wrong_img  = PhotoImage(file='./images/wrong.png')
right_img= PhotoImage(file='./images/right.png')

wrong = Button(image=wrong_img,highlightthickness=0,command=is_known())
right = Button(image=right_img,highlightthickness=0,command=next_card)

wrong.grid(row=1,column=0)
right.grid(row=1,column=1)

next_card()


window.mainloop()