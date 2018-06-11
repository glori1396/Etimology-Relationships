from tec.ic.ia.p2.g07.Relation import Relation
from pyDatalog import pyDatalog
from tkinter import END

pyDatalog.create_terms('Siblings, X, Y, PX, PY, Cousins, X1, Y1')

def siblings_query(first, second):
    Siblings(X, Y, PX, PY) <= (Relation.parent[X] == Relation.parent[Y]) & (Relation.child[X]==PX) & (Relation.child[Y]==PY)
    return Siblings(X, Y, first, second)

def cousins_query(first, second):
    Siblings(X, Y, PX, PY) <= (Relation.parent[X] == Relation.parent[Y]) & (Relation.child[X]==PX) & (Relation.child[Y]==PY)
    Cousins(X, Y, PX, PY) <= Siblings(X1,Y1,Relation.parent[X],Relation.parent[Y]) #& (Relation.child[X]==PX) & (Relation.child[Y]==PY)
    return Cousins(X, Y, first, second)

def clean_msg(results):
    results.config(state='normal')
    results.delete(1.0,END)
    results.config(state='disabled')

def searching_msg(results):
    results.config(state='normal')
    results.insert(END,"Buscando...\n")
    results.config(state='disabled')

def response_msg(results, query, result, status):
    results.config(state='normal')
    if query == 0:
        if status == 'good':
            results.insert(END,"\nRespuesta: Si \n"+str(result)+"\n")
        elif status == 'bad':
            results.insert(END,"\nRespuesta: No \n")
    results.config(state='disabled')

def search(input_first_entry, input_second_entry, p_relations, p_query, results, window, possible_querys, possible_relations, Relations):
    first = input_first_entry.get()
    second = input_second_entry.get()
    relations_selected = p_relations.curselection()
    query = p_query.curselection()
    if first == "" or second == "" or relations_selected == [] or query == ():
        messagebox.showwarning("Error!", "You have to select at least one relation, one query and fill the textboxes.")
    else:
        clean_msg(results)
        query = query[0]
        start = 0
        end = 1000
        printed = False
        for r in relations_selected:
            encontro = False
            while end <= len(Relations[r]):
                searching_msg(results)
                print('Buscando...')

                knowledge = []
                pyDatalog.clear()
                if end>len(Relations[r]):
                    end = len(Relations[r])

                for rel in Relations[r][start:end]:
                    #Carga de datos
                    child_lang, child, relation, parent_lang, parent = rel
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))
                    knowledge.append(Relation(child_lang, child, relation, parent_lang, parent))

                #Queries
                if query == 0: # 'Si dos palabras son heman@s'
                    result = siblings_query(first, second)
                elif query == 1: # 'Si dos palabras son heman@s'
                    result = cousins_query(first, second)

                start+=end
                end+=end
                if end>len(Relations[r]):
                    end = len(Relations[r])

                if result != []:
                    response_msg(results, query, result, 'good')
                    printed = True
                    encontro = True
                    break
            if encontro:
                break
        if not printed:
            response_msg(results, query, result, 'bad')
