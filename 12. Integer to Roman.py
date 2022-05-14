# Task
# https://leetcode.com/problems/integer-to-roman/

# Solution
class Solution:
    def intToRoman(self, arabic_number: int) -> str:
        latin_number = ""

        digit_len = len(str(arabic_number))
        BASIS_DICT = {0: {"basis_1": "I",
                          "basis_2": "V",
                          "basis_3": "X",
                          },
                      1: {"basis_1": "X",
                          "basis_2": "L",
                          "basis_3": "C",
                          },
                      2: {"basis_1": "C",
                          "basis_2": "D",
                          "basis_3": "M",
                          },
                      3: {"basis_1": "M",
                          "basis_2": "V1",
                          "basis_3": "X1",
                          },

                      }

        for index, digit in enumerate(str(arabic_number)[::-1]):
            match digit:
                case "9":
                    latin_number = latin_number + BASIS_DICT[index]["basis_3"] + BASIS_DICT[index]["basis_1"]
                case "8":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"] * 3 + BASIS_DICT[index]["basis_2"]
                case "7":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"] * 2 + BASIS_DICT[index]["basis_2"]
                case "6":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"] + BASIS_DICT[index]["basis_2"]
                case "5":
                    latin_number = latin_number + BASIS_DICT[index]["basis_2"]
                case "4":
                    latin_number = latin_number + BASIS_DICT[index]["basis_2"] + BASIS_DICT[index]["basis_1"]
                case "3":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"] * 3
                case "2":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"] * 2
                case "1":
                    latin_number = latin_number + BASIS_DICT[index]["basis_1"]

        latin_number = latin_number[::-1]

        return latin_number
