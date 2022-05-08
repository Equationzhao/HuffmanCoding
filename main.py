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
