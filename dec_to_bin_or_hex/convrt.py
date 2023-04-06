import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError

class BinaryConverter(Converter):
    def __init__(self, decimal):
        self.decimal = decimal

    def convert(self):
        """
        decimal to bin 
        """
        result = []
        binary = 2
        while True:
            mod_to_str = str(self.decimal % binary)
            result.append(mod_to_str)
            self.decimal = self.decimal // binary

            if self.decimal == 0:
                break

        return not_destruct_reverse(result)

class HexConverter(Converter):
    def __init__(self, decimal):
        self.decimal = decimal

    def convert(self):
        """
        decimal to hex
        """
        result = []
        hex = 16
        while True:
            mod = self.decimal % hex
            mod_to_str = None
            if mod < 10:
                mod_to_str = str(mod)
            elif mod == 10:
                mod_to_str = 'A'
            elif mod == 11:
                mod_to_str = 'B'
            elif mod == 12:
                mod_to_str = 'C'
            elif mod == 13:
                mod_to_str = 'D'
            elif mod == 14:
                mod_to_str = 'E'
            elif mod == 15:
                mod_to_str = 'F'
            result.append(mod_to_str)

            self.decimal = self.decimal // hex

            if self.decimal == 0:
                break

        return not_destruct_reverse(result)

def not_destruct_reverse(number_list):
    """
    not destruct reverse
    This function was created because the built-in function reverse is destructive.
    """
    result = [number_list[len(number_list) - 1 - i]
              for i in range(len(number_list))]

    return ''.join(result)


def main():
    argv = sys.argv
    print(argv[1])
    try:
        decimal = int(argv[1])

        bin_converter = BinaryConverter(decimal)
        bin_result = bin_converter.convert()
        hex_converter = HexConverter(decimal)
        hex_result = hex_converter.convert()

        [print(i) for i in ['hex : ' + hex_result, 'bin : ' + bin_result]]
    except ValueError:
        print('Input Number to Decimal')

main() if __name__ == '__main__' else not None
