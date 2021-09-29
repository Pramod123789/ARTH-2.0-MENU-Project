import os

os.system("tput setaf 2")
print("\t\t\tWelcome to My Menu")
os.system("tput setaf 7")

# os.system("zenity --info --text='welcome to LW'")


print("\t\t\t------------------"	)
print()

print("where u want to run ur program  (local/remote): " , end='')
myhost = input()
print(myhost)

if myhost == "remote":
	remote_ip = input("Enter ur remote host ip : ")

print()

while True:
	print("""
	Press 1 : to date
	Press 2 : to cal
	Press 3 : to ls
	Press 4 : to mkdir
	Press 5 : to exit
	""")

	# espeak-ng

	print("enter ur choice : ", end='')
	ch = input()

	print(ch)

	if myhost == "remote":
		if int(ch) == 1:
			os.system( "ssh {} date".format(remote_ip) )

		elif int(ch) == 2:
			os.system("ssh {} cal".format(remote_ip) )

		elif int(ch) == 3:
			print("ls")

		elif int(ch) == 4:
			print("mkdir")

		elif int(ch) == 5:
			exit()

		else:
			print("not supported")

	input("Press enter to cont .....")
	os.system("clear")

