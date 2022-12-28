class Tree:

    def __init__(self, id_node):
        self.id_node = id_node
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.id_node)

    @classmethod
    def build(cls, elements: list):
        root_node = cls(elements[0])

        for el in elements[1:]:
            root_node.insert(el)

        return root_node

    def insert(self, id_node):
        if self.id_node:
            if id_node < self.id_node:
                if self.left is None:
                    self.left = Tree(id_node)
                else:
                    self.left.insert(id_node)
            elif id_node > self.id_node:
                if self.right is None:
                    self.right = Tree(id_node)
                else:
                    self.right.insert(id_node)
        else:
            self.id_node = id_node

    def findval(self, find_val):
        if find_val < self.id_node:
            if self.left is None:
                return str(find_val) + " Not Found"
            return self.left.findval(find_val)
        elif find_val > self.id_node:
            if self.right is None:
                return str(find_val) + " Not Found"
            return self.right.findval(find_val)
        else:
            print(str(self.id_node) + ' is found')

    def min_value(self) -> int:
        curr_node = self
        while curr_node.left is not None:
            curr_node = curr_node.left

        return curr_node.id_node

    def max_value(self) -> int:
        curr_node = self
        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node.id_node

    def delete_node(self, id_node):

        if self.id_node is None:
            return None

        if id_node < self.id_node:
            self.left = self.left.delete_node(id_node)
            return self

        elif id_node > self.id_node:
            self.right = self.right.delete_node(id_node)
            return self

        if self.left is None:
            return self.right

        elif self.right is None:
            return self.left

        else:
            min_key = self.right.min_value()
            self.id_node = min_key
            self.right = self.right.delete_node(min_key)
            return self

    def print_tree(self, level: int = 0):
        if self.left:
            self.left.print_tree(level + 1)
        print("* " * level if level > 0 else "R ", self.id_node, sep="")
        if self.right:
            self.right.print_tree(level + 1)


tree = Tree.build([10, 15, 2, 5, 1, 6, 13, 17])
tree.print_tree()
print(f'Min value: {tree.min_value()}')
print(f'Max value: {tree.max_value()}')

tree.delete_node(10)
tree.print_tree()
