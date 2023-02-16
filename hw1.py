import data
import math


def vowel_count (word: str) -> str:
    num_of_vowels = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_list = [i for i in word]

    for k in range(len(vowels)):
        for idx in range(len(word_list)):
            if vowels[k] == word_list[idx]:
                num_of_vowels = num_of_vowels + 1
    return num_of_vowels


def short_lists (nested_list):
    newList = []
    for k in range(len(nested_list)):
        if len(nested_list[k]) == 2:
            newList.append(nested_list[k][0])
            newList.append(nested_list[k][1])
    return newList


def ascending_pairs(nested_list):
    newList = []
    for k in range(len(nested_list)):
        if len(nested_list[k]) == 2:
            if nested_list[k][0] > nested_list[k][1]:
                newList.append(nested_list[k][1])
                newList.append(nested_list[k][0])
            else:
                newList.append(nested_list[k][0])
                newList.append(nested_list[k][1])
        else:
            for j in range(len(nested_list[k])):
                newList.append(nested_list[k][j])

    return newList


def add_prices(first: data.Price, second: data.Price) -> data.Price:
    dollar = first.dollars + second.dollars
    cents = first.cents + second.cents
    if cents > 99:
        dollar = dollar + 1
        cents = cents - 100

    return data.Price(dollar, cents)


def rectangle_area(rect: data.Rectangle):
    length = 0
    height = 0
    area = 0
    if rect.top_left.x != rect.bottom_right.x:
        if rect.top_left.x <= 0 and rect.bottom_right.x <= 0:
            length = abs(rect.top_left.x - rect.bottom_right.x)
            print(length)
        elif rect.top_left.x >= 0 and rect.bottom_right.x >= 0:
            length = abs(rect.top_left.x - rect.bottom_right.x)
            print(length)
        elif rect.top_left.x <= 0 and rect.bottom_right.x >= 0:
            length = (rect.top_left.x * -1) + rect.bottom_right.x
            #  print(length)
        elif rect.top_left.x >= 0 and rect.bottom_right.x <= 0:
            length = rect.top_left.x + (rect.bottom_right.x * -1)
            # print(length)
    else:
        area = 0

    if rect.top_left.y != rect.bottom_right.y:
        if rect.top_left.y <= 0 and rect.bottom_right.y <= 0:
            height = abs(rect.top_left.y - rect.bottom_right.y)
        elif rect.top_left.y >= 0 and rect.bottom_right.y >= 0:
            height = abs(rect.top_left.y - rect.bottom_right.y)
        elif rect.top_left.y <= 0 and rect.bottom_right.y >= 0:
            height = (rect.top_left.y * -1) + rect.bottom_right.y
        elif rect.top_left.y >= 0 and rect.bottom_right.y <= 0:
            height = rect.top_left.y + (rect.bottom_right.y * -1)
    else:
        area = 0


    area = length*height
    return area

def books_by_author(name: str, books: list):
    book_list = []
    for k in range(len(books)):
        if books[k].authors == name:
            book_list.append(books[k].title)

    return book_list

def circle_bound(rect: data.Rectangle) -> data.Circle:
    center = (rect.top_left.x + rect.bottom_right.x)/2, (rect.top_left.y + rect.bottom_right.y)/2
    rx = (rect.bottom_right.x - rect.top_left.x)/2
    ry = (rect.top_left.y - rect.bottom_right.y)/2
    radius = math.sqrt(rx*rx + ry*ry)
    return data.Circle(center, radius)

def below_pay_average(emp:list[data.Employee])->list[str]:
    avgPay = sum([p.pay_rate for p in emp]) / len(emp)
    names = [p.name for p in emp if p.pay_rate < avgPay]
    return names

#test get
























