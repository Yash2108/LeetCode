class WordDictionary:

    def __init__(self):
        self.children={}
        self.is_end=False
        

    def addWord(self, word: str) -> None:
        node=self
        for chara in word:
            if chara not in node.children:
                node.children[chara]=WordDictionary()
            node=node.children[chara]
        node.is_end=True

    def search(self, word: str) -> bool:
        node=self
        for idx, chara in enumerate(word):
            if chara!='.' and chara not in node.children:
                # print('Case 1', chara, node.children.keys())
                return False
            elif chara=='.':
                for child in node.children:
                    # print('Case 2', chara, node.children.keys(), child)
                    if node.children[child].search(word[idx+1:]):
                        return True
                return False
            else:
                if chara not in node.children:
                    # print('Case 3', chara, node.children.keys())
                    return False
                else:
                    node=node.children[chara]
        return node.is_end

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)