# D4.11


#### Список роутов:
+ admin/ - панель администратора;
+ index/ - таблица книг в билиотеке(добавлен вывод издалтсва книги);
+ books/ и authors/ - вывод всех книг и авторов библиотеки;
+ publishers/ - вывод списка издательств и их книг;


#### Bootstrap:
Подключен при помощи билиотеки django-bootstrap4, ознакомиться с ней можно [тут.](https://django-bootstrap4.readthedocs.io/en/latest/index.html)


#### Таблица данных новой модели Publisher:
| Издательства | Список книг |
|:------------:|:----------------------------------------------------------------------------------------:|
| Феникс       | Медный всадник, Граф Нулин, The Hitchhiker's Guide to the Galaxy, The Catcher in the Rye |
| Фламинго     | Руслан и Людмила, Новь, So Long, and Thanks for All the Fish                             |
| Ласточка     | The Growth of the Soil, Ревизор                                                          |


#### Для проверки задания:
1. Стянуть репозиторий к себе;
2. Установить зависимости из requirements.txt:
```
    pip install -r requirements.txt
```
3. Запустить сервер:
```
    cd 'my_library'
    python manage.py runserver
```
4. Перейти по данному урлу:
```
    publishers/
```
