import sys
from abc import ABCMeta, abstractmethod

class Converter(metaclass=ABCMeta):
    @abstractmethod
    def convert(self):
        raise NotImplementedError()

class BinaryConverter(Converter):
    def convert(self, binary):
        b_max = len(binary) - 1
        result = 0

        for i in range(len(binary)):
            cnt = int(i)
            if binary[b_max - cnt] == '1':
                result = result + 1 * (2 ** cnt)

        return result

def main():
    n = str(sys.argv[1])

    binary_converter = BinaryConverter()
    bin_to_dec = binary_converter.convert(n)
    print(bin_to_dec)

main() if __name__ == '__main__' else None
