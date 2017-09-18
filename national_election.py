"""
TODO: WRITE DOCSTRING
TODO: WRITE PSEUDOCODE INTO CODE
"""

__author__ = ['Yngve Mardal Moe', 'Brage Sekse Aarset']
__email__ = ['yngve.m.moe@gmail.com', 'brage.aarset@gmail.com']

import numpy as np
import pandas as pd

"""
PSEUDOCODE:


def national_election(data, chosen_election_system, election_districts):

    ## election_districts should be a dataframe/series naming X amount of election
    ## districts and listing the municipalities within them all
    ## the default one is obv. the 19 counties

    ## election_system should contain information about which election method, tiebreakers, etc.

    if election_districts is not default:
        for every district defined in election_districts:
            calculate seat distribution across districts

            party_votes = pandas.Series where data issum of parties' votes across each constituency,  indices/keys are party names
            if election_system is first_past_the_post:
                first_past_the_post(party_votes, )



def calculate_seats(election_districts):
    population and sq km and shit goes into this calculation
"""
