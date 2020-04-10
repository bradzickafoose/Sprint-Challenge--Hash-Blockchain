#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    # find the pair of item weights thats sum equals the weight limit and store in the hash table
    for high_value_index in range(length):
      weight = weights[high_value_index]
      low_value_index = hash_table_retrieve(ht, limit - weight)
      if low_value_index is None:
        hash_table_insert(ht, weight, high_value_index)
      # return the item weights of the two packages that equals the weight limit
      else:
        answer = (high_value_index, low_value_index)
        return answer

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")