class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, new_width):
        self.width = new_width

    def set_height(self, new_height):
        self.height = new_height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.height > 50 or self.width > 50:
            return 'Too big for picture.'

        else:
            pic = ''
            for i in range(self.height):
                pic += f"{'*' * self.width}\n"

            return pic

    def get_amount_inside(self, shape):
        return self.get_area() // shape.get_area()

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def set_side(self, new_side):
        super().set_height(new_side)
        super().set_width(new_side)

    def __str__(self):
        return f'Square(side={self.width})'
