from tkinter import *
from PIL import Image, ImageTk
from string import ascii_uppercase
import random
from tkinter import messagebox

# img = PhotoImage(file='LOSE.png')      
# canvas.create_image(20,20, anchor=NW, image=img)

# run=True
# while run:
root=Tk()#creating object to tkinter class (creating a window)
root.geometry("1050x550")
root.title('Hangman')


bg=ImageTk.PhotoImage(Image.open('BG.png'))
a=Label(root,image=bg)
a.place(x=0,y=0)
# bg2=ImageTk.PhotoImage(Image.open('.png'))
# la=Label(root,image=bg2)
# la.place(x=820,y=90)
letterlist=['A.png','B.png','C.png','D.png','E.png','F.png','G.png','H.png','I.png','J.png','K.png','L.png','M.png','N.png','O.png','P.png','Q.png','R.png','S.png','T.png','U.png','D.png','V.png','W.png','X.png','Y.png','Z.png']
l=['apple','banana','orange','watermelon','cherry','strawberry','bottle','ball','pendrive']
s='.png'
num=random.randint(1,7)

word = random.choice(letterlist)
display_word = '_' * len(word)  # Placeholder for the display word
words=l[num]+s

hangman_images = []
for i in range(1, 7):
    try:
        image = Image.open(f'i.png')  # Ensure these image paths are correct
        hangman_images.append(ImageTk.PhotoImage(image))
    except Exception as e:
        print(f"Error loading image hangman{i}.png: {e}")

length=len(l[num])
print(length)

incorrect_guesses = 0
max_incorrect = 7  # Number of hangman stages
score = 0
guessed_letters = set()
namevalue= StringVar()

ent_name = Entry(root, width=70, borderwidth=10, textvariable=namevalue)
ent_name.place(x=120, y=120)

score = 0

score_label = Label(root, text=f"Score: {score}", font=("impact", 20), bg='#201c4e', fg='white', bd=0)
score_label.place(x=10, y=10)

# ****************************************************************************

# Load hangman images for each step
hangman_images = [ImageTk.PhotoImage(Image.open(f'{i}.png')) for i in range(1, 7)]

# Initialize game state
incorrect_guesses = 0
max_incorrect = len(hangman_images)  # Number of hangman stages

hangman_label = Label(root, image=hangman_images[0])
hangman_label.place(x=820, y=250)

# score_label = Label(root, text=f"Score: {score}", font=("impact", 20))
# score_label.place(x=20, y=20)


# ************************************************************************************

# Function to update the hangman image and score
def update_hangman():
    global incorrect_guesses
    if incorrect_guesses < len(hangman_images):
        hangman_label.config(image=hangman_images[incorrect_guesses])
        hangman_label.image = hangman_images[incorrect_guesses]  # Keep a reference to avoid garbage collection
    else:
        print("No more hangman images available.")




def guess_letter(letter):
    global incorrect_guesses, score, display_word
    if letter in guessed_letters:
        return  # Letter has already been guessed

    guessed_letters.add(letter)
    if letter in word:
        updated_display = ''.join(c if c in guessed_letters else '_' for c in word)
        if '_' not in updated_display:
            messagebox.showinfo("Congratulations", "You've won the game!")
        score += 10  # Increase score for correct guess
    else:
        incorrect_guesses += 1
        update_hangman()  # Update hangman image for incorrect guess
        if incorrect_guesses >= max_incorrect:
            messagebox.showinfo("Game Over", "You've lost the game!")
            # Additional game over handling can be added here, like disabling further guesses

    score_label.config(text=f"Score: {score}")






def new_word():
    global word, num, img
    num = random.randint(0, len(l) - 1)
    word = l[num] + s
    img = PhotoImage(file=word)
    canvas.create_image(20, 20, anchor=NW, image=img)
    canvas.image = img  # Keep a reference to avoid garbage collection

canvas = Canvas(root, width=140, height=140)
canvas.place(x=820, y=90)
new_word()

score = 0

def check():
    global score
    value = ent_name.get()
    a = word.rstrip('.png')
    if value.lower() == a:
        score += 1
        messagebox.showinfo("Result", "Congratulations! You guessed it right!")
    else:
        lose_img = PhotoImage(file='LOSE.png')
        canvas.create_image(20, 20, anchor=NW, image=lose_img)
        canvas.image = lose_img  # Keep a reference to avoid garbage collection
        messagebox.showinfo("Result", "Sorry, wrong guess. Try again!")
    
    # Update the score label
    score_label.config(text=f"Score: {score}")

def clear_entry():
    pass

def insert_letter(letter):
    current_text = ent_name.get()
    ent_name.delete(0, END)
    ent_name.insert(0, current_text + letter)

button2 = Button(root, text='CLEAR ENTRY', command=lambda: ent_name.delete(0, END), font=("impact", 15), bg='#201c4e', fg='white', bd=0)
button2.place(x=300, y=200)


def show_score():
    messagebox.showinfo("Score", f"Your current score is: {score}")

# button1 = Button(root, text='VIEW SCORE', command=show_score, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
# button1.place(x=850, y=440)


button = Button(root, text='CHECK', command=check, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
button.place(x=750, y=480)



button3 = Button(root, text='CHANGE PICTURE', command=new_word, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
button3.place(x=150, y=480)

# button4 = Button(root, text='EXIT', command=root.quit, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
# button4.place(x=1000, y=10)
quit_image = Image.open('exit.png')
quitbtn = ImageTk.PhotoImage(quit_image)
image_width, image_height = quit_image.size
quit = Button(root, image=quitbtn, bd=0, command=root.quit)
quit.place(x=950, y=10)
quit.config(width=image_width, height=image_height)
        
        
img1 = ImageTk.PhotoImage(Image.open(letterlist[0]))  # Image for button A
btn1 = Button(root, image=img1, bg="#B0E9FD", bd=0, command=lambda: insert_letter('A'))
btn1.place(x=10, y=300)


btn1.place(x=10,y=300)
img2=ImageTk.PhotoImage(Image.open(letterlist[1]))
btn2=Button(root,image=img2,bg="#B0E9FD",bd=0,command=lambda: insert_letter('B'))
btn2.place(x=70,y=300)
img3=ImageTk.PhotoImage(Image.open(letterlist[2]))
btn3=Button(root,image=img3,bg="#B0E9FD",bd=0,command=lambda: insert_letter('C'))
btn3.place(x=130,y=300)
img4=ImageTk.PhotoImage(Image.open(letterlist[3]))
btn4=Button(root,image=img4,bg="#B0E9FD",bd=0,command=lambda: insert_letter('D'))
btn4.place(x=190,y=300)
img5=ImageTk.PhotoImage(Image.open(letterlist[4]))
btn5=Button(root,image=img5,bg="#B0E9FD",bd=0,command=lambda: insert_letter('E'))
btn5.place(x=250,y=300)
img6=ImageTk.PhotoImage(Image.open(letterlist[5]))
btn6=Button(root,image=img6,bg="#B0E9FD",bd=0,command=lambda: insert_letter('F'))
btn6.place(x=310,y=300)
img7=ImageTk.PhotoImage(Image.open(letterlist[6]))
btn7=Button(root,image=img7,bg="#B0E9FD",bd=0,command=lambda: insert_letter('G'))
btn7.place(x=370,y=300)
img8=ImageTk.PhotoImage(Image.open(letterlist[7]))
btn8=Button(root,image=img8,bg="#B0E9FD",bd=0,command=lambda: insert_letter('H'))
btn8.place(x=430,y=300)
img9=ImageTk.PhotoImage(Image.open(letterlist[8]))
btn9=Button(root,image=img9,bg="#B0E9FD",bd=0,command=lambda: insert_letter('I'))
btn9.place(x=500,y=300)
img10=ImageTk.PhotoImage(Image.open(letterlist[9]))
btn10=Button(root,image=img10,bg="#B0E9FD",bd=0,command=lambda: insert_letter('J'))
btn10.place(x=560,y=300)
img11=ImageTk.PhotoImage(Image.open(letterlist[10]))
btn11=Button(root,image=img11,bg="#B0E9FD",bd=0,command=lambda: insert_letter('K'))
btn11.place(x=620,y=300)
img12=ImageTk.PhotoImage(Image.open(letterlist[11]))
btn12=Button(root,image=img12,bg="#B0E9FD",bd=0,command=lambda: insert_letter('L'))
btn12.place(x=680,y=300)
img13=ImageTk.PhotoImage(Image.open(letterlist[12]))
btn13=Button(root,image=img13,bg="#B0E9FD",bd=0,command=lambda: insert_letter('M'))
btn13.place(x=740,y=300)
img14=ImageTk.PhotoImage(Image.open(letterlist[13]))
btn14=Button(root,image=img14,bg="#B0E9FD",bd=0,command=lambda: insert_letter('N'))
btn14.place(x=10,y=360)
img15=ImageTk.PhotoImage(Image.open(letterlist[14]))
btn15=Button(root,image=img15,bg="#B0E9FD",bd=0,command=lambda: insert_letter('O'))
btn15.place(x=70,y=360)
img16=ImageTk.PhotoImage(Image.open(letterlist[15]))
btn16=Button(root,image=img16,bg="#B0E9FD",bd=0,command=lambda: insert_letter('P'))
btn16.place(x=130,y=360)
img17=ImageTk.PhotoImage(Image.open(letterlist[16]))
btn17=Button(root,image=img17,bg="#B0E9FD",bd=0,command=lambda: insert_letter('Q'))
btn17.place(x=190,y=360)
img18=ImageTk.PhotoImage(Image.open(letterlist[17]))
btn18=Button(root,image=img18,bg="#B0E9FD",bd=0,command=lambda: insert_letter('R'))
btn18.place(x=250,y=360)
img19=ImageTk.PhotoImage(Image.open(letterlist[18]))
btn19=Button(root,image=img19,bg="#B0E9FD",bd=0,command=lambda: insert_letter('S'))
btn19.place(x=310,y=360)
img20=ImageTk.PhotoImage(Image.open(letterlist[19]))
btn20=Button(root,image=img20,bg="#B0E9FD",bd=0,command=lambda: insert_letter('T'))
btn20.place(x=370,y=360)
img21=ImageTk.PhotoImage(Image.open(letterlist[20]))
btn21=Button(root,image=img21,bg="#B0E9FD",bd=0,command=lambda: insert_letter('U'))
btn21.place(x=430,y=360)
# img22=ImageTk.PhotoImage(Image.open(letterlist[21]))
# btn22=Button(root,image=img22,bg="#B0E9FD",bd=0,command=lambda: insert_letter('V'))
# btn22.place(x=490,y=360)
img23=ImageTk.PhotoImage(Image.open(letterlist[22]))
btn23=Button(root,image=img23,bg="#B0E9FD",bd=0,command=lambda: insert_letter('V'))
btn23.place(x=500,y=360)
img24=ImageTk.PhotoImage(Image.open(letterlist[23]))
btn24=Button(root,image=img24,bg="#B0E9FD",bd=0,command=lambda: insert_letter('W'))
btn24.place(x=560,y=360)
img25=ImageTk.PhotoImage(Image.open(letterlist[24]))
btn25=Button(root,image=img25,bg="#B0E9FD",bd=0,command=lambda: insert_letter('X'))
btn25.place(x=630,y=360)
img26=ImageTk.PhotoImage(Image.open(letterlist[25]))
btn26=Button(root,image=img26,bg="#B0E9FD",bd=0,command=lambda: insert_letter('Y'))
btn26.place(x=690,y=360)


# button = Button(root, text='CHECK',command=check, font=("impact", 20), bg='#201c4e', fg='white', bd=0)
# button.place(x=750, y=440)

# button1 = Button(root, text='VIEW SCORE', font=("impact", 20), bg='#201c4e', fg='white', bd=0)
# button1.place(x=850, y=440)

# button2 = Button(root, text='CLEAR ENTRY', font=("impact", 15), bg='#201c4e', fg='white', bd=0)
# button2.place(x=300, y=200)


root.mainloop()
