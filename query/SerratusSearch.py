from abc import ABC, abstractmethod

class SerratusSearch(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_matches_file(self, **url_params):
        pass

    @abstractmethod
    def get_matches_paginated(self, **url_params):
        pass

    @abstractmethod
    def get_counts(self, **url_params):
        pass

    @abstractmethod
    def get_list(self, **url_params):
        pass
