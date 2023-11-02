# Nama toko pizza 

from colorama import Fore, Style
print(Fore.LIGHTYELLOW_EX + '========================================' , Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX +'Selamat Datang di Python Pizza Surabaya')
print(Fore.LIGHTYELLOW_EX + "========================================", Style.RESET_ALL)

# Memilih menu

from colorama import Fore, Style
print(Fore.LIGHTBLUE_EX + 'silahkan pilih menu yang anda suka', Style.RESET_ALL)

# Pilihan menu dan harga

print(Fore.LIGHTGREEN_EX + "===============Menu Python Pizza Surabaya=============", Style.RESET_ALL)
print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| No | Nama Makanan | Harga |', Style.RESET_ALL)
print(Fore.RED + "-----------------------------------" , Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 1 | Frankfurter BBQ | Rp 43.636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 2 | Meat Momanta | Rp 43.636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 3 | Super Supreme | Rp 43636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 4 | Super Supreme Chicken | Rp 43636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 5 | Mea Lovers | Rp 43.636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 6 | Chicken Lovers | Rp 43.636 |', Style.RESET_ALL)
print (Fore.LIGHTBLUE_EX +'| 7 |  Cheese Lovers | Rp 43.636 |', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '| 8 | American Favourite | Rp 43.636 |', Style.RESET_ALL )

# Input pilihan menu

harga_pizza=0;
pilih_menu = input('Pilih menu pizza yang kamu suka:').lower()
if pilih_menu == '1':
    harga_pizza = 43.636
    print(Fore.LIGHTBLUE_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '2' : 
    harga_pizza += 43.636
    print(Fore.LIGHTBLUE_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '3': 
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '4': 
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '5': 
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '6': 
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '7': 
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
elif pilih_menu == '8':  
    harga_pizza += 43.636
    print(Fore.LIGHTRED_EX + "Harga pizza nya adalah Rp 43.636", Style.RESET_ALL)
else: 
    print(Fore.LIGHTRED_EX + "Masukkan pilihan yang valid", Style.RESET_ALL)
    exit()

# Pilihan menu dan harga crust

print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
print(Fore.LIGHTYELLOW_EX + "============Pilihan Crust Pizza============", Style.RESET_ALL)
print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + '|No| Nama Crust |Harga|', Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "|1| Pan | Free |", Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "|2| StuffedCrust Cheese | Rp 11.819 |", Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "|3| StuffedCrust Sausage | Rp. 9.091 |", Style.RESET_ALL)
print(Fore.LIGHTBLUE_EX + "|4| Cheesy Bite Crust | Rp. 13.637 |", Style.RESET_ALL)

# Input pilihan crust

pilih_crust = input('Pilih crust pizza yang kamu suka:').lower()
if pilih_crust == '1':
    harga_pizza += 0
    print(Fore.LIGHTBLUE_EX + "Harga crust free", Style.RESET_ALL)
elif pilih_crust == '3': 
    harga_pizza += 11.819
    print(Fore.LIGHTBLUE_EX + "Harga crust Rp 11.819", Style.RESET_ALL)
elif pilih_crust == '4': 
    harga_pizza += 9.091
    print(Fore.LIGHTBLUE_EX + "Harga crust Rp 9.091", Style.RESET_ALL)
elif pilih_crust == '5': 
    harga_pizza += 13.637
    print(Fore.LIGHTBLUE_EX + "Harga crust Rp 13.637", Style.RESET_ALL)
else :
    print(Fore.LIGHTRED_EX + "Masukkan pilihan yang valid", Style.RESET_ALL)

# Memilih ukuran pizza

if pilih_menu == "1" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )

    
elif pilih_menu == "2" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )
    
elif pilih_menu == "3" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )

elif pilih_menu == "4" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )

elif pilih_menu == "5" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " ) 

elif pilih_menu == "6" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )   

elif pilih_menu == "7" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )

elif pilih_menu == "2" :
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTYELLOW_EX + "============Pilihan Ukuran Pizza============", Style.RESET_ALL)
    print(Fore.RED + "-----------------------------------", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '|No| Nama Ukuran |Harga|', Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 1 | Personal | Rp 43.636 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 2 | Regular | Rp 57.273 |", Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + "| 3 | Large | Rp 89.091 |", Style.RESET_ALL)
    ukuran_pizza = input("Pilih Ukuran Pizza Anda: " )    
else:
   print (harga_pizza, "Terimakasih Telah Memilih Python Pizza Surabaya")
   
# Input ukuran pizza
if ukuran_pizza == '1' :
       harga_pizza += 43.636
elif ukuran_pizza == '2' :
       harga_pizza += 57.273
elif ukuran_pizza == '3' :
       harga_pizza += 89.091
else :
        print("Ukuran Pizza tidak Valid")
        exit()

# Tambahan Keju

tambah_keju = input("Tambah 19.091 untuk Extra Keju (ya/tidak): ")
if "ya" in tambah_keju:
    harga_pizza += 19.091
    print(Fore.LIGHTGREEN_EX+ "Total pesanan anda adalah Rp." + str(harga_pizza))
else:
    harga_pizza += 0
print(Fore.LIGHTBLUE_EX + "Total pesanan anda adalah Rp." + str(harga_pizza))

# Total biaya
    
print(Fore.LIGHTBLUE_EX + "Terimakasih Telah Memilih Python Pizza Surabaya", Style.RESET_ALL)
    
    


