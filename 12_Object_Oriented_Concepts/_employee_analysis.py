import csv

# Company Class.
class Company:
    def __init__(self):
        self._team = []

    def add_emp(self, name, gender, team, pay):
        self._team.append((name, gender, team, pay))

    # Total Cost
    def total_cost(self):
        total = 0.00
        for emp in self._team:
            total += float(emp[3])
        return total

    # Total Number of male and female employees
    def emp_count_by_gender(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[1]] += 1
        return _count

    # Count of Employees in each department
    def emp_count_by_department(self):
        from collections import defaultdict
        _count = defaultdict(int)
        for emp in self._team:
            _count[emp[2]] += 1
        return _count

# Analysis of employees.csv file
with open('apple_employees.csv') as f:
    apple = Company()
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        apple.add_emp(row[0], row[1], row[2], row[3])

print(apple.total_cost())
print(apple.emp_count_by_gender())
print(apple.emp_count_by_department())
