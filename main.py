import HuffmanCoding

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
print(decoded == string)

################################################################

given_string = "Hello World"
given_Freq = [10, 23, 12, 3, 4, 8, 11, 18]
given_chars = ['H', 'e', 'l', 'o', ' ', 'W', 'r', 'd']

tree2 = c.CreateHuffmanTree2(given_chars, given_Freq)
encoded2 = c.Encode2(given_chars, given_Freq, given_string)
print(encoded2)
decoded2 = c.Decode2(given_chars, given_Freq, encoded2)
decoded3 = c.Decode(tree2, encoded2)

print(decoded2)
print(decoded3)

print(decoded2 == given_string)
print(decoded3 == given_string)
