import random


def batting():
    run=0
    for i in range(1,7):
            Anjali_mam=random.randint(1,6)
            user=int(input("Enter Number Between 1 to 6 :- "))
            if user==Anjali_mam:
                print("Wicket")
                break
            else:
                print("{} made {} Runs".format(name,user))
                run+=user

    print("{} scored {} runs".format(name,run))
    return run
def balling():
    run1=0
    for i in range(1,7):
            user=int(input("Enter Number Between 1 to 6 :- "))
            Anjali_mam=random.randint(1,6)
            if Anjali_mam==user:
                 print("Wicket")
                 break
            else:
              print("Anjali Mam made {} Runs".format(Anjali_mam))
              run1+=Anjali_mam
    print("Anjali Mam  scored {} runs".format(run1))
    return run1
    
l1=["head","tails"]

name=input("Enter Your Name : -")
option=input("Choose Head/Tails :- ").lower()

toss=random.choice(l1)
print("It's a ",toss)
if option==toss:
    print("{} won the toss".format(name))
    choice=input("Choose Batting/Balling :-").lower()
    if choice=="batting":
        run=batting()
        print("---------------Balling---------------")
        run1=balling()
    elif choice=="balling" : 
        run1=balling()
        print("---------------Batting---------------")
        run=batting()
       
        
                
else:
    print("Anjali Mam won the toss")
    l2=["batting","balling"]
    choice=random.choice(l2)
    if choice=="batting":
        run1=balling()
        print("---------------Balling---------------")
        run=batting()
    elif choice=="balling" : 
        run=batting()
        print("---------------Batting---------------")
        run1=balling()

if run > run1:
    print(f"{name} wins the match")
elif run1 > run:
    print("Anjali Mam wins the match")
else:
    print("It's a tie!")
