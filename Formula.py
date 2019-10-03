# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 12:15:22 2018

@author: Tommy Yong
"""

from tkinter import *
import tkinter
window = Tk()
window.geometry("800x375")
window.title("Formula")

# List of oxides molecular weight with number of anions and anion/cation ratio
Database = {'SiO2':[60.08,2,2],'SnO2':[150.69,2,2],'TiO2':[79.90,2,2],'ZrO2':[123.22,2,2],'ThO2':[264.04,2,2],'UO2':[270.03,2,2],
'UO3':[286.03,3,3],'Al2O3':[101.94,3,3/2],'Bi2O3':[465.96,3,3/2],'Fe2O3':[159.69,3,3/2],'Cr2O3':[151.99,3,3/2],'Mn2O3':[157.87,3,3/2],
'Ce2O3':[188.12,3,3/2],'V2O3':[149.88,3,3/2],'Y2O3':[227.81,3,3/2],'La2O3':[325.82,3,3/2],'Ce2O3':[328.24,3,3/2],'Pr2O3':[329.81,3,3/2],
'Nd2O3':[336.48,3,3/2],'Sm2O3':[348.70,3,3/2],'Gd2O3':[362.50,3,3/2],'FeO':[71.85,1,1],'SnO':[134.69,1,1],'MnO':[70.94,1,1],'ZnO':[81.38,1,1],
'CdO':[128.40,1,1],'CuO':[79.54,1,1],'PbO':[223.19,1,1],'MgO':[40.31,1,1],'CaO':[56.08,1,1],'BaO':[153.33,1,1],'SrO':[103.62,1,1],'Li2O':[29.88,1,1/2],
'Na2O':[61.98,1,1/2],'K2O':[84.20,1,1/2],'Cs2O':[281.81,1,1/2],'Rb2O':[186.94,1,1/2],'Nb2O5':[265.78,5,5/2],'P2O5':[141.94,5,5/2],'Ta2O5':[441.89,5,5/2],
'As2O5':[229.84,5,5/2],'MoO3':[143.94,3,3]}

def insertwtpercent():
    list1.insert(END,(oxide.get(),wtpercent.get()))
    wtpercenttotal.set(float(wtpercent.get())+float(wtpercenttotal.get()))

def calculate():
    oxygens = number_of_oxygens.get()
    oxidelist = []
    wt = []
    mw = []
    noanions = []
    acratio = []
    molenumber = []
    atomprop = []
    anionprop = []
    ionsperformula = []
    for row in list1.get(1,END):
        oxidelist.append(row[0])
        wt.append((row[1]))
    for oxide in oxidelist:
        if oxide in Database:
            mw.append(Database[oxide][0])
            noanions.append(Database[oxide][1])
            acratio.append(Database[oxide][2])
    for i in range(len(oxidelist)):
        molenumber.append(float(wt[i])/mw[i])
        atomprop.append(molenumber[i]*noanions[i])
    oxygenfactor = oxygens/sum(atomprop)
    for i in range(len(oxidelist)):
        anionprop.append(atomprop[i]*oxygenfactor)
        ionsperformula.append(anionprop[i]/acratio[i])
    for i in range(len(oxidelist)):
        molenumber[i] = str(round(molenumber[i],4))
        atomprop[i] = str(round(atomprop[i],4))
        anionprop[i] = str(round(anionprop[i],4))
        ionsperformula[i] = str(round(ionsperformula[i],4))
        list2.insert(END,(oxidelist[i]+'|'+molenumber[i]+'|'+atomprop[i]+'|'+anionprop[i]+'|'+ionsperformula[i]))

def delete():
    list1.delete(list1.curselection())

def delete2():
    list2.delete(list2.curselection())

# Add a grid
mainframe = Frame(window)
mainframe.grid(column=0,row=2)
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)

# Create a Tkinter variablep
oxide = StringVar(window)

# List with options
choices = ['SiO2','SnO2','TiO2','ZrO2','ThO2','UO2','UO3','Al2O3','Bi2O3','Fe2O3',
'Cr2O3','Mn2O3','Ce2O3','V2O3','Y2O3','La2O3','Ce2O3','Pr2O3','Nd2O3','Sm2O3','Gd2O3','FeO','SnO','MnO','ZnO',
'CdO','CuO','PbO','MgO','CaO','BaO','SrO','Li2O','Na2O','K2O','Cs2O','Rb2O','Nb2O5','P2O5','Ta2O5','As2O5','MoO3']
oxide.set('SiO2') # set the default option

popupMenu = OptionMenu(mainframe, oxide, *choices)
Label(mainframe, text="Select Oxide").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

b1 = Button(window,text='Enter',width = 12, command = insertwtpercent)
b1.grid(row=2,column=5)
b3 = Button(window,text='Calculate Ions per Formula Unit',width = 25, command = calculate)
b3.grid(row=14,column=2)
b4 = Button(window,text = 'Delete',width = 12,command= delete)
b4.grid(row=3,column=5)
b5 = Button(window,text = 'Delete',width = 12,command= delete2)
b5.grid(row=15,column=5)

# add labels
l0 = Label(window, text= "Enter number of oxygens in formula")
l0.grid(row=0,column=0)
l2 = Label(window, text= "Wt% Oxide")
l2.grid(row=2,column=2)
l3 = Label(window, text= 'Total Wt%')
l3.grid(row=14,column=0)

wtpercenttotal = DoubleVar(window)
l4 = Label(window, textvariable = wtpercenttotal)
l4.grid(row=14,column=1)



number_of_oxygens = DoubleVar()
e1 = Entry(window,textvariable = number_of_oxygens)
e1.grid(row=0,column=1)

wtpercent = StringVar()
e3 = Entry(window, textvariable = wtpercent)
e3.grid(row=2,column=4)

list1 = Listbox(window,height=6,width =80)
list1.grid(row=3,column=0,rowspan = 10, columnspan= 8)
list1.insert(0,('Oxide | Weight Percent'))
sb1 = Scrollbar(window)
sb1.grid(row = 4,column = 10)
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list2 = Listbox(window,height=6,width =80)
list2.grid(row=15,column=0,rowspan = 10, columnspan= 8)
list2.insert(0,('Oxide | Mols | Atom Proportion | Anion Proporation | Ions per Formula Unit'))
sb2 = Scrollbar(window)
sb2.grid(row = 15,column = 10,sticky = N + S)
list2.configure(yscrollcommand=sb2.set)
sb2.configure(command=list1.yview)

window.mainloop()
