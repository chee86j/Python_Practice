import random

# Dictionary of questions, options, and answers
questions = [
    {
        'prompt': 'What are the most common shades of an apple?',
        'options': ['A. Red/Green', 'B. Purple', 'C. Orange', 'D. Yellow'],
        'answer': 'A'
    },
    {
        'prompt': 'What is the capital of France?',
        'options': ['A. London', 'B. Paris', 'C. Rome', 'D. Berlin'],
        'answer': 'B'
    },
    {
        'prompt': 'Which planet is known as the Red Planet?',
        'options': ['A. Venus', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'B'
    },
    {
        'prompt': 'Who wrote "To Kill a Mockingbird"?',
        'options': ['A. Harper Lee', 'B. J.K. Rowling', 'C. Mark Twain', 'D. Ernest Hemingway'],
        'answer': 'A'
    },
    {
        'prompt': 'What is the chemical symbol for water?',
        'options': ['A. Wa', 'B. H2O', 'C. Wi', 'D. H'],
        'answer': 'B'
    },
    {
        'prompt': 'What is the tallest mammal?',
        'options': ['A. Giraffe', 'B. Elephant', 'C. Hippopotamus', 'D. Rhinoceros'],
        'answer': 'A'
    },
    {
        'prompt': 'Which country is home to the kangaroo?',
        'options': ['A. Australia', 'B. Brazil', 'C. Canada', 'D. South Africa'],
        'answer': 'A'
    },
    {
        'prompt': 'Who painted the Mona Lisa?',
        'options': ['A. Vincent van Gogh', 'B. Leonardo da Vinci', 'C. Pablo Picasso', 'D. Michelangelo'],
        'answer': 'B'
    },
    {
        'prompt': 'What is the currency of Japan?',
        'options': ['A. Yen', 'B. Dollar', 'C. Euro', 'D. Pound'],
        'answer': 'A'
    },
    {
        'prompt': 'Which gas do plants absorb to produce oxygen?',
        'options': ['A. Carbon Dioxide', 'B. Oxygen', 'C. Nitrogen', 'D. Hydrogen'],
        'answer': 'A'
    }
]

def run_quiz(questions):
    score = 0
    lifelines = 3 # lifelines to randomly eliminate 2 wrong answers
    for question in questions:
        print(question['prompt']) # prompt is used in python to display a message to the user
        
        options = question['options'] 
        
        for option in question['options']:
            print(option)
        print()
            
        # lifeline feature
        if lifelines > 0:
            print('Lifelines remaining:', lifelines)
            lifeline = input('Would you like to use a Lifeline? (Y/N): ').upper()
            print()
            if lifeline == 'Y':
                print('Using lifeline...')
                correct_answer = next(option for option in options if option.startswith(question['answer'] + '.'))
                incorrect_options = [opt for opt in options if opt != correct_answer]
                options_to_remove = random.sample(incorrect_options, min(2, len(incorrect_options)))
                for opt in options_to_remove:
                    options.remove(opt)
                for opt in options:
                    print(f"Remaining option: {opt}")
                lifelines -= 1
                
        answer = input('Enter Your Answer (A, B, C, D): ').upper()
        if answer == question['answer']:
            print('Correct!\n')
            score += 1
            print()
        else:
            print('Incorrect!')
            print()
    print(f'You got {score} out of {len(questions)} questions right!\n') # f-string formatting is similar to JS template literals
                
run_quiz(questions)

# To execute the code, run the command 'python3 quiz-game.py' in the terminal