# A list of questions for the Quiz

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Rome", "B. Madrid", "C. Paris", "D. Berlin"],
        "answer": "C. Paris",
        "topic": "Geography"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": ["A. List", "B. Set", "C. Dictionary", "D. Tuple"],
        "answer": "D. Tuple",
        "topic": "Python"
    },
    {
        "question": "Who developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Nikola Tesla", "C. Albert Einstein", "D. Galileo Galilei"],
        "answer": "C. Albert Einstein",
        "topic": "Science"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B. Mars",
        "topic": "Astronomy"
    },
    {
        "question": "What is the output of 3 ** 2 in Python?",
        "options": ["A. 5", "B. 6", "C. 9", "D. 8"],
        "answer": "C. 9",
        "topic": "Python"
    },
    {
        "question": "Which of these is NOT a programming language?",
        "options": ["A. Python", "B. Java", "C. HTML", "D. Linux"],
        "answer": "D. Linux",
        "topic": "Tech"
    },
    {
        "question": "Which organ is responsible for pumping blood?",
        "options": ["A. Brain", "B. Lungs", "C. Liver", "D. Heart"],
        "answer": "D. Heart",
        "topic": "Biology"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["A. Central Processing Unit", "B. Central Programming Unit", "C. Central Performance Utility", "D. Computer Power Unit"],
        "answer": "A. Central Processing Unit",
        "topic": "Computer Basics"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1945", "B. 1947", "C. 1950", "D. 1952"],
        "answer": "B. 1947",
        "topic": "History"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. define", "C. function", "D. def"],
        "answer": "D. def",
        "topic": "Python"
    }
]

import random
import time

def run_quiz (questions, time_limit=13):
  score = 0       # To keep track of correct answers
  total_questions = len(questions)   # Total number of questions

  random.shuffle(questions)  # Shuffling questions for randomness and make it feel more like a quiz

  for q in  questions:
    print(f"\nTopic: {q['topic']}")  # Prints the topic of the question
    print(q['question'])   # Prints the question

    # Display each output with a number
    for i, option in enumerate(q['options'], 1):
      print(f"{i}. {option}")

    start_time = time.time()   # Start the timer when question is shown


    # Keep asking the user until a valid input is received i.e between option 1 and 4
    while True:
      user_answer = input(f"\nYour answer (1-{len(q['options'])}): ")
      if user_answer.isdigit() and 1 <= int(user_answer) <= len(q['options']):
        break  # Breaks when a valid input is entered
      print("Invalid Input. Please enter a number between 1 and ", len(q['options']))

    elapsed_time = time.time() - start_time   # Time taken to answer


    # If time exceeds the limit, skip the question
    if elapsed_time > time_limit:
      print("Time's up!")
      continue
    else:

      # Get the user's selected answer from options
      selected_option = q['options'][int(user_answer)-1]

      # Compare the selected answer with the correct answer
      if selected_option == q['answer']:
        print("Correct!")
        score += 1  # Increase the score for correct answer
      else:
        print(f"Sorry, the correct answer was: {q['answer']}")

    # Show the time taken for each question
    print(f"Time taken: {time.time() - start_time:.2f} seconds.")

  # Displays the score and the score percentage after every quiz game
  print(f"\nQuiz Completed! Your Score is: {score}/{total_questions}")
  print(f"Score Percentage: {(score / total_questions)*100:.2f}%")


# Main entry point of the program
if __name__ == "__main__":
  run_quiz(questions)