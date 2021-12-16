from time import perf_counter
import datetime as dt
import random


def hello_decorator(func):
    def inner1(*args, **kwargs):
        returned_value = func(*args, **kwargs)
        return returned_value + "!"

    return inner1


# adding decorator to the function
@hello_decorator
def f_hello(name):
    return name


# print(f_hello("dannel"))


# Crear un decorador log que imprima por pantalla el nombre de la
# función que se haya ejecutado y también la hora de su ejecución

def write_log(funct_name, runtime):
    str_w = " Funcion "+funct_name+" Ejecutada el |" + str(dt.datetime.now().date())+" tiempo de ejecucion " + str(runtime)
    file = open("log.txt", "a")
    file.write(str_w+"\n")
    file.close()


def timer_count(func):
    def wrapper_timer(*args, **kwargs):
        start_time = perf_counter()
        value = func(*args, **kwargs)
        end_time = perf_counter()
        run_time = end_time - start_time
        # print("La funcion se ha ejecutado", dt.datetime.now().date())
        # print(f"Finalizo {func.__name__!r} en {run_time:.5f} segundos")
        write_log(func.__name__, run_time)
        return value

    return wrapper_timer


@timer_count
def sum_all_f_complex(num_times):
    sum_all = 0
    for n in range(0, num_times):
        r1 = random.randint(0, num_times)
        sum_all += n - r1
        for xn in range(0, n):
            sum_all += xn
    return sum_all


sum_all_f_complex(1000)
