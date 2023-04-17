#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
            super().__init__(id)
            self.width = width
            self.height = height
            self.x = x
            self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError('width must be an integer')
            elif value <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError('height must be an integer')
            elif value <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError('x must be an integer')
            elif value < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError('y must be an integer')
            elif value < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = value

        def __str__(self):
                return "[Rectangle] ({}) {}/{} - {}/{}".format(
                        self.id, self.x, self.y, self.width, self.height)

        def area(self):
                return self.width * self.height

        def display(self):
                for i in range(self.y):
                        print()
                for i in range(self.height):
                        for j in range(self.x):
                                print(" ", end="")
                        for j in range(self.width):
                                print("#", end="")
                        print()

        def update(self, *args, **kwargs):
                if args:
                        for i, arg in enumerate(args):
                                if i == 0:
                                        self.width = arg
                                elif i == 1:
                                        self.height = arg
                                elif i == 2:
                                        self.x = arg
                                elif i == 3:
                                        self.y = arg
                elif kwargs:
                        for key, value in kwargs.items():
                                if key == "width":
                                        self.width = value
                                elif key == "height":
                                        self.height = value
                                elif key == "x":
                                        self.x = value
                                elif key == "y":
                                        self.y = value


        def update(self, *args):
                num_args = len(args)
                if num_args > 0:
                        self.id = args[0]
                if num_args > 1:
                        self.width = args[1]
                if num_args > 2:
                        self.height = args[2]
                if num_args > 3:
                        self.x = args[3]
                if num_args > 4:
                        self.y = args[4]

        def update(self, *args, **kwargs):
                num_args = len(args)
                if num_args == 0:
                        for key, value in kwargs.items():
                                setattr(self, key, value)
                else:
                        self.id = args[0]
                        if num_args > 1:
                                self.width = args[1]
                        if num_args > 2:
                                self.height = args[2]
                        if num_args > 3:
                                self.x = args[3]
                        if num_args > 4:
                                self.y = args[4]

        def to_dictionary(self):
                return {'id': self.id, 'width': self.width, 'height':
                        self.height, 'x': self.x, 'y': self.y}
