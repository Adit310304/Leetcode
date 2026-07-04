class Solution(object):
    def average(self, salary):
        sum_salary = sum(salary)
        total = sum_salary - min(salary) - max(salary)
        average = float(total) / (len(salary) - 2)

        return average