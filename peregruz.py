class Clock:
    def __init__(self, hours, minutes, seconds):
        self.seconds = hours * 3600 + minutes * 60 + seconds

    def __str__(self):
        h = self.seconds // 3600
        m = (self.seconds % 3600) // 60
        s = self.seconds % 60
        return f"{h:02}:{m:02}:{s:02}"

    def __sub__(self, other):
        return Clock(0, 0, self.seconds - other.seconds)

    def __mul__(self, other):
        return Clock(0, 0, self.seconds * other.seconds)

    def __floordiv__(self, other):
        return Clock(0, 0, self.seconds // other.seconds)

    def __mod__(self, other):
        return Clock(0, 0, self.seconds % other.seconds)

    def __isub__(self, other):
        self.seconds -= other.seconds
        return self

    def __imul__(self, other):
        self.seconds *= other.seconds
        return self

    def __ifloordiv__(self, other):
        self.seconds //= other.seconds
        return self

    def __imod__(self, other):
        self.seconds %= other.seconds
        return self

c1 = Clock(0, 10, 0)
c2 = Clock(0, 3, 20)

print("c1:", c1)
print("c1 - c2:", c1 - c2)
print("c1 * c2:", c1 * c2)
print("c1 // c2:", c1 // c2)
print("c1 % c2:", c1 % c2)

c1 -= c2
print("c1 -= c2:", c1)

c1 *= c2
print("c1 *= c2:", c1)

c1 //= c2
print("c1 //= c2:", c1)

c1 %= c2
print("c1 % c2:", c1)