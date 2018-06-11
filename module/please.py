import os, sys


print ("\033[1;32mMasukan User Ama Pasword:)")

print ("\033[1;31;1mKalo Gak Tau Pm Mr.Kovlak.Jr ^085848812535^")

username = 'Tn.Kovlak.Jr' 

password = 'CoGans'


def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)


def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")


		if pwd == password:

			print "\n\033[1;34mHello Welcome To Tools Mr.KOVLAK.Jr", 

			sys.exit()


		else:

			print "\n\033[1;36mSorry Invalid Password !!!\033[00m"

			print "Back Login\n"

			restart()


	else:

		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"

		print "Back Login\n"

		restart()


try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()

