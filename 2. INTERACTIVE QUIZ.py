print('BASIR P. WAHAB')
print('1BSCE-B')
print()
print('ICT 09 Programming 1')
print('FINAL PROJECT')
print()
print('PYTHON PROJECT 2 - INTERACTIVE QUIZ')
print()
print()

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.total_questions = len(questions)
        self.current_question_index = 0
        self.correct_answers = 0
        self.user_answers = {}

    def display_question(self):
        question_number = self.current_question_index + 1
        question = self.questions[self.current_question_index]['question']
        print(f"Question {question_number}/{self.total_questions}: {question}")
    
    def get_user_answer(self):
        return input("Your answer: ").strip().lower()

    def check_answer(self, user_answer):
        correct_answer = self.questions[self.current_question_index]['answer'].lower()
        if user_answer == correct_answer:
            print("Correct!")
            self.correct_answers += 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")

    def track_progress(self):
        self.user_answers[self.current_question_index] = {
            'question': self.questions[self.current_question_index]['question'],
            'user_answer': self.get_user_answer(),
            'correct_answer': self.questions[self.current_question_index]['answer']
        }
        self.current_question_index += 1

    def display_results(self):
        print("\nQuiz Results:")
        print("--------------")
        for index, answer_info in self.user_answers.items():
            print(f"Question {index + 1}: {answer_info['question']}")
            print(f"Your answer: {answer_info['user_answer']}")
            print(f"Correct answer: {answer_info['correct_answer']}")
            print()
        
        print(f"Total Correct Answers: {self.correct_answers}/{self.total_questions}")

def main():
    questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "Shakespeare"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the largest mammal?", "answer": "Blue Whale"},
        {"question": "What year did the Titanic sink?", "answer": "1912"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "What is the currency of Japan?", "answer": "Yen"},
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "Who developed the theory of relativity?", "answer": "Einstein"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"}
        # Add more questions here...
    ]

    quiz = Quiz(questions)
    
    print("Welcome to the Interactive Quiz!")
    print("================================")
    print("You will be presented with 10 questions. Type your answer and press Enter.\n")

    while quiz.current_question_index < quiz.total_questions:
        quiz.display_question()
        quiz.track_progress()

    quiz.display_results()

if __name__ == "__main__":
    main()
