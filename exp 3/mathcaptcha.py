import random

def generate_math():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operator = random.choice(operators)
    question = f"{num1} {operator} {num2}"
    result = eval(question)
    return {"question": question, "answer": result}

def validate_captcha(answer, result_actual):
    return answer == result_actual

def main():
    math = generate_math()
    print(f"Question: {math['question']}")
    answer = int(input("Enter the answer: "))
    if validate_captcha(answer, math['answer']):
        print("You are human!")
    else:
        print("You are a robot!")

if __name__ == "__main__":
    main()