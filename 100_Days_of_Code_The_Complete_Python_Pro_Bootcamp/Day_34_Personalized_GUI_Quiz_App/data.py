import requests
from question_model import Question
from quiz_brain import QuizBrain


def get_categories():
    categories_details = "Any Categories: Null;\n"
    response = requests.get("https://opentdb.com/api_category.php")
    response.raise_for_status()
    categories = response.json()
    categories_data = categories["trivia_categories"]
    for cat in categories_data:
        cat_res = f"{cat['name']}: {cat['id']};\n"
        categories_details += cat_res
    return categories_details

def get_questions(parameters):
    question_bank = []
    
    response = requests.get("https://opentdb.com/api.php", params = parameters)
    response.raise_for_status()
    data = response.json()
    question_data = data["results"]

    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)
        
    return QuizBrain(question_bank)

get_categories()