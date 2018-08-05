#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
import random
database = [
    {"question": "Что есть в маминой сумке?", "answer1": "Деньги", "answer2": "Телефон", "answer3": "Салфетки", "answer4": "Деньги и телефон", "correct": 4, "audio": "01.wav"},
    {"question": "Что есть у черепахи?", "answer1": "Ракушка", "answer2": "Ниндзя", "answer3": "Меч", "answer4": "Тело и Домик", "correct": 4, "audio": "02.wav"},
    {"question": "Что есть внутри часов?", "answer1": "Стрелки", "answer2": "Цифры", "answer3": "Шестеренки", "answer4": "Время", "correct": 3, "audio": "03.wav"},
    {"question": "Что есть в носке?", "answer1": "Ноги", "answer2": "Пальцы и Ноги", "answer3": "Дырка", "answer4": "Пальцы", "correct": 2, "audio": "04.wav"},
    {"question": "Что есть в папиной сумке?", "answer1": "Денюшки", "answer2": "Бумажки", "answer3": "Телефон и денюшки", "answer4": "Телефон", "correct": 3, "audio": "05.wav"},
    {"question": "Что есть в сотке?", "answer1": "Мультики", "answer2": "Игры", "answer3": "Музыка", "answer4": "Диск", "correct": 2, "audio": "06.wav"},
    {"question": "Что есть в пылесосе?", "answer1": "Мусор", "answer2": "Лего", "answer3": "Пыль", "answer4": "Монетки", "correct": 3, "audio": "07.wav"},
    {"question": "Что есть на столе?", "answer1": "Мусор", "answer2": "Еда", "answer3": "Тарелки", "answer4": "Чай", "correct": 2, "audio": "08.wav"},
    {"question": "Что есть под домом?", "answer1": "Крыша", "answer2": "Домик", "answer3": "Парковка", "answer4": "Люди", "correct": 4, "audio": "09.wav"},
    {"question": "Что есть под крышей?", "answer1": "Армашка", "answer2": "Чердак", "answer3": "Дом", "answer4": "Антенна", "correct": 1, "audio": "10.wav"},
    {"question": "Что есть во дворе?", "answer1": "Машины", "answer2": "Люди", "answer3": "Качельки и горки", "answer4": "Площадка", "correct": 4, "audio": "11.wav"},
    {"question": "Что есть у Аскара?", "answer1": "Своя машинка", "answer2": "Самолетик", "answer3": "Сок", "answer4": "Мама", "correct": 2, "audio": "12.wav"},
    {"question": "Что есть у Армана?", "answer1": "Свой танк", "answer2": "Садик", "answer3": "Своя база", "answer4": "Машинки", "correct": 3, "audio": "13.wav"},
    {"question": "Что есть в машине?", "answer1": "Двигатель", "answer2": "Мама и папа", "answer3": "Фары", "answer4": "Руль", "correct": 4, "audio": "14.wav"},
    {"question": "Что есть на улице?", "answer1": "Машины", "answer2": "Домики", "answer3": "Песок", "answer4": "Качели", "correct": 2, "audio": "15.wav"},
    {"question": "Что есть у Ерсина?", "answer1": "Свои домик", "answer2": "Пистолет", "answer3": "Игрушки", "answer4": "Самолетик", "correct": 1, "audio": "16.wav"},
    {"question": "Что есть у Аташки?", "answer1": "Инструменты", "answer2": "Машина", "answer3": "Свои игрушки", "answer4": "Телевизор", "correct": 3, "audio": "17.wav"},
    {"question": "Что есть у Апашки?", "answer1": "Аташка", "answer2": "Телефон", "answer3": "Аже", "answer4": "Кухня", "correct": 1, "audio": "18.wav"},
    {"question": "Что есть в садике?", "answer1": "Дети", "answer2": "Машинки", "answer3": "Апайки", "answer4": "Карандаши", "correct": 3, "audio": "19.wav"},
    {"question": "Что есть у Мамы?", "answer1": "Платье", "answer2": "Папа", "answer3": "Аскарик", "answer4": "Своя комната", "correct": 2, "audio": "20.wav"},
    {"question": "Что любит делать Арман?", "answer1": "Играть", "answer2": "Кушать конфеты", "answer3": "Играть компьютер", "answer4": "Плакать", "correct": 3, "audio": "21.wav"},
    {"question": "Что любит делать Аскар?", "answer1": "Есть торт", "answer2": "Мама-Нан", "answer3": "Играть", "answer4": "Компьютер", "correct": 3, "audio": "22.wav"},
    {"question": "Что есть у Даны?", "answer1": "Ляля", "answer2": "Работа", "answer3": "Ербол ага", "answer4": "Сотка", "correct": 3, "audio": "23.wav"},
    {"question": "Что есть на комьютере?", "answer1": "Видео", "answer2": "Игры", "answer3": "Ютюб", "answer4": "Мультики", "correct": 2, "audio": "24.wav"},
    {"question": "Что есть на телефоне?", "answer1": "Чехол", "answer2": "Фотографии", "answer3": "Мультики", "answer4": "Игры", "correct": 4, "audio": "25.wav"},
    {"question": "Что есть в розетке?", "answer1": "Ток", "answer2": "Напряжение", "answer3": "Две дырки", "answer4": "Провода", "correct": 1, "audio": "26.wav"},
    {"question": "Что есть в лампочке?", "answer1": "Свет", "answer2": "Электричество", "answer3": "Стекло", "answer4": "Лампочка", "correct": 4, "audio": "27.wav"},
    {"question": "Что есть в кармане?", "answer1": "Дырка", "answer2": "Машинки", "answer3": "Деньги", "answer4": "Танк", "correct": 2, "audio": "28.wav"},
    {"question": "Что есть в Автобусе?", "answer1": "Люди", "answer2": "Руль", "answer3": "Окна", "answer4": "Подушка", "correct": 1, "audio": "29.wav"},
    {"question": "Что есть на кухне?", "answer1": "Телевизор", "answer2": "Стол", "answer3": "Стул", "answer4": "Сут", "correct": 2, "audio": "30.wav"},
    {"question": "Что есть у Аташки дома?", "answer1": "Пылесос", "answer2": "Аташка", "answer3": "Апашка", "answer4": "Инструменты", "correct": 3, "audio": "31.wav"},
    {"question": "Что есть в детской и спальне?", "answer1": "Игрушки и шторы", "answer2": "Кровать и игрушки", "answer3": "Кровать и шкафчик", "answer4": "Стол и стулья", "correct": 2, "audio": "32.wav"},
    {"question": "Что есть в ауле?", "answer1": "Асыл", "answer2": "Ерсин", "answer3": "Айша", "answer4": "Апуля и Луиза", "correct": 2, "audio": "33.wav"},
    {"question": "Что есть на солнце?", "answer1": "Планеты", "answer2": "Огонь", "answer3": "Лава", "answer4": "Солнце", "correct": 4, "audio": "34.wav"},
    {"question": "Что есть на луне?", "answer1": "Дырки", "answer2": "Свет", "answer3": "Ямы", "answer4": "Космос", "correct": 3, "audio": "35.wav"},
    {"question": "Что есть в пакете?", "answer1": "Масло", "answer2": "Хлеб", "answer3": "Продукты", "answer4": "Игрушки", "correct": 4, "audio": "36.wav"},
    {"question": "Что есть на стульчике?", "answer1": "Сидушка", "answer2": "Игрушка", "answer3": "Арман", "answer4": "Спинка", "correct": 3, "audio": "37.wav"},
    {"question": "Что есть на стене?", "answer1": "Микроб", "answer2": "Рисунок", "answer3": "Часы", "answer4": "Розетка", "correct": 1, "audio": "38.wav"},
    {"question": "Что есть в самолете?", "answer1": "Окна", "answer2": "Крылья", "answer3": "Пассажиры", "answer4": "Двигатели", "correct": 3, "audio": "39.wav"},
    {"question": "Что есть на дороге?", "answer1": "Полиция", "answer2": "Знаки", "answer3": "Машины", "answer4": "Палочки", "correct": 3, "audio": "40.wav"},
    {"question": "Что есть на деревьях?", "answer1": "Яблочки", "answer2": "Листочки", "answer3": "Белки", "answer4": "Бананы", "correct": 2, "audio": "41.wav"},
    {"question": "Что есть в Шымкенте?", "answer1": "Люди", "answer2": "Игрушки", "answer3": "Ауыл", "answer4": "Ерсин", "correct": 1, "audio": "42.wav"},
    {"question": "Что есть в голове?", "answer1": "Глазки", "answer2": "Волосы", "answer3": "Ушки", "answer4": "Мозги", "correct": 4, "audio": "43.wav"},
    {"question": "Что есть во рту?", "answer1": "Зубы", "answer2": "Язык", "answer3": "Шоколад", "answer4": "Горло", "correct": 2, "audio": "44.wav"},
    {"question": "Что есть в шортах?", "answer1": "Дырки для ног", "answer2": "Пижама", "answer3": "Ноги", "answer4": "Писюлька", "correct": 4, "audio": "45.wav"},
    {"question": "Что есть на потолке?", "answer1": "Люстры", "answer2": "Лампочки", "answer3": "Люди", "answer4": "Шторы", "correct": 3, "audio": "46.wav"},
    {"question": "Что есть в маминой комнате?", "answer1": "Свет", "answer2": "Обед", "answer3": "Кровать", "answer4": "Книга", "correct": 2, "audio": "47.wav"},
    {"question": "Что есть в ванной?", "answer1": "Тазик", "answer2": "Щетка", "answer3": "Сабын", "answer4": "Стралка", "correct": 1, "audio": "48.wav"},
    {"question": "Что есть в жизни?", "answer1": "Поезд", "answer2": "Игры", "answer3": "Садик", "answer4": "Игры, компьютер", "correct": 4, "audio": "49.wav"},
    {"question": "Что есть в холодильнике?", "answer1": "Тортик", "answer2": "Еда", "answer3": "Биос", "answer4": "Май", "correct": 1, "audio": "50.wav"},
    {"question": "Что есть у танка?", "answer1": "Бронированная Башня", "answer2": "Мощный двигатель", "answer3": "Длинная пушка", "answer4": "Водитель", "correct": 3, "audio": "51.wav"},
    {"question": "Что есть на базе?", "answer1": "Машинки", "answer2": "Танки", "answer3": "Большой робот", "answer4": "Меч", "correct": 2, "audio": "52.wav"},
    {"question": "Что есть в майнкрафте?", "answer1": "Крипер", "answer2": "Железо", "answer3": "Дерево", "answer4": "Дом", "correct": 3, "audio": "53.wav"},
    {"question": "Что есть в магазине?", "answer1": "Продукты", "answer2": "Сок", "answer3": "Киндер", "answer4": "Пиченьки", "correct": 1, "audio": "54.wav"},
    {"question": "Что есть в ресторане?", "answer1": "Человеки", "answer2": "Кытыр-кытыр картошка", "answer3": "Пицца", "answer4": "Официант", "correct": 1, "audio": "55.wav"},
]

# Create your views here.
def index(request):

    return render(request, 'index.html', database[random.randint(0,len(database)-1)])

def special(request):
    d = {"question": "Кто прекрасней всех на свете?", "answer1": "Мама Армана и Аскара", "answer2": "Папа Армана и Аскара",
         "answer3": "Аташка Армана и Аскара", "answer4": "Нет правильного ответа", "correct": 1, "audio": "congrat.wav"}
    return render(request, 'index.html', d)