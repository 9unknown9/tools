#module
import os,sys,time,random

#Mau Coba Lgi
def lagi():
    f = raw_input("Mau Coba Lagi Ngab [ya/tidak] : ")
    if f  =="ya":
       os.system("python2 game.py")
    elif f =="tidak":
         sys.exit

#menu
def menu():
    os.system("clear")
    print "\033[1;92m\t pilih mana ngab\n"
    print "1.) Kertas"
    print "2.) Gunting"
    print "3.) Batu"
    Com = random.choice(("Kertas","Gunting","Batu"))
    pil = raw_input("Pilih sesuai Menu : ")

    #Kertas
    if pil =="1":
       print "Lu       : Kertas"
       print "komputer : ",Com
       if Com =="Kertas":
       	      print "Draw"
       elif Com =="Gunting":
              print "Lu Kalah"
       elif Com =="Batu":
              print "Lu Menang"

       lagi()
    #Gunting
    if pil =="2":
       print "Lu       : Gunting"
       print "komputer : ",Com
       if Com =="Kertas":
              print "Lu Menang"
       elif Com =="Gunting":
              print "Draw"
       elif Com  =="Batu":
              print "Lu Kalah"

       lagi()
    #Batu
    if pil =="3":
       print "Lu       : Batu"
       print "komputer : ",Com
       if Com =="Kertas":
              print "Lu Kalah"
       elif Com =="Gunting":
              print "Lu Menang"
       elif Com =="Batu":
              print "Draw"

       lagi()
menu()
