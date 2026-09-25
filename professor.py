# py.professor
import random

def get_level():
    """دریافت سطح بازی از کاربر (1، 2 یا 3)"""
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)
        continue

def generate_integer(level):
    """تولید یک عدد صحیح غیر منفی با تعداد رقم مشخص (level)"""
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")

def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)  # عدد اول
        y = generate_integer(level)  # عدد دوم
        answer = x + y
        attempts = 0
        correct = False

        while attempts < 3:
            guess = input(f"{x} + {y} = ")  # **دقیقا همان ترتیب تولید اعداد**
            attempts += 1

            if not guess.isdigit():
                print("EEE")
                continue

            if int(guess) == answer:
                print(f"{answer} = {x} + {y}")
                score += 1
                correct = True
                break
            else:
                print("EEE")

        if not correct:
            print(f"{answer} = {x} + {y}")

    print("Score:")
    print(score)

if __name__ == "__main__":
    main()
