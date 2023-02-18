class HashTable:
    def __init__(self, max):
        self.max = max
        self.arr = [None for i in range(self.max)]
        
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val
        
    def __getitem__(self, key):
        h = self.get_hash(key)
        return self.arr[h]
    
    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None
        
t = HashTable(20)
t["march 6"] = 130
t["july 8"] = 19
print(t.arr)
t["march 6"]
del t["march 6"]
print(t.arr)
