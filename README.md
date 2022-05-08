# HuffmanCoding
This is a python program that implements the Huffman coding algorithm.

## usage
```python
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
```
input : This is a python program

Result :
```result
Enter a string: This is a python program
001010101011110010010111100100110110011100011010010101111010110011100001111011000011010111
This is a python program
True

```
