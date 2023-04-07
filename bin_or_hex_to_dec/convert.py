import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError()

class BinaryToDecConverter(Converter):
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

class HexToDecConverter(Converter):
    def __init__(self):
        self.weight = 16
        self.hex_dict = {
            'A': '10',
            'B': '11',
            'C': '12',
            'D': '13',
            'E': '14',
            'F': '15',
        }

    def convert(self, n_hex):
        h_max = len(n_hex) - 1
        result = 0

        for i in range(len(n_hex)):
            cnt = int(i)
            current_num = n_hex[h_max - cnt]

            if current_num.upper() in self.hex_dict.keys():
                current_num = self.hex_dict[current_num.upper()]

            result = result + int(current_num) * (self.weight ** cnt)

        return result

def main():
    c = str(sys.argv[1])
    n = str(sys.argv[2])

    if c == 'b':
        binary_converter = BinaryToDecConverter()
        result = binary_converter.convert(n)
    elif c == 'h':
        hex_converter = HexToDecConverter()
        result = hex_converter.convert(n)
    else:
        print('First Arg <b> or <h> Second Arg <Num> : python convert.py b 10 or python convert.py h 1f')

    print(result)

main() if __name__ == '__main__' else None
