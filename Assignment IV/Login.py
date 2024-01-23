logindict={}

def signin(): #Signin Function
    print("\nSignin Menu")
    A = input("Enter your login ID: ")
    B = input("Enter your password: ")
    if A in logindict and logindict[A]["Password"]==B:
        print("Login Successful !!")
        if input("Enter S to sign out: ")==("S"or"s"):home()
    elif A not in logindict:
        if input("Invalid ID !!\nEnter S to Signup or T to try Again: ")==("S"or"s"):signup()
        else:signin()
    else:
        if input("Login Unsuccessful !\n\nForgot password ?\nEnter R to recover, T to try again: ")==("R"or"r"):recovery(A)
        else:signin()

def recovery(A): #Recovery Function
    if input(f"{logindict[A]['RecoveryQ']}: ") == logindict[A]["RecoveryA"]:
        logindict[A]["Password"]=input("Identity Verification Successful\nEnter new password:")
    else:
        if input("Incorrect Answer!!\nEnter S to Signup or T to try again")==("T"or"t"):recovery(A)
        else:signup()
def signup(): #Signup Function
    print("\nSignup Menu")
    A=input("Enter your login ID: ")
    if A in logindict:
        print("That ID is already taken, please choose another one!!")
        signup()
    logindict[A]={"LoginID":A,"Password":input("Enter your Password: "),"RecoveryQ":input("Enter your account recovery Question: "),"RecoveryA":input("Enter account Recovery Answer: ")}
    if input("\nSignup Successful\nEnter anything to go to go to signin menu ")!=None:signin()

def home(): #Home main function
    print("Welcome to the Simple login Application\n")
    if input("Enter 1 to Sign in anything else to Sign Up:") == "1":
        signin()
    else:
        signup()

home() #Calling Home main function