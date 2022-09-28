class Student:
    name = None

    def say_hi(self):
        print(f"hi, {self.name}")

    def say_hi1(self, msg):
        print(f"hi, {msg}")


s1 = Student()
s1.name = "ABC"
# hi, ABC
# hi, 666
s1.say_hi()
s1.say_hi1("666")
