from tec.ic.ia.p2.g07.Queries.Query import Query
from tec.ic.ia.p2.g07.Relation import Relation
from pyDatalog import pyDatalog

"""
This model creates a logistic regression to predict votes in 1st and 2nd round
using Tensorflow.
"""

pyDatalog.create_terms('siblings', 'X', 'Y')

class Siblings(Query):
    def __init__(self, relations, first_entry, second_entry):
        super().__init__(relations, first_entry, second_entry)

    def execute_query(self):
        siblings(X,Y,R) <= (Relation.relation[X]==R) & (Relation.relation[Y]==R)
