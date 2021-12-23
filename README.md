## Aplicación de vuelos para la aerolina A.A.

### La aplicación permitirá:

1. Comprar modificar y cancelar vuelos
2. Indicar tiempo estimado de vuelo y hora de llegada en los usos horarios de origen y destino

### Para realizar esta actividad necesitaremos:

1. Módulo datetime
2. Una clase vuelo (Flight)
3. Un JSON para guardar los vuelos comprados
4. Un decorador para guardar los vuelos en el JSON

### Clase vuelo:

* origin: Airport_instance
* destination: Airport_instance
* departures_hours: list (**horarios de partida**)
* tiempo de vuelo: float
* ETA: method -> float (**Estimated Time of Arrival**)

### JSON

* Tendrá un identificador único
* Registrará las propiedades mencionadas en la clase Flight