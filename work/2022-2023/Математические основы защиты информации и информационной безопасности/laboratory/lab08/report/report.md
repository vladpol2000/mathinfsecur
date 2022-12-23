---
# Front matter
lang: ru-RU
title: "Лабораторная работа 8"
subtitle: "Целочисленная арифметика многократной точности" 
author: "Пологов Владислав Александрович"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: false # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Serif
monofont: PT Serif
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы 

## Цель работы

Реализовать программно следующие алгоритмы:

    1. Сложение неотрицательных целых чисел;
    2. Вычитание неотрицательных целых чисел;
    3. Умножение неотрицательных целых чисел столбиком;
    4. Быстрый столбки;
    5. Деление многоразрядных целых чисел.


# Описание реализации

## Описание реализации

Для реализации алгоритмов использовались средства языка Python. 

# Реализация 

## Алгоритм, реализующий сложение неотрицательных целых чисел

На вход  будут подаваться два неотрицательных числа u и v разрядностью n с основанием системы счисления b. На выходе получим сумму w = w_0 w_1 w_2..., w_0 - цифра переноса, которая всегда равна 0 либо 1. Алгоритм представлен на рисунке 1. (рис. -@fig:001)
Код, реализующий данный алгоритм, представлен на рисунке 2. (рис. -@fig:002)

## Алгоритм, реализующий сложение неотрицательных целых чисел

![Алгоритм, реализующий сложение неотрицательных целых чисел](image/image1.png){ #fig:001 width=100% }


## Код, реализующий алгоритм сложения неотрицательных целых чисел

![Код, реализующий алгоритм сложения неотрицательных целых чисел](image/image2.png){ #fig:002 width=100% }


## Алгоритм, реализующий вычитание неотрицательных целых чисел

На вход  будут подаваться два неотрицательных числа u и v разрядностью n с основанием системы счисления b. На выходе получим разность w = w_0 w_1 w_2... = u - v. Алгоритм представлен на рисунке 3. (рис. -@fig:003)
Код, реализующий данный алгоритм, представлен на рисунке 4. (рис. -@fig:004)

## Алгоритм, реализующий вычитание неотрицательных целых чисел

![Алгоритм, реализующий вычитание неотрицательных целых чисел](image/image3.png){ #fig:003 width=100% }


## Код, реализующий алгоритм вычитания неотрицательных целых чисел

![Код, реализующий алгоритм вычитания неотрицательных целых чисел](image/image4.png){ #fig:004 width=100% }


## Алгоритм, реализующий умножение неотрицательных целых чисел столбиком

На вход  будут подаваться два неотрицательных числа u и v с основанием системы счисления b. На выходе получим произведение w = w_0 w_1 w_2... = u * v. Алгоритм представлен на рисунке 5. (рис. -@fig:005)
Код, реализующий данный алгоритм, представлен на рисунке 6. (рис. -@fig:006)

## Алгоритм, реализующий умножение неотрицательных целых чисел столбиком

![Алгоритм, реализующий умножение неотрицательных целых чисел](image/image5.png){ #fig:005 width=100% }


## Код, реализующий алгоритм умножения неотрицательных целых чисел столбиком

![Код, реализующий алгоритм умножения неотрицательных целых чисел](image/image6.png){ #fig:006 width=100% }


## Алгоритм быстрый столбик

На вход  будут подаваться два неотрицательных числа u и v с основанием системы счисления b. На выходе получим произведение w = w_0 w_1 w_2... = u * v. Алгоритм представлен на рисунке 7. (рис. -@fig:007)
Код, реализующий данный алгоритм, представлен на рисунке 8. (рис. -@fig:008)

## Алгоритм быстрый столбик

![Алгоритм, реализующий метод умножения "быстрый столбик"](image/image7.png){ #fig:007 width=100% }


## Код, реализующий алгоритм быстрый столбик

![Код, реализующий алгоритм быстрый столбик](image/image8.png){ #fig:008 width=100% }


## Алгоритм деления многоразрядных целых чисел

На вход  будут подаваться два неотрицательных числа u и v разрядностью n и t соответственно. На выходе получим частное q и остаток r. Алгоритм представлен на рисунке 9. (рис. -@fig:009)
Код, реализующий данный алгоритм, представлен на рисунке 10. (рис. -@fig:010)

## Алгоритм деления многоразрядных целых чисел

![Алгоритм, реализующий алгоритм деления многоразрядных целых чисел](image/image9.png){ #fig:009 width=100% }


## Код, реализующий алгоритм деления многоразрядных целых чисел

![Код, реализующий алгоритм деления многоразрядных целых чисел](image/image10.png){ #fig:010 width=100% }


# Вывод 

* Реализованы следующие алгоритмы:
    1. Сложение неотрицательных целых чисел;
    2. Вычитание неотрицательных целых чисел;
    3. Умножение неотрицательных целых чисел столбиком;
    4. Быстрый столбки;
    5. Деление многоразрядных целых чисел.