'''
Задание 2. Найдите корни квадратного уравнения
Ax² + Bx + C = 0 двумя способами:
1) с помощью математических формул нахождения 
корней квадратного уравнения;
2) с помощью дополнительных библиотек Python.
'''


from numpy import sqrt

from sympy import Eq, Symbol, solve


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


def get_input_values():
    print("Введите первый коэффициент квадратного уравнения")
    first_ratio = input()

    print("Введите второй коэффициент квадратного уравнения")
    second_ratio = input()

    print("Введите свобоный член квадратного уравнения")
    third_ratio = input()

    return first_ratio, second_ratio, third_ratio


def get_equation_solution(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant == 0:
        return [str(- b / (2 * a))]
    elif discriminant > 0:
        x1 = - b + sqrt(discriminant) / (2 * a)
        x2 = - b - sqrt(discriminant) / (2 * a)
        return list(map(str, [x1, x2]))


def get_equation_solution_sympy(a, b, c):
    x = Symbol('x')

    eq=Eq(a * x**2 + b * x + c, 0)

    return solve(eq)
        

def main():
    output_str = "Введены неверные значения чисел"
    input_values = get_input_values()

    if all(
        is_float(input_value) for input_value in input_values
        ):
        first_ratio, second_ratio, third_ratio = input_values

        equation_solutions_def = get_equation_solution(
            float(first_ratio),
            float(second_ratio),
            float(third_ratio)
        )

       
        equation_solutions_sympy = get_equation_solution_sympy(
                float(first_ratio),
                float(second_ratio),
                float(third_ratio)
            )

        if equation_solutions_def:
            output_str = (
                f"""Решения уравнения с помощью математических формул: 
                {", ".join(equation_solutions_def)}"""
            )
        else:
            output_str = "Уравнение не имеет решений"
        
        if equation_solutions_sympy:
            output_str = (
                f"""Решения уравнения с помощью доп. библиотек: 
                {", ".join(list(map(str, equation_solutions_sympy)))}"""
            )
        else:
            output_str = "Уравнение не имеет решений"

    print(output_str)


if __name__ == "__main__":
    main()
