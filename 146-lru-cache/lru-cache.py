class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache={}
        self.oldest=[]

    def get(self, key: int) -> int:
        if key in self.cache:
            idx=self.oldest.index(key)
            update_key=self.oldest.pop(idx)
            self.oldest.append(update_key)

            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:

            if len(self.cache)==self.capacity:
                delete_key = self.oldest.pop(0)
                del self.cache[delete_key]
            
            self.cache[key] = value
            self.oldest.append(key)
        
        else:
            self.cache[key] = value

            idx=self.oldest.index(key)
            update_key=self.oldest.pop(idx)
            self.oldest.append(update_key)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)