import subprocess

newMac = input("Enter ur new mac : " )
dev = input("Enter net interface : ")

def mac_change(newMac,dev):
     subProc=subprocess.run
     try:

         subProc(["ifconfig", dev, "down"] )
         subProc(["ifconfig",dev,"hw","ether" , newMac ] )
         subProc(["ifconfig",dev,"up"] )

         print("############### Mac address is changed successfully ####################")
         subProc("ifconfig " ,shell=True)
     except:
         print("There was an error")
mac_change(newMac,dev)         