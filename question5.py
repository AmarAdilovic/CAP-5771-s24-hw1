'''
Question 5: 
 Consider the following dataset that contains the age and gender information for 9 users who visited a given website.
 
 Answers to each subquestion is a dictionary with keys:
 "bin1", "bin2", and "bin3". Each value is a list of integers.

 USERID | 1      | 2      | 3      | 4      | 5      | 6      | 7      | 8      | 9      |
 AGE    | 17     | 24     | 25     | 28     | 32     | 38     | 39     | 49     | 68     |
 GENDER | Female | Male   | Male   | Male   | Female | Female | Female | Male   | Male   |
 '''

'''
Question Notes:

    Discretization methods for classification is dependent on if class information is used (supervised) or not (unsupervised).

    Supervised Discretization Approach:
        - Using additional information (like class labels) produces better results than unsupervised discretization
        - Member Purity:
            - Members belong to the same class
            - Process
                - Sort the data based on attribute values within each class.
                - Maximize purity by minimizing mixing of different classes within bins
                - Create bins based on those splits, aim for class label purity

    Unsupervised Discretization
        - Performed without using any class labels or target information
        - Solely based on the distribution of the attribute values
   
        Equal Interval Width Approach:
            -  Divides the range of the attributes into a user-specified number of intervals/bins each having the same width
                - Can be badly impacted by outliers
                - Process
                    - Determine attribute range, divide that range into a user-specified num of bins with equal width
                    - Using attribute values assign to respective bins
        
        Equal Frequency/Depth Approach:
            - Puts the same number of objects in each interval
            - Divide the data into bins where each bin has roughly the same num of data points/objects
            - Process
                - Determine total num of points, divide data into specified num of bins where each bin has the same num of data
                - Using attribute values assign to respective bins

'''

# a) Suppose you apply an equal interval width approach to discretize the Age attribute into 3 bins.
# Show the userIDs assigned to each of the 3 bins.
def question5_1():
    """
    answer = {
            'bin1': [d1,d2,d3...]
            'bin2': [e1,...],
            'bin3': [f1,...]
    }
    where di, ei, fi are integers. 
    """
    # Age goes from 17 - 68
    # 68 - 17 = 51 / num_bins (3) = 17
    # width of each bin is roughly 17
    # 17 - 33
    # 34 - 50
    # 51 - 68
    return {
        'bin1': [1, 2, 3, 4, 5],
        'bin2': [6, 7, 8],
        'bin3': [9]
    }

#  (b) Repeat the previous question using the equal frequency approach.
def question5_2():
    # 9 total data points, 3 bins, so each bin will have 3 values
    return {
        'bin1': [1, 2, 3],
        'bin2': [4, 5, 6],
        'bin3': [7, 8, 9]
    }

# (c) Repeat question (a) using a supervised discretization approach (with Gender as class attribute).
# Specifically, choose the bins in such a way that their members are as pure as possible
# (i.e., belonging to the same class).
def question5_3():
    # Gender as class attribute:
    # Male User IDs (Age): 
    # 2 (24), 3 (25), 4 (28), 8 (49), 9 (68)
    # Female User IDs (Age):
    # 1 (17), 5 (32), 6 (38), 7 (39) 
    # Age ranges taking into account gender
    # Bin 1 : 17 - 28
    # Bin 2 : 29 - 40
    # Bin 3 : 41 - 68
    # Only 1 is not paired with the same class
    return {
        'bin1': [1, 2, 3, 4],
        'bin2': [5, 6, 7],
        'bin3': [8, 9]
    } 
