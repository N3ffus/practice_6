"""
Практическая работа №4
Автор: Андрей Васильев
Вариант 5
"""
import random


def create_matrix():
    """
    Создает матрицу
    """
    LEFT_BORDER = 5
    RIGHT_BORDER = 10

    rows = random.randint(LEFT_BORDER,RIGHT_BORDER)
    cols = random.randint(LEFT_BORDER,RIGHT_BORDER)
    
    matrix = [[random.randint(0,256) for i in range(cols)] for i in range(rows)]
    return matrix


def integral_view(image):
    """
    Переводит матрицу контрастности в
    интегральный вид
    """
    rows = len(image)
    cols = len(image[0])
    integral_matrix = [[0]*cols for i in range(rows)]
    
    for x in range(rows):
        for y in range(cols):
            integral_matrix[x][y] = image[x][y]
            
            if x > 0:
                if y > 0:
                    integral_matrix[x][y] -= integral_matrix[x-1][y-1]
                integral_matrix[x][y] += integral_matrix[x-1][y]
            if y > 0:
                integral_matrix[x][y] += integral_matrix[x][y-1]
    
    return integral_matrix
    

def rect_sum(image, x1, y1, x2, y2):
    """
    Считает сумму внутри прямоугольника
    """
    integral_matrix = integral_view(image)

    if x1 > 0 and y1 > 0:
        sum_a = integral_matrix[x1-1][y1-1]
    else:
        sum_a = 0
    
    if x1 > 0:
        sum_b = integral_matrix[x1-1][y2]

    if x2 > 0 and y2 > 0:
        sum_c = integral_matrix[x2][y2]
    
    if y1 > 0:
        sum_d = integral_matrix[x2][y1-1]
    
    summa = sum_a + sum_c - sum_b - sum_d
    return summa


