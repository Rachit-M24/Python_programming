#DAY::13-MAY-2024 
#FIND  & CALCULATE SQUARE ROOT OF GIVEN NUMBER


#___SOLUTION ONE____#(USING EXPONENTIATION)
# num=int(input("Enter the value:"));
# sr = num**(1/2);
# print(f"The square root of {num} is {sr}")


#___SOLUTION TWO___#(USING MATH MODULE)
# import math
# num=int(input("Enter the value:"));
# sr=math.sqrt(num);
# print(f"The square root of {num} is {sr}");

#DAY::13-MAY-2024
#FIND AREA OF TRIANGLE


#___SOLUTION___#

# height = float(input("Enter the height:"))
# base = float(input("Enter the base :")) 

# area= 0.5*height*base;
# print(f"The Area of triangle is:{area}")


#DAY::13-MAY-2024
#SWAP THE TWO NUMBER


#___SOLUTION ONE___#(USING THE THIRD VARIBALE)
# num1 = 12
# num2 = 21
# print(f"Value of before swapping x:{num1} and y:{num2}")

# temp = num1
# num1 = num2
# num2 = temp
# print(f"Value after swapping x:{num1} and y:{num2}")


#___SOLUTION TWO___#(USING LEFT and RIGHT)
# x=int(input("Enter the value of x:"))
# y=int(input("Enter the value of y:"))

# print(f"Value of before swapping x:{x} and y:{y}")

# x,y = y,x

# print(f"Value of after swapping x:{x} and y:{y}")

#DAY:18-04-24
#SUBSTRING AND SLICING IN PYTHON

# a = "The series called Game of Throns"
# print(a[0:32])




# class Node:
#   def __init__(self,data=None,next=None):
#     self.data= data
#     self.next = next

# class LinkedList():
#   def __init__(self,head=None):
#     self.head = head

#   def insert_at_begining(self,data):
#     node = Node(data,self.head)
#     self.head = node

#   def print(self):
#     if self.head is None:
#       print("The Linked List is empty.")
#       return

#     itr = self.head
#     llstr = ' '
    
#     while itr:
#        llstr += str(itr.data) + '-->'
#        itr = itr.next
#     print(llstr)
    
# if __name__ == '__main__':       
#   ll = LinkedList()
#   ll.insert_at_begining(59)
#   ll.insert_at_begining(899)
#   ll.print()


#DAY:19-04-2024
#LEETCODE- 13
# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_Integer = {
#             "I": 1,
#             "V": 5,
#             "X": 10,
#             "L": 50,
#             "C": 100,
#             "D": 500,
#             "M": 1000,
#         }
#         last = "I"
#         sum = 0
#         for numeral in s[::-1]:
#             if roman_Integer[numeral] > roman_Integer[last]:
#                 sum += roman_Integer[numeral]
#             else:
#                 sum -= roman_Integer[numeral]
#                 last = numeral
#         return sum

# sol = Solution()
# print(sol.romanToInt("DM"))

#DAY:19-04-2024
#LEETCODE- 3
#3. Longest Substring Without Repeating Characters

# class Solution:
#     def lengthOfLongestSubstring(self, s):
#         cur, sofar , start = 0,0,0
#         N = len(s)
#         lookup = {}
#         i = 0

#         while i < N:
#             if s[i] not in lookup:
#                cur += 1
#             else:
#                start = max(start,lookup[s[i]])
#                cur = i-start 
#             lookup[s[i]] = i
#             sofar = max(cur , sofar)
#         return sofar
            
# sol = Solution()
# print(sol.lengthOfLongestSubstring("abcabcbb"))

class Solution:
    def isPalindrome(self, x: int):
        number = str(x)

        reversed = number[::-1]       
        if number == reversed:
            return (f"{number} is a palindrome")
        elif number != reversed:
            return (f"{number} is not palindrome")
sol = Solution()
print(sol.isPalindrome(-343))
        
