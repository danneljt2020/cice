import math


class Stadistics:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def n(self):
        return len(self.x)

    @property
    def avg_x(self):
        return sum(self.x) / self.n

    @property
    def avg_y(self):
        return sum(self.y) / self.n

    @property
    def variance_x(self):
        x_media = self.avg_x
        s1 = 0
        for j in self.x:
            d_pow = pow((j - x_media), 2)
            s1 = s1 + d_pow
        return s1 / self.n

    @property
    def variance_y(self):
        y_media = self.avg_y
        s1 = 0
        for j in self.y:
            d_pow = pow((j - y_media), 2)
            s1 = s1 + d_pow
        return s1 / self.n

    def sumxy(self):
        sum_xy = 0
        for i in range(0, self.n):
            sum_xy += self.x[i] * self.y[i]
        return sum_xy

    @property
    def co_variance(self):
        return (self.sumxy() / self.n) - self.avg_x * self.avg_y

    @property
    def r(self):
        den = self.co_variance
        num = math.sqrt(self.variance_x) * math.sqrt(self.variance_y)
        return den / num

    @property
    # TODO
    def B(self):
        den = self.n * self.sumxy() - (sum(self.x) * sum(self.y))

        return den

    def __str__(self):
        return f"X {self.x}\nY: {self.y}\nN: {self.n}"


data_2 = Stadistics([1, 2, 3], [10, 20, 27])
print(data_2.B)
