# Binary operators: ———————————————————————————————————————————————————————————>
print 5 >> 4  # Right Shift
print 5 << 1  # Left Shift
print 8 & 5   # Bitwise AND
print 9 | 4   # Bitwise OR
print 12 ^ 42 # Bitwise XOR
print ~88     # Bitwise NOT


# The '<<' binary operator: ———————————————————————————————————————————————————>
bit_seq = 0b1010010
# << is the same as: multiplying x by 2**y
print 0b1010010 * 2** 6
print 82 * 2** 6

bit_seq = bit_seq << 6
print bit_seq
print bin(bit_seq)


# The '>>' binary operator: ———————————————————————————————————————————————————>
bit_seq_2 = 0b1010010
# >> is the same as: floor-dividing x by 2**y
print 0b1010010 // 2** 3
print 82 // 2** 3

bit_seq_2 = bit_seq_2 >> 3
print bit_seq_2
print bin(bit_seq_2)


# The '&' binary operator: ————————————————————————————————————————————————————>
result = 0b1110 & 0b101
print bin(result)

# You need to allign the binary numbers from the right.
# 0b1110
#    |
# 0b_101

# This is how you allign the binary seqeunces:
# binary_example_0 : 11010101 - 213
#                    00001010 -  10
#                    ========
#                    00000000 -   0

# binary_example_1 : 1010111100 - 700
#                    0101010101 - 341
#                    ==========
#                    0000010100 -  20

# binary_example_2 : 1010001 - 29
#                    0011101 - 81
#                    =======
#                    0010001 - 17



binary_example_0 = 0b11010101 & 0b1010
binary_example_1 = 0b1010111100 & 0b101010101
binary_example_2 = 0b11101 & 0b1010001

print bin(binary_example_0)
print bin(binary_example_1)
print bin(binary_example_2)


# '|' Binary operator: ————————————————————————————————————————————————————————>
result_0 = 0b1110 | 0b101
result_1 = 0b1101101010 | 0b0000110100
result_2 = 0b1111111 | 0b0000000
result_3 = 0b1010100001 | 0b0010101000

print bin(result_0) # Produces: ------1111
print bin(result_1) # Produces: 1101111110
print bin(result_2) # Produces: ---1111111
print bin(result_3) # Produces: 1010101001

# Binary operator is analogous to 'or' in boolean logic:

# 1110   1101101010   1111111    1010100001
# 0101   0000110100   0000000    0010101000
# ====   ==========   =======    ==========
# 1111   1101111110   1111111    1010101001


# '~' Binary operator: ————————————————————————————————————————————————————————>
# Adds 1 and returns the negative.
print ~1          # -2
print ~2          # -3
print ~3          # -4
print ~42         # -43
print ~123        # -124


# '^' binary operator: ————————————————————————————————————————————————————————>
# Returns bit if bit is either 1 on one side but not both.
# Thus, 1 ^ 1 = 0, however, 1 ^ 0 = 1
result_1 = 0b1110 ^ 0b101
result_2 = 0b10101111111 ^ 0b1010101
result_3 = 0b1011010101 ^ 0b11000001

print bin(result_1)
print bin(result_2)
print bin(result_3)

#  1110    10101111111    1011010101
#  0101    00001010101    0011000001
#  ====    ===========    ==========
#  1011    10100101010    1000010100


# Binary numbers: —————————————————————————————————————————————————————————————>
print 0b1,          # 1
print 0b10,         # 2
print 0b11,         # 3
print 0b100,        # 4
print 0b101,        # 5
print 0b110,        # 6
print 0b111         # 7
print "******"
print 0b1 + 0b11    # 4
print 0b11 * 0b11   # 9


# Binary Conversion: ——————————————————————————————————————————————————————————>
# produces 0b1010
# which is in essence the binary representation of 10
print bin(10)
# >>> 0b1010

# conversely 'print 0b1010' produces the decimal representation of 1010
print 0b1010
# >>> 10


# Binary Tricks #1 : ——————————————————————————————————————————————————————————>
def check_bit4(input):
  mask = 0b01000         # checks to see if the fourth bit from the right is on.
  result = input & mask
  if result > 0:
    return "on"
  else:
    return "off"


# Binary Tricks #2 : ——————————————————————————————————————————————————————————>
a = 0b10111011
mask = 0b100            # turns the third bit from the right on.
result = a | mask

print bin(result)


# Binary Tricks #3 : ——————————————————————————————————————————————————————————>
a = 0b11101110
mask = 0b11111111
flipped = a ^ mask  # flips all of the bits. e.g. 1010 = 0101
print bin(flipped)


# Binary Tricks #4 : ——————————————————————————————————————————————————————————>
def flip_bit(number, n):
  bit_to_flip = 0b1 << (n -1)
  result = number ^ bit_to_flip
  return bin(result)

print flip_bit(0b1001, 2)
