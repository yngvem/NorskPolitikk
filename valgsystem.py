"""
TODO: WRITE DOCSTRING
"""

__author__ = ['Yngve Mardal Moe', 'Brage Sekse Aarset']
__email__ = ['yngve.m.moe@gmail.com', 'brage.aarset@gmail.com']

import numpy as np


def first_past_the_post(votes_dict, no_seats):
    """Computes the no. of seats the different parties gets using a FPTP voting system.

    TODO: WRITE ABOUT FPTP!
    In case of ties the votes will be split evenly, if this is not possible, the excess
    seats will be distributed randomly amongst the winners.

    Arguments:
    ----------
    votes_dict : dict
        A dictionary containing the party names as key and no. of votes the
        corresponding party gets as values.
    no_seats : int
        No of seats for parliament to hand out.
    """
    parties, party_votes = list(votes_dict.keys()), list(votes_dict.values())
    parties, party_votes = np.array(parties), np.array(party_votes)
    max_votes = party_votes.max()

    no_winners = np.sum(party_votes == party_votes.max())

    no_extra = no_seats % no_winners
    winners = parties[party_votes == max_votes].copy()
    np.random.shuffle(winners)
    gains_extras = winners[:no_extra]

    seat_distribution = {
        party: int(no_seats/no_winners + (party == gains_extras)) if votes == max_votes else 0
            for party, votes in zip(parties, party_votes)
    }

    lost_votes = {party: votes if votes != party_votes.max() else 0
        for party, votes in zip(parties, party_votes)
    }

    return seat_distribution, lost_votes
