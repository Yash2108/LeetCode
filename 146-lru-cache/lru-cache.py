class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
    
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache={}
        self.least_recent, self.most_recent = Node(0, 0), Node(0, 0)
        self.least_recent.next, self.most_recent.prev = self.most_recent, self.least_recent
    
    def insert(self, node):
        prev, nxt = self.most_recent.prev, self.most_recent
        
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

        # new.p=most.prev
        # new.n=most
        # most.p.n=new
        # most.p=new
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


    # def insert(self, node):
    #     prev, nxt = self.most_recent.prev, self.most_recent
    #     prev.next = nxt.prev = node
    #     node.next, node.prev = nxt, prev

        
    #     self.most_recent.prev.next = self.most_recent.prev = node
    #     node.prev = self.most_recent.prev
    #     node.next=self.most_recent


    def get(self, key: int) -> int:
        '''
        remove
        insert
        return
        '''

        if key in self.cache:
            #TODO: remove
            self.remove(self.cache[key])
            #TODO: insert
            self.insert(self.cache[key])
            return self.cache[key].value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        '''
        remove if exists
        make node
        insert at front
        if cap hit, remove lru
        '''

        if key in self.cache:
            #TODO: remove
            self.remove(self.cache[key])
        #TODO: insert
        # node=
        self.cache[key]=Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache)>self.capacity:
            lru=self.least_recent.next
            self.remove(lru)
            del self.cache[lru.key]
        #TODO: remove least


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)