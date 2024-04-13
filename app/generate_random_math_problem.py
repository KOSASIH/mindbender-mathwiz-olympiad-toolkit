import random
import numpy as np

def generate_random_math_problem(difficulty):
    """
    Generates a random mathematical problem based on the given difficulty level.

    Parameters:
    difficulty (int): The difficulty level of the problem (1-5).

    Returns:
    tuple: A tuple containing the problem as a string and the correct answer.
    """
    operators = ['+', '-', '*', '/']
    num1 = random.randint(1, 10 ** difficulty)
    num2 = random.randint(1, 10 ** difficulty)
    operator = random.choice(operators)

    if operator == '/':
        while num2 == 0:
            num2 = random.randint(1, 10 ** difficulty)
        problem = f"{num1} {operator} {num2}"
        answer = num1 / num2
    else:
        problem = f"{num1} {operator} {num2}"
        if operator == '+':
            answer = num1 + num2
        elif operator == '-':
            answer = num1 - num2
        else:
            answer = num1 * num2

    return problem, answer

def solve_math_problem(problem):
    """
    Solves a given mathematical problem using a neural network trained with TensorFlow.

    Parameters:
    problem (str): The mathematical problem as a string.

    Returns:
    float: The solution to the problem.
    """
    # Load the trained neural network model
    import tensorflow as tf
    model = tf.keras.models.load_model('math_solver.h5')

    # Preprocess the input
    input_layer = tf.keras.layers.Input(shape=(1,))
    x = tf.keras.layers.Dense(128, activation='relu')(input_layer)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    output_layer = tf.keras.layers.Dense(1, activation='linear')(x)
    model = tf.keras.models.Model(inputs=input_layer, outputs=output_layer)

    # Encode the problem as a numerical input
    encoded_problem = np.zeros((1, 1))
    for i, char in enumerate(problem):
        if char == '+':
            encoded_problem[0, i] = 1
        elif char == '-':
            encoded_problem[0, i] = 2
        elif char == '*':
            encoded_problem[0, i] = 3
        elif char == '/':
            encoded_problem[0, i] = 4
        else:
            encoded_problem[0, i] = int(char)

    # Use the neural network to solve the problem
    solution = model.predict(encoded_problem)[0][0]

    return solution

def check_answer(problem, user_answer, correct_answer):
    """
    Checks if the user's answer is correct.

    Parameters:
    problem (str): The mathematical problem as a string.
    user_answer (float): The user's answer.
    correct_answer (float): The correct answer.

    Returns:
    bool: True if the user's answer is correct, False otherwise.
    """
    return abs(user_answer - correct_answer) < 1e-9

def main():
    difficulty = int(input("Enter the difficulty level (1-5): "))
    problem, correct_answer = generate_random_math_problem(difficulty)
    print(f"Problem: {problem}")
    user_answer = float(input("Enter your answer: "))
    if check_answer(problem, user_answer, correct_answer):
        print("Correct!")
    else:
        print(f"Wrong! The correct answer is {correct_answer}")

if __name__ == "__main__":
    main()
