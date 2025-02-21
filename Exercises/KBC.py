#list of questions
questions =[
    ["Hanumaan ji kiske liye sanjeevani booti laaye the ?", "Seeta mata","Ram Ji","Vibhisana","Lakshman"], #Lakshman
    ["Name the person who became the prime minister of India third time.","Rahul Gandhi","Aditya Nath Yogi","Indira Gandhi","Sir Narendra Modi"], #Sir Narendra Modi
    ["Which language is mostly used for Machine Learning Projects","Java","HTML","C++","Python"], #Python 
    ["Which god is known as \'Gauri Nandan\'?","Agni","Indra","Hanuman","Ganesha"], #Ganesha
    ["India\'s National Anthem was written by- ","RK Narayan","Chetan Bhagat","Arijit Singh","Rabindranath Tagore"], #Rabindranath Tagore
    ["How many religions are there in India?",7,8,9,6], #6
    ["How many states are there in India?",29,22,27,28], #28
    ["Name the first Indian woman to win a medal in the Olympics.","P.T.Usha","Kunjarani Devi","Sania Mirza","Karnam Maleshwari"], #Karnam Maleshwari
    ["Which city is known as the \"Silicon Valley of India\" ?", "Delhi","Mumbai","Chennai","Bangalore"] #Bangalore
]

winnings=[1000,5000,10000,40000,80000,320000,640000,2500000,10000000]

print("Welcome to KBC!!! Let's begin the game. Here is your first question.")

for i in range(0,len(questions)):
    money=0   #amount of cash earned by the participant
    question=questions[i]
    print(f"\nQuestion for Rs. {winnings[i]} is now on your computer screen !")
    print(f"{question[0]}")
    print(f"\na. {question[1]}    b. {question[2]}") 
    print(f"c. {question[3]}     d. {question[4]}") 

    reply= int(input("\nYour answer is(1-4 or 0 to quit): "))
    if(reply == 0):
        money = winnings[i-1]
        break
    elif (reply == 4):
        print(f"\nSahi jawaab, you won Rs. {winnings[i]}")
        if(i==2):
            money==5000
        elif(i==5):
            money=32000
        elif(i==8):
            money=10000000
    else:
        print("Wrong answer!")
        break

print(f"Aapki Inaam Raashi hai Rs. {money}")

