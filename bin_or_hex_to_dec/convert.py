import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError()

class DecToBinaryConverter(Converter):
    def __init__(self):
        self.weight = 2

    def convert(self, binary):
        b_max = len(binary) - 1
        result = 0

        for i in range(len(binary)):
            cnt = int(i)
            current_num = binary[b_max - cnt]
            if current_num == '1':
                result = result + current_num * (self.weight ** cnt)

        return result

class DecToHexConverter(Converter):
    def __init__(self):
        self.weight = 16
        self.hex_dict = {
            '10': 'A',
            '11': 'B',
            '12': 'C',
            '13': 'D',
            '14': 'E',
            '15': 'F',
        }

    def convert(self, n_hex):
        h_max = len(n_hex) - 1
        calc_hex = int(n_hex)
        result = []

        while True:
            mod = calc_hex % self.weight
            mod_to_str = ''

            if mod < 10:
                mod_to_str = str(mod)
            else:
                mod_to_str = self.hex_dict[str(mod)]

            result.append(mod_to_str)

            calc_hex = calc_hex // self.weight

            if calc_hex <= 0:
                break

        result.reverse()
        return ''.join(result)

def main():
    c = str(sys.argv[1])
    n = str(sys.argv[2])

    if c == 'b':
        binary_converter = DecToBinaryConverter()
        result = binary_converter.convert(n)
    elif c == 'h':
        hex_converter = DecToHexConverter()
        result = hex_converter.convert(n)
    else:
        print('First Arg <b> or <h> Second Arg <Num> : python convert.py b 10 or python convert.py h 1f')

    print(result)

main() if __name__ == '__main__' else None
