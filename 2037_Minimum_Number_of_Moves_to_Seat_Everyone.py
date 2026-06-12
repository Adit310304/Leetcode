class Solution(object):
    def minMovesToSeat(self, seats, students):
        sorted_seats = sorted(seats)
        sorted_students = sorted(students)
        count = 0
        previous = 0

        for i in range(len(sorted_seats)):
            if sorted_seats[i] != previous:
                count += abs(sorted_seats[i] - sorted_students[i])
        
        return count