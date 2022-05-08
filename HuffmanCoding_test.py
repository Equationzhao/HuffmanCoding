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

if __name__ == '__main__':
    unittest.main()
