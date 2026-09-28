
#  🎈Лабораторная работа №1: Знакомство с Git и Python

Добро пожаловать в мой первый учебный репозиторий! Здесь представлены результаты выполнения лабораторной работы по настройке рабочей среды разработки, освоению системы контроля версий **Git** и написанию первого скрипта на **Python**.

##  ⚙️ Что было сделано

-   [x] **Настроен Git и GitHub:** зарегистрирован аккаунт и создан первый удаленный репозиторий.

-   [x] **Установлен и настроен Python:** проверена работоспособность интерпретатора и окружения.
    
-   [x] **Настроена рабочая среда (VS Code):** установлены и сфигурированы расширения для комфортной разработки на Python и работы с Git.
    
-   [x] **Изучен синтаксис Markdown:** оформлена документация проекта в файле `README.md`.
    

## 💻 Пример кода на Python

В ходе лабораторной работы был написан скрипт, выполняющий построение и вывод треугольника Паскаля:

```python
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

```

## 🚀 Запуск скрипта

Если вы хотите запустить проект локально:

1.  Склонируйте репозиторий:
    
    ```powershell
    git clone https://github.com/MaxStep07/AU_software_development_task_0.git
    
    ```
    
2.  Перейдите в папку проекта:
    
    ```powershell
    cd AU_software_development_task_0
    
    ```
    
3.  Запустите скрипт:
    
    ```powershell
    python main.py
    
    ```
