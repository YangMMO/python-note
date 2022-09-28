class Animal:
    # 父类多态方法
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("miao")


class Dot(Animal):
    def speak(self):
        print("wang")


# 使用多态方法
def speak(animal: Animal):
    animal.speak()


cat = Cat()
dog = Dot()

# miao
# wang
speak(cat)
speak(dog)
