from tec.ic.ia.p2.g07.Relation import Relation
from tec.ic.ia.p2.g07.Queries import *

knowledge = []
tree = [['Ana', 'Rodrigo'], ['Juan', 'Rodrigo'], ['Rodrigo', 'Melissa'], ['Manuel', 'Roberto'], \
        ['Roberto', 'Julio'], ['Chris', 'Julio'], ['Julio', 'Melissa'], ['Melissa', 'Armando'], \
        ['Erick', 'Tatiana'], ['Tatiana', 'Armando']]

def create_tree(knowledge):
    for rel in tree:
        knowledge.append(Relation('lang_example_1', rel[0], 'relation', \
                                  'lang_example_2', rel[1]))


def test_siblings_relation():
    knowledge = []
    create_tree(knowledge)
    results = siblings_query('Ana', 'Juan')
    assert results != []

def test_cousins_relation():
    knowledge = []
    create_tree(knowledge)
    results = cousins_query('Erick', 'Julio')
    assert results != []

def test_cousins_2_level_relation():
    knowledge = []
    create_tree(knowledge)
    results = cousins_query('Erick', 'Roberto')
    assert results != []

def test_son_relation():
    knowledge = []
    create_tree(knowledge)
    results = son_query('Melissa', 'Armando')
    assert results != []

def test_uncle_relation():
    knowledge = []
    create_tree(knowledge)
    results = uncle_query('Julio', 'Juan')
    assert results != []

def test_language_relation():
    knowledge = []
    create_tree(knowledge)
    results = language_related_query('lang_example_2', 'Rodrigo')
    assert results != []

def test_language_origin_relation():
    knowledge = []
    create_tree(knowledge)
    results = language_and_origin_query('lang_example_1', 'Rodrigo')
    assert results != []

def test_list_languages_relation():
    knowledge = []
    create_tree(knowledge)
    _,results = list_languages_related_query('Rodrigo')
    assert results != []

def test_cont_common_words_relation():
    knowledge = []
    #create_tree(knowledge)
    knowledge.append(Relation('afr','hola', 'relation','esp', 'di'))
    knowledge.append(Relation('afl','hola', 'relation','esp2', 'di2'))
    knowledge.append(Relation('afr','hola2', 'relation','esp', 'di'))
    knowledge.append(Relation('afl','hola2', 'relation','esp2', 'di2'))
    _,results = cont_common_words_query('afr', 'afl')
    assert results != []

def test_list_common_words_relation():
    knowledge = []
    #create_tree(knowledge)
    knowledge.append(Relation('afr','hola', 'relation','esp', 'di2'))
    knowledge.append(Relation('afr','hola', 'relation','esp', 'di'))
    knowledge.append(Relation('afl','hola', 'relation','esp2', 'di2'))
    knowledge.append(Relation('afr','hola2', 'relation','esp', 'di'))
    knowledge.append(Relation('afl','hola2', 'relation','esp2', 'di2'))
    _,results = list_common_words_query('afr', 'afl')
    assert results != []

def test_most_relevant_language_relation():
    knowledge = []
    #create_tree(knowledge)
    knowledge.append(Relation('afr','hola', 'relation','esp', 'di2'))
    knowledge.append(Relation('afr','hola2', 'relation','esp', 'di'))
    knowledge.append(Relation('afr','hola3', 'relation','esp2', 'di2'))
    knowledge.append(Relation('afr','hola4', 'relation','esp', 'di'))
    knowledge.append(Relation('afr','hola5', 'relation','esp2', 'di2'))
    _,_, results = most_relevant_language_query('afr')
    assert results != []

def test_all_relevant_language_relation():
    knowledge = []
    #create_tree(knowledge)
    knowledge.append(Relation('afr','hola', 'relation','esp', 'di2'))
    knowledge.append(Relation('afr','hola2', 'relation','esp', 'di'))
    knowledge.append(Relation('afr','hola3', 'relation','esp2', 'di2'))
    knowledge.append(Relation('afr','hola4', 'relation','esp', 'di'))
    knowledge.append(Relation('afr','hola5', 'relation','esp2', 'di2'))
    _, results = percentages_relevant_language_query('afr')
    assert results != []
