

questions =[
             {
                "question": "What is the Formula Of Sulfur",
                "options": ["A.M","B.L","C.K","D.S"],
                "answer" :"C",
                "prize": "1000"
},
]
total_winning = 0
print("Welcome to Kaun banega Crorepati!\n")


for index, q in enumerate(questions):
    print(f"Question {index+ 1}: {q['question']}")
    for option in q["options"]:
        print(option)



user_answer = input("Enter Your Answer (A/B/C/D) :").upper()


if user_answer == q['answer']:
    total_winning = q['prize']
    print(f"Correct! You've won ₹{q['prize']}.Total: ₹{total_winning}\n") 
else:
    print('incorrect answer! Game over \n')


print(f"you are taking home ₹{total_winning}. Thank you for playing!")





