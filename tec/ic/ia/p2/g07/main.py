from tec.ic.ia.p2.g07.Relation import Relation
from pyDatalog import pyDatalog
import csv
from tkinter import messagebox, Tk, Label, Entry, Button, StringVar,\
                    Listbox, END, EXTENDED, Scrollbar, Text

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
                                      row[1], row[2][0:second_index], row[2][second_index+2:]))
    messagebox.showinfo("Let's Continue!", "The upload is done!")
    #     print("Done!")
    # print(Relation.first_lang[X]=='ang')
    # {'rel:is_derived_from', 'rel:etymologically', 'rel:etymological_origin_of', 'rel:etymology', 'rel:variant:orthography', 'rel:etymologically_related', 'rel:has_derived_form', 'rel:derived'}
    notbusy(window)

#Graphic User Interface
def ui():
    Relations = []

    #Window Properties
    window = Tk()
    window.title("Project 2 - Ethymological Relationships")
    window.geometry("960x600+200+100")

    #Title
    Label(window, text="Ethymological Relationships",font="Helvetica 18 bold").place(x=337,y=50)

    #Entry DB
    Label(window, text="Database File:" ,font="Helvetica 14").place(x=300,y=130)

    input = StringVar()
    Entry(window, font = "Helvetica 12",textvariable=input).place(x=435,y=132)

    #Button input database
    enter_db = Button(window, font = "Helvetica 12", text="Enter",command=lambda: db_input(input, window, Relations)).place(x=630,y=125)

    #Relations
    Label(window, text="Relations:" ,font="Helvetica 12").place(x=10,y=200)
    relations = Listbox(window,height=8, font="Helvetica 12", selectmode=EXTENDED)
    relations.place(x=10,y=220)

    for item in ['rel:is_derived_from', 'rel:etymologically', 'rel:etymological_origin_of', 'rel:etymology',
                 'rel:variant:orthography', 'rel:etymologically_related', 'rel:has_derived_form', 'rel:derived']:
        relations.insert(END, item)

    #Querys
    Label(window, text="Querys:" ,font="Helvetica 12").place(x=200,y=200)
    querys = Listbox(window,height=7, width=30, font="Helvetica 12")
    querys.place(x=200,y=220)
    scrollbar = Scrollbar(window, orient="horizontal")
    scrollbar.place(x=200,y=360, width=270)
    scrollbar.config(command=querys.xview)

    for item in ['Si dos palabras son heman@s', 'Si dos palabras son prim@s', 'Si una palabra es hij@ de otra',
                'Si una palabra es ti@', 'Si son prim@s y en qué grado', 'Si una palabra está relacionada con un idioma',
                'Palabras en un idioma originadas por una palabra específica', 'Listar los idiomas relacionados con una palabra',
                'Contar todas las palabras comunes entre dos idiomas', 'Listar todas las palabras comunes entre dos idiomas',
                'Idioma que más aportó a otro', 'Listar todos los idiomas que aportaron a otro']:
        querys.insert(END, item)

    #Results
    Label(window, text="Results:" ,font="Helvetica 12").place(x=100,y=380)
    results = Text(window, font = "Helvetica 12", height=10, state='disabled')
    results.place(x=100,y=400)
    # results.config(state='normal')
    # results.insert(END,"sada\nsada\nsada\nsada\nsada\nsada\nsada\nsada\nsada\nsada\nsada\n")
    # results.config(state='disabled')

    #Entry
    first_entry = Label(window, text="First word:" ,font="Helvetica 14").place(x=500,y=240)
    input_first_entry = StringVar()
    Entry(window, font = "Helvetica 12",textvariable=input_first_entry).place(x=625,y=242)

    #Entry
    second_entry = Label(window, text="Second word:" ,font="Helvetica 14").place(x=500,y=300)
    input_second_entry = StringVar()
    Entry(window, font = "Helvetica 12",textvariable=input_second_entry).place(x=625,y=302)

    #Button search
    Button(window, font = "Helvetica 12", text="Search",command=lambda: db_input(input, window, Relations)).place(x=850,y=270)

    #Ejecuta la ventana
    window.mainloop()

ui()
