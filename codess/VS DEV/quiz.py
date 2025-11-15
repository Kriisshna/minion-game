
def answers(b):
    q={1:"d", 2:"c",3:"a",4:"b"}
    return q[b]

def questions(c):
    qq={1:"""who is the best indian cricketer?
      a.Rohith Sharma
      b.Dhoni
      c.kohli
      d.Sachin""",
      2:"""which is an even number?
      a.1
      b.3
      c.2
      d.7""",
      3:"""which is a fruit?
      a.tomato
      b.carrot
      c.beans
      d.onion""",
      4:"""who has the bomb?
      a.manu
      b.jobin
      c.dev
      d.yaswanth"""}
    print(qq[c])






print("wht is your name")
s=0
name=input()
print("hi",name,"welcome to the quiz")
for i in range (1,5):
    questions(i)
    a=input("do you want to continue(yes/no):")
    if a=="yes":
        ans=input("enter the answer:")
        x=answers(i)
        if ans==x:
             s=s+1
             print("your answer is correct")
        else:
            s=s-1
            print("your answer is wrong, correct option is",x)
        print("your score is",s)        

    else:
        print("quiz has stop")
        break

