# https://github.com/vgenov-py/t603/blob/master/ex4.md
import json

# Opening JSON file data books
file = open('data.json', )

# returns JSON object as a dictionary
DB = json.load(file)

genre = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]


def pretty_book(books):
    for book in books:
        print("-".center(50, "-"))
        for k,v in book.items():
            print(f"{k}: {v}")


# Verify if exist book , return the index book if exist
def exist_book(id_book):
    flag = -1
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            flag = key
    return flag


# find books by key,value in the dictionary
def find_by_key_value(key, value):
    respond = []
    for book in DB:
        if book[key].lower() == value.lower():
            respond.append(book)
    return respond


# delete book by ID
def delete_book_by_id(id):
    msg = "El libro con ID :" + id + " no se encuentra en la Base de Datos!"
    index_book = exist_book(id)
    if index_book >= 0:
        DB.pop(index_book)
        msg = "El libro ha sido eliminado satisfactoriamente."
    return msg


# update book by ID, key value
def update_book(id_book, book_title, book_author, book_gender):
    msg = "Fails"
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            DB[key]['title'] = book_title
            DB[key]['author'] = book_author
            DB[key]['genre'] = book_gender
            msg = "El libro ha sido modificado satisfactoriamente."
    return msg


# add new book
def add_book(id_book, book_title, book_author, book_gender):
    msg = "Existe un libro con el mismo ID."
    if exist_book(id_book) == -1:
        new_book = {
            "id": id_book,
            "title": book_title,
            "author": book_author,
            "genre": book_gender
        }
        DB.append(new_book)
        msg = "El libro ha sido adicionado satisfactoriamente."
    return msg


# Search Book
def search_book(selected_option):
    respond = []
    if selected_option == "1":
        id_book = input("ID: ")
        respond = find_by_key_value("id", id_book)
    if selected_option == "2":
        title = input("Titulo: ")
        respond = find_by_key_value("title", title)
    if selected_option == "3":
        autor = input("Autor: ")
        respond = find_by_key_value("autor", autor)
    if selected_option == "4":
        print("Seleccione el Genero:")
        # show the gender list to select
        for key, value in enumerate(genre):
            print(key, value)
        gender_option = int(input("genero: "))
        if gender_option >= 0 and gender_option <= len(genre) - 1:
            respond = find_by_key_value("genre", genre[gender_option])
        else:
            print("Ha seleccionado una opcion no valida! Pongase los ESPEJUELOS!")

    if len(respond) > 0:
        print("-".center(50, "-"))
        print("Resultado de la Busqueda:")
        pretty_book(respond)
    else:
        print("No se han encontrado resultados para el parametro introducido")




