#GroupA_Practical2
'''Write a Python program to store marks scored in subject “Fundamental of Data
Structure” by N students in the class. Write functions to compute following:
a) The average score of class
b) Highest score and lowest score of class
c) Count of students who were absent for the test
d) Display mark with highest frequency'''

def avgScore(mark):
    # Calculate the average score of the class
    Total = 0
    count = 0
    for i in mark:
        Total = Total + i
        count = count + 1

    return Total / count


def maxScore(mark):
    # Find the highest score in the class
    max_val = mark[0]
    for m in mark:
        if m > max_val:
            max_val = m
    return max_val


def minScore(mark):
    # Find the lowest score in the class
    min_val = mark[0]
    for i in mark:
        if i < min_val:
            min_val = i
    return min_val


def countAbsent(mark):
    # Count the number of students absent for the test
    count = 0
    for i in mark:
        if i == 0:
            count = count + 1

    return count


def freqMax(mark):
    # Find the mark with the highest frequency
    max_freq = 0
    element = maxScore(mark)
    for i in mark:
        freq = 0
        for j in mark:
            if i == j:
                freq = freq + 1
        if freq > max_freq:
            max_freq = freq
            element = i
    res = [max_freq, element]
    return res


# Main
N = 5  # Set the number of students
print("Note: If a student is absent, add marks = 0")
Marks = [85, 90, 75, 60, 0]  # Pre-declared list of marks

# Calculate and display various statistics
average = avgScore(Marks)
print("Average Score of the class:", average)

highest = maxScore(Marks)
print("Highest Score in the class:", highest)

lowest = minScore(Marks)
print("Lowest Score in the class:", lowest)

absent_count = countAbsent(Marks)
print("Number of students absent:", absent_count)

frequency_result = freqMax(Marks)
print("Mark with the highest frequency:", frequency_result[1])
