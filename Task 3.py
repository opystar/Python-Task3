#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


#Welcome Screen 
print("NUMBER GUESSING GAME")

    
#Generate a random secret number between 1 and 20
secret_num1= random.randint(1, 10)
secret_num2= random.randint(1, 20)
secret_num3= random.randint(1, 50)


#Instruction
print("""
INSTRUCTION: There are three levels in this game. You would have 6 attempts to guess a secret number between 1 and 10 
correctly at the Easy level; 4 attempts for numbers between 1 and 20 and 3 attempts for numbers between 1 and 50""")

#Code section

start=False

start= input("Welcome to the Guessing Game. Are you ready to start now? YES/NO ")

while start:
    if start.upper()=="NO":
        print("""Thank you. See you next time
    ____      ______
    |  | |  | |
    | /  |__| |____
    | \   ||  |
    |__|  ||  |_____""") 


    break
     
if start.upper()=="YES":
    print("Great! Let's go!!")
    
    #stage choice

    stage= {'1': 'Easy', '2':'Medium', '3': 'Hard'}


    stage_choice=input("Please select a level: 1 for Easy, 2 for Medium, 3 for Hard. Enter a number only:  ")
    for key in stage_choice:
        print (f"You have selected {stage[stage_choice]} level. Now let's play!")


        guess_count=0
        guess_limit1 = 6
        guess_limit2 = 4
        guess_limit3 = 3

        if stage_choice=="1":

            while guess_count< guess_limit1:
                try:
                    guess1 = int(input("Your guess: "))     
                    guess_count +=1
                    guess_counter = guess_limit1 - guess_count

                    if guess1 == secret_num1:
                        print(""" Great!
                        You got it right!! 
                        You won!!!""")
                        break
                    
                    while guess_counter >= 1:
                        if guess1 != secret_num1:
                            print (f"That was wrong. You have made {guess_count} attempt(s). You have {guess_counter} attempt(s) left!!!")
                            break
                        else:
                            print("""Sorry You failed; 
                                         Better luck next time!!!""")
                            break

                            guess_counter =False   

                except ValueError:
                    print("Invalid entry. Please enter a number.")
                    

            else:
                if guess_count==guess_limit1:
                    print(f"""You have made maximum number of attempts for this level. 
                        This is the secret number: {secret_num1}. 
                        Better luck next time!""")
                    print("""
    _____   ____         _____     ____          ____   ___
    |      |    |  |\ /| |        |    | |    | |      |   | 
    |   __ |____|  | | | |___     |    |  |  |  |____  |__/  
    |____| |    |  |   | |____    |____|    |   |____  |   \                
                            """)
                    break


        if stage_choice=="2":

            while guess_count< guess_limit2:
                try:

                    guess2 = int(input("Your guess: "))     
                    guess_count +=1
                    guess_counter = guess_limit2 - guess_count

                    if guess2 == secret_num2:
                        print(""" Great!
                             You got it right!! 
                             You won!!!""")
                        break
                    else:
                        while guess_counter:
                            if guess2 != secret_num2 and guess_count < guess_limit2:
                                print (f"That was wrong. You have made {guess_count} attempt(s). You have {guess_counter} attempt(s) left!!!")
                                break
                            
                            elif guess_count == guess_limit2:
                                print("""Sorry You failed; 
                                         Better luck next time!!!""")
                                break

                        guess_counter =False   
                except ValueError:
                    print("Invalid entry. Please enter a number.")
                    

            else:
                if guess_count==guess_limit2:
                    print(f"""You have made maximum number of attempts for this level. 
                This is the secret number: {secret_num2}. 
                Better luck next time!""")
                    print("""
    _____   ____         _____     ____          ____   ___
    |      |    |  |\ /| |        |    | |    | |      |   | 
    |   __ |____|  | | | |___     |    |  |  |  |____  |__/  
    |____| |    |  |   | |____    |____|    |   |____  |   \                
                    """)
                    break

        if stage_choice=="3":
            #try:

            while guess_count< guess_limit3:
                try:

                    guess3 = int(input("Your guess: "))     
                    guess_count +=1
                    guess_counter = guess_limit3 - guess_count

                    if guess3 == secret_num3:
                        print(""" Great!
                        You got it right!! 
                        You won!!!""")
                        break

                    while guess_counter >= 1:
                        if guess3 != secret_num3:
                            print (f"That was wrong. You have made {guess_count} attempt(s). You have {guess_counter} attempt(s) left!!!")
                            break
                        guess_counter =False   

                except ValueError:
                    print("Invalid entry. Please enter a number.")
                    

            else:
                if guess_count==guess_limit3:
                    print(f"""You have made maximum number of attempts for this level. 
                This is the secret number: {secret_num3}. 
                Better luck next time!""")
                    print("""
    _____   ____         _____     ____          ____   ___
    |      |    |  |\ /| |        |    | |    | |      |   | 
    |   __ |____|  | | | |___     |    |  |  |  |____  |__/  
    |____| |    |  |   | |____    |____|    |   |____  |   \                
                   """)
                    break
        


# In[ ]:




