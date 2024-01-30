'''
Question 8:  Measures of Similarity and Dissimilarity 
 Consider the following binary vectors:
    x1 = (1, 1, 1, 1, 1)
    x2 = (1, 1, 1, 0, 0)
    y1 = (0, 0, 0, 0, 0)
    y2 = (0, 0, 0, 1, 1)
    y3 = (0, 1, 0, 1, 1)

 The answer to each subquestion should either be a list of two points or the string "equally similar".
 The two points are taken from 'x1', 'x2', 'y1', 'y2', 'y3'.
'''

'''
Question Notes:

Value of 1 means two objects are completely similar
Value of 0 indicates not at all similar

x = (1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
y = (0, 0, 0, 0, 0, 0, 1, 0, 0, 1)

f00 = num attributes where x and y are 0     = 7
f11 = num attributes where x and y are 1     = 0
f01 = num attributes where x is 0 and y is 1 = 2
f10 = num attributes where x is 1 and y is 0 = 1 

Jaccard coefficient:

    f11 / f01 + f10 + f11 = 0 / 2 + 1 + 0 = 0 / 3 = 0

Simple Matching Coefficient (SMC):

    number of matching attribute values / number of attributes 

    f11 + f00 / f01 + f10 + f11 + f00 

    0 + 7 / 2 + 1 + 0 + 7 = 7 / 10 = 0.7

Simple Eucliedean Distance (Euclidean):

Cosine Similarity:

'''

# (a) According to Jaccard coefficient, which pair of vectors--(x1, x2) or (y1, y2) are more similar to each other?
def question8_1():
    """
    answer = 'string'  or ['pt1', 'pt2']
    answer = "equally similar" | ['x1', 'x2', 'y1', 'y2', 'y3']
    """

    # x1 = (1, 1, 1, 1, 1)
    # x2 = (1, 1, 1, 0, 0)

    # f00 = num attributes where x and y are 0     = 0
    # f11 = num attributes where x and y are 1     = 3
    # f01 = num attributes where x is 0 and y is 1 = 0
    # f10 = num attributes where x is 1 and y is 0 = 2 

    # f11 / f01 + f10 + f11 = 3 / 0 + 2 + 0 = 3 / 2 = 1.5


    # y1 = (0, 0, 0, 0, 0)
    # y2 = (0, 0, 0, 1, 1)

    # f00 = num attributes where x and y are 0     = 3
    # f11 = num attributes where x and y are 1     = 0
    # f01 = num attributes where x is 0 and y is 1 = 2
    # f10 = num attributes where x is 1 and y is 0 = 0

    # f11 / f01 + f10 + f11 = 0


    return ['x1', 'x2']

#  (b) According to simple matching coefficient, which pair of vectors (x1, x2) or (y1, y2) are more similar to each other?
def question8_2():
    # x1 = (1, 1, 1, 1, 1)
    # x2 = (1, 1, 1, 0, 0)

    # f00 = num attributes where x and y are 0     = 0
    # f11 = num attributes where x and y are 1     = 3
    # f01 = num attributes where x is 0 and y is 1 = 0
    # f10 = num attributes where x is 1 and y is 0 = 2 

    #  f11 + f00 / f01 + f10 + f11 + f00 
    #  3 + 0 / 0 + 3 + 0 + 2
    #  3 / 5


    # y1 = (0, 0, 0, 0, 0)
    # y2 = (0, 0, 0, 1, 1)

    # f00 = num attributes where x and y are 0     = 3
    # f11 = num attributes where x and y are 1     = 0
    # f01 = num attributes where x is 0 and y is 1 = 2
    # f10 = num attributes where x is 1 and y is 0 = 0

    #  f11 + f00 / f01 + f10 + f11 + f00 
    #  0 + 3 / 0 + 3 + 2 + 0
    # 3 / 5
    return "equally similar"

#  (c) According to simple Euclidean distance, which pair of vectors (x1, x2) or (y1, y2) are more similar to each other?
def question8_3():
    # x1 = (1, 1, 1, 1, 1)
    # x2 = (1, 1, 1, 0, 0)
    # 2

    # y1 = (0, 0, 0, 0, 0)
    # y2 = (0, 0, 0, 1, 1)
    # 2

    return "equally similar" 

#  (d) According to simple Euclidean distance, which pair of vectors (x1, y1) or (x2, y3) are more similar to each other?
def question8_4():
    # x1 = (1, 1, 1, 1, 1)
    # y1 = (0, 0, 0, 0, 0)
    # 5

    # x2 = (1, 1, 1, 0, 0)
    # y3 = (0, 1, 0, 1, 1)
    # 4
    return ['x2', 'y3'] 
