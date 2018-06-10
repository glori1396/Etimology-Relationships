from pyDatalog import pyDatalog
class Relation(pyDatalog.Mixin): # --> Employee inherits the pyDatalog capability

    def __init__(self, first_lang, first, relation, second_lang, second):
        # call the initialization method of the Mixin class
        super(Relation, self).__init__()
        self.first_lang = first_lang
        self.first = first
        self.relation = relation
        self.second_lang = second_lang
        self.second = second

    def __repr__(self): # specifies how to display a Relation
        return self.first_lang+":"+self.first+" "+self.relation+" "+self.second_lang+":"+self.second
