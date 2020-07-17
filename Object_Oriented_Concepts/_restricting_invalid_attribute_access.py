class Employee:
    def __init__(self, fname, lname, pay, languages):
        self.fname = fname
        self.lname = lname
        self.pay = pay
        self.languages = languages

# __setattr__ is called only for missing attributes.
    def __setattr__(self, name, value):
        if name not in {'fname', 'lname', 'pay'}:
            raise AttributeError('Cannot set ', name)
        super().__setattr__(name, value)
