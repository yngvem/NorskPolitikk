#Saint_lagues metode-utkast


def saint_lague(votes_dict, no_seats):
    """

    Notes about running this function:
    This function needs to be told what quotient_modifier or "delingstall" will
    be used (Norway currently uses 1.4, but normally this is 1 (aka not used))


    if any parties are tied in votes, what then?
    something must be done, not quite sure what?
    maybe that for each round where they are tied, they both
    get seats, and once there is a tie and there is not enough
    seats left for them to get one each it will be randomly decided?

    Pseudocode:
    make a list that's a copy of the party_votes list
        this list will be used for the quotients, which will be redefined
        when a party gets a seat and their votes are divided by 3, 5 or whatever
    other definitions?
    make a party_seats list full of zeroes that's as long as there are parties

    divide the quotients by the quotient_modifier aka "delingstall"
    The quotient modifier is normally 1 but in Norway it's 1.4

    check for ties amongst parties #(I think it's more efficient to split it like this?)
        otherwise we would have to check for ties constantly,
        even though there will practically never be a tie in real life

    if there is a tie:
        while no_seats:
            find the parties with the highest current quotient
            if there are more seats left than there are tied parties:
                give those party a seat each in the party_seats list
                no_seats -= number of parties that just received a seat
                their new quotients = no_votes/1 + 2 * (the number of seats they have gotten)
            else:
                distribute the remaining seats randomly between these parties
                (in a fair way I mean, nobody should get two)
                no_seats = 0

    else:
        while no_seats:
            find the party with the highest current quotient
            give that party a seat in the party_seats list
            no_seats -= 1
            their new quotient = no_votes/1 + 2 * (the number of seats they have gotten)

    seat_distribution = {
        party: seats
            for party, seats in zip(parties, party_seats)
    }

    lost_votes = {party: votes
        for party, votes in zip(parties, quotients)
    }
    """

    #actual code scraps below
    parties, party_votes = list(votes_dict.keys()), list(votes_dict.values())
    parties, party_votes = np.array(parties), np.array(party_votes)

    party_quotients = party_votes.copy()

    while no_seats:
