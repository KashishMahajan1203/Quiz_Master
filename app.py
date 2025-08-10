from flask import Flask, render_template, request, jsonify
import json
import os
from quiz.quiz_manager import QuizManager

app = Flask(__name__)

# Initialize quiz manager
quiz_manager = QuizManager()

@app.route('/')
def index():
    """Serve the main quiz page"""
    return render_template('index.html')

@app.route('/api/categories')
def get_categories():
    """Get available quiz categories"""
    try:
        with open('data/questions.json', 'r') as f:
            data = json.load(f)
            categories = list(data.keys())
            return jsonify({'categories': categories})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/questions/<category>')
def get_questions(category):
    """Get questions for a specific category"""
    try:
        with open('data/questions.json', 'r') as f:
            data = json.load(f)
            if category in data:
                questions = data[category]
                # Format questions for frontend
                formatted_questions = []
                for q in questions:
                    formatted_questions.append({
                        'question': q['question'],
                        'options': q['options'],
                        'correct': q['correct_option']
                    })
                return jsonify({'questions': formatted_questions})
            else:
                return jsonify({'error': 'Category not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/submit', methods=['POST'])
def submit_quiz():
    """Submit quiz answers and get results"""
    try:
        data = request.json
        answers = data.get('answers', [])
        questions = data.get('questions', [])
        
        score = 0
        for i, answer in enumerate(answers):
            if i < len(questions) and answer == questions[i]['correct']:
                score += 1
        
        percentage = (score / len(questions)) * 100
        
        # Determine message based on score
        if percentage >= 80:
            message = "🏆 Excellent! You're a quiz master!"
        elif percentage >= 50:
            message = "👍 Good job! Keep practicing!"
        else:
            message = "😔 Try again! You can do better!"
        
        return jsonify({
            'score': score,
            'total': len(questions),
            'percentage': round(percentage, 1),
            'message': message
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
