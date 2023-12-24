class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        hash_key = 0
        for char in key:
            hash_key += ord(char)
        return hash_key % self.MAX
    
    def set(self, key, value):
        h = self.get_hash(key)
        
        # Enumerate on self.arr[h] instead of self.arr[h]
        # for idx, element in enumerate(self.arr[h]):
        #     if len(element) == 2 and element[0] == key:
        #         print('yes')
        #         break
        #     print(element[0])
        
        # Append (key, value) pair to self.arr[h]
        self.arr[h] = value

    def  get(self, key):
        h = self.get_hash(key)
        
        # Iterate through key-value pairs in self.arr[h]
        for k, v in self.arr[h]:
            if k == key:
                return v
        
        # Return None if key is not found
        return None

# Create an instance of the HashTable
hashTable = HashTable()

# Insert key-value pairs
# hashTable["March 6"] = 120
# hashTable["April 19"] = 4567
# hashTable["March"] = 2020
# hashTable["March"] = 1010

hashTable.set("March 6", 1010)
hashTable.set("April 19", 1010)
hashTable.set("March", 1010)
hashTable.set("Nonexistent Key", 1010)


# print(hashTable.arr)

# print(hashTable.
print(hashTable.get("March"))
# Retrieve values using get method
# print(hashTable.get("March 6"))  # Output: 120
# print(hashTable.get("April 19"))  # Output: 4567
