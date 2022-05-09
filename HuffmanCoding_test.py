import unittest

import HuffmanCoding


class TestHuffmanCoding(unittest.TestCase):
    def test_char_list(self):
        string = "Hello World"
        char_list = ["H", "e", "l", "o", " ", "W", "r", "d"]
        h = HuffmanCoding.Huffman()
        res = h._Huffman__to_list(string)
        self.assertEqual(res, char_list)

    def test_Get_Freq(self):
        string = "Hello World"
        freq_list = [1, 1, 3, 2, 1, 1, 1, 1]
        h = HuffmanCoding.Huffman()
        _, res = h._Huffman__GetFreq(string)
        self.assertEqual(res, freq_list)

    def test_Total(self):
        c = HuffmanCoding.Huffman()

        string = input("Enter a string: ")

        # Create Huffman tree of any string
        tree = c.CreateHuffmanTree(string)
        # Encode the string
        encoded = c.Encode(string)
        print(encoded)
        # Use the encoded string and Huffman tree to decode the string
        decoded = c.Decode(tree, encoded)
        print(decoded)
        # Check if the decoded string is the same as the original
        self.assertEqual(decoded, string)

        ################################################################

        given_string = "FORGET"
        given_Freq = [2, 3, 4, 4, 5, 7]
        given_chars = ['F', 'O', 'R', 'G', 'E', 'T']

        tree2 = c.CreateHuffmanTree2(given_chars, given_Freq)
        encoded2 = c.Encode2(given_chars, given_Freq, given_string)
        print(encoded2)
        decoded2 = c.Decode2(given_chars, given_Freq, encoded2)
        decoded3 = c.Decode(tree2, encoded2)

        print(decoded2)
        print(decoded3)

        self.assertEqual(decoded2, given_string)
        self.assertEqual(decoded3, given_string)

    def test_encode(self):
        c = HuffmanCoding.Huffman()
        HuffmanCoding.encode("README.md", "README.md.huff")

    def test_decode(self):
        c = HuffmanCoding.Huffman()
        HuffmanCoding.decode("README.md.huff", "README.md")


if __name__ == '__main__':
    unittest.main()
