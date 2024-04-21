question=['who is the president of Pakistan ?\n a) Imran khan\n b) Nawaz sareef \n c) Balawal bhoto',
          'who is the president of Pakistan ?\n a) Imran khan\n b) Nawaz sareef \n c) Balawal bhoto',
          'who is the president of Pakistan ?\n a) Imran khan\n b) Nawaz sareef \n c) Balawal bhoto',
          'who is the president of Pakistan ?\n a) Imran khan\n b) Nawaz sareef \n c) Balawal bhoto',
          'who is the president of Pakistan ?\n a) Imran khan\n b) Nawaz sareef \n c) Balawal bhoto']
lis=['a','c','c','a','a']
incorrect = 0
current_money = 0
rupees=[1000,5000,8000,10000,15000]
for i in range(5):
    if incorrect!= 2:
        print(question[i])
        ans=input()
        if ans==lis[i]:
            print("            Congratuallition!! your answer is correct.\n")
            current_money = rupees[i] + current_money
            print("            You have won ",current_money,' rupees. \n')
        else:
            print("              False \n              Correct answer is ",lis[i])
            incorrect = incorrect + 1
            print(incorrect)
    else:
        print("                  you cannot play more ......")
        break
