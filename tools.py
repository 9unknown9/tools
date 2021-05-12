#module
import os,sys

def menu():
    os.system("clear")
    print "\033[1;96m========================================================"
    print "\033[1;93m                         Tools"
    print "\033[1;92m                        -------"
    print "                  penembang:sks_mint"
    print "\033[1;96m--------------------------------------------------------"
    print "\033[1;91m1.)Calculator"
    print "2.)Game Unfaedah"
    print "3.)exit"
    print "\033[1;96m========================================================"
    print "\033[1;92m"
    f = raw_input("Mau No Berapa Ngab : ")

#system
    if f  =="1":
       os.system("https://github.com/9unknown9/kalkulator.py")
       os.system("cd kalkulator.py")
       os.system("python2 calculator.py")

    elif f =="2":
         os.system("https://github.com/9unknown9/game-unfaedah")
         os.system("cd game-unfaedah")
         os.system("python2 game.py")

    elif f =="3":
       os.system("exit")

menu()
