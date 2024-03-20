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

class Payment:
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