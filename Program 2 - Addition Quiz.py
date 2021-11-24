# Program 2: Addition Quiz
# Create a program that will automatically generate two random numbers to add (0 to 99).
# Let the user answer and evaluate if the user has the correct answer.
# The program will ask the user 10 addition operation.
# Display the result summary of the 10 operations (Example: 9/10).

# Steps
# 1. Import random module.
import random
# 2. Create a dictionary for the questions.
questions = {}
# 3. Set the score to 0 first because the quiz will start at 0.
userScore = 0

# 4. Create a for loop for the 10 random questions that will be given.
for integer in range(10):
    # 5. Define the first random number from 0 to 99 using random.randint function.
    integer_firstNumber = random.randint(0, 99)