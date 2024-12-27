class Trie:

    def __init__(self):
        self.children={}
        self.is_end=False

    def insert(self, word: str) -> None:
        node=self
        for chara in word:
            if chara not in node.children:
                node.children[chara]=Trie()
            node=node.children[chara]
        node.is_end=True

    def search(self, word: str) -> bool:
        node=self
        for chara in word:
            if chara not in node.children:
                return False
            node=node.children[chara]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node=self
        for chara in prefix:
            if chara not in node.children:
                return False
            node=node.children[chara]
        return True        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)