#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * (length - 1)

    for ticket in tickets:
      if ticket.source != "NONE":
        hash_table_insert(hashtable, ticket.source, ticket.destination)
      else:
        route[0] = ticket.destination

    for key in range(length - 1):
      next_destination = hash_table_retrieve(hashtable, route[key])
      if next_destination != "NONE":
        route[key+1] = next_destination

    return route