# PiPicoPapagei
#dies PRG soll die Zubehöreingabe des FTDX3000 ergänzen und 
#eine Textdauerschleife ermöglichen.
# es klappt bei allen YAESU-TRX die ein FH2 verwenden
# Es funktioniert auch bei Anpassung der Schaltung am:
# IC9700, IC7300 und beim IC705
#DL1YAR Novembr 2023

#from machine import Pin
#import utime



import board
import digitalio
import time

import analogio
# Pinfestlegungen
# erster Test


Tast1 = digitalio.DigitalInOut(board.GP11)   #Texttaster an Pin 
Tast2 = digitalio.DigitalInOut(board.GP12)   #Texttaster an Pin
Tast3 = digitalio.DigitalInOut(board.GP13)   #Texttaster an Pin 
Tast4 = digitalio.DigitalInOut(board.GP14)   #Texttaster an Pin 
Timer = digitalio.DigitalInOut(board.GP15)   #Timer Wiederholzeit



T4 = digitalio.DigitalInOut(board.GP16)		# Text1-Taster am Modul FH-2
T4.direction = digitalio.Direction.OUTPUT 	#
T3 = digitalio.DigitalInOut(board.GP17) # Text2-Taster
T3.direction = digitalio.Direction.OUTPUT
T2 = digitalio.DigitalInOut(board.GP18) # Text3-Taster
T2.direction = digitalio.Direction.OUTPUT
T1 = digitalio.DigitalInOut(board.GP19) # Text4-Tastert
T1.direction = digitalio.Direction.OUTPUT


led = digitalio.DigitalInOut(board.LED)
led1 = digitalio.DigitalInOut(board.GP7)
led.direction = digitalio.Direction.OUTPUT
led1.direction = digitalio.Direction.OUTPUT




merker = 0
merker_l = 0
#zeit   = 0
#WARTEN = 0

def Text_aus(x): #Textausgabe 1-4
	global merker, merker_l,zeit
	#Led_Ausgabe.value = True
	led.value =True
	led1.value =True
	print("Text_aus ",x)
	if (x ==1):
		T1.value = True
	if (x ==2):
		T2.value = True
	if (x ==3):
		T3.value = True
	if (x ==4):
		T4.value = True
	time.sleep(0.1)
	T1.value = False
	T2.value = False
	T3.value = False
	T4.value = False
	time.sleep(0.8)
	led.value =False
	led1.value =False
	
def toggle_Led_Timer():
	global merker, merker_l,zeit
	print(x,'  ',y)
	if (merker_l == 0):
		led.value = True
		led1.value = True
		merker_l =1
	elif (merker_l ==1):
		led.value = False
		led1.value = False
		merker_l =0
    
#########################################################
        
        

      
        
########################################################        
merker =0
x = 0  #allgemeiner Zähler
y = 0
print("  ---DL1YAR IC9K7 Papagei am 29.2.2024-------")
#hauptschleife###########################################
while True:
	while (Tast1.value == True):
		merker = 1
		Text_aus(merker)
	while (Tast2.value == True):
		merker = 2
		Text_aus(merker)
	while (Tast3.value == True):
		merker = 3
		Text_aus(merker)
	while (Tast4.value == True):
		merker = 4
		Text_aus(merker)
	while(merker !=0):
		x=x+1
		toggle_Led_Timer()
		time.sleep(0.5)
		if (x ==y):
			print(" ausgabe")
			Text_aus(merker)
			x=0
		if(Timer.value == True):#wiedrholung starten
			print(" WIEDERHOLUNG")
			while(Timer.value == True):#wiedrholung starten
				time.sleep(0.1)
			Text_aus(merker)
			y=x #Zaehler setzen
			x=0
		while((Tast1.value == True)or (Tast2.value == True)or (Tast3.value == True)or (Tast4.value == True)):
			print(" Stopp")
			y=0
			x=0
			merker = 0
			led.value = False
			led1.value = False
			time.sleep(0.1)  #gegen Tastenprellen
