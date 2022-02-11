from tkinter import *
import os
import platform
from tkinter import ttk
import tkinter
from tkinter.filedialog import askopenfilename
import shutil
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import colorchooser
from typing import DefaultDict
from PIL import Image
import os
import PIL
import glob
#from subprocess import call
import RPi.GPIO as GPIO
import time

import random

"""
For speech install this on rPi
aplay /usr/share/sounds/alsa/*
If you are able to hear the sounds like “Front Center”,”Front Left”, “Front Right” and so on, your sound is working!  
sudo apt-get install espeak
Examples
espeak "Text you wish to hear back" 2>/dev/null
espeak "Hello World" 2>/dev/null
"""

root=Tk()
root.title("ICOS (Interactive COncept Simplifier)")
if platform.system() == "Windows":
    root.iconbitmap("Logo.ico")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

#Format directions
srcActuals="ActualStates.txt"
srcConfig="Configuration.txt"
srcInter="Interaction.txt"

#Funcion para obtener
def Obtain(srcS,index):
	File=open(srcS,"r")
	Lines=File.readlines()
	File.close()
	Result=Lines[index].rstrip("\n")
	Result.strip()
	return Result
	pass

#Interacciones
GPIO.setmode(GPIO.BOARD)

#Pin Arrays
RGB1 = [40,37,38]
RGB2 = [35,36,31]
RGB3 = [29,27,28]
RGB4 = [15,16,13]
RGB5 = [12,10,8]
Buzzer = 7

#Pin set Modes
#RGB1
GPIO.setup(RGB1[0], GPIO.OUT)
GPIO.setup(RGB1[1], GPIO.OUT)
GPIO.setup(RGB1[2], GPIO.OUT)

#RGB2
GPIO.setup(RGB2[0], GPIO.OUT)
GPIO.setup(RGB2[1], GPIO.OUT)
GPIO.setup(RGB2[2], GPIO.OUT)

#RGB3
GPIO.setup(RGB3[0], GPIO.OUT)
GPIO.setup(RGB3[1], GPIO.OUT)
GPIO.setup(RGB3[2], GPIO.OUT)

#RGB4
GPIO.setup(RGB4[0], GPIO.OUT)
GPIO.setup(RGB4[1], GPIO.OUT)
GPIO.setup(RGB4[2], GPIO.OUT)

#RGB5
GPIO.setup(RGB5[0], GPIO.OUT)
GPIO.setup(RGB5[1], GPIO.OUT)
GPIO.setup(RGB5[2], GPIO.OUT)

#Buzzer
GPIO.setup(Buzzer, GPIO.OUT)

#SET OFF
GPIO.output(RGB1[0],True)
GPIO.output(RGB2[0],True)
GPIO.output(RGB3[0],True)
GPIO.output(RGB4[0],True)
GPIO.output(RGB5[0],True)

GPIO.output(RGB1[1],True)
GPIO.output(RGB2[1],True)
GPIO.output(RGB3[1],True)
GPIO.output(RGB4[1],True)
GPIO.output(RGB5[1],True)

GPIO.output(RGB1[2],True)
GPIO.output(RGB2[2],True)
GPIO.output(RGB3[2],True)
GPIO.output(RGB4[2],True)
GPIO.output(RGB5[2],True)

GPIO.output(Buzzer,False)

#Obtener configuracion
global Configures
Configures =[[Obtain(srcConfig,2),Obtain(srcConfig,3),Obtain(srcConfig,4),Obtain(srcConfig,5),Obtain(srcConfig,6),Obtain(srcConfig,7),Obtain(srcConfig,8)],
			[Obtain(srcConfig,11),Obtain(srcConfig,12),Obtain(srcConfig,13),Obtain(srcConfig,14),Obtain(srcConfig,15),Obtain(srcConfig,16),Obtain(srcConfig,17)],
			[Obtain(srcConfig,20)],[Obtain(srcConfig,23)],[Obtain(srcConfig,26)],[Obtain(srcConfig,29)]]

#Words of the images
FW0 = eval(Obtain(srcConfig,32))
FW1 = eval(Obtain(srcConfig,33))
FW2 = eval(Obtain(srcConfig,34))
FW3 = eval(Obtain(srcConfig,35))
FW4 = eval(Obtain(srcConfig,36))
FW5 = eval(Obtain(srcConfig,37))
FW6 = eval(Obtain(srcConfig,38))
FW7 = eval(Obtain(srcConfig,39))
Word = [FW0,FW1,FW2,FW3,FW4,FW5,FW6,FW7]

#Directions of the images
srcCon=[["","","","","","","","","","","","","","",""],
		["C1/001.png","C1/002.png","C1/003.png","C1/004.png","C1/005.png","C1/006.png","C1/007.png","C1/008.png","C1/009.png","C1/010.png","C1/011.png","C1/012.png","C1/013.png","C1/014.png","C1/015.png"],
		["C2/001.png","C2/002.png","C2/003.png","C2/004.png","C2/005.png","C2/006.png","C2/007.png","C2/008.png","C2/009.png","C2/010.png","C2/011.png","C2/012.png","C2/013.png","C2/014.png","C2/015.png"],
		["C3/001.png","C3/002.png","C3/003.png","C3/004.png","C3/005.png","C3/006.png","C3/007.png","C3/008.png","C3/009.png","C3/010.png","C3/011.png","C3/012.png","C3/013.png","C3/014.png","C3/015.png"],
		["C4/001.png","C4/002.png","C4/003.png","C4/004.png","C4/005.png","C4/006.png","C4/007.png","C4/008.png","C4/009.png","C4/010.png","C4/011.png","C4/012.png","C4/013.png","C4/014.png","C4/015.png"],
		["C5/001.png","C5/002.png","C5/003.png","C5/004.png","C5/005.png","C5/006.png","C5/007.png","C5/008.png","C5/009.png","C5/010.png","C5/011.png","C5/012.png","C5/013.png","C5/014.png","C5/015.png"],
		["C6/001.png","C6/002.png","C6/003.png","C6/004.png","C6/005.png","C6/006.png","C6/007.png","C6/008.png","C6/009.png","C6/010.png","C6/011.png","C6/012.png","C6/013.png","C6/014.png","C6/015.png"],
		["C7/001.png","C7/002.png","C7/003.png","C7/004.png","C7/005.png","C7/006.png","C7/007.png","C7/008.png","C7/009.png","C7/010.png","C7/011.png","C7/012.png","C7/013.png","C7/014.png","C7/015.png"]]

#Names of the flanges
global FName
FName=  [Configures[0][0],Configures[0][1],Configures[0][2],Configures[0][3],Configures[0][4],Configures[0][5],Configures[0][6]]

#Color of the flanges
global FColor
FColor= [Configures[1][0],Configures[1][1],Configures[1][2],Configures[1][3],Configures[1][4],Configures[1][5],Configures[1][6]]

#Text Color
global TxtBack
TxtBack=Configures[2][0]
#Color de fuente
global TxtColor
TxtColor= Configures[3][0]

#Sentence Color
global SColor
SColor=Configures[4][0]

#System in use
global System
System=Configures[5][0]#PC or rPi

#None photo
Non = PhotoImage(file="None.png")

#Concepts Flanges Images
ICon1 = PhotoImage(file="Concepts/001.png")
ICon2 = PhotoImage(file="Concepts/001.png")
ICon3 = PhotoImage(file="Concepts/001.png")
ICon4 = PhotoImage(file="Concepts/001.png")
ICon5 = PhotoImage(file="Concepts/001.png")
ICon6 = PhotoImage(file="Concepts/001.png")
ICon7 = PhotoImage(file="Concepts/001.png")

#Concepts Buttons Images
#Concepts1
CBImg1_1 = PhotoImage(file=srcCon[1][0])
CBImg1_2 = PhotoImage(file=srcCon[1][1])
CBImg1_3 = PhotoImage(file=srcCon[1][2])
CBImg1_4 = PhotoImage(file=srcCon[1][3])
CBImg1_5 = PhotoImage(file=srcCon[1][4])
CBImg1_6 = PhotoImage(file=srcCon[1][5])
CBImg1_7 = PhotoImage(file=srcCon[1][6])
CBImg1_8 = PhotoImage(file=srcCon[1][7])
CBImg1_9 = PhotoImage(file=srcCon[1][8])
CBImg1_10 = PhotoImage(file=srcCon[1][9])
CBImg1_11 = PhotoImage(file=srcCon[1][10])
CBImg1_12 = PhotoImage(file=srcCon[1][11])
CBImg1_13 = PhotoImage(file=srcCon[1][12])
CBImg1_14 = PhotoImage(file=srcCon[1][13])
CBImg1_15 = PhotoImage(file=srcCon[1][14])
#Concepts2
CBImg2_1 = PhotoImage(file=srcCon[2][0])
CBImg2_2 = PhotoImage(file=srcCon[2][1])
CBImg2_3 = PhotoImage(file=srcCon[2][2])
CBImg2_4 = PhotoImage(file=srcCon[2][3])
CBImg2_5 = PhotoImage(file=srcCon[2][4])
CBImg2_6 = PhotoImage(file=srcCon[2][5])
CBImg2_7 = PhotoImage(file=srcCon[2][6])
CBImg2_8 = PhotoImage(file=srcCon[2][7])
CBImg2_9 = PhotoImage(file=srcCon[2][8])
CBImg2_10 = PhotoImage(file=srcCon[2][9])
CBImg2_11 = PhotoImage(file=srcCon[2][10])
CBImg2_12 = PhotoImage(file=srcCon[2][11])
CBImg2_13 = PhotoImage(file=srcCon[2][12])
CBImg2_14 = PhotoImage(file=srcCon[2][13])
CBImg2_15 = PhotoImage(file=srcCon[2][14])
#Concepts3
CBImg3_1 = PhotoImage(file=srcCon[3][0])
CBImg3_2 = PhotoImage(file=srcCon[3][1])
CBImg3_3 = PhotoImage(file=srcCon[3][2])
CBImg3_4 = PhotoImage(file=srcCon[3][3])
CBImg3_5 = PhotoImage(file=srcCon[3][4])
CBImg3_6 = PhotoImage(file=srcCon[3][5])
CBImg3_7 = PhotoImage(file=srcCon[3][6])
CBImg3_8 = PhotoImage(file=srcCon[3][7])
CBImg3_9 = PhotoImage(file=srcCon[3][8])
CBImg3_10 = PhotoImage(file=srcCon[3][9])
CBImg3_11 = PhotoImage(file=srcCon[3][10])
CBImg3_12 = PhotoImage(file=srcCon[3][11])
CBImg3_13 = PhotoImage(file=srcCon[3][12])
CBImg3_14 = PhotoImage(file=srcCon[3][13])
CBImg3_15 = PhotoImage(file=srcCon[3][14])
#Concepts4
CBImg4_1 = PhotoImage(file=srcCon[4][0])
CBImg4_2 = PhotoImage(file=srcCon[4][1])
CBImg4_3 = PhotoImage(file=srcCon[4][2])
CBImg4_4 = PhotoImage(file=srcCon[4][3])
CBImg4_5 = PhotoImage(file=srcCon[4][4])
CBImg4_6 = PhotoImage(file=srcCon[4][5])
CBImg4_7 = PhotoImage(file=srcCon[4][6])
CBImg4_8 = PhotoImage(file=srcCon[4][7])
CBImg4_9 = PhotoImage(file=srcCon[4][8])
CBImg4_10 = PhotoImage(file=srcCon[4][9])
CBImg4_11 = PhotoImage(file=srcCon[4][10])
CBImg4_12 = PhotoImage(file=srcCon[4][11])
CBImg4_13 = PhotoImage(file=srcCon[4][12])
CBImg4_14 = PhotoImage(file=srcCon[4][13])
CBImg4_15 = PhotoImage(file=srcCon[4][14])
#Concepts5
CBImg5_1 = PhotoImage(file=srcCon[5][0])
CBImg5_2 = PhotoImage(file=srcCon[5][1])
CBImg5_3 = PhotoImage(file=srcCon[5][2])
CBImg5_4 = PhotoImage(file=srcCon[5][3])
CBImg5_5 = PhotoImage(file=srcCon[5][4])
CBImg5_6 = PhotoImage(file=srcCon[5][5])
CBImg5_7 = PhotoImage(file=srcCon[5][6])
CBImg5_8 = PhotoImage(file=srcCon[5][7])
CBImg5_9 = PhotoImage(file=srcCon[5][8])
CBImg5_10 = PhotoImage(file=srcCon[5][9])
CBImg5_11 = PhotoImage(file=srcCon[5][10])
CBImg5_12 = PhotoImage(file=srcCon[5][11])
CBImg5_13 = PhotoImage(file=srcCon[5][12])
CBImg5_14 = PhotoImage(file=srcCon[5][13])
CBImg5_15 = PhotoImage(file=srcCon[5][14])
#Concepts6
CBImg6_1 = PhotoImage(file=srcCon[6][0])
CBImg6_2 = PhotoImage(file=srcCon[6][1])
CBImg6_3 = PhotoImage(file=srcCon[6][2])
CBImg6_4 = PhotoImage(file=srcCon[6][3])
CBImg6_5 = PhotoImage(file=srcCon[6][4])
CBImg6_6 = PhotoImage(file=srcCon[6][5])
CBImg6_7 = PhotoImage(file=srcCon[6][6])
CBImg6_8 = PhotoImage(file=srcCon[6][7])
CBImg6_9 = PhotoImage(file=srcCon[6][8])
CBImg6_10 = PhotoImage(file=srcCon[6][9])
CBImg6_11 = PhotoImage(file=srcCon[6][10])
CBImg6_12 = PhotoImage(file=srcCon[6][11])
CBImg6_13 = PhotoImage(file=srcCon[6][12])
CBImg6_14 = PhotoImage(file=srcCon[6][13])
CBImg6_15 = PhotoImage(file=srcCon[6][14])
#Concepts7
CBImg7_1 = PhotoImage(file=srcCon[7][0])
CBImg7_2 = PhotoImage(file=srcCon[7][1])
CBImg7_3 = PhotoImage(file=srcCon[7][2])
CBImg7_4 = PhotoImage(file=srcCon[7][3])
CBImg7_5 = PhotoImage(file=srcCon[7][4])
CBImg7_6 = PhotoImage(file=srcCon[7][5])
CBImg7_7 = PhotoImage(file=srcCon[7][6])
CBImg7_8 = PhotoImage(file=srcCon[7][7])
CBImg7_9 = PhotoImage(file=srcCon[7][8])
CBImg7_10 = PhotoImage(file=srcCon[7][9])
CBImg7_11 = PhotoImage(file=srcCon[7][10])
CBImg7_12 = PhotoImage(file=srcCon[7][11])
CBImg7_13 = PhotoImage(file=srcCon[7][12])
CBImg7_14 = PhotoImage(file=srcCon[7][13])
CBImg7_15 = PhotoImage(file=srcCon[7][14])

CBImg = [[CBImg1_1,CBImg1_2,CBImg1_3,CBImg1_4,CBImg1_5,CBImg1_6,CBImg1_7,CBImg1_8,CBImg1_9,CBImg1_10,CBImg1_11,CBImg1_12,CBImg1_13,CBImg1_14,CBImg1_15],
		[CBImg2_1,CBImg2_2,CBImg2_3,CBImg2_4,CBImg2_5,CBImg2_6,CBImg2_7,CBImg2_8,CBImg2_9,CBImg2_10,CBImg2_11,CBImg2_12,CBImg2_13,CBImg2_14,CBImg2_15],
		[CBImg3_1,CBImg3_2,CBImg3_3,CBImg3_4,CBImg3_5,CBImg3_6,CBImg3_7,CBImg3_8,CBImg3_9,CBImg3_10,CBImg3_11,CBImg3_12,CBImg3_13,CBImg3_14,CBImg3_15],
		[CBImg4_1,CBImg4_2,CBImg4_3,CBImg4_4,CBImg4_5,CBImg4_6,CBImg4_7,CBImg4_8,CBImg4_9,CBImg4_10,CBImg4_11,CBImg4_12,CBImg4_13,CBImg4_14,CBImg4_15],
		[CBImg5_1,CBImg5_2,CBImg5_3,CBImg5_4,CBImg5_5,CBImg5_6,CBImg5_7,CBImg5_8,CBImg5_9,CBImg5_10,CBImg5_11,CBImg5_12,CBImg5_13,CBImg5_14,CBImg5_15],
		[CBImg6_1,CBImg6_2,CBImg6_3,CBImg6_4,CBImg6_5,CBImg6_6,CBImg6_7,CBImg6_8,CBImg6_9,CBImg6_10,CBImg6_11,CBImg6_12,CBImg6_13,CBImg6_14,CBImg6_15],
		[CBImg7_1,CBImg7_2,CBImg7_3,CBImg7_4,CBImg7_5,CBImg7_6,CBImg7_7,CBImg7_8,CBImg7_9,CBImg7_10,CBImg7_11,CBImg7_12,CBImg7_13,CBImg7_14,CBImg7_15]]

def ReadText(TextToRead,Sys):
	if(Sys=="rPi"):
		"""
		cmd_beg= 'espeak '
		cmd_end= ' 2>/dev/null'
		TextToRead= TextToRead.replace(' ', '_')
		call([cmd_beg+TextToRead+cmd_end], shell=True)
		"""
	elif(Sys=="PC"):
		print(TextToRead)
		pass
	pass
def modificar(arch,line,val):
	File=open(arch, "r")
	lines=File.readlines()
	File.close()
	lines[line]=str(val)+"\n"
	File_New=open(arch, "w")
	for l in lines:
		File_New.write(l)
		pass
	File_New.close()
	pass
def BChange(srcC,bColor,FNum):
	#Introducir en renglon1 la ubicacion de la flange
	CImg1.config(image = CBImg[FNum][0])
	CImg2.config(image = CBImg[FNum][1])
	CImg3.config(image = CBImg[FNum][2])
	CImg4.config(image = CBImg[FNum][3])
	CImg5.config(image = CBImg[FNum][4])
	CImg6.config(image = CBImg[FNum][5])
	CImg7.config(image = CBImg[FNum][6])
	CImg8.config(image = CBImg[FNum][7])
	CImg9.config(image = CBImg[FNum][8])
	CImg10.config(image = CBImg[FNum][9])
	CImg11.config(image = CBImg[FNum][10])
	CImg12.config(image = CBImg[FNum][11])
	CImg13.config(image = CBImg[FNum][12])
	CImg14.config(image = CBImg[FNum][13])
	CImg15.config(image = CBImg[FNum][14])
	Words.config(bg = bColor)
	LImg1.config(text= Word[FNum+1][0])
	LImg2.config(text= Word[FNum+1][1])
	LImg3.config(text= Word[FNum+1][2])
	LImg4.config(text= Word[FNum+1][3])
	LImg5.config(text= Word[FNum+1][4])
	LImg6.config(text= Word[FNum+1][5])
	LImg7.config(text= Word[FNum+1][6])
	LImg8.config(text= Word[FNum+1][7])
	LImg9.config(text= Word[FNum+1][8])
	LImg10.config(text= Word[FNum+1][9])
	LImg11.config(text= Word[FNum+1][10])
	LImg12.config(text= Word[FNum+1][11])
	LImg13.config(text= Word[FNum+1][12])
	LImg14.config(text= Word[FNum+1][13])
	LImg15.config(text= Word[FNum+1][14])
	modificar(srcC,1,str(FNum+1))
	pass
def SendImage(srcC,Flange,ConceptImg,SelectedConcepts,WordsC):
	if (SelectedConcepts == 0):
		SConscept1.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts == 1):
		SConscept2.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts == 2):
		SConscept3.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts == 3):
		SConscept4.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts == 4):
		SConscept5.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts == 5):
		SConscept6.config(image = CBImg[Flange-1][ConceptImg])
		pass
	if (SelectedConcepts<=6):
		modificar(srcC,3,str(SelectedConcepts+1))
		modificar(srcC,4+SelectedConcepts,WordsC[Flange][ConceptImg])
		pass
	pass
def DownButton(srcC,SelectedConcepts):
	if (SelectedConcepts == 1):
		SConscept1.config(image = Non)
		pass
	if (SelectedConcepts == 2):
		SConscept2.config(image = Non)
		pass
	if (SelectedConcepts == 3):
		SConscept3.config(image = Non)
		pass
	if (SelectedConcepts == 4):
		SConscept4.config(image = Non)
		pass
	if (SelectedConcepts == 5):
		SConscept5.config(image = Non)
		pass
	if (SelectedConcepts == 6):
		SConscept6.config(image = Non)
		pass
	if (SelectedConcepts>0):
		modificar(srcC,3,str(SelectedConcepts-1))
		modificar(srcC,3+SelectedConcepts,"")
		pass
	pass
def End(srcC):
	modificar(srcC,3,"0")
	modificar(srcC,4,"")
	modificar(srcC,5,"")
	modificar(srcC,6,"")
	modificar(srcC,7,"")
	modificar(srcC,8,"")
	modificar(srcC,9,"")
	SConscept1.config(image = Non)
	SConscept2.config(image = Non)
	SConscept3.config(image = Non)
	SConscept4.config(image = Non)
	SConscept5.config(image = Non)
	SConscept6.config(image = Non)
	pass
def Play(srcC,Syst):
	SelcConc=[Obtain(srcC,4),Obtain(srcC,5),Obtain(srcC,6),Obtain(srcC,7),Obtain(srcC,8),Obtain(srcC,9)]
	print(SelcConc)
	
	File=open(srcC,"r")
	Lines=File.readlines()
	File.close()
	SelcConc=[Lines[4],Lines[5],Lines[6],Lines[7],Lines[8],Lines[9]]
	print(SelcConc)
	for i in SelcConc:
		print(str(i),end="")
	print()
	print(SelcConc)
	
	if SelcConc[0] != "":
		wSel=SelcConc[0]+"    "
		ReadText(wSel,Syst)
		pass
	if SelcConc[1] != "":
		wSel=SelcConc[1]+"    "
		ReadText(wSel,Syst)
		pass
	if SelcConc[2] != "":
		wSel=SelcConc[2]+"    "
		ReadText(wSel,Syst)
		pass
	if SelcConc[3] != "":
		wSel=SelcConc[3]+"    "
		ReadText(wSel,Syst)
		pass
	if SelcConc[4] != "":
		wSel=SelcConc[4]+"    "
		ReadText(wSel,Syst)
		pass
	if SelcConc[5] != "":
		wSel=SelcConc[5]+"    "
		ReadText(wSel,Syst)
		pass

	if (SelcConc[0]=="Yo" and SelcConc[1]=="Estresado"):
		print("Estresado")

		Tp = 0

		GPIO.output(RGB1[Tp],False)
		time.sleep(1)
		GPIO.output(RGB1[Tp],True)
		GPIO.output(RGB2[Tp],False)
		time.sleep(1)
		GPIO.output(RGB2[Tp],True)
		GPIO.output(RGB3[Tp],False)
		time.sleep(1)
		GPIO.output(RGB3[Tp],True)
		GPIO.output(RGB4[Tp],False)
		time.sleep(1)
		GPIO.output(RGB4[Tp],True)
		GPIO.output(RGB5[Tp],False)
		time.sleep(1)
		GPIO.output(RGB5[Tp],True)
		GPIO.output(RGB4[Tp],False)
		time.sleep(1)
		GPIO.output(RGB4[Tp],True)
		GPIO.output(RGB3[Tp],False)
		time.sleep(1)
		GPIO.output(RGB3[Tp],True)
		GPIO.output(RGB2[Tp],False)
		time.sleep(1)
		GPIO.output(RGB2[Tp],True)
		GPIO.output(RGB1[Tp],False)
		time.sleep(1)
		GPIO.output(RGB1[Tp],True)
		GPIO.output(RGB2[Tp],False)
		time.sleep(1)
		GPIO.output(RGB2[Tp],True)
		GPIO.output(RGB3[Tp],False)
		time.sleep(1)
		GPIO.output(RGB3[Tp],True)
		GPIO.output(RGB4[Tp],False)
		time.sleep(1)
		GPIO.output(RGB4[Tp],True)
		GPIO.output(RGB5[Tp],False)
		time.sleep(1)
		GPIO.output(RGB5[Tp],True)
		pass
	
	if (SelcConc[0]=="Yo" and SelcConc[1]=="Hambre"):
		GPIO.output(Buzzer,True)
		time.sleep(2)
		GPIO.output(Buzzer,False)
		pass

	if (SelcConc[0]=="Colores"):
		num = random.randint(0,2)
		GPIO.output(RGB1[num],False)
		GPIO.output(RGB2[num],False)
		GPIO.output(RGB3[num],False)
		GPIO.output(RGB4[num],False)
		GPIO.output(RGB5[num],False)
		time.sleep(2)
		GPIO.output(RGB1[num],True)
		GPIO.output(RGB2[num],True)
		GPIO.output(RGB3[num],True)
		GPIO.output(RGB4[num],True)
		GPIO.output(RGB5[num],True)
		pass

	if (SelcConc[0]=="Yo Quiero" and SelcConc[1]=="Bailar"):
		num = random.randint(0,2)
		GPIO.output(RGB1[num],False)
		GPIO.output(RGB2[num],False)
		GPIO.output(RGB3[num],False)
		GPIO.output(RGB4[num],False)
		GPIO.output(RGB5[num],False)
		GPIO.output(Buzzer,True)
		time.sleep(1)
		GPIO.output(RGB1[num],True)
		GPIO.output(RGB2[num],True)
		GPIO.output(RGB3[num],True)
		GPIO.output(RGB4[num],True)
		GPIO.output(RGB5[num],True)
		GPIO.output(Buzzer,False)
		time.sleep(1)
		num = random.randint(0,2)
		GPIO.output(RGB1[num],False)
		GPIO.output(RGB2[num],False)
		GPIO.output(RGB3[num],False)
		GPIO.output(RGB4[num],False)
		GPIO.output(RGB5[num],False)
		GPIO.output(Buzzer,True)
		time.sleep(1)
		GPIO.output(RGB1[num],True)
		GPIO.output(RGB2[num],True)
		GPIO.output(RGB3[num],True)
		GPIO.output(RGB4[num],True)
		GPIO.output(RGB5[num],True)
		GPIO.output(Buzzer,False)
		time.sleep(1)
		num = random.randint(0,2)
		GPIO.output(RGB1[num],False)
		GPIO.output(RGB2[num],False)
		GPIO.output(RGB3[num],False)
		GPIO.output(RGB4[num],False)
		GPIO.output(RGB5[num],False)
		GPIO.output(Buzzer,True)
		time.sleep(1)
		GPIO.output(RGB1[num],True)
		GPIO.output(RGB2[num],True)
		GPIO.output(RGB3[num],True)
		GPIO.output(RGB4[num],True)
		GPIO.output(RGB5[num],True)
		GPIO.output(Buzzer,False)
		time.sleep(1)
		num = random.randint(0,2)
		GPIO.output(RGB1[num],False)
		GPIO.output(RGB2[num],False)
		GPIO.output(RGB3[num],False)
		GPIO.output(RGB4[num],False)
		GPIO.output(RGB5[num],False)
		GPIO.output(Buzzer,True)
		time.sleep(1)
		GPIO.output(RGB1[num],True)
		GPIO.output(RGB2[num],True)
		GPIO.output(RGB3[num],True)
		GPIO.output(RGB4[num],True)
		GPIO.output(RGB5[num],True)
		GPIO.output(Buzzer,False)
		pass
	End(srcC)
	pass
def UbFlange(srcF):
	File=open(srcF,"r")
	Lines=File.readlines()
	File.close()
	ActualFlange=int(Lines[1])
	return ActualFlange
	pass
def SelConcepts(srcC):
	File=open(srcC,"r")
	Lines=File.readlines()
	File.close()
	ActualConcepts=int(Lines[3])
	return ActualConcepts
	pass
def Reload():
	global Configures
	global FColor
	global FName
	global TxtBack
	global SColor
	global System
	Configures =[[Obtain(srcConfig,2),Obtain(srcConfig,3),Obtain(srcConfig,4),Obtain(srcConfig,5),Obtain(srcConfig,6),Obtain(srcConfig,7),Obtain(srcConfig,8)],
			[Obtain(srcConfig,11),Obtain(srcConfig,12),Obtain(srcConfig,13),Obtain(srcConfig,14),Obtain(srcConfig,15),Obtain(srcConfig,16),Obtain(srcConfig,17)],
			[Obtain(srcConfig,20)],[Obtain(srcConfig,23)],[Obtain(srcConfig,26)],[Obtain(srcConfig,29)]]
	FColor= [Configures[1][0],Configures[1][1],Configures[1][2],Configures[1][3],Configures[1][4],Configures[1][5],Configures[1][6]]
	FName=  [Configures[0][0],Configures[0][1],Configures[0][2],Configures[0][3],Configures[0][4],Configures[0][5],Configures[0][6]]
	TxtBack=Configures[2][0]
	TxtColor=Configures[3][0]
	SColor=Configures[4][0]
	System=Configures[5][0]#PC or rPi
	#.configure()
	pass
def EndConfigure(srcS):
	conf = [[TxtFlange1N,TxtFlange2N,TxtFlange3N,TxtFlange4N,TxtFlange5N,TxtFlange6N,TxtFlange7N],
			[TxtFlange1C,TxtFlange2C,TxtFlange3C,TxtFlange4C,TxtFlange5C,TxtFlange6C,TxtFlange7C],
			[TxtTBack],[TxtTColor],[TxtSColor],[TxtSystem]]
	#Configures=
	modificar(srcS,2,conf[0][0].get())
	modificar(srcS,3,conf[0][1].get())
	modificar(srcS,4,conf[0][2].get())
	modificar(srcS,5,conf[0][3].get())
	modificar(srcS,6,conf[0][4].get())
	modificar(srcS,7,conf[0][5].get())
	modificar(srcS,8,conf[0][6].get())
	modificar(srcS,11,conf[1][0].get())
	modificar(srcS,12,conf[1][1].get())
	modificar(srcS,13,conf[1][2].get())
	modificar(srcS,14,conf[1][3].get())
	modificar(srcS,15,conf[1][4].get())
	modificar(srcS,16,conf[1][5].get())
	modificar(srcS,17,conf[1][6].get())
	modificar(srcS,20,conf[2][0].get())
	modificar(srcS,23,conf[3][0].get())
	modificar(srcS,26,conf[4][0].get())
	modificar(srcS,29,conf[5][0].get())
	Reload()
	WConfig.withdraw()
	Words.config(bg = FColor[int(Obtain(srcActuals,1))-1])
	Concepts1.config(bg = conf[1][0].get())
	Concepts2.config(bg = conf[1][1].get())
	Concepts3.config(bg = conf[1][2].get())
	Concepts4.config(bg = conf[1][3].get())
	Concepts5.config(bg = conf[1][4].get())
	Concepts6.config(bg = conf[1][5].get())
	Concepts7.config(bg = conf[1][6].get())
	#WConfig.destroy
	root.update()
	root.deiconify()
	pass
def Configure():
	root.withdraw()
	WConfig.deiconify()
	pass

#Start Frame 0
modificar(srcActuals,1,1)

#Frames
Words = Frame(root, bg=FColor[0], width=screen_width, height=screen_height-(screen_height*6/20))
Words.pack() #Start of the Principal Frame with the first Flange Color
Sentence = Frame(root, bg=SColor, width=screen_width, height=screen_height*6/20)
Sentence.pack()#Start the part of the sentences

#Flanges
Concepts1 = Button(Words, text = FName[0], image= ICon1, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[0], command=lambda:BChange(srcActuals,Obtain(srcConfig,11),0));Concepts1.place(x=0,y=0)
Concepts2 = Button(Words, text = FName[1], image= ICon2, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[1], command=lambda:BChange(srcActuals,FColor[1],1));Concepts2.place(x=screen_width/7,y=0)
Concepts3 = Button(Words, text = FName[2], image= ICon3, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[2], command=lambda:BChange(srcActuals,FColor[2],2));Concepts3.place(x=screen_width*2/7,y=0)
Concepts4 = Button(Words, text = FName[3], image= ICon4, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[3], command=lambda:BChange(srcActuals,FColor[3],3));Concepts4.place(x=screen_width*3/7,y=0)
Concepts5 = Button(Words, text = FName[4], image= ICon5, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[4], command=lambda:BChange(srcActuals,FColor[4],4));Concepts5.place(x=screen_width*4/7,y=0)
Concepts6 = Button(Words, text = FName[5], image= ICon6, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[5], command=lambda:BChange(srcActuals,FColor[5],5));Concepts6.place(x=screen_width*5/7,y=0)
Concepts7 = Button(Words, text = FName[6], image= ICon7, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[6], command=lambda:BChange(srcActuals,FColor[6],6));Concepts7.place(x=screen_width*6/7,y=0)

#ConceptImages
CImg1 = Button(Words, image= CBImg1_1, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),0,SelConcepts(srcActuals),Word));CImg1.place(x=screen_width/21,y=screen_height*2/20)
CImg2 = Button(Words, image= CBImg1_2, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),1,SelConcepts(srcActuals),Word));CImg2.place(x=screen_width*5/21,y=screen_height*2/20)
CImg3 = Button(Words, image= CBImg1_3, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),2,SelConcepts(srcActuals),Word));CImg3.place(x=screen_width*9/21,y=screen_height*2/20)
CImg4 = Button(Words, image= CBImg1_4, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),3,SelConcepts(srcActuals),Word));CImg4.place(x=screen_width*13/21,y=screen_height*2/20)
CImg5 = Button(Words, image= CBImg1_5, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),4,SelConcepts(srcActuals),Word));CImg5.place(x=screen_width*17/21,y=screen_height*2/20)
CImg6 = Button(Words, image= CBImg1_6, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),5,SelConcepts(srcActuals),Word));CImg6.place(x=screen_width/21,y=screen_height*6/20)
CImg7 = Button(Words, image= CBImg1_7, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),6,SelConcepts(srcActuals),Word));CImg7.place(x=screen_width*5/21,y=screen_height*6/20)
CImg8 = Button(Words, image= CBImg1_8, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),7,SelConcepts(srcActuals),Word));CImg8.place(x=screen_width*9/21,y=screen_height*6/20)
CImg9 = Button(Words, image= CBImg1_9, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),8,SelConcepts(srcActuals),Word));CImg9.place(x=screen_width*13/21,y=screen_height*6/20)
CImg10 = Button(Words, image= CBImg1_10, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),9,SelConcepts(srcActuals),Word));CImg10.place(x=screen_width*17/21,y=screen_height*6/20)
CImg11 = Button(Words, image= CBImg1_11, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),10,SelConcepts(srcActuals),Word));CImg11.place(x=screen_width/21,y=screen_height*10/20)
CImg12 = Button(Words, image= CBImg1_12, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),11,SelConcepts(srcActuals),Word));CImg12.place(x=screen_width*5/21,y=screen_height*10/20)
CImg13 = Button(Words, image= CBImg1_13, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),12,SelConcepts(srcActuals),Word));CImg13.place(x=screen_width*9/21,y=screen_height*10/20)
CImg14 = Button(Words, image= CBImg1_14, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),13,SelConcepts(srcActuals),Word));CImg14.place(x=screen_width*13/21,y=screen_height*10/20)
CImg15 = Button(Words, image= CBImg1_15, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:SendImage(srcActuals,UbFlange(srcActuals),14,SelConcepts(srcActuals),Word));CImg15.place(x=screen_width*17/21,y=screen_height*10/20)

#ConceptNames
LImg1 = Label(Words, text=Word[UbFlange(srcActuals)][0], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg1.place(x=screen_width/21,y=screen_height*9/40)
LImg2 = Label(Words, text=Word[UbFlange(srcActuals)][1], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg2.place(x=screen_width*5/21,y=screen_height*9/40)
LImg3 = Label(Words, text=Word[UbFlange(srcActuals)][2], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg3.place(x=screen_width*9/21,y=screen_height*9/40)
LImg4 = Label(Words, text=Word[UbFlange(srcActuals)][3], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg4.place(x=screen_width*13/21,y=screen_height*9/40)
LImg5 = Label(Words, text=Word[UbFlange(srcActuals)][4], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg5.place(x=screen_width*17/21,y=screen_height*9/40)
LImg6 = Label(Words, text=Word[UbFlange(srcActuals)][5], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg6.place(x=screen_width/21,y=screen_height*17/40)
LImg7 = Label(Words, text=Word[UbFlange(srcActuals)][6], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg7.place(x=screen_width*5/21,y=screen_height*17/40)
LImg8 = Label(Words, text=Word[UbFlange(srcActuals)][7], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg8.place(x=screen_width*9/21,y=screen_height*17/40)
LImg9 = Label(Words, text=Word[UbFlange(srcActuals)][8], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg9.place(x=screen_width*13/21,y=screen_height*17/40)
LImg10 = Label(Words, text=Word[UbFlange(srcActuals)][9], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg10.place(x=screen_width*17/21,y=screen_height*17/40)
LImg11 = Label(Words, text=Word[UbFlange(srcActuals)][10], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg11.place(x=screen_width/21,y=screen_height*25/40)
LImg12 = Label(Words, text=Word[UbFlange(srcActuals)][11], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg12.place(x=screen_width*5/21,y=screen_height*25/40)
LImg13 = Label(Words, text=Word[UbFlange(srcActuals)][12], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg13.place(x=screen_width*9/21,y=screen_height*25/40)
LImg14 = Label(Words, text=Word[UbFlange(srcActuals)][13], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg14.place(x=screen_width*13/21,y=screen_height*25/40)
LImg15 = Label(Words, text=Word[UbFlange(srcActuals)][14], width=int(((screen_width/7)-((screen_width/7)%7))/7), height=int(((screen_height/15)-((screen_height/15)%40))/40), bg=TxtBack, fg=TxtColor, bd= 3);LImg15.place(x=screen_width*17/21,y=screen_height*25/40)

#Sentences Parts
SConscept1 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:DownButton(srcActuals,SelConcepts(srcActuals)));SConscept1.place(x=screen_width/21,y=screen_height/20)
SConscept2 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:DownButton(srcActuals,SelConcepts(srcActuals)));SConscept2.place(x=screen_width*4/21,y=screen_height/20)
SConscept3 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:DownButton(srcActuals,SelConcepts(srcActuals)));SConscept3.place(x=screen_width*7/21,y=screen_height/20)
SConscept4 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:DownButton(srcActuals,SelConcepts(srcActuals)));SConscept4.place(x=screen_width*10/21,y=screen_height/20)
SConscept5 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:DownButton(srcActuals,SelConcepts(srcActuals)));SConscept5.place(x=screen_width*13/21,y=screen_height/20)
SConscept6 = Button(Sentence, image= Non, width=screen_width/7, height=screen_height*3/20, bd= -2, command= lambda:End(srcActuals));SConscept6.place(x=screen_width*16/21,y=screen_height/20)

#Globales
End(srcActuals)

#Play Selection
PlayButton = Button(Sentence, text=">>", width=int(screen_width/400), height=int(((screen_height/15)-((screen_height/15)%40))/40), bd= -2, command= lambda:Play(srcActuals,System), bg="white");PlayButton.place(x=screen_width*39/42,y=screen_height*9/80)

#Configuration Window
WConfig=Tk()
WConfig.title("Configuracion ICOS")
#WConfig.iconbitmap('Logo.ico')
#Labels Flanges
LFlanges=Label(WConfig, text="Pestañas").grid(column=0,row=0)
LFlange1=Label(WConfig, text="Pestaña 1").grid(column=1,row=1)
LFlange1N=Label(WConfig, text="Nombre").grid(column=1,row=2)
LFlange1C=Label(WConfig, text="Color").grid(column=1,row=3)
LFlange2=Label(WConfig, text="Pestaña 2").grid(column=1,row=4)
LFlange2N=Label(WConfig, text="Nombre").grid(column=1,row=5)
LFlange2C=Label(WConfig, text="Color").grid(column=1,row=6)
LFlange3=Label(WConfig, text="Pestaña 3").grid(column=1,row=7)
LFlange3N=Label(WConfig, text="Nombre").grid(column=1,row=8)
LFlange3C=Label(WConfig, text="Color").grid(column=1,row=9)
LFlange4=Label(WConfig, text="Pestaña 4").grid(column=1,row=10)
LFlange4N=Label(WConfig, text="Nombre").grid(column=1,row=11)
LFlange4C=Label(WConfig, text="Color").grid(column=1,row=12)
LFlange5=Label(WConfig, text="Pestaña 5").grid(column=1,row=13)
LFlange5N=Label(WConfig, text="Nombre").grid(column=1,row=14)
LFlange5C=Label(WConfig, text="Color").grid(column=1,row=15)
LFlange6=Label(WConfig, text="Pestaña 6").grid(column=1,row=16)
LFlange6N=Label(WConfig, text="Nombre").grid(column=1,row=17)
LFlange6C=Label(WConfig, text="Color").grid(column=1,row=18)
LFlange7=Label(WConfig, text="Pestaña 7").grid(column=1,row=19)
LFlange7N=Label(WConfig, text="Nombre").grid(column=1,row=20)
LFlange7C=Label(WConfig, text="Color").grid(column=1,row=21)
#TextBoxes Flanges
TxtFlange1N=Entry(WConfig);TxtFlange1N.grid(column=2,row=2);TxtFlange1N.insert(0,Obtain(srcConfig,2))
TxtFlange2N=Entry(WConfig);TxtFlange2N.grid(column=2,row=5);TxtFlange2N.insert(0,Obtain(srcConfig,3))
TxtFlange3N=Entry(WConfig);TxtFlange3N.grid(column=2,row=8);TxtFlange3N.insert(0,Obtain(srcConfig,4))
TxtFlange4N=Entry(WConfig);TxtFlange4N.grid(column=2,row=11);TxtFlange4N.insert(0,Obtain(srcConfig,5))
TxtFlange5N=Entry(WConfig);TxtFlange5N.grid(column=2,row=14);TxtFlange5N.insert(0,Obtain(srcConfig,6))
TxtFlange6N=Entry(WConfig);TxtFlange6N.grid(column=2,row=17);TxtFlange6N.insert(0,Obtain(srcConfig,7))
TxtFlange7N=Entry(WConfig);TxtFlange7N.grid(column=2,row=20);TxtFlange7N.insert(0,Obtain(srcConfig,8))
TxtFlange1C=Entry(WConfig);TxtFlange1C.grid(column=2,row=3);TxtFlange1C.insert(0,Obtain(srcConfig,11))
TxtFlange2C=Entry(WConfig);TxtFlange2C.grid(column=2,row=6);TxtFlange2C.insert(0,Obtain(srcConfig,12))
TxtFlange3C=Entry(WConfig);TxtFlange3C.grid(column=2,row=9);TxtFlange3C.insert(0,Obtain(srcConfig,13))
TxtFlange4C=Entry(WConfig);TxtFlange4C.grid(column=2,row=12);TxtFlange4C.insert(0,Obtain(srcConfig,14))
TxtFlange5C=Entry(WConfig);TxtFlange5C.grid(column=2,row=15);TxtFlange5C.insert(0,Obtain(srcConfig,15))
TxtFlange6C=Entry(WConfig);TxtFlange6C.grid(column=2,row=18);TxtFlange6C.insert(0,Obtain(srcConfig,16))
TxtFlange7C=Entry(WConfig);TxtFlange7C.grid(column=2,row=21);TxtFlange7C.insert(0,Obtain(srcConfig,17))
#Blanco
Space1=Label(WConfig, text=" ").grid(column=0,row=22)
#Text Back
LTBack=Label(WConfig, text="Fondo del Texto Palabras").grid(column=0,row=23)
TxtTBack=Entry(WConfig);TxtTBack.grid(column=1,row=24);TxtTBack.insert(0,Obtain(srcConfig,20))
#Blanco
SpaceE=Label(WConfig, text=" ").grid(column=0,row=25)
#Font Text
LTColor=Label(WConfig, text="Color Texto Palabras").grid(column=0,row=26)
TxtTColor=Entry(WConfig);TxtTColor.grid(column=1,row=27);TxtTColor.insert(0,Obtain(srcConfig,23))
#Blanco
Space2=Label(WConfig, text=" ").grid(column=0,row=28)
#Source Color
LSColor=Label(WConfig, text="Color Parte Oracion").grid(column=0,row=29)
TxtSColor=Entry(WConfig);TxtSColor.grid(column=1,row=30);TxtSColor.insert(0,Obtain(srcConfig,26))
#Blanco
Space3=Label(WConfig, text=" ").grid(column=0,row=31)
#System
LSystem=Label(WConfig, text="Sistema Usado").grid(column=0,row=32)
TxtSystem=Entry(WConfig);TxtSystem.grid(column=1,row=33);TxtSystem.insert(0,Obtain(srcConfig,29))
#Blanco
Space4=Label(WConfig, text=" ").grid(column=0,row=34)
#Boton Final
EndConfiguration=Button(WConfig,text="Terminar",command=lambda:EndConfigure(srcConfig)).grid(column=3,row=35)
WConfig.withdraw()

#Configuration
#ConfigButton = Button(Words, text="o", width=int(screen_width/400), height=int(((screen_height/15)-((screen_height/15)%40))/40), bd= -2, command= lambda:Configure(), bg="white");ConfigButton.place(x=screen_width*41/42,y=screen_height*5/80) #x=screen_width*40/42,y=screen_height*10/80

root.mainloop();