import time
# countdown
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

print("Welcome to my computer Quiz Game!")
while True:
    playing = input("Do you need to play Qize Game? [Y(Yes)/N(No)]")

    if playing.lower() in ["y", 'yes']:

        # collecting user details
        print("********** Registation **********")
        while True:
            name = input("Enter Your Name : ")
            if name =="":
                print("Empty, Enter Again")
            else:
                break
        while True:
            age = input("Enter Your Age : ")
            if age =="":
                print("Empty, Enter Again")
            elif age.isnumeric() == False:
                print("Enter Wrong, Please Enter your age ")
            else:
                break

        print("Great, Ready for the Exam")
        while True:
            t = input("How Many Seconds Do you need for ready the Exam? ")
            if t =="":
                print("Empty, Enter Again")
            elif t.isnumeric() == False:
                print("Please Enter the Seconds ")
            else:
             countdown(int(t))
             print("Let's Start!")
             break

        mark = 0 # mark

        # Quiz start
        print("Quiz 01 - mark 10")
        quiz01 = input("What is the Sri Lankan national game? ")
        
        if quiz01.lower() == ("volly ball") or quiz01.lower() == ("vollyball"):
            print("you Are correct")
            mark = mark + 10
        else:
            print("you are incorrect")

        print("Quiz 02 - mark 20")
        quiz02 = input("What is the Sri Lankan national flower? ")
        
        if quiz02.lower() == ("nilmanel") or quiz02.lower() == ("nil manel"):
            print("you Are correct")
            mark = mark + 20
        else:
            print("you are incorrect")

        print("Quiz 03 - mark 30")
        quiz03 = input("What is the Sri Lankan national food? ")
        
        if quiz03.lower() == ("kiribath") or quiz03.lower() == ("milk rice"):
            print("you Are correct")
            mark = mark + 30
        else:
            print("you are incorrect")

        print("Quiz 04 - mark 40")
        quiz04 = input("What is the Sri Lankan highest mountain? ")
        
        if quiz04.lower() == ("Piduruthalagala"):
            print("you Are correct")
            mark = mark + 40
        else:
            print("you are incorrect")

        # results
        m = int(mark)
        print("You Compleate all the quizs. Here is your Results")
        print("you are "+ name +" "+ age + " years old")
        print("Your scoure is " , mark)        
        if int(m) > 30:
            print("CONGRATUTATIONS! YOU PASSED THE EXAM")
        else:
            print("YOU ARE FAIL")
        break

    elif playing.lower() in ["n", 'no']:
        quit()
    else:
        print("You Enter Wrong, Please Enter Again")