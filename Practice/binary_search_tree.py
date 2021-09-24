class BinarySearchTree:

    def __init__(self):
        self.root = None

    def search(self, value):
        if self._search(self.root, value) is None:
            return False
        return True

    def _search(self, node_to_search, value):
        if node_to_search is None or value == node_to_search.value:
            return node_to_search

        if value > node_to_search.value:
            return self._search(node_to_search.right_child, value)

        if value < node_to_search.value:
            return self._search(node_to_search.left_child, value)

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return

        self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value, current_node)
            return self._insert(current_node.right_child, value)

        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value, current_node)
            return self._insert(current_node.left_child, value)

        return

    def delete(self, value):
        pass

    def max_value(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.right_child is not None:
            current_node = current_node.right_child

        return current_node.value

    def min_value(self):
        if self.root is None:
            return None

        current_node = self.root
        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node.value

    def print_tree(self):
        self._print_node(self.root)

    def _print_node(self, node):
        print(node.value, end = " ")
        if node.left_child is not None:
            self._print_node(node.left_child)
        if node.right_child is not None:
            self._print_node(node.right_child)


class Node:

    def __init__(self, value, parent=None):
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.value = value


bst = BinarySearchTree()
bst.insert(8)
bst.insert(9)
bst.insert(6)
bst.insert(10)
bst.insert(-2)
bst.insert(3)
bst.insert(300)
bst.insert(4)
bst.insert(-100)
bst.print_tree()
