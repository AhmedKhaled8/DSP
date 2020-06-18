class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.isleaf = False
        self.symbolval = None # 0~255
        self.prev = self

    def get_bit(self, bit):
        node = self.prev.right if bit == 1 else self.prev.left
        if node.isleaf:
            self.prev = self # reset
            return node.symbolval
        else:
            self.prev = node
            return None
     
    def print_tree(self):
        maps = {}
        tmp = []
        self.__dfs(maps, tmp, self)
        print(maps)
    def __dfs(self, maps, tmp, node):
        """
        maps: dict, str codeword to int symbolval
        tmp: list of "1" or "0"
        """
        if node.isleaf:
            codeword = "".join(tmp)
            maps[codeword] = node.symbolval
            return
        if node.left:
            tmp.append("0")
            self.__dfs(maps, tmp, node.left)
            tmp.pop()
        if node.right:
            tmp.append("1")
            self.__dfs(maps, tmp, node.right)
            tmp.pop()


def create_huffman_tree(bits, huffvals):
    root = Node()
    root.left = Node()
    root.right = Node()
    possible_leafs = [root.left, root.right]
    idx = 0 # pos in huffvals
    for x in bits:
        for i in range(x):
            possible_leafs[i].symbolval = huffvals[idx]
            possible_leafs[i].isleaf = True
            idx += 1
        copy_remain = possible_leafs[x:]
        possible_leafs = []
        for node in copy_remain:
            node.left, node.right = Node(), Node()
            possible_leafs.append(node.left)
            possible_leafs.append(node.right)
    return root
