'''
Question 6: 
 Consider an attribute X of a data set that takes the values { x1, x2, ..., x9 } (sorted in increasing order of magnitude).
 
 We apply two methods (equal interval width and equal frequency) to discretize the attribute into three bins.
 The bins obtained are shown below:
 Equal Interval Width: { x1, x2, x3 }, { x4, x5, x6, x7, x8 }, { x9 }
 Equal Frequency: { x1, x2, x3 }, { x4, x5, x6 }, { x7, x8, x9 }

 Explain what will be the effect of applying the following transformations on each discretization method,
 i.e., whether the elements assigned to each bin can change if you discretize the attribute after applying
 the transformation function below.
 
 Note that x̄ denotes the average value and σx denotes standard deviation of attribute X.

 The answer to each subquestion is a dictionary with two keys:
 'equal_width' and 'equal_freq'.
 The values of each key is a list of two values: a string and an integer.
 The string is either Change or No change.
 The value of the integer is chosen among (1,..., 10), chosen according to the list below:

    1. The transformation leads to an inversion of the original order of values.
    2. The distance between xi and xi+1 does not change uniformly.
    3. The average value x̄ becomes the smallest value post-transformation.
    4. The relative ordering of points changes
    5. The transformation causes negative values to become positive and vice versa.
    6. The transformation results in all values becoming equal
    7. The distance between xi and xi+1 change uniformly.
    8. The standard deviation σx becomes zero after the transformation.
    9. No change in the relative ordering of points
    10. The maximum and minimum values of X get swapped after the transformation.

'''

'''
Question Notes:

'''

# (a) X -> X - x̄, (i.e., if the attribute values are centered).
def question6_1():
    """
    answer = {
        'equal_width': ['Change/No Change', (1, ..., 10)],
        'equal_frequency': ['Change/No Change', (1, ..., 10)]
    }
    """
    #  Test data { 17, 24, 25, 34, 35, 38, 39, 49, 68 }

    # (17 + 24 + 25 + 34 + 35 + 38 + 39 + 49 + 68) / 9
    # x̄ = 36.56

    # Transformed { -19.56, -12.56, -11.56, -2.56, -1.56, 1.44, 2.44, 12.44, 31.44 }
    
    #  Equal Interval Width: { x1, x2, x3 }, { x4, x5, x6, x7, x8 }, { x9 }
    # width of each bin is roughly 17
    # 17 - 33
    # 34 - 50
    # 51 - 68
    # { 17, 24, 25 }, { 34, 35, 38, 39, 49 }, { 68 }
    # -19.56 - -3.56
    # -2.56 - 13.44
    # 14.44 - 31.44
    # { -19.56, -12.56, -11.56 }, { -2.56, -1.56, 1.44, 2.44, 12.44 }, { 31.44 }

    #  Equal Frequency: { x1, x2, x3 }, { x4, x5, x6 }, { x7, x8, x9 }
    # 9 total data points, 3 bins, so each bin will have 3 values
    #  { 17, 24, 25 } { 34, 35, 38 } { 39, 49, 68 }
    #  { -19.56, -12.56, -11.56 }, { -2.56, -1.56, 1.44 }, { 2.44, 12.44, 31.44 }

    return {
        'equal_width': ['No Change', 9],
        'equal_frequency': ['No Change', 9]
    }

# (b) X -> (X - x̄)/(σx) (i.e., if the attribute values are standardized).
def question6_2():
    #  Test data { 17, 24, 25, 34, 35, 38, 39, 49, 68 }

    # x̄ = 36.56
    # σx = 14.28

    # Transformed { -1.37, -0.88, -0.81, -0.18, -0.11, 0.10, 0.17, 0.87, 2.20 }

    # width of each bin is roughly 17
    # { 17, 24, 25 }, { 34, 35, 38, 39, 49 }, { 68 }

    # width of each bin is roughly 1.19
    # -1.37 - -0.17
    # -0.18 - 1.00
    # 1.01 - 2.20
    # { -1.37, -0.88, -0.81 }, { -0.18, -0.11, 0.10, 0.17, 0.87 }, { 2.20 }

    return {
        'equal_width': ['Change', 7],
        'equal_frequency': ['Change', 7]
    }

# (c) X -> exp[(X - x̄)/(σx)] (i.e., if the values are standardized and exponentiated).
def question6_3():
    return {
        'equal_width': ['No Change', 9],
        'equal_frequency': ['No Change', 9]
    } 

