class SimplifiedEnum(type):
    def __new__(meta, name, bases, class_dict):
        class_dict.update({key: key for key in class_dict['__keys']})
        return type.__new__(meta, name, bases, class_dict)


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
