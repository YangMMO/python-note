class Clock:
    id = None
    price = None

    def ring(self):
        # 可发出声音
        import  winsound
        # 间隔频率 2， 持续 3
        winsound.Beep(2000, 3000)


clock1 = Clock()
clock1.id = "1101"
clock1.price = 12.00
print(f"id: {clock1.id}, price: {clock1.price}")
clock1.ring()

clock2 = Clock()
clock2.id = "1102"
clock2.price = 19.00
print(f"id: {clock2.id}, price: {clock2.price}")
clock2.ring()

