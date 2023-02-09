import phonenumbers as nomor

from phonenumbers import geocoder, carrier, timezone

def main():
    os.system("clear")
    os.system("figlet ZinXploit")
    banner = '''
   

    )               )                          
 ( /(            ( /(         (             )  
 )\()) (         )\())        )\     (   ( /(  
((_)\  )\   (   ((_)\  `  )  ((_) (  )\  )\()) 
 _((_)((_)  )\ )__((_) /(/(   _   )\((_)(_))/  
|_  /  (_) _(_/(\ \/ /((_)_\ | | ((_)(_)| |_   
 / /   | || ' \))>  < | '_ \)| |/ _ \| ||  _|  
/___|  |_||_||_|/_/\_\| .__/ |_|\___/|_| \__|  
                      |_|                      

'''

    print(banner)

teks = input("Enter the phone number : ")

konv = nomor.parse(teks)

nomorTelepon = geocoder.description_for_number(konv, "id")
isp = carrier.name_for_number(konv, "id")
zonaWaktu = timezone.time_zones_for_number(konv)

print("Nomor dari Negara : ", nomorTelepon)
print("ISP nomor : ", isp)
print("Zona waktu nomor : ", zonaWaktu)

