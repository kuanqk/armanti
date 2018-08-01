#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
import random
database = [
    {"question": "Что есть в маминой сумке?", "answer1": "Ножницы", "answer2": "Телефон", "answer3": "Салфетки", "answer4": "Компьютер", "correct": 3, "audio": "audio11.wav"},
    {"question": "Что есть у черепахи?", "answer1": "Ракушка", "answer2": "Ниндзя", "answer3": "Меч", "answer4": "Глобус", "correct": 1, "audio": "turtle.wav"},
    {"question": "Что есть внутри часов?", "answer1": "Стрелки", "answer2": "Цифры", "answer3": "Картинка", "answer4": "Время", "correct": 4, "audio": "clock.wav"},
    {"question": "Что есть в носке?", "answer1": "Ноги", "answer2": "Мусор", "answer3": "Дырка", "answer4": "Пальцы", "correct": 3, "audio": "socks.wav"},
    {"question": "Что есть в папином рюкзаке?", "answer1": "Мышка", "answer2": "Бумажки", "answer3": "Документы", "answer4": "Телефон", "correct": 1, "audio": "rucksack.wav"},
    {"question": "Что есть в плэйстейшне?", "answer1": "Мультики", "answer2": "Игры", "answer3": "Музыка", "answer4": "Диск", "correct": 4, "audio": "playstation.wav"},
    {"question": "Что есть в пылесосе?", "answer1": "Пауки", "answer2": "Лего", "answer3": "Хотвилс", "answer4": "Монетки", "correct": 1, "audio": "pylesos.wav"},
    {"question": "Что есть на столе?", "answer1": "Мусор", "answer2": "Еда", "answer3": "Тарелки", "answer4": "Чай", "correct": 2, "audio": "table.wav"},
    {"question": "Что есть под домом?", "answer1": "Крыша", "answer2": "Норка", "answer3": "Парковка", "answer4": "Земля", "correct": 1, "audio": "house.wav"},
    {"question": "Что есть под крышей?", "answer1": "Чердак", "answer2": "Мыши", "answer3": "Дом", "answer4": "Антенна", "correct": 4, "audio": "roof.wav"},
    {"question": "Что есть во дворе?", "answer1": "Холод", "answer2": "Люди", "answer3": "Качельки и горки", "answer4": "Машины", "correct": 3, "audio": "yard.wav"},
    {"question": "Что есть у Куаныша?", "answer1": "Свой телефон", "answer2": "Школьный рюкзак", "answer3": "Сок", "answer4": "Хотвилс", "correct": 2, "audio": "Kuanysh.wav"},
    {"question": "Что есть у Данияра?", "answer1": "Свой телефон", "answer2": "Школа", "answer3": "Сок", "answer4": "Часы", "correct": 2, "audio": "Dadik.wav"},
    {"question": "Что есть в машине?", "answer1": "Двигатель", "answer2": "Мама и папа", "answer3": "Фары", "answer4": "Водитель", "correct": 1, "audio": "car.wav"},
    {"question": "Что есть на улице?", "answer1": "Машины", "answer2": "Алтын Булак", "answer3": "Снег", "answer4": "Качели", "correct": 3, "audio": "street.wav"},
    {"question": "Что есть у Хайдара?", "answer1": "Дырокол", "answer2": "Пистолет", "answer3": "Игрушки", "answer4": "Палатка", "correct": 1, "audio": "Khaidar.wav"},
    {"question": "Что есть у Амины?", "answer1": "Куклы", "answer2": "Часы", "answer3": "Заколка", "answer4": "Волосы", "correct": 2, "audio": "Amina.wav"},
    {"question": "Что есть у Али?", "answer1": "Субару", "answer2": "Телефон", "answer3": "Школа", "answer4": "Рубашка", "correct": 3, "audio": "Ali.wav"},
    {"question": "Что есть у Адильки?", "answer1": "Фломастеры", "answer2": "Машинки", "answer3": "Калейдоскоп", "answer4": "Карандаши", "correct": 3, "audio": "Adil.wav"},
    {"question": "Что есть у Айшонки?", "answer1": "Платье", "answer2": "Куклы", "answer3": "Адилька", "answer4": "Заколка", "correct": 1, "audio": "Aisha.wav"},
    {"question": "Сколько раз отжимается Данияр?", "answer1": "12", "answer2": "5", "answer3": "8", "answer4": "10", "correct": 4, "audio": "sport.wav"},
    {"question": "Что есть у Сауле тате?", "answer1": "Торт", "answer2": "Манты", "answer3": "Субару", "answer4": "Компьютер", "correct": 3, "audio": "Sauka.wav"},
    {"question": "Что есть на комьютере?", "answer1": "Видео", "answer2": "Игры", "answer3": "Ютюб", "answer4": "Работа", "correct": 1, "audio": "computer.wav"},
    {"question": "Что есть на телефоне?", "answer1": "Чехол", "answer2": "Фотографии", "answer3": "Мультики", "answer4": "Игры", "correct": 4, "audio": "phones.wav"},
    {"question": "Что есть в розетке?", "answer1": "Ток", "answer2": "Напряжение", "answer3": "Две дырки", "answer4": "Провода", "correct": 1, "audio": "outlet.wav"},
    {"question": "Что есть в лампочке?", "answer1": "Свет", "answer2": "Электричество", "answer3": "Стекло", "answer4": "Солнце", "correct": 2, "audio": "lightbulb.wav"},
    {"question": "Что есть в кармане?", "answer1": "Дырка", "answer2": "Телефон", "answer3": "Деньги", "answer4": "Ключи", "correct": 4, "audio": "pocket.wav"},
    {"question": "Что есть в Мазде?", "answer1": "Турбо", "answer2": "Руль", "answer3": "Окна", "answer4": "Подушка", "correct": 1, "audio": "mazda.wav"},
    {"question": "Что есть в Хонде?", "answer1": "Сиденья", "answer2": "Руль", "answer3": "Бампер", "answer4": "Двери", "correct": 3, "audio": "honda.wav"},
    {"question": "Что есть в Школе?", "answer1": "Часы", "answer2": "Уроки", "answer3": "Тетради", "answer4": "Учительница", "correct": 1, "audio": "school.wav"},
    {"question": "Что есть в детской и спальне?", "answer1": "Столы", "answer2": "Кабинет", "answer3": "Кровать", "answer4": "Кресло", "correct": 2, "audio": "kidsroom.wav"},
    {"question": "Что есть в ауле?", "answer1": "Горки", "answer2": "Арлан", "answer3": "Двор", "answer4": "Телевизор", "correct": 4, "audio": "aul.wav"},
    {"question": "Что есть на солнце?", "answer1": "Планеты", "answer2": "Огонь", "answer3": "Желе", "answer4": "Планеты", "correct": 2, "audio": "sun.wav"},
    {"question": "Что есть на луне?", "answer1": "Дырки", "answer2": "Свет", "answer3": "Желе", "answer4": "Космос", "correct": 1, "audio": "moon.wav"},
    {"question": "Что есть в пакете?", "answer1": "Масло", "answer2": "Хлеб", "answer3": "Продукты", "answer4": "Еще пакеты", "correct": 3, "audio": "bag.wav"},
    {"question": "Что есть на стульчике?", "answer1": "Сидушка", "answer2": "Игрушка", "answer3": "Дом", "answer4": "Батут", "correct": 1, "audio": "chair.wav"},
    {"question": "Что есть на стене?", "answer1": "Шкаф", "answer2": "Рисунок", "answer3": "Обои", "answer4": "Розетка", "correct": 4, "audio": "wall.wav"},
    {"question": "Что есть в самолете?", "answer1": "Окна", "answer2": "Крылья", "answer3": "Турбо двигатель", "answer4": "Телевизоры", "correct": 1, "audio": "airplane.wav"},
    {"question": "Что есть на дороге?", "answer1": "Полиция", "answer2": "Знаки", "answer3": "Машины", "answer4": "Палочки", "correct": 4, "audio": "road.wav"},
    {"question": "Что есть на деревьях?", "answer1": "Яблочки", "answer2": "Листики", "answer3": "Белки", "answer4": "Бананы", "correct": 1, "audio": "trees.wav"},
    {"question": "Что есть в Баку на 10 этаже?", "answer1": "Балкон", "answer2": "Игрушки", "answer3": "Пистолет", "answer4": "Палатка", "correct": 3, "audio": "Baku.wav"},
    {"question": "Что есть в носике?", "answer1": "Казюльки", "answer2": "Волосы", "answer3": "Насморк", "answer4": "Дырки", "correct": 1, "audio": "nose.wav"},
    {"question": "Что есть во рту?", "answer1": "Зубы", "answer2": "Язык", "answer3": "Шоколад", "answer4": "Горло", "correct": 2, "audio": "mouth.wav"},
    {"question": "Что есть в шортах?", "answer1": "Дырки для ног", "answer2": "Пижама", "answer3": "Ноги", "answer4": "Карман", "correct": 4, "audio": "short.wav"},
    {"question": "Что есть на потолке?", "answer1": "Люстры", "answer2": "Лампочки", "answer3": "Шарик", "answer4": "Шторы", "correct": 2, "audio": "potolok.wav"},
    {"question": "Что есть в лампочке?", "answer1": "Свет", "answer2": "Светодиоды", "answer3": "Батарейки", "answer4": "Кнопка", "correct": 3, "audio": "light2.wav"},
    {"question": "Что есть в жизни?", "answer1": "Поезд", "answer2": "Игры", "answer3": "Школа", "answer4": "Кнопка", "correct": 4, "audio": "life.wav"},
    {"question": "Что есть в ванной?", "answer1": "Кран", "answer2": "Раковина", "answer3": "Зеркало", "answer4": "Вода", "correct": 4, "audio": "bathroom.wav"},
]

# Create your views here.
def index(request):

    return render(request, 'index.html', database[random.randint(0,len(database)-1)])

def special(request):
    d = {"question": "Кто прекрасней всех на свете?", "answer1": "Мама Куаныша и Данияра", "answer2": "Папа Куаныша и Данияра",
         "answer3": "Кто живет на дне океана", "answer4": "Нет правильного ответа", "correct": 1, "audio": "congrat.mp3"}
    return render(request, 'index.html', d)