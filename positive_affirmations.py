from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import random
class main_page:
    def __init__(self, root):
        
        self.root = root
        
        self.bg_img = Image.open('positivity.jpg')
        self.bg_img = self.bg_img.resize((650,450))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        
        self.bg_lbl = Label(root, image= self.bg_img)
        self.bg_lbl.place(x = 0, y = 0)
        
        self.header = Label(root, text = "Live life to the fullest, and focus on the positive", fg = "white", bg = "Black", font = ("Times New Roman", 24, 'bold'))
        self.header.pack(fill = 'x')
        
        self.login_btnA = Button(root, text = 'All Smiles!', bg = 'white', font=('Times New Roman', 15, 'bold'),  command= self.affirmations)
        self.login_btnA.place(x= 250, y = 250)
        
    def affirmations(self):
        positive_affirmations = [
        "I am deserving of love and happiness.",
        "I believe in myself and my abilities.",
        "I am in control of my thoughts and emotions.",
        "I attract positive energy into my life.",
        "I am grateful for all the blessings in my life.",
        "I am constantly growing and evolving.",
        "I radiate confidence and self-assurance.",
        "I am worthy of success and abundance.",
        "I am open to new opportunities and experiences.",
        "I am resilient and can overcome any challenge.",
        "I trust the journey of my life.",
        "I am surrounded by loving and supportive people.",
        "I am at peace with my past and excited about my future.",
        "I am a source of inspiration to others.",
        "I am kind, compassionate, and forgiving.",
        "I am the architect of my own destiny.",
        "I am in tune with my inner wisdom.",
        "I embrace change as a chance for growth.",
        "I attract positive and loving relationships.",
        "I am confident in my ability to achieve my goals.",
        "I am a magnet for success and prosperity.",
        "I love and accept myself unconditionally.",
        "I am worthy of all the good things life has to offer.",
        "I am grateful for the present moment.",
        "I am a beacon of positivity and optimism.",
        "I am filled with joy and gratitude every day.",
        "I am capable of achieving greatness.",
        "I am a powerful creator of my reality.",
        "I am motivated and driven to succeed.",
        "I am free to be myself without judgment.",
        "I am aligned with my purpose in life.",
        "I am open to receiving love and abundance.",
        "I am a source of love and positivity in the world.",
        "I am constantly improving and growing.",
        "I am surrounded by abundance and prosperity.",
        "I am in harmony with the universe.",
        "I am a force for good in the world.",
        "I am worthy of all the love and happiness I desire.",
        "I am a magnet for positive opportunities.",
        "I am confident in my ability to overcome obstacles.",
        "I am resilient and bounce back from adversity.",
        "I am at peace with my past and excited about my future.",
        "I am a source of inspiration to others.",
        "I am kind, compassionate, and forgiving.",
        "I am the architect of my own destiny.",
        "I am in tune with my inner wisdom.",
        "I embrace change as a chance for growth.",
        "I attract positive and loving relationships.",
        "I am confident in my ability to achieve my goals.",
        "I am a magnet for success and prosperity."
        ]
        messagebox.showinfo('Be positive!',random.choice(positive_affirmations))
        

root = Tk()
root.geometry("650x450+500+100")
root.configure(bg = 'grey')
root.title("Be Positive")
main = main_page(root)
root.mainloop()
