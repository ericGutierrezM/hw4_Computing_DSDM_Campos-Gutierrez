##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts and returns
# the number of times that Simba appears in a list of
# strings. Example:
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

def count_simba(strings):
    return sum(map(lambda string: string.count("Simba"), strings))


# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.

import pandas as pd

def get_day_month_year(dates):
    def extract_components(date):
        return date.day, date.month, date.year
    
    components = map(extract_components, dates)
    return pd.DataFrame(components, columns=["day", "month", "year"])


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance

from geopy.distance import geodesic # type: ignore
from functools import reduce

def compute_distance(coordinates_pairs):
    distances = map(lambda pair: geodesic(pair[0], pair[1]).kilometers, coordinates_pairs)
    return reduce(lambda acc, val: acc + [val], distances, [])


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13

def sum_general_int_list(items):
    def reducer(acc, item):
        if isinstance(item, int):
            return acc + item
        elif isinstance(item, list):
            return acc + sum_general_int_list(item)
        else:
            return acc
    return reduce(reducer, items, 0)