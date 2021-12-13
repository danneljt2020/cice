from stadistics import Stadistics
from covid_api import *
import matplotlib.pyplot as plt


# get Y value from data json
def get_y2(analize_obj):
    result = []
    # print(len(data['2020/12/09']))
    for val in analize_obj.x:
        result.append(analize_obj.prediction_y(val))
    return result


x = [num for num in range(1, len(get_data_by_date()) + 1)]
y = []

for zone in get_data_by_date().values():
    y.append(sum(z['casos_confirmados_totales'] for z in zone))
y.reverse()

analize_1_obj = Stadistics(x, y)

plt.plot(x, y, label="Casos Totales", color="r")
plt.plot(x, get_y2(analize_1_obj), label="Prediccion", linestyle='dashed')
plt.xlabel("Semanas")
plt.ylabel("Casos Acumulados")
plt.legend()
plt.show()
