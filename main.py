# Author: Equationzhao
# File: main.py
# Time: 2022/5/8
# Description: decode/encode file

from HuffmanCoding import encode, decode

import sys

mode = ""

if len(sys.argv) >= 2:
    mode = sys.argv[1]
else:
    print("Bad argv\nuse \'python3 main.py -h\' for help")
    sys.exit(1)

if mode == "-e":
    if len(sys.argv) == 4:
        input_file = sys.argv[2]
        output_file = sys.argv[3]
    elif len(sys.argv) == 3:
        input_file = sys.argv[2]
        output_file = input_file + ".huff"
    else:
        print("Usage: python3 main.py -e <input_file> <output_file>")
        sys.exit(1)
    try:
        encode(input_file, output_file)
    except FileNotFoundError:
        print(str.format("Error: File {} not found", input_file))
        sys.exit(1)
    except IOError:
        print("IOError\nPlease ensure you have the R/W access to the file")
        sys.exit(1)

elif mode == "-d":
    if len(sys.argv) == 4:
        input_file = sys.argv[2]
        output_file = sys.argv[3]
    elif len(sys.argv) == 3:
        input_file = sys.argv[2]
        output_file = input_file + ".decoded"
    else:
        print("Usage: python3 main.py -d <input_file> <output_file>")
        sys.exit(1)

    try:
        decode(input_file, output_file)
    except FileNotFoundError:
        print(str.format("Error: File {} not found", input_file))
        sys.exit(1)
    except IOError:
        print("IOError\nPlease ensure you have the R/W access to the file")
        sys.exit(1)

elif mode == "-h":
    print('Usage for encode: python3 main.py -e <input_file> -optional<output_file>\n'
          'Usage for decode: python3 main.py -d <input_file> -optional<output_file>\n'
          'Default output file is \n'
          '\tdecode : <input_file>.huff and <input_file>.huff.ch2freq\n'
          '\tencode : <input_file>.encoded\n'
          )
    sys.exit(0)
elif mode == "-v":
    print('Version: 0.1\n'
          'Author: Equationzhao 赵方程\n'
          'This is a simple Huffman coding tool\n'
          )
    sys.exit(0)
else:
    print("Bad argv\nuse \'python3 main.py -h\' for help")
    sys.exit(1)
