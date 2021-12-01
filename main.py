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
    

