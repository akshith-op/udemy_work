import random
def problem(arr):
    arr.insert(random.randint(0,len(arr)),random.randint(0,101))
    temp = arr
    for i in arr:
        if temp.index(i) % 2 == 1:
            if i >= arr[arr.index(i)+1]:
                pass
            else:
                arr.pop(arr.index(i))
        else:
            if i <= arr[arr.index(i)+1]:
                pass
            else:
                arr.pop(arr.index(i))
    return arr


result = problem([100, 1, 10, 3, 20, 25, 24])
print(result)

# # # def pandu_project(n):
# # #     amstrong_sum = 0
# # #     n = str(n)
# # #     for i in n:
# # #         amstrong_sum += int(i) ** 3
# # #     if amstrong_sum == int(n):
# # #         return True
# # #     else:
# # #         return False


# # # a = print(pandu_project(407))


# # def amst(n):
# #     temp = n
# #     sum = 0
# #     while temp != 0:
# #         num = temp % 10
# #         sum += num ** 3
# #         temp //= 10
# #     if sum == n:
# #         return True
# #     else:
# #         return False


# # a = amst(408)
# # print(a)


# a = [35, 67, 837, 3, 21, 2, 5, 9, 12]
# n = len(a)
# for i in range(0, n - 1):
#     for j in range(0, n - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# # print(a)
# def quick_sort(small,mid,large):
# arr = [2,4,5,9,3,6,9,1,3]
# pivot = arr[-1]
# for i in arr:
#     if i < pivot:
#         i.append(small)
#     elif i == pivot:
#         i.append(mid)
#     else:
#         i.append(large)
# print(small,mid,large)

