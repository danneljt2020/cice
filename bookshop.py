# https://github.com/vgenov-py/t603/blob/master/ex4.md
import json

# Opening JSON file data books
file = open('data.json', )

# returns JSON object as a dictionary
DB = json.load(file)

genre = ["Narrativa extranjera", "Divulgación científica", "Narativa policíaca", "Ciencia ficción", "Autoayuda"]


# Verify if exist book , return the index book if exist
def existBook(id_book):
    flag = None
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            flag = key
    return flag


# find books by key,value in the dictionary
def findByKeyValue(key, value):
    respond = []
    for book in DB:
        if book[key].lower() == value.lower():
            respond.append(book)
    return respond


# delete book by ID
def deleteBookById(id):
    msg = "El libro con ID :" + id + " no se encuentra en la Base de Datos!"
    index_book = existBook(id)
    if index_book:
        DB.pop(index_book)
        msg = "El libro ha sido eliminado satisfactoriamente."
    return msg


# update book by ID, key value
def updateBook(id_book, book_title, book_author, book_gender):
    msg = "Fails"
    for key, book in enumerate(DB):
        if book["id"].lower() == id_book.lower():
            DB[key]['title'] = book_title
            DB[key]['author'] = book_author
            DB[key]['genre'] = book_gender
            msg = "El libro ha sido modificado satisfactoriamente."
    return msg

# add new book
def addBook(id_book, book_title, book_author, book_gender):
    msg = "Existe un libro con el mismo ID."
    if not existBook(id_book):
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
def searchBook(selected_option):
    if selected_option == "1":
        id = input("ID: ")
        respond = findByKeyValue("id", id)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "2":
        title = input("Titulo: ")
        respond = findByKeyValue("title", title)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "3":
        autor = input("Autor: ")
        respond = findByKeyValue("autor", autor)
        print("Resultado de la Busqueda:", respond)
    if selected_option == "4":
        print("Seleccione el Genero:")
        # show the gender list to select
        for key, value in enumerate(genre):
            print(key, value)
        gender_option = int(input("genero: "))
        if gender_option >= 0 and gender_option <= len(genre) - 1:
            respond = findByKeyValue("genre", genre[gender_option])
            print("Resultado de la Busqueda:", respond)
        else:
            print("Ha seleccionado una opcion no valida! Pongase los ESPEJUELOS!")



