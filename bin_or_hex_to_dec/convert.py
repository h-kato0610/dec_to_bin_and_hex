import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError()

class DecToBinaryConverter(Converter):
    def convert(self, binary):
        b_max = len(binary) - 1
        result = 0

        for i in range(len(binary)):
            cnt = int(i)
            if binary[b_max - cnt] == '1':
                result = result + 1 * (2 ** cnt)

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
        result = 0

        for i in range(len(n_hex)):
            tmp = n_hex[h_max - i] 
            result_tmp = 0

            if tmp in self.hex_dict.keys():
                hex_num = int(self.hex_dict[tmp])
                result_tmp = hex_num * (self.weight ** i)
            else:
                result_tmp = int(tmp) * (self.weight ** i)

            result = result + result_tmp

        return hex(int(n_hex))

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
