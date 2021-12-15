from stadistics import Stadistics
from covid_api import *
from datetime import datetime, timedelta
import math
import matplotlib.pyplot as plt


# get Y value from data json
def get_y2(analize_obj):
    result = []
    # print(len(data['2020/12/09']))
    for val in analize_obj.x:
        result.append(analize_obj.prediction_y(val))
    return result


# Prediction function!
def prediction_cases(std_object, last_date, future_date):
    date_fut = datetime.strptime(future_date, '%Y/%m/%d')
    delta = date_fut - last_date  # diff between dates
    y_days = len(std_object.x) + delta.days / 7
    return std_object.prediction_y(y_days)


# x = [num for num in range(1, len(get_data_by_date()) + 1)]


# basic casos_confirmados_totales
def pretiction_casos_confirmados_totales_Y():
    y = []
    for zone in get_data_by_date().values():
        y.append(sum(z['casos_confirmados_totales'] for z in zone))
    y.reverse()
    return y


# get tasa_incidencia_acumulada_activos_ultimos_14dias by date
def tasa_incidencia_acumulada_Y(date_analize):
    y = []
    for zone in get_data_by_date().values():
        inform_date = datetime.strptime(zone[0]['fecha_informe'], '%Y/%m/%d %H:%M:%S')

        if inform_date.strftime('%Y/%m/%d') == date_analize:
            y = ([z['tasa_incidencia_acumulada_ultimos_14dias'] for z in zone])

    y.reverse()
    return y


def ec_student(std_1, std_2):
    num = std_1.avg_y - std_2.avg_y
    den_part_1 = (std_1.n - 1) * std_1.quasi_variance_y + (std_2.n - 1) * std_2.quasi_variance_y
    den_part_2 = std_1.n + std_2.n - 2
    den_fin = den_part_1 / den_part_2
    den_squart = den_fin * (1 / std_1.n + 1 / std_2.n)
    return num / math.sqrt(den_squart)


y_now_dic = tasa_incidencia_acumulada_Y("2021/12/14")
y_past_dic = tasa_incidencia_acumulada_Y("2020/12/15")

x_new = [num for num in range(0, len(y_past_dic))]

analice_now_dic = Stadistics(x_new, y_now_dic)
analice_past_dic = Stadistics(x_new, y_past_dic)


# ESTA OK
print(ec_student(analice_now_dic, analice_past_dic))

# TODO Analisis y grafica de casos_confirmados_totales
# analize_1_obj = Stadistics(x, pretiction_casos_confirmados_totales_Y())
# plt.plot(x, pretiction_casos_confirmados_totales_Y(), label="Casos Totales", color="r")
# plt.plot(x, get_y2(analize_1_obj), label="Prediccion", linestyle='dashed')
# plt.xlabel("Semanas")
# plt.ylabel("Casos Acumulados")
# plt.legend()
# plt.show()
