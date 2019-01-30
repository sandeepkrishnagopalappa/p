import os

print(os.getcwd())

print(os.listdir())


# li = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
# s_li = sorted(li, reverse=False)

# print(s_li)

# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# print(sorted(tup))
# nums = list(range(0,1000))
# even_list = [n for n in nums if not n % 2 == 0]
# print(even_list, end=',')


# my_dict = {}
# for c in my_word:
#     my_dict[c] = my_word.count(c)
# print(my_dict)

# my_list = []
# start_index = 0
# end_index = 0
# my_sentence = 'myNameIsAmithab'
# for c in my_sentence:
#     if c.isupper():
#         end_index = my_sentence.index(c)
#         my_list.append(my_sentence[start_index:end_index])
#         start_index = end_index
# my_list.append(my_sentence[start_index:])
#
# print(my_list)


# name = ['Steve', 'Bill', 'Mark']
# company = ['Apple', 'Microsoft', 'Google']
# my_dict = {}
# for name, company in zip(name, company):
#     my_dict.update({name:company})
#
# print(my_dict)
# print(dir(list))
class Employee:

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay

    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.pay}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_email(self):
        return f'{self.first_name}.{self.last_name}@company.com'

    def get_pay(self):
        return self.pay


emp_1 = Employee('Steve', 'Jobs', 90000)
emp_2 = Employee('Bill', 'Gates', 80000)
emp_3 = Employee('Tammy', 'Harper', 70000)
emp_4 = Employee('Johny', 'Ive', 60000)

emp_list = [emp_1, emp_2, emp_3, emp_4]

print(sorted(emp_list, key=lambda emp: emp.pay))


# class Developer(Employee):
#
#     def __init__(self, first_name, last_name, pay, prog_lang):
#         super().__init__(first_name, last_name, pay)
#         self.prog_lang = prog_lang
#
#     def get_prog_lang(self):
#         return self.prog_lang

# dev1 = Developer('Steve', 'Jobs', 50000, 'Java')
# dev2 = Developer('Bill', 'Gates', 60000, 'Python')

# print(dev1.get_full_name())

# print(dev2.get_email())

# print(dev1.prog_lang)

# print(dev2.prog_lang)