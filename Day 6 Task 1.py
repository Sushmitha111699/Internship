class Payment:
    def pay(self):
        print("Payment method selected")
class GooglePay(Payment):
    def pay(self):
        print("Payment made using Google Pay")
class PhonePe(Payment):
    def pay(self):
        print("Payment made using PhonePe")
class CreditCard(Payment):
    def pay(self):
        print("Payment made using Credit Card")
payment = Payment()
gpay = GooglePay()
phonepe = PhonePe()
credit_card = CreditCard()
payment.pay()
gpay.pay()
phonepe.pay()
credit_card.pay()