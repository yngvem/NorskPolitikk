"""
TODO: WRITE DOCSTRING
"""

__author__ = ['Yngve Mardal Moe', 'Brage Sekse Aarset']
__email__ = ['yngve.m.moe@gmail.com', 'brage.aarset@gmail.com']

import numpy as np
import pandas as pd


def _saint_lague_divisor(seats):
    return 2*seats + 1


def _dhondts_divisor(seats):
    return seats + 1


def highest_quotient_method(votes, num_seats, quotient_modifier=1.4, divisor_method='saint_lague',
                            tie_breaker='favour_small'):
    """Returns the no. of seats of the different parties using a highest quotient method.

    Arguments:
    ----------
    votes : pandas.Series
        A series where the indices are the parties and the values are the votes the corresponding
        parties got.
    num_seats : int
        The total number of seats to distribute.
    quotient_modifier : float
        The number all votes are divided by before distributing seats.
    divisor_method : int or str
        Indicating whether to use the Saint Legauës (Webster) method or the D'Hondts method
        for distributing seats. Saint Legauës method will be used if this variable is
        either 0, 'sl', 'saint_lague' or 'webster' and D'Hondts method will be used
        if this variable is either 0, 'dh' or 'dhondts'
    tie_breaker : int or str
        Indicating how ties should be broken. If this variable is 'favour_small' or 0
        ties will be broken by giving the party with the least no. of seats the next seat.
        If this variable is 'favour_large' or 1 ties will be broken by giving the party
        with the most no. of seats the next seat. Lastly, if this variable is 'random' or 2
        ties will be broken randomly.

    Returns:
    --------
    party_seats : pandas.Series
        The distribution of the party seats for each of the parites.
    lost_votes : pandas.series
        The total no. of seats that did not count towards any seats for each of the parties.
    """
    if tie_breaker == 0 or str(tie_breaker).lower() == 'favour_small':
        votes = votes.sort_values(ascending=True)
    elif tie_breaker == 1 or str(tie_breaker).lower() == 'favour_large':
        votes = votes.sort_values(ascending=False)
    else:
        votes = votes.sample(frac=1)  # Shuffle votes

    num_parties = len(votes)

    party_quotients = votes.copy()
    party_seats = pd.Series(np.zeros(num_parties), index=votes.index)

    party_quotients /= quotient_modifier

    saint_lague_strings = ['sl', 'saint_lague', 'webster']
    dhondts_strings = ['dh', 'dhondts']
    if divisor_method == 0 or str(divisor_method).lower() in saint_lague_strings:
        divisor = _saint_lague_divisor
    elif divisor_method == 1 or str(divisor_method).lower() in dhondts_strings:
        divisor = _dhondts_divisor
    else:
        raise ValueError('`divisor_method` is invalid.')

    for _ in range(num_seats):
        winner = party_quotients.argmax()
        party_seats[winner] += 1
        party_quotients[winner] = votes[winner]/divisor(party_seats[winner])

    lost_votes = party_quotients
    return party_seats, lost_votes


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
