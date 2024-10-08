#!/usr/bin/python3
import os

def CowSay(s1):
    while(1):
        os.system("clear")
        print(s1)
        s = input("Enter a String --> ")
        print("\nSelect a CowFile...\n1. Default\n2. Dragon\n3. Blowfish\n4. Frogs\n5. Bunny\n6. Skeleton\n7. Fox\n8. Moose\n9. Hello Kitty\n10. Sheep\n11. Three Eyes\n12. Ren\n13. Go Back")
        ch = int(input("Enter Your Choice --> "))
        if(ch==1):
            os.system("cowsay "+s)
        elif(ch==2):
            os.system("cowsay -f dragon "+s)
        elif(ch==3):
            os.system("cowsay -f blowfish "+s)
        elif(ch==4):
            os.system("cowsay -f bud-frogs "+s)
        elif(ch==5):
            os.system("cowsay -f bunny "+s)
        elif(ch==6):
            os.system("cowsay -f skeleton "+s)
        elif(ch==7):
            os.system("cowsay -f fox "+s)
        elif(ch==8):
            os.system("cowsay -f moose "+s)
        elif(ch==9):
            os.system("cowsay -f hellokitty "+s)
        elif(ch==10):
            os.system("cowsay -f sheep "+s)
        elif(ch==11):
            os.system("cowsay -f three-eyes "+s)
        elif(ch==12):
            os.system("cowsay -f ren "+s)
        elif(ch==13):
            return
        else:
            print("Invalid Choice..")
        if(ch!=13):
            input("\nPress any key to continue...")


def Zen(s1):
    while(1):
        os.system("clear")
        print(s1+"\n1. Calendar\n2. Entry\n3. Color Selection\n4. File Selection\n5. Info\n6. Change Title\n7. Dialog Box\n8. Go Back")
        ch = int(input("Enter Your Choice --> "))
        if(ch==1):
            os.system("zenity --calendar")
        elif(ch==2):
            os.system("zenity --entry")
        elif(ch==3):
            os.system("zenity --color-selection")
        elif(ch==4):
            os.system("zenity --file-selection")
        elif(ch==5):
            os.system("zenity --info")
        elif(ch==6):
            s = input("Enter desired title --> ")
            os.system("zenity --info --title=\""+s+"\"")
        elif(ch==7):
            print("\n1. Calendar\n2. Date")
            x = int(input("Enter Your Choice --> "))
            if(x==1):
                os.system("zenity --info --text=\"$(cal)\" --width=200")
            elif(x==2):
                os.system("zenity --info --text=\"$(date)\" --width=200")
        elif(ch==8):
            return
        else:
            print("Invalid Choice..")
        input("\nPress any key to Continue...")

def Docker(s):
    while(1):
        os.system("clear")
        print(s+"\n1. Images\n2. Total Containers\n3. Containers in running state\n4. Launch an OS\n5. Start and Get inside launched OS\n6. Download an Image\n7. Go back\n")
        ch = int(input("\nEnter Your Choice --> "))
        if(ch==1):
            os.system("docker images")
        elif(ch==2):
            os.system("docker ps -a")
        elif(ch==3):
            os.system("docker ps")
        elif(ch==4):
            os.system("docker images")
            s1 = input("Which image you want to use? --> ")
            name = input("OS name? --> ")
            os.system("docker run -it --name="+name+"   "+s1)
            os.system("exit")
            print("OS named "+name+" is created")
        elif(ch==5):
            os.system("docker ps -a")
            x = input("\nEnter desire 'name' or 'OS ID' :: ")
            os.system("docker start "+x)
            os.system("docker attach "+x)
        elif(ch==6):
            s1 = input("\nImage name to be downloaded? --> ")
            os.system("docker pull "+s1)
            print("\nImage Downloaded")
            os.system("docker images")
        elif(ch==7):
            return;
        else:
            print("Invalid Input..")
        input("\nPress any key to Continue..")


def Cont():
    while(1):
        os.system("clear")
        print("\n1. Docker\n2. Kubernetes\n3. Go Back\n")
        ch = int(input("\nEnter your choice --> "))
        if(ch==1):
            Docker("\nTry out Some Docker Commands");
        elif(ch==2):
            pass
        elif(ch==3):
            return;
        else:
            print("\nInvalid Choice..")
        if(ch!=3):
            input("\nPress any Key to Continue...")

def Linux(s1):
    while(1):
        os.system("clear")
        print(s1+"\n1. Date\n2. Calendar\n3. sl\n4. figlet\n5. banner\n6. zenity\n7. cowsay\n8. espeak-ng\n9. To Go back\n")
        ch = int(input("Enter Your Choice --> "))
        if(ch==1):
            os.system("date")
        elif(ch==2):
            os.system("cal")
        elif(ch==3):
            os.system("sl")
        elif(ch==4):
            s = input("Enter a String --> ")
            os.system("figlet "+s)
        elif(ch==5):
            s = input("Enter a String --> ")
            os.system("banner "+s)
        elif(ch==6):
            Zen("\nExplore Zenity....")
        elif(ch==7):
            CowSay("\nExplore Cowsay...")
        elif(ch==8):
            s = print("Enter a String --> ")
            os.system("espeak-ng \""+s+"\"")
        elif(ch==9):
            return
        else:
            print("\nInvalid Choice..")
        if(ch!=6 or ch!=7):
            input("\nPress any key to Continue...")



def DS():
    while(1):
        os.system("clear")
        print("\n1. Salary Prediction(LR)\n2. Go back")
        ch = int(input("\nEnter Choice :: "))
        if(ch==1):
            x = input("How much yrs's of experience? :: ")
            os.system("python3 test.py "+x)
        elif(ch==2):
            return;
        else:
            print("\nInvalid Choice..")
        input("\nPress any key to continue...")

def DSA():
    while(1):
        os.system("clear")
        print("\n1.Bubble Sort\n2. Binary Search \n3. Go back \n4. Quit")
        ch =  int(input("\nEnter Choice :: "))
        if (ch==1):
            os.system("python3 bubble.py ")
        elif(ch==2):
            os.system("python3 binary_search.py ")
        elif(ch==3):
            return
        elif(ch==4):
            exit()
        else:
            print("\nInvalid Choice..")



while(1):
    os.system("clear")
    print("\n1. Basic Linux Commands\n2. DS\n3. Containers\n4. DSA\n5. Quit\n")
    ch = int(input("Enter Your Choice --> "))
    if(ch==1):
        Linux("\nTry Some Linux Commands....")
    elif(ch==2):
        DS();
    elif(ch==3):
        Cont();
    elif(ch==4):
        DSA();
    elif(ch==5):
        exit()
    else:
        print("\nInvalid Choice")

