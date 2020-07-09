class Parent:
    def spam(self):
        print('Parent.Spam')


class A(Parent):
    def spam(self):
        print('A.Spam')
        super().spam()


class B(A):
    def spam(self):
        print('B.Spam')
        super().spam()


class C(B):
    def spam(self):
        print('C.Spam')
        super().spam()


class D(Parent):
    def spam(self):
        print('D.Spam')
        super().spam()


class E(A, D):
    pass