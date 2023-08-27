#1
class UserMainCode:
    @classmethod
    def SortStudentMarks(cls, input1, input2, input3):
        marks = input3

        # Step 2: Calculate the averages
        averages = [sum(subject) / input1 for subject in zip(*marks)]

        # Step 4: Find the index of the subject with the lowest average
        lowest_avg_idx = averages.index(min(averages))

        # Step 5: Initialize the total marks list
        total_marks = []

        # Step 6: Calculate the total marks for each student
        for student in marks:
            student_marks = sum(student[:lowest_avg_idx] + student[lowest_avg_idx+1:])
            total_marks.append(student_marks)

        # Step 7: Return the total_marks list
        return total_marks
input1 = 3
input2 = 5
input3 = [[75, 76, 65, 87, 87], [78, 76, 68, 56, 89], [67, 87, 78, 77, 65]]
result = UserMainCode.SortStudentMarks(input1, input2, input3)
print(result)

#2 
class Solution:
    @classmethod
    def largestSubarray(cls, input1, input2):
        count = 0
        maxLength = 0
        countDict = {}

        for i in range(input1):
            if input2[i] == 0:
                count -= 1
            else:
                count += 1

            if count == 0:
                maxLength = i + 1

            if count in countDict:
                maxLength = max(maxLength, i - countDict[count])
            else:
                countDict[count] = i

        return maxLength

input1 = 4
input2 = [1, 1, 0, 1]
print(Solution.largestSubarray(input1, input2))  # Output: 2

input1 = 5
input2 = [1, 1, 1, 1, 1]
print(Solution.largestSubarray(input1, input2))  # Output: 0


#3
class UserMainCode(object):
    @classmethod
    def letter(cls, input1):

# Read only region end
# Write code here
        alaphabet_values= {'A':0,"B":1,"C":1,"D":2,"E":3,"F":5,"G":8,"H":13,"I":21,"J":34,"K":55,"L":89,"M":144,"N":233,"O":377,"P":610,"Q":987,"R":1597,"S":2584,"T":4181,"U":6765,"V":10946,"W":17711,"X":28657,"Y":46386,"Z":75025}
        sum_of_letters = 0
        for letter in input1:
            if letter in alaphabet_values:
                sum_of_letters += alaphabet_values[letter]
        return sum_of_letters