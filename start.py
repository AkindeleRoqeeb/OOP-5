class item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

        # Actions to execute
        item.all.append(self)

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

    def apply_discount(self):
        self.price = self.price * self.pay_rate

item1 = item("phone", 100, 1)
item2 = item("laptop", 1000, 3)
item3 = item("cable", 10, 6)
item4 = item("muse", 50, 6)
item5 = item("keyboard", 75, 5)

print(item.all)
      #####################################
for instance in item.all:
    print(instance.name)


########################################################################################

class item:
    pay_rate = 0.8 # The pay rate after 20% discount
    all = []
    def __init__(self, name: str, price: float, quantity: float, quality=0):
        ############### run validation to the recieve argument ######################
        # assert price >= 0
        ##################### OR ###############
        assert price >= 0, f"price {price} is not greater or equal zero"

        # assert quality >= 0
        ##################### OR ###############
        assert quality >= 0, f"quality {quality} is not greater or equal zero"

        self.name = name
        self.price = price
        self.quantity = quantity
        self.quality = quality

        # Actions to execute
        item.all.append(self)

    ############## Asign to self object ############################
    def calculate_total_price(self):
        return self.price * self.quality

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"item('{self.name}', {self.price}, {self.quantity}, {self.quality})"

item1 = item("phone", 100, 1)
item2 = item("laptop", 1000, 3)
item3 = item("cable", 10, 6)
item4 = item("muse", 50, 6)
item5 = item("keyboard", 75, 5)

print(item.all)
      #####################################
for instance in item.all:
    print(instance.name)