from tec.ic.ia.p2.g07.Relation import Relation
from tec.ic.ia.p2.g07.Queries import search
#from pyDatalog import pyDatalog
import csv
from tkinter import messagebox, Tk, Label, Entry, Button, StringVar,\
                    Listbox, END, EXTENDED, Scrollbar, Text

#pyDatalog.create_terms('X, Y, PX, PY')

######################################## Relación de parentesco.

 #& (Relation.child[X]==PX) & (Relation.child[Y]==PY)

def busy(window):
    window.config(cursor="wait")

def notbusy(window):
    window.config(cursor="")

def db_input(input, window, Relations, possible_relations):
    busy(window)
    inverted = [0,1,2,5]
    try:
        with open(input.get(), 'r', encoding="utf8") as csvfile:
            spamreader = csv.reader(csvfile, delimiter='\t', lineterminator='\n')
            c = 0
            for row in spamreader:
                first_index = row[0].index(":")
                second_index = row[2].index(":")
                relation = row[1]
                if possible_relations.index(relation) in inverted:
                    child_lang = row[2][0:second_index]
                    child = row[2][second_index+2:]
                    parent_lang = row[0][0:first_index]
                    parent = row[0][first_index+2:]
                else:
                    child_lang = row[0][0:first_index]
                    child = row[0][first_index+2:]
                    parent_lang = row[2][0:second_index]
                    parent = row[2][second_index+2:]
                Relations[possible_relations.index(relation)].append([child_lang, child, relation, parent_lang, parent])
                #Relations.append(Relation(child_lang, child, relation, parent_lang, parent))
                # if c==100:
                #     break
                # c+=1
            #pyDatalog.clear()

        messagebox.showinfo("Let's Continue!", "The upload is done!")
    except:
        messagebox.showwarning("Error!", "The file can't be upload.")
    #     print("Done!")
    #print(Relation.child_lang[X]=='ang')

    #print(len(Relations))
    notbusy(window)

        #print(o_query)

#Graphic User Interface
def ui():
    Relations = [[],[],[],[],[],[],[],[]]
    possible_querys = ['Si dos palabras son heman@s', 'Si dos palabras son prim@s', 'Si una palabra es hij@ de otra',
                'Si una palabra es ti@', 'Si son prim@s y en qué grado', 'Si una palabra está relacionada con un idioma',
                'Palabras en un idioma originadas por una palabra específica', 'Listar los idiomas relacionados con una palabra',
                'Contar todas las palabras comunes entre dos idiomas', 'Listar todas las palabras comunes entre dos idiomas',
                'Idioma que más aportó a otro', 'Listar todos los idiomas que aportaron a otro']
    possible_relations = ['rel:derived','rel:etymological_origin_of','rel:etymologically', 'rel:etymologically_related','rel:etymology',
                          'rel:has_derived_form','rel:is_derived_from','rel:variant:orthography']

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
    enter_db = Button(window, font = "Helvetica 12", text="Enter",command=lambda: db_input(input, window, Relations, possible_relations)).place(x=630,y=125)

    #Relations
    Label(window, text="Relations:" ,font="Helvetica 12").place(x=10,y=200)
    relations = Listbox(window,height=8, font="Helvetica 12", selectmode=EXTENDED, exportselection=0)
    relations.place(x=10,y=220)

    for item in possible_relations:
        relations.insert(END, item)

    #Querys
    Label(window, text="Querys:" ,font="Helvetica 12").place(x=200,y=200)
    querys = Listbox(window,height=7, width=30, font="Helvetica 12", exportselection=0)
    querys.place(x=200,y=220)
    scrollbar = Scrollbar(window, orient="horizontal")
    scrollbar.place(x=200,y=360, width=270)
    scrollbar.config(command=querys.xview)

    for item in possible_querys:
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
    Button(window, font = "Helvetica 12", text="Search",command=lambda: search(input_first_entry, \
            input_second_entry, relations, querys, results, window, possible_querys, possible_relations, Relations)).place(x=850,y=270)

    #Ejecuta la ventana
    window.mainloop()

ui()
