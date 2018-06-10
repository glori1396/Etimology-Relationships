from tec.ic.ia.p2.g07.Relation import Relation
from pyDatalog import pyDatalog
import csv
from tkinter import messagebox, Tk, Label, Entry, Button, StringVar

pyDatalog.create_terms('X')

def busy(window):
    window.config(cursor="wait")

def notbusy(window):
    window.config(cursor="")

def db_input(input, window, Relations):
    busy(window)
    with open(input.get(), 'r', encoding="utf8") as csvfile:
        spamreader = csv.reader(csvfile, delimiter='\t', lineterminator='\n')
        for row in spamreader:
            first_index = row[0].index(":")
            second_index = row[2].index(":")
            Relations.append(Relation(row[0][0:first_index], row[0][first_index+2:],
                                      row[1][4:], row[2][0:second_index], row[2][second_index+2:]))
    messagebox.showinfo("Let's Continue!", "The upload is done!")
    #     print("Done!")
    # print(Relation.first_lang[X]=='ang')
    notbusy(window)
    print(len(Relations))

#Graphic User Interface
def ui():
    Relations = []

    #Window Properties
    window = Tk()
    window.title("Project 2 - Ethimological Relationships")
    window.geometry("960x600+200+100")

    #Title
    Label(window, text="Ethimological Relationships",font="Helvetica 18 bold").place(x=337,y=50)

    #Entry
    Label(window, text="Database File:" ,font="Helvetica 14").place(x=300,y=130)

    input = StringVar()
    Entry(window, font = "Helvetica 12",textvariable=input).place(x=435,y=132)

    #Button input database
    enter_db = Button(window, font = "Helvetica 12", text="Enter",command=lambda: db_input(input, window, Relations)).place(x=630,y=125)

    #Ejecuta la ventana
    window.mainloop()

ui()
