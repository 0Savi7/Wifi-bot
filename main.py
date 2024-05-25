#Modules
import subprocess
import tkinter as tk
from tkinter import simpledialog

#Subprogram
def network():
    bot = tk.Tk()
    bot.withdraw()
    network_name = simpledialog.askstring("wifipassword","Please input the name of the wifi password: " )
    return(network_name)



network_name = network()

if not network_name:
    print("Network name has not been provided program is Exiting....")

else:
     netsh = f'netsh wlan show profile name="{network_name}" key=clear > wifipassword.txt'
     try:
         netsh_output = subprocess.run(netsh, shell=True, check=True)
        
        

     except subprocess.CalledProcessError as e:
          print(f'Command could not be executed because of: {e}')
    
     except Exception as e:
          print(f'Command could not be executed because of: {e}')
    
     
     
     
     
