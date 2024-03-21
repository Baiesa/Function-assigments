'''
4. The Quiz Game

Objective:
The aim of this assignment is to create a quiz game that asks questions and checks answers.

Task 1: Develop a list of questions and answers.
Task 2: Write a function that quizzes the user and takes their answers.
Task 3: Score the quiz and give the user feedback on their performance.
'''

class QuizGame:
    def __init__(self, questions_answers):
        self.questions_answers = questions_answers

    def quiz_user(self):
        score = 0
        total_questions = len(self.questions_answers)

        for question, answer in self.questions_answers:
            user_answer = input(question + " ")
            if user_answer.lower() == answer.lower():
                print("Correct!")
                score += 1
            else:
                print("Incorrect. The correct answer is:", answer)

        return score, total_questions

    def give_feedback(self, score, total_questions):
        percentage = (score / total_questions) * 100
        print("You answered", score, "out of", total_questions, "questions correctly.")
        print("Your score:", percentage, "%")

def main():
    questions_answers = [
        ("What is the capital of France?", "Paris"),
        ("What is 2 + 2?", "4"),
        ("Who wrote 'Romeo and Juliet'?", "Shakespeare"),
        ("What is the chemical symbol for water?", "H2O")
    ]

    quiz = QuizGame(questions_answers)
    score, total_questions = quiz.quiz_user()
    quiz.give_feedback(score, total_questions)

if __name__ == "__main__":
    main()