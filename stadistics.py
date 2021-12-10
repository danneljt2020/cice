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

    def sum_xy(self):
        sum_xy = 0
        for i in range(0, self.n):
            sum_xy += self.x[i] * self.y[i]
        return sum_xy

    def sum_x(self):
        sum_x = 0
        for i in range(0, self.n):
            sum_x += self.x[i]
        return sum_x

    def sum_xpow(self):
        sum_x_pow = 0
        for i in range(0, self.n):
            sum_x_pow += pow(self.x[i], 2)
        return sum_x_pow

    @property
    def co_variance(self):
        return (self.sum_xy() / self.n) - self.avg_x * self.avg_y

    @property
    def r(self):
        den = self.co_variance
        num = math.sqrt(self.variance_x) * math.sqrt(self.variance_y)
        return den / num

    @property
    def B(self):
        den = self.n * self.sum_xy() - (sum(self.x) * sum(self.y))
        num = self.n * self.sum_xpow() - pow(self.sum_x(), 2)
        return den / num

    @property
    def B_0(self):
        return self.avg_y - self.B * self.avg_x

    def prediction_y(self, x_value):
        return self.B * x_value + self.B_0

    def __str__(self):
        return f"X {self.x}\nY: {self.y}\nN: {self.n}"



