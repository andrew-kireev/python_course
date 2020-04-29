


class Value:
    def __init__(self):
        self.value = None

    @staticmethod
    def _prepare_value(obj, value):
        attr_name = "commission"
        assert hasattr(obj, attr_name), \
            f"{obj} doesn't have attribute \"{attr_name}\""

        res = value * (1 - obj.commission)
        return res

    def __get__(self, obj, obj_type):
        return self.value

    def __set__(self, obj, value):
        self.value = self._prepare_value(obj, value)


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission



new_account = Account(0.1)
new_account.amount = 100

print(new_account.amount)