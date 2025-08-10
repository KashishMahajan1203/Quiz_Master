import json
from typing import Dict, List
from .question import Question

class Quiz:
    """Represents a quiz with questions from a specific category"""
    
    def __init__(self, category: str):
        self.category = category
        self.questions: List[Question] = []
        self.score = 0
        
    def load_questions(self, file_path: str) -> None:
        """
        Load questions from JSON file
        
        Args:
            file_path (str): Path to JSON file containing questions
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data.get(self.category, []):
                    question = Question(
                        item['question'],
                        item['options'],
                        item['correct_option']
                    )
                    self.questions.append(question)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")
            
    def start_quiz(self) -> None:
        """Start the quiz interaction"""
        if not self.questions:
            print("No questions loaded for this category!")
            return
            
        print(f"\n=== {self.category} Quiz ===")
        for i, question in enumerate(self.questions):
            print(f"\nQuestion {i+1}:")
            question.display()
            while True:
                try:
                    answer = int(input("Your answer (1-4): ")) - 1
                    if 0 <= answer < len(question.options):
                        break
                    print("Invalid choice! Enter 1-4")
                except ValueError:
                    print("Please enter a number between 1-4")
                    
            if question.is_correct(answer):
                print("✅ Correct!")
                self.score += 1
            else:
                correct_answer = question.options[question.correct_option]
                print(f"❌ Wrong! Correct answer was: {correct_answer}")
                
    def show_result(self) -> None:
        """Display quiz results"""
        total = len(self.questions)
        percentage = (self.score / total) * 100
        
        print("\n=== Quiz Results ===")
        print(f"Category: {self.category}")
        print(f"Score: {self.score}/{total} ({percentage:.1f}%)")
        
        if percentage >= 80:
            print("🏆 Excellent!")
        elif percentage >= 50:
            print("👍 Good job!")
        else:
            print("😔 Try again!")
