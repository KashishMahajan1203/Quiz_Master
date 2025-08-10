from .quiz import Quiz
import json
from typing import Dict

class QuizManager:
    """Manages quiz categories and execution"""
    
    def __init__(self):
        self.categories: Dict[str, Quiz] = {}
        
    def load_categories(self, file_path: str) -> None:
        """
        Load available quiz categories from JSON file
        
        Args:
            file_path (str): Path to JSON file
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self.categories = {
                    category: Quiz(category)
                    for category in data.keys()
                }
        except FileNotFoundError:
            print(f"Error: File {file_path} not found")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format")
            
    def show_categories(self) -> None:
        """Display available quiz categories"""
        print("\nAvailable Quiz Categories:")
        for i, category in enumerate(self.categories.keys(), 1):
            print(f"{i}. {category}")
            
    def select_category(self) -> Quiz:
        """Let user select a quiz category"""
        while True:
            self.show_categories()
            try:
                choice = int(input("Select category (number): ")) - 1
                category = list(self.categories.keys())[choice]
                return self.categories[category]
            except (ValueError, IndexError):
                print("Invalid selection! Please try again.")
                
    def run(self, questions_file: str) -> None:
        """
        Run the complete quiz application
        
        Args:
            questions_file (str): Path to questions JSON file
        """
        print("=== Welcome to QuizMaster ===")
        self.load_categories(questions_file)
        
        while True:
            quiz = self.select_category()
            quiz.load_questions(questions_file)
            quiz.start_quiz()
            quiz.show_result()
            
            if input("\nTake another quiz? (y/n): ").lower() != 'y':
                print("Thanks for playing!")
                break
