#module
import os,time,sys
os.system("clear")

#coba lagi
def lagi():
    f = raw_input("Mau Coba Lagi Ngab [ya/tidak] : ")
    if f  =="ya":
       os.system("python2 calculator.py")
    elif f =="tidak":
         sys.exit
#menu
print '     *=====================================*'
print '       buat orang yg gak bisa matematika '
print '     -------------------------------------'
print '             pengembang:sks_mint'
print '     *=====================================*'
print '     1.)pertambahan'
print '     2.)perkalian'
print '     3.)pengurangan'
print '     4.)pembagian '
print '     *=====================================*'
print '         mau no berapa  ngab'
print

#system
pilih = input('pilih ngab : ')
if pilih == 1:

      print
      angka_1 = input('angka pertama : ')
      angka_2 = input('angka kedua : ')
      total = angka_1 + angka_2
      print 'hasil pertambahan =',total

elif pilih == 2:

      print
      angka_1 = input('angka pertama : ')
      angka_2 = input('angka kedua : ')
      total = angka_1 * angka_2
      print 'hasil perkalian =',total

elif pilih == 3:

      print
      angka_1 = input('angka pertama : ')
      angka_2 = input('angka kedua : ')
      total = angka_1 - angka_2
      print 'hasil pengurangan =',total
elif pilih == 4:

      print
      angka_1 = input('angka pertama : ')
      angka_2 = input('angka kedua : ')
      total = angka_1 / angka_2
      print 'hasil pembagian =',total

lagi()
