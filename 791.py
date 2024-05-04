# # def custom_sort(char, order_string):
# #     try:
# #         return order_string.index(char)
# #     except ValueError:
# #         # If the character is not found in order_string, place it at the end
# #         return len(order_string)

# # original_string = "adcb"
# # order_string = "cbd"

# # sorted_string = ''.join(sorted(original_string, key=lambda x: custom_sort(x, order_string)))

# # print("Original String:", original_string)
# # print("Sorted String based on order_string:", sorted_string)
# n=260
# while n>1:
#     print(n)
#     if n%4 == 0:
#         n=n//4
#     else:
#         print(False)
#         break
# print(True)
st ='89'

st=list(st)
print(int(''.join(st)))
for i,j in enumerate(st):
    print(i,j)