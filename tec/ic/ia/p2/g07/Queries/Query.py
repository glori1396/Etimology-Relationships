from abc import ABC, abstractmethod

"""
This class implement an abstract class as a definition of a query.
"""

class Query(ABC):
    def __init__(self, relations, first_entry, second_entry):
        self.relations = relations
        self.first_entry = first_entry
        self.second_entry = second_entry

    @abstractmethod
    def execute_query(self):
        pass
