from quiz.quiz_manager import QuizManager

def main():
    quiz_manager = QuizManager()
    quiz_manager.run("data/questions.json")

if __name__ == "__main__":
    main()
