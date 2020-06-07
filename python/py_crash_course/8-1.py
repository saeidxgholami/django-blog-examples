def display_message():
    print("I'm learning how to define and use functions in python.")

def favorite_book(title):
    print("My favorite book is", title)


def add(x, y):
    return x + y



nums1 = [1, 2, 3, 4]
nums2 = [7, 2, 1, 2]

for a, b in zip(nums1, nums2):
    # print(add(a, b))
    pass

for i in range(len(nums1)):
    # print(add(nums1[i], nums2[i]))
    pass

x = 1
for i in nums1[x:]:
    r = nums1[x-1] + i
    print(r)
    x += 1


