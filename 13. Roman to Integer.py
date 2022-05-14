# Task
# https://leetcode.com/problems/roman-to-integer/

# Solution
class Solution:
    def romanToInt(self, latin_number: str) -> int:
        arabic_number = 0
        pass_iteration = 0
        latin_number_rev = latin_number[::-1]
        for i in range(len(latin_number_rev)):
            if not pass_iteration:
                match latin_number_rev[i]:
                    case "M":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "C":
                                arabic_number += 900
                                pass_iteration = True
                            else:
                                arabic_number += 1000
                        else:
                            arabic_number += 1000
                    case "D":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "C":
                                arabic_number += 400
                                pass_iteration = True
                            else:
                                arabic_number += 500
                        else:
                            arabic_number += 500
                    case "C":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "X":
                                arabic_number += 90
                                pass_iteration = True
                            else:
                                arabic_number += 100
                        else:
                            arabic_number += 100
                    case "L":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "X":
                                arabic_number += 40
                                pass_iteration = True
                            else:
                                arabic_number += 50
                        else:
                            arabic_number += 50
                    case "X":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "I":
                                arabic_number += 9
                                pass_iteration = True
                            else:
                                arabic_number += 10
                        else:
                            arabic_number += 10
                    case "V":
                        if i < len(latin_number_rev) - 1:
                            if latin_number_rev[i + 1] == "I":
                                arabic_number += 4
                                pass_iteration = True
                            else:
                                arabic_number += 5
                        else:
                            arabic_number += 5
                    case "I":
                        arabic_number += 1
            else:
                pass_iteration = 0
        return arabic_number
