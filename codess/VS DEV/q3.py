
# def seat(m):
#     if m==1 or m==4:
#         print("lower")
#     elif m==2 or m==5:
#         print("middle")
#     elif m==3 or m==6:
#         print("upper")
#     elif m==7 :
#         print("side lower")
#     else:
#         print("side upper")
           
    
# name=input("enter name:")
# m= int(input())
# seat(m%8)


def seat(m):
    seat_map = {
        1: "Lower",
        4: "Lower",
        2: "Middle",
        5: "Middle",
        3: "Upper",
        6: "Upper",
        7: "Side Lower",
        0: "Side Upper"
    }
    return seat_map[m]

name = input("Enter your name: ")
m = int(input("Enter your seat number: "))
seat_type = seat(m % 8)
print(f"Hello {name}, your seat type is: {seat_type}")
