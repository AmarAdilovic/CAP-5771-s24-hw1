'''
Question 3: 
 Classify the following attributes as:
 1) discrete or continuous,
 2) qualitative or quantitative,
 3) nominal, ordinal, interval, or ratio.
 
 Choose the most comprehensive attribute.
 If the attribute is both interval or ratio, choose ratio.

 The answer to each subquestion is a list of three strings.
 ["Discrete/Continuous", "Qualitative/Quantitative", "Nominal/Ordinal/Interval/Ratio"]
'''

#  (a) Julian Date, which is the number of days elapsed since 12 noon Greenwich Mean Time of January 1, 4713 BC.
def question3_1():
    # answer = ['string', 'string', 'string']
    #  ["Discrete/Continuous", "Qualitative/Quantitative", "Nominal/Ordinal/Interval/Ratio"]
    return  ["Continuous", "Quantitative", "Ratio"]


#  (b) Movie ratings provided by users (1-star, 2-star, 3-star, or 4-star).
def question3_2():
    return ["Discrete", "Qualitative", "Ordinal"]


# (c) Mood level of a blogger (cheerful, calm, relaxed, bored, sad, angry or frustrated).
def question3_3():
    return ["Discrete", "Qualitative", "Nominal"] 

#  (d) Average number of hours a user spent on the Internet in a week.
def question3_4():
    return ["Continuous", "Quantitative", "Ratio"]

#  (e) IP address of a machine.
def question3_5():
    return ["Discrete", "Qualitative", "Nominal"]

#  (f) Richter scale (in terms of energy release during an earthquake).
def question3_6():
    return ["Discrete", "Qualitative", "Ordinal"]

# (g) Salary above the median salary of all employees in an organization.
def question3_7():
    return ["Continuous", "Quantitative", "Ratio"]

#  (h) Undergraduate level (freshman, sophomore, junior, and senior) for measuring years in college.
def question3_8():
    return ["Discrete", "Qualitative", "Ordinal"]
