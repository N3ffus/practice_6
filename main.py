"""
Практическая работа №6
Автор: Андрей Васильев
Вариант 5
"""
import random


def create_matrix():
    """
    Создает рандомную матрицу

    Returns:
        Матрица размером от 5x5 до 10x10, заполненная
        рандомными числами

    Examples:
        >>> create_matrix()
        [[185, 48, 190, 128, 16, 11],
        [214, 254, 170, 73, 219, 99],
        [210, 173, 90, 204, 148, 209],
        [189, 186, 173, 25, 84, 235],
        [224, 126, 43, 104, 25, 47]]
    """
    LEFT_BORDER = 5
    RIGHT_BORDER = 10

    rows = random.randint(LEFT_BORDER,RIGHT_BORDER)
    cols = random.randint(LEFT_BORDER,RIGHT_BORDER)
    
    matrix = [[random.randint(0, 256) for i in range(cols)] for i in range(rows)]
    return matrix


def integral_view(image):
    """
    Переводит матрицу контрастности в
    интегральный вид

    Args:
        image: двумерный список изображения

    Returns:
        Матрица в интегральном виде

    Examples:
        >>> integral_view([[185, 48, 190, 128, 16, 11],
        [214, 254, 170, 73, 219, 99],
        [210, 173, 90, 204, 148, 209],
        [189, 186, 173, 25, 84, 235],
        [224, 126, 43, 104, 25, 47]])

        [[185, 233, 423, 551, 567, 578],
        [399, 701, 1061, 1262, 1497, 1607],
        [609, 1084, 1534, 1939, 2322, 2641],
        [798, 1459, 2082, 2512, 2979, 3533],
        [1022, 1809, 2475, 3009, 3501, 4102]]
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

    Args:
        image: двумерный список изображения
        x1: начальная координата по x
        y1: начальная координата по y
        x2: конечная координата по x
        y2: конечная координата по y

    Returns:
        Сумма внутри прямоугольника

    Examples:
        >>> rect_sum([[185, 48, 190, 128, 16, 11],
        [214, 254, 170, 73, 219, 99],
        [210, 173, 90, 204, 148, 209],
        [189, 186, 173, 25, 84, 235],
        [224, 126, 43, 104, 25, 47]], 1, 1, 2, 2)

        687
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


