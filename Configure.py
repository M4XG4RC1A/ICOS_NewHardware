from tkinter import *
import platform
from tkinter import ttk
import tkinter
from tkinter.filedialog import askopenfilename
import os
import shutil
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
from tkinter import colorchooser
from typing import DefaultDict
from PIL import Image
import os
import PIL
import glob

root=Tk()
root.title("ICOS (Interactive COncept Simplifier)")
if platform.system() == "Windows":
    root.iconbitmap("Logo.ico")

#Funcion para obtener
def Obtain(srcS,index):
	File=open(srcS,"r")
	Lines=File.readlines()
	File.close()
	Result=Lines[index].rstrip("\n")
	Result.strip()
	return Result
	pass

srcActuals="ActualStates.txt"
srcConfig="Configuration.txt"
srcInter="Interaction.txt"
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

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
def changeImg(Flange,Id):
    fileName = askopenfilename(filetypes = [("Images", "*.jpg *.jpeg *.png")])
    if fileName != None and str(fileName) != "" and str(fileName)!="()":
        name = ""
        name = askstring('Concepto Nuevo', 'Inserte Nombre del Concepto')
        while name == "" or name == None:
            name = askstring('Concepto Nuevo', 'Inserte Nombre del Concepto')
        showinfo('Procesando...', 'Insertando Concepto: {}'.format(name))
        if srcCon[Flange][Id-1] != fileName:
            shutil.copyfile(fileName, srcCon[Flange][Id-1])

            #Resize Image
            image = Image.open(srcCon[Flange][Id-1])
            width, height = image.size
            res = True
            widthR=screen_width/7
            propW = widthR/width
            heightR=screen_height*5/40
            propH = heightR/height
            if propW>propH:
                prop = propH
            else:
                prop = propW
            width2 = int(width*prop)
            height2 =int(height*prop)
            if width2 != width or height2 != height:
                image = image.resize((width2,height2), Image.NEAREST)
                os.remove(srcCon[Flange][Id-1])
                image.save(srcCon[Flange][Id-1])
            
            newImg = PhotoImage(file=srcCon[Flange][Id-1])
            CBImg[Flange-1][Id-1] = newImg
            Word[Flange][Id-1] = name
            modificar(srcConfig,32+Flange,'["'+'","'.join(Word[Flange])+'"]')
            showinfo('Terminado', 'Concepto Agregado')
            BChange(srcActuals,FColor[Flange-1],Flange-1)
            actList()
def changeClr(btn):
    color_codeCode = colorchooser.askcolor(title ="Choose color")
    Flange = UbFlange(srcActuals)
    color_code = color_codeCode[1]
    #Words.config(bg = eval(color_code))
    if color_code != None:
        FColor[Flange-1] = color_code
        modificar(srcConfig,10+Flange,color_code)
        BChange(srcActuals,FColor[Flange-1],Flange-1)
        Concepts1.config(bg=FColor[0])
        Concepts2.config(bg=FColor[1])
        Concepts3.config(bg=FColor[2])
        Concepts4.config(bg=FColor[3])
        Concepts5.config(bg=FColor[4])
        Concepts6.config(bg=FColor[5])
        Concepts7.config(bg=FColor[6])
def changeClrSent(btn):
    color_codeCode = colorchooser.askcolor(title ="Choose color")
    color_code = color_codeCode[1]
    if color_code != None:
        Sentence.config(bg=color_code)
        modificar(srcConfig,26,color_code)
def actList():
    Concepts = []
    for f in Word:
        for o in f:
            if not(o in Concepts):
                Concepts.append(o)
    inter1.config(values=Concepts)
    inter2.config(values=Concepts)
    inter3.config(values=Concepts)
    inter4.config(values=Concepts)
    inter5.config(values=Concepts)
    inter6.config(values=Concepts)
    c1Inter.set('')
    c2Inter.set('')
    c3Inter.set('')
    c4Inter.set('')
    c5Inter.set('')
    c6Inter.set('')
def ResetCode():
    Code.delete('1.0', END)
def loadAction(arch):
    File=open(arch, "a")
    Conc = [c1Inter.get(),c2Inter.get(),c3Inter.get(),c4Inter.get(),c5Inter.get(),c6Inter.get()]
    File.write('["'+'","'.join(Conc)+'"]')
    File.write("\nStart\n")
    File.write(Code.get("1.0","end-1c"))
    File.write("\nEnd\n")
    File.close()
    ResetCode()
    actList()
#Frames
Words = Frame(root, bg=FColor[0], width=screen_width, height=screen_height-(screen_height*6/20))
Words.pack() #Start of the Principal Frame with the first Flange Color
Sentence = Frame(root, bg=SColor, width=screen_width, height=screen_height*6/20)
Sentence.pack()#Start the part of the sentences
Words.bind("<Button-1>",changeClr)
Sentence.bind("<Button-1>",changeClrSent)

#Flanges
Concepts1 = Button(Words, text = FName[0], image= ICon1, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[0], command=lambda:BChange(srcActuals,Obtain(srcConfig,11),0));Concepts1.place(x=0,y=0)
Concepts2 = Button(Words, text = FName[1], image= ICon2, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[1], command=lambda:BChange(srcActuals,FColor[1],1));Concepts2.place(x=screen_width/7,y=0)
Concepts3 = Button(Words, text = FName[2], image= ICon3, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[2], command=lambda:BChange(srcActuals,FColor[2],2));Concepts3.place(x=screen_width*2/7,y=0)
Concepts4 = Button(Words, text = FName[3], image= ICon4, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[3], command=lambda:BChange(srcActuals,FColor[3],3));Concepts4.place(x=screen_width*3/7,y=0)
Concepts5 = Button(Words, text = FName[4], image= ICon5, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[4], command=lambda:BChange(srcActuals,FColor[4],4));Concepts5.place(x=screen_width*4/7,y=0)
Concepts6 = Button(Words, text = FName[5], image= ICon6, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[5], command=lambda:BChange(srcActuals,FColor[5],5));Concepts6.place(x=screen_width*5/7,y=0)
Concepts7 = Button(Words, text = FName[6], image= ICon7, width=screen_width/7, height=screen_height/20, bd= -2, bg= FColor[6], command=lambda:BChange(srcActuals,FColor[6],6));Concepts7.place(x=screen_width*6/7,y=0)

#ConceptImages
CImg1 = Button(Words, image= CBImg1_1, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),1));CImg1.place(x=screen_width/21,y=screen_height*2/20)
CImg2 = Button(Words, image= CBImg1_2, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),2));CImg2.place(x=screen_width*5/21,y=screen_height*2/20)
CImg3 = Button(Words, image= CBImg1_3, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),3));CImg3.place(x=screen_width*9/21,y=screen_height*2/20)
CImg4 = Button(Words, image= CBImg1_4, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),4));CImg4.place(x=screen_width*13/21,y=screen_height*2/20)
CImg5 = Button(Words, image= CBImg1_5, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),5));CImg5.place(x=screen_width*17/21,y=screen_height*2/20)
CImg6 = Button(Words, image= CBImg1_6, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),6));CImg6.place(x=screen_width/21,y=screen_height*6/20)
CImg7 = Button(Words, image= CBImg1_7, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),7));CImg7.place(x=screen_width*5/21,y=screen_height*6/20)
CImg8 = Button(Words, image= CBImg1_8, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),8));CImg8.place(x=screen_width*9/21,y=screen_height*6/20)
CImg9 = Button(Words, image= CBImg1_9, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),9));CImg9.place(x=screen_width*13/21,y=screen_height*6/20)
CImg10 = Button(Words, image= CBImg1_10, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),10));CImg10.place(x=screen_width*17/21,y=screen_height*6/20)
CImg11 = Button(Words, image= CBImg1_11, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),11));CImg11.place(x=screen_width/21,y=screen_height*10/20)
CImg12 = Button(Words, image= CBImg1_12, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),12));CImg12.place(x=screen_width*5/21,y=screen_height*10/20)
CImg13 = Button(Words, image= CBImg1_13, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),13));CImg13.place(x=screen_width*9/21,y=screen_height*10/20)
CImg14 = Button(Words, image= CBImg1_14, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),14));CImg14.place(x=screen_width*13/21,y=screen_height*10/20)
CImg15 = Button(Words, image= CBImg1_15, width=screen_width/7, height=screen_height*5/40, bd= -2, command=lambda:changeImg(UbFlange(srcActuals),15));CImg15.place(x=screen_width*17/21,y=screen_height*10/20)

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

# Set Flange
BChange(srcActuals,FColor[UbFlange(srcActuals)-1],UbFlange(srcActuals)-1)

#Actions
c1Inter = StringVar()
c2Inter = StringVar()
c3Inter = StringVar()
c4Inter = StringVar()
c5Inter = StringVar()
c6Inter = StringVar()

Concepts = []
for f in Word:
    for o in f:
        if not(o in Concepts):
            Concepts.append(o)
Label(Sentence, text="Concepts", font=('Arial',int(screen_height*3/260))).place(x=screen_width*2/60,y=int(screen_height*3*4/260))
inter1 = ttk.Combobox(Sentence, textvariable=c1Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter2 = ttk.Combobox(Sentence, textvariable=c2Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter3 = ttk.Combobox(Sentence, textvariable=c3Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter4 = ttk.Combobox(Sentence, textvariable=c4Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter5 = ttk.Combobox(Sentence, textvariable=c5Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter6 = ttk.Combobox(Sentence, textvariable=c6Inter, values=Concepts, state='readonly', font=('Arial',int(screen_height*3/260)))
inter1.place(x=screen_width/60,y=int(screen_height*3*6/260))
inter2.place(x=screen_width/60,y=int(screen_height*3*8/260))
inter3.place(x=screen_width/60,y=int(screen_height*3*10/260))
inter4.place(x=screen_width/60,y=int(screen_height*3*12/260))
inter5.place(x=screen_width/60,y=int(screen_height*3*14/260))
inter6.place(x=screen_width/60,y=int(screen_height*3*16/260))

Code = Text(Sentence,font=('Arial',int(screen_height*3/260)),height=12,width=int(screen_width/10)+2)
Code.place(x=screen_width*8/60,y=int(screen_height*3*2/260))
Save = Button(Sentence,text="Save Interaction",font=('Arial',int(screen_height*3/260)),height=1,width=int(screen_width/10),command=lambda:loadAction(srcInter))
Save.place(x=screen_width*8/60,y=int(screen_height*3*18/260))
root.mainloop();