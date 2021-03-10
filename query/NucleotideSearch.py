from .SerratusSearch import SerratusSearch
from .counts.nucleotide import get_counts_from_params


class NucleotideSearch(SerratusSearch):
    def __init__(self):
        return super().__init__('nucleotide')

    def get_matches_file(self, **url_params):
        pass

    def get_matches_paginated(self, **url_params):
        pass

    def get_counts(self, **url_params):
        return get_counts_from_params(**url_params)

    def get_list(self, **url_params):
        pass
