# En

# Write a function that takes the binary representation of an unsigned integer and
# returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type.
# In this case, the input will be given as a signed integer type.
# It should not affect your implementation, as the integer's internal binary representation is the same,
# whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation.
# Therefore, in Example 3, the input represents the signed integer. -3.

# Constraints:

# The input must be a binary string of length 32.

# Ru

# Напишите функцию, которая принимает двоичное представление целого числа без знака и
# возвращает количество имеющихся у него битов '1' (также известное как вес Хэмминга).

# Примечание:

# Обратите внимание, что в некоторых языках, таких как Java, не существует целочисленного типа без знака.
# В этом случае входные данные будут представлены в виде целого числа со знаком.
# # Это не должно повлиять на вашу реализацию, так как внутреннее двоичное представление целых чисел одно и то же,
# независимо от того, подписано оно или нет.
# В Java компилятор представляет целые числа со знаком, используя обозначение дополнения 2.
# Следовательно, в примере 3 входные данные представляют собой целое число со знаком. -3.

# Ограничения:

# Входными данными должна быть двоичная строка длиной 32.

class Solution:
    def hammingWeight(self, n: int) -> int:
        return str(bin(n)).count("1")
