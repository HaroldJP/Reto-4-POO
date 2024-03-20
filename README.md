# Reto-4-POO-🥵
 ## Punto 1
 Include the class exercise in the repo.

 ```python
import math

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.__start = Point(x1, y1)
        self.__end = Point(x2, y2)
        self.length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

class Shape:
    def __init__(self, *args):
        self.is_regular = args[0]
        self.vertice1 = Point(args[1], args[2])
        self.vertice2 = Point(args[3], args[4])
        self.vertice3 = Point(args[5], args[6])
        self.vertice4 = Point(args[7], args[8])
        self.edge1 = Line(args[9], args[10], args[11], args[12])
        self.edge2 = Line(args[13], args[14], args[15], args[16])
        self.edge3 = Line(args[17], args[18], args[19], args[20])
        self.edge4 = Line(args[21], args[22], args[23], args[24])
        self.angle1 = args[25]
        self.angle2 = args[26]
        self.angle3 = args[27]
        self.angle4 = args[28]
        self.width = args[29]
        self.height = args[30]

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass

    def compute_vertices(self):
        pass

class Rectangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)

    def compute_inner_angles(self):
        return [90, 90, 90, 90]
    
    def compute_vertices(self):
        return [self.vertice1.get_x(), self.vertice1.get_y()], [self.vertice2.get_x(), self.vertice2.get_y()], [self.vertice3.get_x(), self.vertice3.get_y()], [self.vertice4.get_x(), self.vertice4.get_y()]

    def initialization_rectangle():
        x = float(input("Enter the x coordinate for the rectangle's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the rectangle's bottom-left corner: "))
        width = float(input("Enter the rectangle's width: "))
        height = float(input("Enter the rectangle's height: "))

        rectangle = Rectangle(True, x, y, x + width, y, x + width, y + height, x, y + height, #vertices
        x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x , y + height, x, y + height, x, y, #edges
        90, 90, 90, 90, #angles
        width, height) #width, height

        print("Area:", rectangle.compute_area())
        print("Perimeter:", rectangle.compute_perimeter())
        print("Inner Angles:", rectangle.compute_inner_angles())
        print("Vertices:", rectangle.compute_vertices())

    #def is_inside(self, point):
        #return self.vertice1.x <= point.x <= self.vertice3.x and self.vertice1.y <= point.y <= self.vertice3.y

class Square(Rectangle):
    def __init__(self, *args):
        super().__init__(*args)

    def initialization_square():
        x = float(input("Enter the x coordinate for the square's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the square's bottom-left corner: "))
        width = float(input("Enter the square's width: "))
        height = width
        square = Square(True, x, y, x + width, y, x + width, y + height, x, y + height, #vertices
        x, y, x + width, y, x + width, y, x + width, y + height, x + width, y + height, x , y + height, x, y + height, x, y, #edges
        90, 90, 90, 90, #angles
        width, height) #width, height
        print("Area:", square.compute_area())
        print("Perimeter:", square.compute_perimeter())
        print("Inner Angles:", square.compute_inner_angles())
        print("Vertices:", square.compute_vertices())

class Triangle(Shape):
    def __init__(self, *args):
        super().__init__(*args)

    def compute_perimeter(self):
        return self.edge1.length + self.edge2.length + self.edge3.length
    
    def compute_area(self):
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self.edge1.length) * (s - self.edge2.length) * (s - self.edge3.length))

    def compute_inner_angles(self):
        a = self.edge1.length
        b = self.edge2.length
        c = self.edge3.length
        self.angle1 = math.acos((a**2 - b**2 - c**2) / (-2 * b * c))
        self.angle2 = math.acos((b**2 - a**2 - c**2) / (-2 * a * c))
        self.angle3 = math.acos((c**2 - a**2 - b**2) / (-2 * a * b))
        return math.degrees(self.angle1), math.degrees(self.angle2), math.degrees(self.angle3)
    
    def compute_vertices(self):
        return [(self.vertice1.get_x(), self.vertice1.get_y()),
                (self.vertice2.get_x(), self.vertice2.get_y()),
                (self.vertice3.get_x(), self.vertice3.get_y())]

class Isosceles(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    def initialization_isosceles_triangle():
        x = float(input("Enter the x coordinate for the isosceles triangle's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the isosceles triangle's bottom-left corner: "))
        base_length = float(input("Enter the isosceles triangle's base length: "))
        equal_side_length = float(input("Enter the isosceles triangle's equal side length: "))
        isosceles_triangle = Isosceles(False, x, y, x + base_length, y, (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), 0, 0,
            x, y, x + base_length, y, x + base_length, y, (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), (x + base_length) - ( base_length / 2), y + math.sqrt((equal_side_length)**2 - ((x + base_length) - ( x + base_length - (base_length / 2)))**2), x, y, 0, 0, 0, 0, 
            0, 0, 0, 0, 
            base_length, math.sqrt(equal_side_length**2 - (base_length / 2)**2))
        print("Area:", isosceles_triangle.compute_area())
        print("Perimeter:", isosceles_triangle.compute_perimeter())
        print("Inner Angles:", isosceles_triangle.compute_inner_angles())
        print("Vertices:", isosceles_triangle.compute_vertices())

class Equilateral(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    def initialization_equilateral_triangle():
        x = float(input("Enter the x coordinate for the equilateral triangle's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the equilateral triangle's bottom-left corner: "))
        side_length = float(input("Enter the equilateral triangle's side length: "))
        equilateral_triangle = Equilateral(True, x, y, x + side_length, y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, 0, 0,
            x, y, x + side_length, y, x + side_length, y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, (x + side_length) - (side_length / 2), (side_length**2 - (((x + side_length) - side_length / 2) - (x + side_length))**2)**(1/2) + y, x, y, 0, 0, 0, 0,
            60, 60, 60, 0,
            side_length, (side_length**2 - (side_length / 2)**2)**(1/2))
        print("Perimeter:", equilateral_triangle.compute_perimeter())
        print("Area:", equilateral_triangle.compute_area())
        print("Inner Angles:", equilateral_triangle.compute_inner_angles())
        print("Vertices:", equilateral_triangle.compute_vertices())

class Scalene(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    def initialization_scalene_triangle():
        x1 = float(input("Enter the x coordinate for the scalene triangle's first vertice: "))
        y1 = float(input("Enter the y coordinate for the scalene triangle's first vertice: "))
        x2 = float(input("Enter the x coordinate for the scalene triangle's second vertice: "))
        y2 = float(input("Enter the y coordinate for the scalene triangle's second vertice: "))
        x3 = float(input("Enter the x coordinate for the scalene triangle's third vertice: "))
        y3 = float(input("Enter the y coordinate for the scalene triangle's third vertice: "))
        scalene_triangle = Scalene(False, x1, y1, x2, y2, x3, y3, 0, 0,
            x1, y1, x2, y2, x2, y2, x3, y3, x3, y3, x1, y1, 0, 0, 0, 0,
            0, 0, 0, 0,
            math.sqrt((x2 - x1)**2 + (y2 - y1)**2), 0)
        
        print("Area:", scalene_triangle.compute_area())
        print("Perimeter:", scalene_triangle.compute_perimeter())
        print("Inner Angles:", scalene_triangle.compute_inner_angles())
        print("Vertices:", scalene_triangle.compute_vertices())

class TriRectangle(Triangle):
    def __init__(self, *args):
        super().__init__(*args)

    def initialization_tri_rectangle():
        x = float(input("Enter the x coordinate for the triangle rectangle's bottom-left corner: "))
        y = float(input("Enter the y coordinate for the triangle rectangle's bottom-left corner: "))
        width = float(input("Enter the triangle rectangle's width: "))
        height = float(input("Enter the triangle rectangle's height: "))
        tri_rectangle = TriRectangle(False, x, y, x + width, y, x, y + height, 0, 0,
            x, y, x + width, y, x + width, y, x, y + height, x, y + height, x, y, 0, 0, 0, 0,
            0, 0, 0, 0,
            width, height)
        print("Area:", tri_rectangle.compute_area())
        print("Perimeter:", tri_rectangle.compute_perimeter())
        print("Inner Angles:", tri_rectangle.compute_inner_angles())
        print("Vertices:", tri_rectangle.compute_vertices())

if __name__ == "__main__":
    #Rectangle.initialization_rectangle()
    #Square.initialization_square()
    #Equilateral.initialization_equilateral_triangle()
    #TriRectangle.initialization_tri_rectangle()
    #Isosceles.initialization_isosceles_triangle()
    Scalene.initialization_scalene_triangle()
```

## Punto 2

The restaurant revisted
Add setters and getters to all subclasses for menu item
Override calculate_total_price() according to the order composition (e.g if the order includes a main course apply some disccount on beverages)
Add the class Payment() following the class example.

```python
class MenuItem:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price

class Beverage(MenuItem):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.__temperature = temperature # hot or cold

    def set_temperature(self, temperature):
        self.__temperature = temperature

    def get_temperature(self):
        return self.__temperature

class FastFood(MenuItem):
    def __init__(self, name, price, type_cooking):
        super().__init__(name, price)
        self.__type_cooking = type_cooking # baked or fried

    def set_type_cooking(self, type_cooking):
        self.__type_cooking = type_cooking

    def get_type_cooking(self):
        return self.__type_cooking 

class Lunch(MenuItem):
    def __init__(self, name, price, kind):
        super().__init__(name, price)
        self.__kind = kind # Executive or ordinary

    def set_kind(self, kind):
        self.__kind = kind

    def get_kind(self):
        return self.__kind

class Protein(MenuItem):
    def __init__(self, name, price, type_animal):
        super().__init__(name, price)
        self.__type_animal = type_animal

    def set_type_animal(self, type_animal):
        self.__type_animal = type_animal

    def get_type_animal(self):
        return self.__type_animal

class Order:
    def __init__(self, items):
        self.__items = items
        self.discounts_applied = []

    def set_items(self, items):
        self.__items = items

    def get_items(self):
        return self.__items

    def calculate_total_price(self):
        total_price = sum(item.get_price() for item in self.__items)

        # Check if the order includes a main course
        has_lunch = any(isinstance(item, Lunch) for item in self.__items)
        has_fast_food = any(isinstance(item, FastFood) for item in self.__items)

        # Apply discount on beverages
        if has_lunch or has_fast_food:
            for item in self.__items:
                if isinstance(item, Beverage):
                    if has_lunch and has_fast_food:
                        discount = 0.1 * item.get_price()  # 10% discount on beverages
                        reason = "10% discount on beverages due to lunch and fast food"
                    else:
                        discount = 0.05 * item.get_price()  # 5% discount on beverages
                        reason = "5% discount on beverages"
                    total_price -= discount  # Apply discount on beverage
                    self.discounts_applied.append((item.get_name(), discount, reason))

        # Apply discount on fast food
        if has_lunch and has_fast_food:
            for item in self.__items:
                if isinstance(item, FastFood):
                    discount = 0.05 * item.get_price()  # 5% discount on fast food
                    total_price -= discount  # Apply discount on fast food
                    self.discounts_applied.append((item.get_name(), discount, "5% discount on fast food due to lunch"))

        return total_price

class Payment():
    def __init__(self, total_price, payment_amount):
        self.__total_price = total_price
        self.__payment_amount = payment_amount

    def set_total_price(self, total_price):
        self.__total_price = total_price

    def get_total_price(self):
        return self.__total_price

    def set_payment_amount(self, payment_amount):
        self.__payment_amount = payment_amount

    def get_payment_amount(self):
        return self.__payment_amount

    def calculate_change(self):
        return self.__payment_amount - self.__total_price

if __name__=="__main__":

    coca_cola = Beverage(name="Coca-cola", price=3500, temperature="Cold beverage")
    orange_juice = Beverage(name="Orange juice", price=3000, temperature="Cold beverage")
    lemonade = Beverage(name="Lemonade", price=2500, temperature="Cold beverage")
    water = Beverage(name="Water", price=2000, temperature="Cold beverage")
    coffee = Beverage(name="Coffee", price=2500, temperature="Hot beverage")
    chocolate = Beverage(name="Chocolate", price=2500, temperature="Hot beverage")

    hot_dog = FastFood(name="Hot dog", price=10000, type_cooking="Fried")
    hamburger = FastFood(name="Hamburger", price=12000, type_cooking="Fried")
    pizza = FastFood(name="Pizza", price=8000, type_cooking="Baked")

    lentils = Lunch(name="Lentils with rice and salad", price=7000, kind="Ordinary")
    beans = Lunch(name="Beans with rice and salad", price=7000, kind="Ordinary")
    pasta = Lunch(name="Pasta with bread and salad", price=6500, kind="Executive")

    beef = Protein(name="Beef", price=6000, type_animal="Cow")
    chicken = Protein(name="Chicken", price=5500, type_animal="Chicken meal")
    fish = Protein(name="Mojarra", price=7800, type_animal="Fish meal")

    # Enter your order
    your_order = [lemonade, chicken, pizza, lentils]

    order = Order(your_order)

    # Total price
    total_price = order.calculate_total_price()

    print("Order:")
    for item in order.get_items():
        print(f"- {item.get_name()}: ${item.get_price()}")

    print(f"Total price: ${total_price}")

    if order.discounts_applied:
        print("\nDiscounts applied:")
        for discount in order.discounts_applied:
            print(f"- {discount[2]} for {discount[0]}: ${discount[1]}")
    else:
        print("\nNo discounts applied.")

    payment_amount = float(input("Enter payment amount: "))
    payment = Payment(total_price, payment_amount)

    change = payment.calculate_change()
    if change >= 0:
        print(f"Change: ${change}")
    else:
        print("Insufficient payment.")
```
