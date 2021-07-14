#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Created on 12.07.2021 9:47:23

import re,sys,os

def greet():
    print("-------------------\n  Приветсвуем вас   \n     в игре    \n "
          " крестики-нолики   \n-------------------")
    print(" \n формат ввода: x y \n x - номер строки  \n y - номер столбца ")
def greet_note():
    print(" формат ввода: x y \n x - номер строки  \n y - номер столбца ")



def draw_board():
    print(" =================")
    print("     0   1   2   ")
    print(" -----------------")
    for i, row in enumerate(board):
        print(f" {i} | {' | '.join(row)} |")
        if i != 2:
          print(" -----------------")
        else:print(" =================")

def ask():                                              #ФУНКЦИЯ ВВОДА ДАННЫХ
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2:
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()):       #ПРОВЕРКА ВВЕДЕНЫХ ДАННЫХ
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:            
            print(" Координаты вне диапазона! ")
            continue

        if board[x][y] != " ":
            print(" Клетка занята! ")
            continue

        return x, y

def check_win():                                        #ФУНКЦИЯ ПРОВЕРКИ ИГРОВОГО ПОЛЯ
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))) #СОЗДАЕМ КОРТЕЖ С ВЫИГРАШНЫМИ КОМБИНАЦИЯМИ
    for cord in win_cord:                               #ПРОВЕРКА НА СОВПАДЕНИЕ ВЫИГРАШНЫХ КОМБИНАЦИЙ И РАСПОЛОЖЕНИЕ ЗНАКОВ НА ДОСКЕ 
        symbols = []
        for c in cord:
            symbols.append(board[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False

                                               #ЗАПУСК ИГРЫ
greet()                                        #ПРИВЕТСТВИЕ                                   
board = [[" "] * 3 for i in range(3) ]         #ЗАДАЕМ ПОЛЕ
count = 0
while True:                                    #СЧИТАЕМ И КОНТРОЛИРУЕМ ХОД ИГРЫ
    count += 1
    draw_board()
    if count % 2 == 1:
        print("\n Ходит крестик!")
        greet_note()
    else:
        print("\n Ходит нолик!")
        greet_note()
    x, y = ask()

    if count % 2 == 1:
        board[x][y] = "X"
    else:
        board[x][y] = "0"

    if check_win():
        break

    if count == 9:
        print(" Ничья!")
        break
#END