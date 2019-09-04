

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, capacity_modulo):
    h = 5381
    for x in string:
        h = (( h << 5) + h) + ord(x)
    result = h & 0xFFFFFFFF
    return result % capacity_modulo


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        hash_table.storage[index] = LinkedPair(key, value)
    else:
        current_node = hash_table.storage[index]
        while current_node.next is not None:
            if current_node.key == key:
                current_node.value = value
                return
            else:
                current_node = current_node.next
        if current_node.key == key:
            current_node.value = value
            return
        current_node.next = LinkedPair(key, value)

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity) 
    if hash_table.storage[index] is None:
        print("warning no value found at key index")
        return
    hash_table.storage[index] = None


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] is None:
        print("No value found at specified index")
        return None
    else:
        current_node = hash_table.storage[index]
        while current_node is not None:
            if current_node.key == key:
                return current_node.value
            current_node = current_node.next
        if current_node is None:
            print("There is no value for this key")
            return None

# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_table = HashTable(hash_table.capacity*2)
    for x in range(0, hash_table.capacity):
        if hash_table.storage[x] is not None:
            hash_table_insert(new_table, hash_table.storage[x].key, hash_table.storage[x].value)
    return new_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
