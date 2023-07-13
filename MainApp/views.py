from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
author = {
            "name": "Иван",
            "middle": "Петрович",
            "surname": "Иванов",
            "phone": "8-923-600-01-02",
            "email": "vasya@mail.ru"
}
my_name = "Серебренников А.А."
head = "Изучаем django"
row = "Автор"

items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def home(request):
    text = f"""<h1>{head}</h1>
              <strong>{row}</strong>: <i>{my_name}</i>"""
    return HttpResponse(text)

def about(request):
    result = f"""Имя : <b>{author["name"]}</b><br> 
                Отчество : <b>{author["middle"]}</b><br>
                Фамилия : <b>{author["surname"]}</b><br> 
                телефон : <b>{author["phone"]}</b><br>
                email : <b>{author["email"]}</b><br>"""
    return HttpResponse(result)


# url /item/1
# url /item/2
# Списки, кортежи, строки - это индексы
# Словари - это ключи
def get_item(request, id):
    """ По указанному id функция возвращает имя и количество"""
    for item in items:
       if  item["id"] == id:
            print(item["name"], item["quantity"])
            result = f""" 
            <h2>Имя: {item["name"]} </h2>
            <p>Количество: {item["quantity"]} </p>
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'Item with id = {id} not found')
#<ol>
#   <li> .... </li>

def items_list(request):
    result = "<h2>Список товаров</h2><ol>"
    for item in items:
        result += f"<li>{item['name']}</li>"
    result += "</ol>"
    return HttpResponse(result)


