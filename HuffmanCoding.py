# Author: Equationzhao
# Time: 2022/5/6
# Usage: import HuffmanCoding
# Module: HuffmanCoding
# Description: This is a python3 program that can encode and decode a string using Huffman coding.

# Huffman coding is a method of encoding strings using a tree structure.
# The tree is made up of nodes, where each node has a character and a frequency.
import os


class Node:
    def __init__(self):
        self.freq = 0  # 频率
        self.left_child = -1  # 左孩子
        self.right_child = -1  # 右孩子
        self.parent = -1  # 父节点
        self.isCandidate = False  # 是否是候选节点
        self.chr = 0  # 字符


class Huffman:

    def __init__(self):
        pass

    @staticmethod
    def __to_list(chars):
        res = []
        for i in chars:
            if i not in res:
                res.append(i)
        return res

    @staticmethod
    def __GetFreq(chars):
        freq_list = []

        char_list = Huffman.__to_list(chars)

        for i in range(len(char_list)):
            freq_list.append(chars.count(char_list[i]))

        return char_list, freq_list

    def GetCharListAndFreqList(self, chars) -> (list, list):
        char_list, freq_list = self.__GetFreq(chars)
        return char_list, freq_list

    @staticmethod
    def __FindMin(trees: list) -> int:
        if len(trees) == 0:
            return -1
        minv = float('inf')
        Id = -1
        for i in range(len(trees)):
            if trees[i].isCandidate and trees[i].freq < minv:
                minv = trees[i].freq
                Id = i
        return Id

    # input chars and their frequencies
    # tree
    @staticmethod
    def __CreateHuffmanTree(self, chars: list, freq_list: list) -> list:
        trees = []
        for i in range(len(freq_list)):
            n = Node()
            n.freq = freq_list[i]
            n.left_child = -1
            n.right_child = -1
            n.parent = -1
            n.isCandidate = True
            n.chr = chars[i]
            trees.append(n)

        while True:
            minId1 = self.__FindMin(trees)
            if minId1 == -1:
                break
            else:
                trees[minId1].isCandidate = False
                minId2 = self.__FindMin(trees)
                if minId2 == -1:
                    break
                else:
                    trees[minId2].isCandidate = False
                    parent = Node()
                    parent.freq = trees[minId1].freq + trees[minId2].freq
                    parent.left_child = minId1
                    parent.right_child = minId2
                    parent.parent = -1
                    parent.isCandidate = True
                    parent.chr = ""
                    trees.append(parent)
                    trees[minId1].parent = len(trees) - 1
                    trees[minId2].parent = len(trees) - 1

        return trees

    def CreateHuffmanTree(self, chars) -> list:
        char_list, freq_list = self.__GetFreq(chars)
        return self.__CreateHuffmanTree(self, char_list, freq_list)

    def CreateHuffmanTree2(self, char_list, freq_list) -> list:
        return self.__CreateHuffmanTree(self, char_list, freq_list)

    # input tree
    # output code
    @staticmethod
    def __GenerateHuffmanCode(trees: list) -> list:

        codes = []
        for i in range(len(trees)):
            code = ""
            if trees[i].left_child == -1:
                pid = trees[i].parent
                cid = i
                while pid != -1:
                    if cid == trees[pid].left_child:
                        code = "0" + code
                    else:
                        code = "1" + code
                    cid = pid
                    pid = trees[pid].parent
                codes.append(code)
        return codes

    def GenerateHuffmanCode(self, chars) -> list:
        trees = self.CreateHuffmanTree(chars)
        return self.__GenerateHuffmanCode(trees)

    def GenerateHuffmanCode2(self, char_list, freq_list) -> list:
        trees = self.CreateHuffmanTree2(char_list, freq_list)
        return self.__GenerateHuffmanCode(trees)

    # input chars
    # output code
    def Encode(self, chars: str):
        res = ""
        ch2huf = {}

        char_list, freq_list = self.__GetFreq(chars)
        trees = self.__CreateHuffmanTree(self, char_list, freq_list)
        codes = self.__GenerateHuffmanCode(trees)

        for i in range(len(char_list)):
            ch2huf.setdefault(char_list[i], codes[i])

        for i in range(len(chars)):
            res += ch2huf[chars[i]]

        return res

    def Encode2(self, char_list: list, freq_list: list, chars: str):
        res = ""
        ch2huf = self.CreateCh2huf(char_list, freq_list)

        for i in range(len(chars)):
            res += ch2huf[chars[i]]

        return res

    def CreateCh2huf(self, char_list, freq_list):
        ch2huf = {}
        trees = self.__CreateHuffmanTree(self, char_list, freq_list)
        codes = self.__GenerateHuffmanCode(trees)
        for i in range(len(char_list)):
            ch2huf.setdefault(char_list[i], codes[i])
        return ch2huf

    @staticmethod
    def Decode(vtrees, code):

        res = ""
        Id = len(vtrees) - 1
        for i in range(len(code)):
            if code[i] == "0":
                Id = vtrees[Id].left_child
            else:
                Id = vtrees[Id].right_child
            if vtrees[Id].left_child == -1:
                res += vtrees[Id].chr
                Id = len(vtrees) - 1

        return res

    def Decode2(self, given_chars, given_Freq, encoded2) -> str:
        vTrees = self.__CreateHuffmanTree(self, given_chars, given_Freq)
        return self.Decode(vTrees, encoded2)


def encode(input_file: str, output_file: str):
    def run():
        input_file_obj = open(input_file, "r")
        content = input_file_obj.read()
        input_file_obj.close()
        output_file_obj = open(output_file, "w")
        huffman = Huffman()
        char_list, Freq_list = huffman.GetCharListAndFreqList(content)
        output_file_ch2freq = open(output_file + ".ch2freq", "w")
        output_file_ch2freq.write(str(char_list) + "\n")
        output_file_ch2freq.write(str(Freq_list))
        output_file_ch2freq.close()
        output_file_obj.write(huffman.Encode(content))
        output_file_obj.close()

    if os.path.exists(output_file):
        print(output_file + " or " + output_file + ".ch2freq" + " has already existed, do you want to overwrite it? ("
                                                                "y/n)")
        choice = input()
        if choice == "y" or choice == "Y":
            run()
        elif choice == "n" or choice == "N":
            print("exit")
        else:
            print("invalid input")
    else:
        run()


def decode(input_file: str, output_file: str):
    def run():
        ch2freq = input_file + ".ch2freq"
        input_file_obj = open(input_file, "r")
        content = input_file_obj.read()
        input_file_obj.close()
        output_file_obj = open(output_file, "w")
        ch2freq_obj = open(ch2freq, "r")
        char_list = eval(ch2freq_obj.readline())
        Freq_list = eval(ch2freq_obj.readline())
        ch2freq_obj.close()
        huffman = Huffman()
        output_file_obj.write(huffman.Decode2(char_list, Freq_list, content))
        output_file_obj.close()

    if os.path.exists(output_file):
        print(output_file + " has already existed, do you want to override it?(y/n)")
        choice = input()
        if choice == "y" or choice == "Y":
            run()
        elif choice == "n" or choice == "N":
            print("exit")
        else:
            print("invalid input")
    else:
        run()
