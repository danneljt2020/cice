from stadistics import *
from covid_api import *


# print(get_data("covid.json")['data'])


# data_2 = Stadistics([1, 2, 3], [10, 20, 27])
# print(data_2.prediction_y(1))

print("TOTAL CONTAGIOS:", get_confirmed_by_month(12))
