import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError()

class BinaryConverter(Converter):
    def __init__(self, decimal):
        self.decimal = decimal
        self.weight = 2

    def convert(self):
        """
        decimal to bin 
        """
        result = []
        while True:
            mod_to_str = str(self.decimal % self.weight)
            result.append(mod_to_str)
            self.decimal = self.decimal // self.weight

            if self.decimal == 0:
                break

        return not_destruct_reverse(result)

class HexConverter(Converter):
    def __init__(self, decimal):
        self.decimal = decimal
        self.weight = 16
        self.hex_dict = {
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F'
        }

    def convert(self):
        """
        decimal to hex
        """
        result = []
        while True:
            mod = self.decimal % self.weight
            mod_to_str = None
            if mod < 10:
                mod_to_str = str(mod)
            else:
                mod_to_str = self.hex_dict[str(mod)]

            result.append(mod_to_str)

            self.decimal = self.decimal // self.weight

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
