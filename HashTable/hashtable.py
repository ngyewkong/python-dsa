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
