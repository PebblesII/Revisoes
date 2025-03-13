import random
import time
import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

clear()


#Variables
answer = random.randint(0, 100)
attempts = 0
user = -1
#Start




while user != answer:
    print("-" * 50)
    user = int(input("Make a choice between 0 to 100: "))
    print("-" * 50)

    print("Wrong")
    attempts += 1
    print(f"Attempt: {attempts}")
    print(answer)
    print("-" * 50)
    time.sleep(1)
    
    if attempts >= 10 and attempts < 20:

        time.sleep(1)
        print(f"The answear is between {answer - 20} to {answer + 20}")
        print("-" * 50)
    
    elif attempts >= 20:

        time.sleep(1)
        print(f"The answear is between {answer - 10} to {answer + 10}")
        print("-" * 50)



    time.sleep(3)
    clear()
    