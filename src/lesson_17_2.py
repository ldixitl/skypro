from abc import ABC, abstractmethod


class Order:

    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        return sum(quantities * prices for quantities, prices in zip(self.quantities, self.prices))


class Authorizer(ABC):
    @abstractmethod
    def is_authorized(self) -> bool:
        pass


class AuthorizerSMS(Authorizer):

    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"Верификация SMS кода {code}")
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class AuthorizerRobot(Authorizer):

    def __init__(self):
        self.authorized = False

    def not_a_robot(self):
        self.authorized = True

    def is_authorized(self) -> bool:
        return self.authorized


class PaymentProcessor(ABC):

    @abstractmethod
    def pay(self, order):
        pass


class DebitPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code, authorizer: Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован")

        print("Обработка дебетового типа платежа")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):

    def __init__(self, security_code):
        self.security_code = security_code

    def pay(self, order):
        print("Обработка кредитного типа платежа")
        print(f"Проверка кода безопасности: {self.security_code}")
        order.status = "paid"


class PayPalPaymentProcessor(PaymentProcessor):

    def __init__(self, user_email, authorizer: Authorizer):
        self.user_email = user_email
        self.authorizer = authorizer

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Не авторизован")

        print("Обработка типа платежа PayPal")
        print(f"Отправка платежа на почту: {self.user_email}")
        order.status = "paid"


if __name__ == "__main__":
    # Создаем заказ
    order1 = Order()
    # Добавляем товары в заказ
    order1.add_item("Клавиатура", 1, 2500)
    order1.add_item("SSD", 1, 7500)
    order1.add_item("USB-кабель", 2, 250)
    # Печатаем стоимость заказа
    print(order1.total_price())
    # Оплачиваем заказ
    authorizer = AuthorizerSMS()
    # authorizer.verify_code(465839)
    authorizer.verify_code(524354)
    payment_processor = DebitPaymentProcessor("0372846", authorizer)
    print(order1.status)
    payment_processor.pay(order1)
    print(order1.status)

    authorizer_robot = AuthorizerRobot()
    authorizer_robot.not_a_robot()
    paypal_payment = PayPalPaymentProcessor("user@mail.com", authorizer_robot)
    paypal_payment.pay(order1)
