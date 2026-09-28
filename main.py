def print_pascal_triangle(triangle):
    '''
    Выводит треугольник Паскаля
    '''
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))
        
        
def pascal_triangle(rows):
    '''
    Генерирует строки треугольника Паскаля
    '''
    triangle = []
    
    for i in range(rows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    
    return triangle
        
triangle_of_Pascal = pascal_triangle(10)
print_pascal_triangle(triangle_of_Pascal)
