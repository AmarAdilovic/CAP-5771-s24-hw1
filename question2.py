'''
Question 2 : 
Classify the following attributes as binary, discrete, or continuous.
Also classify them as qualitative (nominal or ordinal) or quantitative (interval or ratio).
Some cases may have more than one interpretation, so briefly indicate your reasoning if you think there may be some ambiguity.

The answer must be a list of three strings.
["Binary/Discrete/Continuous", "Qualitative/Quantitative", "Nominal/Ordinal/Interval/Ratio"]
'''

'''
Question Notes:

Term Definitions (taken from the textbook):
    Binary:
        - Categorical variable that can only possibly have two values
        - Examples
            - Gender, yes/no, True/False
    Discrete:
        - Numerical that can take on distinct, separate values
            - Usually counted in whole numbers
        - Examples
            - Number of students, number of pencils, etc.
    Continuous:
        - Infinite number of values within a given range
            - Can measure them with great precision
        - Examples
            - Height, Weight, Temperature, Time

    Qualitative:
        - Also known as categorical attributes
            - Lack most of the properties of numbers, should be treated as symbols.

        Nominal:
            - Values are just different names
            - Nominal values provide only enough information to distinguish one object from another
                - No intrinsic ordering
            - Examples
                - Zip codes, employee ID numbers, eye color, gender
            - Operations
                - Mode, entropy, contingency, correlation, X^2 test 

        Ordinal:
            - Values provide enough information to order objects (< or >)
            - Examples
                - Hardness of minerals, {good, better, best}, grades, Calendar dates
            - Operations
                - Median, Percentiles, Rank correlation, Run tests, Sign tests
        
    Quantitative:
        - Also known as numeric attributes
            - Represented by numbers and have most of the properties of numbers
                - Can be integer-valued or continuous

        Interval:
            - Differences between values are meaningful and consistent
                - A unit of measurement exists (+, -)
            - Examples
                - Temperature in Celsius/Fahrenheit
            - Operations
                - Mean, standard deviation, Pearson's correlation t and F tests

        Ratio:
            - Both differences and ratios are meaningful (*, /)
                - Has a true 0, where the absence of that thing can be measured
                - Both a clear order of values but also a meaningful zero point
            - Examples 
                - Temperature in Kelvin, monetary quantities, counts, age, mass, length, electrical current
            - Operations
                - Geometric mean, harmonic mean, percent variation
'''

#  (a) Number of courses registered by a student in a given semester.
def question2_1():
    # answer = ['string', 'string', 'string']
    # ["Binary/Discrete/Continuous", "Qualitative/Quantitative", "Nominal/Ordinal/Interval/Ratio"]
    return ["Discrete", "Quantitative", "Ratio"]

#  (b) Speed of a car (in miles per hour).
def question2_2():
    return ["Continuous", "Quantitative", "Ratio"]

#  (c) Decibel as a measure of sound intensity.
def question2_3():
    return ["Continuous", "Quantitative", "Interval"] 

#  (d) Hurricane intensity according to the Sar-Simpson Hurricane Scale.
def question2_4():
    return ["Discrete", "Qualitative", "Ordinal"]

#  (e) Social security number.
def question2_5():
    return ["Discrete", "Qualitative", "Nominal"]
