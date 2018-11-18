import random


class games:
  abc=True
  def rps():
    player_1 = input("enter ur guess: " )
    player_2 = input("enter ur guess:" )
    a = "rock"
    b = "paper"
    c = "scissor"

    if player_1==player_2:
        print("the game is draw")
    elif player_1==a and player_2==b:
        print("player_2 wins")
    elif player_1==a and player_2==c:
        print("player_1 wins")
    elif player_1==b and player_2==a:
        print("player_1 wins")
    elif player_1==b and player_2==c:
        print("player_2 wins")
    elif player_1==c and player_2==a:
        print("player_2 wins")
    elif player_1==c and player_2==b:
        print("player_1 wins")
    else:
        print("invalid")
  def gue():
     print("welcome to guess the crct number game")   
     chars  = "1234567890"
     for i in range(1):
         a = random.randint(1,101)
         number = int(input("enter the number:"))
         d = len(str(abs(number)))
         c = [1,2,3]
         no_of_inputs = 1
         if d in c:
             while number !=a:
                 if number > a:
                     print("ur guess is too high")
                 elif number < a:
                     print("ur guess is too low")
                 elif number == a:
                     print("u win")
                 number = int(input("enter the number:"))
                 no_of_inputs +=1
         else:
               print("enter a valid number")
         print("number of inputs:",no_of_inputs)
  def cowbull():
        print("welcome to cows bulls game")	
        a = random.randint(1000,9999)
        b=[int(i) for i in str(a)]
        guess=0
        playing=True
        while playing:
            c=input('Guess 4 digit number: ')
            d=[int(i) for i in str(c)]
            cow=0
            bull=4
            for i in range(len(c)):
                if b[i] == d[i]:
                    cow += 1
                    bull -= 1
            guess += 1
            print('You have ',cow,'cows and',bull,'bulls')
            if cow==4:
                print('Correct!!! you guessed',a,'in',guess,'tries')

class game1(games):
     def p():
        print("1)rock,paper,scissor 2)guess game 3)cows&bulls 4)quit")
        x=int(input("enter the number"))
        if x==1:
            games.rps()
        elif x==2:
            games.gue()
        elif x==3:
            games.cowbull()
        elif x==4:
            games.abc=False
        else:
            print("enter the rignt number")
while games.abc:
    game1.p()


    
                   
