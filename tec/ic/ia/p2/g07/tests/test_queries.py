from tec.ic.ia.p2.g07.Relation import Relation
from tec.ic.ia.p2.g07.Queries import *

knowledge = []
tree = [['Ana', 'Rodrigo'], ['Juan', 'Rodrigo'], ['Rodrigo', 'Melissa'], ['Manuel', 'Roberto'], \
        ['Roberto', 'Julio'], ['Chris', 'Julio'], ['Julio', 'Melissa'], ['Melissa', 'Armando'], \
        ['Erick', 'Tatiana'], ['Tatiana', 'Armando'], ['Tatiana', 'Armando2']]

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

# def test_cousins_2_level_relation():
#     knowledge = []
#     create_tree(knowledge)
#     results = cousins_query('Roberto', 'Erick')
#     print(results)
#     assert results == []

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
    create_tree(knowledge)
    results = cont_common_words('lang_example_1', 'lang_example_2')
    print(results)
    assert results == []
