'''
Question 4: 
State the type of each attribute given below before and after we have performed the following transformation.

The answer to each subquestion is a list of two strings.
The state of attributes are one of nominal, ratio, ordinal, or interval.
["Nominal/Ordinal/Interval/Ratio", "Nominal/Ordinal/Interval/Ratio"]
'''

'''
Question Notes:

    Nominal:
        - Values are just different names
        - Nominal values provide only enough information to distinguish one object from another
            - No intrinsic ordering
        - Examples
            - Zip codes, employee ID numbers, eye color, gender

    Ordinal:
        - Values provide enough information to order objects (< or >)
        - Examples
            - Hardness of minerals, {good, better, best}, grades, Calendar dates?

    Interval:
        - Differences between values are meaningful and consistent
            - A unit of measurement exists (+, -)
        - Examples
            - Temperature in Celsius/Fahrenheit

    Ratio:
        - Both differences and ratios are meaningful (*, /)
            - Has a true 0, where the absence of that thing can be measured
            - Both a clear order of values but also a meaningful zero point
        - Examples 
            - Temperature in Kelvin, monetary quantities, counts, age, mass, length, electrical current


    Discretized = the process of transforming a continuous variable into a discrete one
'''

# (a) Hair color of a person is mapped to the following values: 
# black = 0, brown = 1, red = 2, blonde = 3, grey = 4, white = 5.
def question4_1():
    # answer = ['string', 'string']
    # ["Nominal/Ordinal/Interval/Ratio", "Nominal/Ordinal/Interval/Ratio"]
    return ["Nominal", "Ordinal"]


# (b) Grade of a student (from 0 to 100) is mapped to the following scale:
#  A = 4.0, A- = 3.5, B = 3.0, B- = 2.5, C = 2.0, C- = 1.5, D = 1.0, D = 0.5, E = 0.0
def question4_2():
    return ["Ratio", "Interval"]

#  (c) Age of a person is discretized to the following scale:
# Age < 12, 12 <= Age < 21, 21 <= Age < 45, 45 <= Age < 65, Age > 65.
def question4_3():
    return ["Ratio", "Ordinal"] 

#  (d) Annual income of a person is discretized to the following scale:
# Income < $20K, $20K <= Income < $60K, $60K <= Income < $120K, $120K <= Age < $250K, Age >= $250K.
def question4_4():
    return ["Ratio", "Ordinal"]

#  (e) Height of a person is changed from meters to feet.
def question4_5():
    return ["Ratio", "Ratio"]

#  (f) Height of a person is changed from meters to (Short, Medium, Tall) .
def question4_6():
    return ["Ratio", "Ordinal"]

# (g) Height of a person is changed from feet to number of inches above 4 feet.
def question4_7():
    return ["Ratio", "Ratio"]

#  (h) Weight of a person is standardized by subtracting it with the mean of the weight for all people 
# and dividing by its standard deviation.
def question4_8():
    return ["Ratio", "Ratio"]
