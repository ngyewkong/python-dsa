def num_pointer():
    num1 = 11

    num2 = num1

    print("Before num2 value is updated: ")
    print("num1 = ", num1)
    print("num2 = ", num2)

    # num1 & num2 points to the same address in memory
    print("\nnum1 points to: ", id(num1))  # 140626154887792
    print("num2 points to: ", id(num2))  # 140626154887792

    # reassign num2 to a new integer
    num2 = 22

    print("\nAfter num2 value is updated: ")
    print("num1 = ", num1)
    print("num2 = ", num2)

    # num1 & num2 points to the same address in memory
    print("\nnum1 points to: ", id(num1))  # 140626154887792
    print("num2 points to: ", id(num2))  # 140626154888144
    # num2 points to a diff address in memory but num1 points to same address in memory as before

    # Integers are immutable -> cannot change that integer in the particular place in mem once created
    # You can point the variable (eg num2) to a diff integer stored in a diff place in mem


def dict_pointer():
    dict1 = {
        "value": 11
    }
    dict2 = dict1
    print("Before dict2 value is updated: ")
    print("dict1 = ", dict1)
    print("dict2 = ", dict2)

    # dict1 & dict2 points to the same address in memory
    print("\ndict1 points to: ", id(dict1))  # 140399640608000
    print("dict2 points to: ", id(dict2))  # 140399640608000

    # reassign dict2 value to 22
    dict2["value"] = 22
    print("\nAfter dict2 value is updated: ")
    print("dict1 = ", dict1)
    print("dict2 = ", dict2)

    # dict1 & dict2 points to the same address in memory
    print("\ndict1 points to: ", id(dict1))  # 140399640608000
    print("dict2 points to: ", id(dict2))  # 140399640608000
    # when dict2 is updated with value=22
    # dict1 value changed to 22 as well
    # dict1 & dict2 points to the same address in memory as before update
    # Dictionary can be changed/mutable

    # when a dictionary has no variables pointing to it any more
    # no way to access the dictionary -> remove the dictionary through garbage collection in python


# num_pointer()
dict_pointer()
