from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

PARAMETERS = {}


class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)
        
        # Ask for user inputs
        self.amount_label = Label(text = "Number of questions", fg = "white", bg = THEME_COLOR)
        self.amount_label.grid(row = 0, column = 0)
        
        self.amount_input = Entry(width = 30)
        self.amount_input.grid(row = 0, column = 1)
        
        self.category_label = Label(text = "Type of questions", fg = "white", bg = THEME_COLOR)
        self.category_label.grid(row = 1, column = 0)
        
        self.category_input = Entry(width = 30)
        self.category_input.grid(row = 1, column = 1)
        self.category_input.focus()
        
        self.generate_button = Button(text = "Generate Questions", highlightthickness=0, command=self.generate_questions, width=43)
        self.generate_button.grid(row=2, column=0, columnspan=2)
        
        self.score_label = Label(text = "Score: 0", fg = "white", bg = THEME_COLOR)
        self.score_label.grid(row = 3, column = 1)
        
        self.canvas = Canvas(width=300, height=250, bg = "white")
        self.question_text = self.canvas.create_text(
            150, 
            125, 
            width = 280,
            text="Some Questions Text", 
            fill = THEME_COLOR, 
            font = ("Arial", 20, "italic")
        )
        self.canvas.grid(row=4, column=0, columnspan=2, pady = 30)
        
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=5, column=0)
        
        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=5, column=1)
        
        self.get_next_question()
        
        self.window.mainloop()
        
    def generate_questions(self):
        global PARAMETERS
        amount = self.amount_input.get()
        category = self.category_input.get()
        PARAMETERS = {
            "amount": amount,
            "type": "boolean",
            "category": category,
            }
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text = "You've reached the end of the quiz.")
            self.true_button.config(state = "disabled")
            self.false_button.config(state = "disabled")
        
    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)
    
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        