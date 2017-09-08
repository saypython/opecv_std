from test import A
s=A()
s.p()
s.g()
s.a=16
s._a=17
s.__a=18
print(s.a)
print(s._a)
print(s.g())