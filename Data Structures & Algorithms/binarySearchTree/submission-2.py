class TreeNode:
    def __init__(self, key: int, value: int) -> None:
        self.key = key
        self.value = value
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        node = TreeNode(key, val)

        if not self.root:
            self.root = node
            return
        
        curr = self.root

        while True:
            if key < curr.key:
                if not curr.left:
                   curr.left = node
                   return
                curr = curr.left
            elif key > curr.key:
                if not curr.right:
                    curr.right = node
                    return
                curr = curr.right
            else:
                curr.value = val
                return


    def get(self, key: int) -> int:
        curr = self.root

        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.value
        

        return -1


    def getMin(self) -> int:
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.value if curr else -1


    def getMax(self) -> int:
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.value if curr else -1


    def remove(self, key: int) -> None:

        def _remove(node: TreeNode | None, key: int):
            if not node:
                return None

            if key < node.key:
                node.left = _remove(node.left, key)
            elif key > node.key:
                node.right = _remove(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                else:
                    min_node = node.right
                    while min_node and min_node.left:
                        min_node = min_node.left
                    
                    node.key = min_node.key
                    node.value = min_node.value

                    node.right = _remove(node.right, min_node.key)
            return node
            
        self.root = _remove(self.root, key)


    def getInorderKeys(self) -> List[int]:
        arr = []

        def dfs(node: TreeNode | None):
            if not node:
                return
            
            dfs(node.left)
            arr.append(node.key)
            dfs(node.right)
        
        dfs(self.root)
        return arr

