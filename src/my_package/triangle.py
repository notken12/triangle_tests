def get_triangle_type(sides) -> str:
    a, b, c = sides
    if a <= 0 or b <= 0 or c <= 0:
        return 'invalid'
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return 'equilateral'
        if a == b or b == c or a == c:
            return 'isosceles'
        else:
            return 'scalene'
    else:
        return 'invalid'
