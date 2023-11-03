# key-value pair -> dictionary in python
# get an address back in addition to the key-value pair
# the address is where the hash is stored
# dictionary or hashtable is one-way only
# cannot use the address to get the key
# deterministic -> for a particular hash function
# get back the same result ie the address that the hash is stored

# List impl to create a Hash Table
# create our own hash function to hash the key
# handle collison when the diff key-value pair is at the same address
# separate chaining method -> via linked list impl (done in this code)
# linear probing (open addressing) (prevents addresses from being reused)
# prime number of addresses is btr as it increases the amount of randomness
# for how the key-value pairs are distributed through the hashtable
# ie 0-6 instead of 0-7 (7 addresses is btr than 8 addresses)

class HashTable:
    def __init__(self, size=7) -> None:
        # this create a list of size=size being passed in (default is 7)
        # all the list elements is None
        self.data_map = [None] * size

    # hash function
    def __hash__(self, key):
        my_hash = 0
        # loop through the letters in the key being passed in
        # ord() gives the ascii number of the letter
        # * 23 is cos 23 is prime number
        # modulus of the len(7) will give a value of 0-6 which is the address space
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    # print helper function
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    # set method
    def set_item(self, key, value):
        # figure out the address
        index = self.__hash__(key)

        # initialize empty list only if the index is empty
        if self.data_map[index] == None:
            self.data_map[index] = []
        # append the key-value as list into the list (either empty or alr have another element pair)
        self.data_map[index].append([key, value])

    # get method
    def get_item(self, key):
        index = self.__hash__(key)
        # check if the index address holds not a None element
        if self.data_map[index] is not None:
            # loop through the inner list of the specific address space to get the item
            for i in range(len(self.data_map[index])):
                # check if the i keypair its key in the list matches the key we specify when we call the method
                if self.data_map[index][i][0] == key:
                    # return the value of the value pair
                    return self.data_map[index][i][1]
        # cannot find said key return None
        return None

    # keys method
    def keys(self):
        # set a list to hold the keys
        all_keys = []
        # for loop to iterate through the data_map
        # nested loop to loop through the inner list to find the keys
        for i in range(len(self.data_map)):
            # check if the inner list in each address space is not None then iterate
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # append the key the 0th element to the all keys list
                    all_keys.append(self.data_map[i][j][0])
        # return all keys list
        return all_keys


# sample setup for HashTable
print("----- test HashTable setup class -----")
my_hash_table = HashTable()
# print out the address space 0-6 and the values (all None as it is only initialized)
my_hash_table.print_table()

# set
print("----- set_item -----")
my_hash_table.set_item('bolts', 4000)
my_hash_table.set_item('washers', 100)
my_hash_table.set_item('lumber', 70)
# print out 0: None 1: None 2: None 3: None 4: [['bolts', 4000], ['washers', 100]] 5: None 6: [['lumber], 70]
my_hash_table.print_table()

# get
print("----- get_item -----")
print("The qty of washers is {}".format(
    my_hash_table.get_item('washers')))  # 100
print("The qty of screws is {}".format(
    my_hash_table.get_item('screws')))  # None

# key
print("----- keys -----")
print("The keys in the Hash Table are {}".format(
    my_hash_table.keys()))  # ['bolts', 'washers', 'lumber']

# Big O
# hash function for each key is O(1)
# set_item is also O(1)
# get_item is also O(1) to get the address one more step to get the item
# worst case is O(n) if all items are being stored at the same address
# assumption is distributed (good distribution) amd larger address space
# collisions are rare
# dictionary in python the impl
# to place a key-value pair O(1)
# to lookup by key O(1) lookup by value is not O(1)

# Interview Qn (Compare two lists and find the common match)
# 1st Approach (Naive) -> not recommended for interview
# 1 nested for loop to iterate both lists and compare
# O(n^2) not efficient


def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if (i == j):
                return True
    # for no match return False
    return False


list1 = [1, 3, 5]
list2 = [2, 4, 5]

# Interview Qn - Naive Approach
print("----- Nested for loops to compare matching elements in 2 lists -> Naive Approach -----")
print(item_in_common(list1, list2))  # True as 5 is common

# Efficient Approach is to use dictionary/hashtable
# loop through the first list and store it dictionary key-value pair (element: boolean)
# search by key to find match
# have to go through each list once -> O(2n) -> O(n) which more efficient than O(n^2)


def item_in_common_dict(list1, list2):
    # create dict
    my_dict = {}
    # iterate through the first list and add to dict
    for i in list1:
        # add the element as key with value True
        my_dict[i] = True

    # iterate through the second list O(n) and use it to get on dict O(1)
    for j in list2:
        if j in my_dict:
            return True

    # return False for no matches
    return False


# Interview Qn - Efficient Approach
print("----- Dictionary to compare matching elements in 2 lists -> Efficient Approach -----")
print(item_in_common_dict(list1, list2))  # True
