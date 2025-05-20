import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    score=0
    for i in range(NUM_ROUNDS):
        print(f"Round {i+1}")
        x=random.randint(1,100)
        y=random.randint(1,100)
        print(f"Your number is {y}")
        z=input("Do you think your number is higher or lower than the computer's?: ")
        if(x<y and z=="higher"):
           print(f"You were right! The computer's number was {x}")
           score+=1
        elif(x>y and z=="lower"):
            print(f"You were right! The computer's number was {x}")
            score+=1
        else:
            print(f"Aww, that's incorrect. The computer's number was {x}")
        print(f"Your score is now {score}\n")
        
        
    print("Thanks for playing!")
    
   

if __name__ == "__main__":
    main()
