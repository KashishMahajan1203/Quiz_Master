class Question:
    """Represents a quiz question with text, options, and correct answer"""
    
    def __init__(self, question_text: str, options: list, correct_option: int):
        """
        Initialize a question
        
        Args:
            question_text (str): The question text
            options (list): List of answer options
            correct_option (int): Index of correct option (0-based)
        """
        self.question_text = question_text
        self.options = options
        self.correct_option = correct_option
        
    def is_correct(self, answer_index: int) -> bool:
        """
        Check if the provided answer is correct
        
        Args:
            answer_index (int): The selected option index
            
        Returns:
            bool: True if answer is correct, False otherwise
        """
        return answer_index == self.correct_option
    
    def display(self) -> None:
        """Display the question and options"""
        print(self.question_text)
        for i, option in enumerate(self.options):
            print(f"{i+1}. {option}")
