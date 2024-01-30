'''
Question 9: Which similarity or distance measure is most effective for each of the domains given below 

The answer to each subquestion should be a string, one of:
["SMC"/"Jaccard"/"Euclidean"/"Cosine Similarity"]
'''

'''"
Question Notes:

'''

# (a) Which measure, Jaccard or Simple Matching Coefficient, is most appropriate to compare
# how similar are the answers provided by students in an exam.
# Assume that the answers to all the questions in the exam are either True or False.
def question9_1():
    """
    answer = string'
    """
    return "SMC"

# (b) Which measure, Jaccard or Simple Matching Coefficient, is most appropriate to compare
# how similar are the locations visited by tourists at an amusement park.
# Assume the location information is stored as binary yes/no attributes
# (yes means a location was visited by the tourist and no means a location has not been visited).
def question9_2():
    return "Jaccard"

# (c) Which measure, Euclidean distance or correlation coefficient, is most appropriate to compare two rows in a network trace.
# For each row, we record information about
# the number of packets transmitted,
# number of bytes transferred,
# number of acknowledgments sent,
# and duration of the session.
def question9_3():
    return "Euclidean" 

# (d)Which measure, Euclidean distance or cosine similarity, is most appropriate to compare 
# the coordinates of a moving object in a 2-dimensional space.
# For example, using GPS data, the object maybe located at (314 West, 124 North)
# at time t1 and(294 West, 125 North) at another time t2 .
# Note: wemayuse+/- to indicateEast/West orNorth/Southdirectionswhencomputingthesimilarityordistance measures.
def question9_4():
    return "Cosine Similarity"  

# (e) Whichmeasure,Euclideandistanceor cosine similarity, ismostap
# propriatetocomparethesimilarityof itemsboughtbycustomersata
#  grocerystore. Assumeeachcustomer isrepresentedbya0/1binary
#  vectorof items(wherea1meansthecustomerhadpreviouslybought
#  theitem)
def question9_5():
    return "Cosine Similarity" 

