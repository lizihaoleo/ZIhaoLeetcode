#
# @lc app=leetcode id=211 lang=python3
#
# [211] Add and Search Word - Data structure design
#

# @lc code=start
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.children = {}
        self.end = False
    
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TreeNode('-1')

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        cur = self.root
        for x in word:
            if x not in cur.children:
                cur.children[x] = TreeNode(x)
            cur = cur.children[x]
        cur.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        stack = [(self.root,word)]

        while stack:
            # print([(w,x.val,x.end) for x,w in stack])
            node, w = stack.pop()
            if not w:
                if node.end:
                    return True
            elif w[0] == '.':
                for child in node.children.values():
                    stack.append((child,w[1:]))
            else:
                if w[0] in node.children:
                    stack.append((node.children[w[0]],w[1:]))
        return False
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# @lc code=end

