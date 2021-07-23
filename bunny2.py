import tkinter as tk
from tkinter.constants import BOTTOM, CENTER, INSERT, N, S
from typing import Sized
from PIL import Image, ImageTk

#Canvas size of the Application
class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master, height = 500, width = 1500, bg = "#d3cbf0")
        self.master = master
        self.pack()
        
#Answer list
        self.response = ["Yes", "No", "Yes", "Yes", "Yes"] 

#Home Screen page
    def create_home_screen(self):
        self.exit_button = tk.Button(self, text = "Exit", font = ("Impact", 18), height = 1, width = 8, command = lambda: self.exit_screen())
        self.exit_button.place(anchor = "center", x = 80, y = 395)

        self.start_button = tk.Button(self, text = "Start", font = ("Impact", 18), height = 1, width = 8, command = lambda: self.question_screen())
        self.start_button.place(anchor = "center", x = 640, y = 395)

        self.frame = tk.Frame(self, bg = "#d3cbf0")
        self.frame.place(relx = 0.25, rely = 0.2, relwidth=0.5, relheight=0.4)

        self.title = tk.Label(self.frame, text = "Bunny Python", font = ("Impact", 30), bg = "#d3cbf0")
        self.title.place(anchor = "center", x = 180, y = 20)

#Calling fuctions to clear frame
    def exit_screen(self):
        self.exit_button.destroy()

    def question_screen(self):
        self.start_button.destroy()

        for widget in self.frame.winfo_children():
            widget.destroy()

        self.continue_button = tk.Button(self, text = "Continue", font = ("Impact", 20), height = 1, width = 8, command = lambda: self.answer_screen())
        self.continue_button.place(anchor = "center", x = 640, y = 395)

#Explanation
        self.right_frame = tk.Frame(self, bg = "#d3cbf0", bd = 10)
        self.right_frame.place(relx = 0.55, rely = 0.2, relwidth = 0.4, relheight = 0.5)      

#Title
        self.qtitle = tk.Label(self, text = "Yes or No Questions about Python", font = ("Times", 25, "bold"), bg = "#d3cbf0")
        self.qtitle.place(x = 180, y = 0)

#Question from 1-5
        self.question1 = tk.Label(self, text = "1. Does the hashtag make a comment in python code?", font = ("Times", 15, "bold"), bg = "#e6e6ff")
        self.question1.place(x = 30, y = 50)

        self.yes1 = tk.Button(self, text = "Yes", font = ("Times", 15, "bold"), command = lambda: self.answer_response(1, "Yes"))
        self.yes1.place(x = 30, y = 80)

        self.no1 = tk.Button(self, text = "No", font = ("Times", 15, "bold"), command = lambda: self.answer_response(1, "No"))
        self.no1.place(x = 100, y = 80)

        self.question2 = tk.Label(self, text = "2. Will this print(hello) show up in the terminal?", font = ("Times", 15, "bold"), bg = "#e6e6ff")
        self.question2.place(x = 30, y = 110)

        self.yes2 = tk.Button(self, text = "Yes", font = ("Times", 15, "bold"), command = lambda: self.answer_response(2, "Yes"))
        self.yes2.place(x = 30, y = 140)

        self.no2 = tk.Button(self, text = "No", font = ("Times", 15, "bold"), command = lambda: self.answer_response(2, "No"))
        self.no2.place(x = 100, y = 140)

        self.question3 = tk.Label(self, text = "3. Does int mean integer?", font = ("Times", 15, "bold"), bg = "#e6e6ff")
        self.question3.place(x = 30, y = 170)

        self.yes3 = tk.Button(self, text = "Yes", font = ("Times", 15, "bold"), command = lambda: self.answer_response(3, "Yes"))
        self.yes3.place(x = 30, y = 200)

        self.no3 = tk.Button(self, text = "No", font = ("Times", 15, "bold"), command = lambda: self.answer_response(3, "No"))
        self.no3.place(x = 100, y = 200)

        self.question4 = tk.Label(self, text = "4. Will an input ask the user a question?",font = ("Times", 15, "bold"), bg = "#e6e6ff")
        self.question4.place(x = 30, y = 230)

        self.yes4 = tk.Button(self, text = "Yes", font = ("Times", 15, "bold"), command = lambda: self.answer_response(4, "Yes"))
        self.yes4.place(x = 30, y = 260)

        self.no4 = tk.Button(self, text = "No", font = ("Times", 15, "bold"), command = lambda: self.answer_response(4, "No"))
        self.no4.place(x = 100, y = 260)

        self.question5 = tk.Label(self, text = "5. Does this have a variable? distance = 3", font = ("Times", 15, "bold"), bg = "#e6e6ff")
        self.question5.place(x = 30, y = 290)

        self.yes5 = tk.Button(self, text = "Yes", font = ("Times", 15, "bold"), command = lambda: self.answer_response(5, "Yes"))
        self.yes5.place(x = 30, y = 320)

        self.no5 = tk.Button(self, text = "No", font = ("Times", 15, "bold"), command = lambda: self.answer_response(5, "No"))
        self.no5.place(x = 100, y = 320)
        
#Check answers
    def answer_response(self, question_num, answer):
        if self.response[question_num -1] == answer:
            self.correct = tk.Label(self, text = "You are correct !", font = ("Times", 22, "bold"), bg = "#dfcbe6")
            self.correct.place(anchor = "center", x = 540, y = 150)
        else:
            self.explain = tk.Label(self, text = "You are incorrect", font = ("Times", 22, "bold"), bg = "#dfcbe6")
            self.explain.place(anchor = "center", x = 540, y = 150)
        
#Explanantion for each question
    def answer_screen(self):
        self.continue_button.destroy()

        self.new_frame = tk.Frame(self, bg = "#d3cbf0")
        self.new_frame.place(x = 0, y = 0, relwidth= 1, relheight= 0.8)

        self.answer1 = tk.Label(self, text = "1. Explanation: There are 2 types of comment, one is hashtag # and the other is Multi Line Comments", font = ("Impact, 12"), bg = "#e6e6ff")
        self.answer2 = tk.Label(self, text = "2. Explanation: Incorrect, because it needs to be a string and to make is a string it need quotes.", font = ("Impact, 12"), bg = "#e6e6ff")
        self.answer3 = tk.Label(self, text = "3. Explanation: Int does mean integer and it is a used when whole numbers are being used.", font = ("Impact, 12"), bg = "#e6e6ff")
        self.answer4 = tk.Label(self, text = "4. Explanation: It will ask the user for input because it tells the computer to allow the user to add their response.", font = ("Impact, 12"), bg = "#e6e6ff")
        self.answer5 = tk.Label(self, text = "5. Explanation: The answer is yes because the variable is distance which is used to represents the value.", font = ("Impact, 12"), bg = "#e6e6ff")

        self.answer1.place(x = 20, y = 90)
        self.answer2.place(x = 20, y = 120)
        self.answer3.place(x = 20, y = 150)
        self.answer4.place(x = 20, y = 180)
        self.answer5.place(x = 20, y = 210)

root = tk.Tk()
root.geometry('720x450')
root.resizable(0, 0)
app = Application(master = root)
app.create_home_screen()
app.mainloop()