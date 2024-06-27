import random
list=[1,2,3,4,5,6]
print("lets play roll the dice against compiutar.")
userinput=input("click 'enter' to roll your dice:")
rollcomp=random.choice(list)

rolluser=random.choice(list)

    
print("your roll is "+"'"+str(rolluser)+"'")
tst=input("click 'enter' to see ")
print("compiuter roll is"+"'"+str(rollcomp)+"'")






if int(rollcomp)<int(rolluser):
    print("you won!!")

else:
    print("sorry,you lost")

