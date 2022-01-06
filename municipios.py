import collections


# Obtener municipio por código INE
def getMunicipioByCodeINE(data, ine):
    municipio = "Municipio no encontrado."
    for i, row in enumerate(data):
        if row[2] == ine:
            municipio = row
    return municipio


# Obtener el municipio más grande
def getMunicipioBig(data):
    big = []
    aux = 0
    for i, row in enumerate(data):
        if float(row[5]) > aux:
            big = row
            aux = float(row[5])
    return big


# Obtener superficie total
def getSuperficieTotal(data):
    superficie_total = 0
    for i, row in enumerate(data):
        superficie_total += float(row[5])
    return superficie_total


# Obtener densidad total
def getDensidadTotal(data):
    densidad_total = 0
    for i, row in enumerate(data):
        densidad_total += float(row[6])
    return densidad_total


# Obtener la población de Madrid superficie por densidad da poblacion
def getPoblacionMadrid(data):
    poblacion_total = 0
    for i, row in enumerate(data):
        poblacion_total += float(row[6]) * float(row[5])
    return poblacion_total


# Obtener la población media de los municipios
def getPoblacionMedia(data):
    return getPoblacionMadrid(data) / len(data)


# Ley de bendford
def verifyLeyBendford(data):
    # data = [11, 87,33,112,5,112,1186]
    results = []

    first_all_digits = list(map(lambda n: str(n)[0], data))  # get all frist digits
    first_digit_freq = collections.Counter(first_all_digits)  # count key value
    # print(first_digit_freq)

    for n in range(1, 10):
        frequency = first_digit_freq[str(n)]
        frequency_percent = frequency / len(data)  # percent
        results.append({"NUMERO": n,
                        "Aparece": round(frequency, 3),
                        "Porciento": round(frequency_percent, 3),
                        })

    return results
