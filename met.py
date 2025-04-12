#property

# class Account:
#     def __init__(self, owner, balance):
#         self._owner = owner
#         self._balance = balance
#     @property
#     def balance(self):
#         return self._balance
#     @balance.setter
#     def balance(self, value):
#         if value >= 0:
#             self._balance = value
#         else:
#             print("Баланс не может быть отрицательным.")
# acc1 = Account("Иван", 1000)
# print("Баланс: ", acc1.balance)
# acc1.balance = 1500
# print("Баланс: ", acc1.balance)
# acc1.balance = -500

#get и set

class Account:
    def __init__(self, owner, balance):
        self._owner = owner
        self._balance = balance
    def get_balance(self):
        return self._balance
    def set_balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Баланс не может быть отрицательным.")
acc1 = Account("Ольга", 500)
print("Баланс:", acc1.get_balance())
acc1.set_balance(900)
print("Баланс: ", acc1.get_balance())
acc1.set_balance(-300)