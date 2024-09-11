# def repeat(s, exclaim):
#     """
#     Returns the string 's' repeated 3 times.
#     If exclaim is true, add exclamation marks.
#     """

#     result = s + s + s # can also use "s * 3" which is faster (Why?)
#     if exclaim:
#         result = result + '!!!'
#     return result

# def main():
#     print(repeat('yay',False))
#     print(repeat('woo hoo',True))

# if __name__ == "__main__":
#     main()


import sys

# # Now can refer to sys.xxx facilities
# sys.exit(0)

help(sys.exit)