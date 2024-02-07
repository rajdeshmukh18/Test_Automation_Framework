class A:
    def __init__(self):
        print("Hello from A constructor")
    def display(self):
        print("Hello from A display()")

class B(A):
    def __init__(self):
        super().__init__()
        print('Hello from B Constructor')
    def display2(self):
        print("Hello from B display2()")
b=B()
b.display2()