print("Hi what's your name")
n=input()
print(f"hello {n} welcome to the quiz")


qs={
    1:"""who is the best footballer
      a-neymar
      b-mbappe
      c-ronaldo
      d-messi""",
    2:"""1-2-3-_  .next number is
      a-4
      b-32
      c-3
      d-2343434332433""",
    3:"""which is an even number
      a-33
      b-2
      c-3
      d-5"""
      }
ans={1:"c",2:"a",3:"b"}
m=0
for i in range (1,4):
    b=input("do you want to continue quiz(yes/no):")
    if b=="yes":
        print(qs[i])
        z=input("do you want to continue(yes/no):")
        if z=="yes":
            y=input("enter the answer:")
        else:
            break
        if y==ans[i]:
            print("hooray you got a point")
            m=m+1
        else:
            print("booooo")
            m=m-1
        print(f"your current mark is {m}")
    else:
        print(f"your final score is {m}")     
        break



