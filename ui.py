from tkinter import *
from quiz_brain import QuizBrain

FONTS=("Arial",20,"italic")
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz_initialize=quiz_brain
        self.window=Tk()
        self.window.title("QUIZEEEEEER")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label=Label(text="Score:0",font=FONTS,bg=THEME_COLOR,fg="white")
        self.label.grid(row=0,column=1)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_generated=self.canvas.create_text(
            150,
            125,
            width=280,
            text="abcd:",
            font=FONTS
        )
        self.canvas.grid(row=1,column=0,columnspan=2,pady=20)
        self.get_next_question()

        # self.label.config(padx=20,pady=20)

        self.true_button=self.buttonimage("images/true.png", 2, 0,command=self.true_answer)
        self.false_button=self.buttonimage("images/false.png",2,1,command=self.false_answer)


        self.window.mainloop()


    def buttonimage(self,image_link,x,y,command):
        createdimage=PhotoImage(file=image_link)
        self.button=Button(image=createdimage,highlightthickness=0,command=command)
        self.button.image = createdimage
        self.button.grid(row=x,column=y)
        return self.button

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_initialize.still_has_questions():
            self.label.config(text=f"Score:{self.quiz_initialize.score}")
            next_text=self.quiz_initialize.next_question()
            self.canvas.itemconfig(self.question_generated,text=next_text)
        else:
            self.canvas.itemconfig(self.question_generated,text="You have reached end of quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def true_answer(self):
        is_right=self.quiz_initialize.check_answer(True)
        self.feedback(is_right)

    def false_answer(self):
        is_right=self.quiz_initialize.check_answer(False)
        self.feedback(is_right)
    def feedback(self,isright):
        if isright:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)





