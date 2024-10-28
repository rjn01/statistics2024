## Monty Hall problem 

import random as rm

def checkProb(total):
    correct_answer=0
    #loop for total number
    for i in range(total):
        door = [1,0,0]
        #shuffle door every time
        rm.shuffle(door)
        #print(f"Here are the option for door: {door}")
        #taking one value out of 3 options
        person_choice= rm.randint(0,2)
        #print(f"Here is person_choice: {person_choice}")
        
        
        #person has choose and now host will open one
        host_choose = [i for i in range(3) if i !=person_choice and door[i]!=1]
        #print(f"value after host taken one out {host_choose}")
        
        
        #person now have to take one out of the left 2 choice
        #shuffling again
        rm.shuffle(host_choose)
        
        #host takes out the first
        host_choice = host_choose[0]
        
        #checking if it is correct
        value = [i for i in range(len(door)) if i!=host_choice and i!=person_choice]
        #print(f"value is {value[0]}")
        
        
        if door[value[0]]==1:
            correct_answer+=1
        
    
    print(f"total wins: {correct_answer}")
    
    return correct_answer/total



if __name__ == "__main__":
    #total number of time 100000
    total = 10**5
    
    result = 100*checkProb(total)
    
    print(f"win percentage when switching: {result}")
