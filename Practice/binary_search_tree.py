class BinarySearchTree:

    def __init__(self):
        self.root = None

    def depth(self):
        return self._depth(self.root, 1)

    def _depth(self, node, depth):
        max_depth = depth
        if node.left_child is not None:
            max_depth = max(max_depth, self._depth(node.left_child, depth + 1))
        if node.right_child is not None:
            max_depth = max(max_depth, self._depth(node.right_child, depth + 1))
        return max_depth

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
        node_to_delete = self._search(self.root, value)
        if not node_to_delete:
            raise KeyError()

        if not node_to_delete.left_child and not node_to_delete.right_child:
            self._delete_leaf(node_to_delete)

        elif not node_to_delete.left_child or not node_to_delete.right_child:
            self._delete_node_with_one_child(node_to_delete)

        else:
            self._delete_node_with_two_children(node_to_delete)

    def _delete_leaf(self, node):
        if node.parent.left_child == node:
            node.parent.left_child = None
        else:
            node.parent.right_child = None
        del node

    def _delete_node_with_one_child(self, node):
        if node.left_child:
            node.value = node.left_child.value
            node.left_child = None

        else:
            node.value = node.right_child.value
            node.right_child = None

    def _delete_node_with_two_children(self, node):
        node_to_swap = self._min_node(node.right_child)
        node.value = node_to_swap.value
        self._delete_leaf(node_to_swap)

    def _max_node(self, start_position):
        if start_position is None:
            return None

        current_node = start_position
        while current_node.right_child is not None:
            current_node = current_node.right_child

        return current_node

    def _min_node(self, start_position):
        if start_position is None:
            return None

        current_node = start_position
        while current_node.left_child is not None:
            current_node = current_node.left_child

        return current_node

    def max_value(self):
        return self._max_node(self.root).value

    def min_value(self):
        return self._min_node(self.root).value

    def print_elements(self):
        self._print_element(self.root)

    def _print_element(self, node):
        print(node.value, end=" ")
        if node.left_child is not None:
            self._print_element(node.left_child)
        if node.right_child is not None:
            self._print_element(node.right_child)

    def print_tree(self):
        depth = self.depth()
        levels = [" " * (2 + 5 * int((2 ** (depth - (i+1)//3 - 2)))) for i in range(depth * 3 - 2)]
        for i in range(-1, -3, -1):
            levels[i] += " " * 2
            print(levels[i])
        for i in range(0, depth*3, 3):
            levels[i] = levels[i][:-1]
        self._print_node(self.root, levels, 0, depth)
        for level in levels:
            print(level)

    def _print_node(self, node, levels, current_level_index, depth):
        current_depth = current_level_index // 3 + 1
        levels[current_level_index] += str(node.value).center(3)

        if node.left_child is not None:
            levels[current_level_index + 1] += "|"
            levels[current_level_index + 2] += "|"
            if depth - current_depth == 1:
                levels[current_level_index + 2] += "¯" * 3
                self._print_node(node.left_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " " * 3
            else:
                levels[current_level_index + 2] += "¯" * (5 * 2 ** (depth - current_depth - 2))
                self._print_node(node.left_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " " * (5 * 2 ** (depth - current_depth - 1) - 3)

            levels[current_level_index + 1] += " " * (10 * 2 ** (depth - current_depth - 1) - 1)

        elif current_level_index < len(levels) - 2 and node.right_child is not None:
            if depth - current_depth == 1:
                levels[current_level_index + 2] += " " * 3
                levels[current_level_index + 3] += " " * 6

                levels[current_level_index + 2] += "¯" * 3
                levels[current_level_index + 2] += "|" + " " * 3
                self._print_node(node.right_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " "
            else:
                levels[current_level_index + 2] += " " * (5 * 2 ** (depth - current_depth - 2) - 1)
                levels[current_level_index + 2] += "¯" * (5 * 2 ** (depth - current_depth - 2))
                levels[current_level_index + 2] += "|" + " " * (5 * 2 ** (depth - current_depth - 1) - 1)
                self._print_node(node.right_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " " * (5 * 2 ** (depth - current_depth - 1) - 3)

                levels[current_level_index + 2] += " " * (5 * 2 ** (depth - current_depth - 2))
                levels[current_level_index + 3] += " " * (5 * 2 ** (depth - current_depth - 1) - 3)
            levels[current_level_index + 1] += "|"
            levels[current_level_index + 1] += " " * (10 * 2 ** (depth - current_depth - 1) - 1)

        if node.right_child is not None and node.left_child is not None:
            if depth - current_depth == 1:
                levels[current_level_index + 2] += "¯" * 2
                levels[current_level_index + 2] += "|" + " " * 3
                self._print_node(node.right_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " "
            else:
                levels[current_level_index + 2] += "¯" * (5 * 2 ** (depth - current_depth - 2) - 1)
                levels[current_level_index + 2] += "|" + " " * (5 * 2 ** (depth - current_depth - 1) - 1)
                self._print_node(node.right_child, levels, current_level_index + 3, depth)
                levels[current_level_index + 3] += " " * (5 * 2 ** (depth - current_depth - 1) - 3)

        elif current_level_index < len(levels) - 2 and node.left_child is not None:
            if depth - current_depth == 1:
                levels[current_level_index + 2] += " " * 6
                levels[current_level_index + 3] += " " * 4
            else:
                levels[current_level_index + 2] += " " * (5 * 2 ** (depth - current_depth - 2))
                levels[current_level_index + 3] += " " * (5 * 2 ** (depth - current_depth - 1) - 3)


class Node:

    def __init__(self, value, parent=None):
        self.left_child = None
        self.right_child = None
        self.parent = parent
        self.value = value


bst = BinarySearchTree()
elements = [9, 100, 10, 6, 8, 3, -2, 300, 4, 7]
for elem in elements:
    bst.insert(elem)

bst.print_elements()
print()
bst.delete(300)
bst.print_elements()
print()
bst.delete(4)
bst.print_elements()
print()
bst.delete(3)
bst.print_elements()
print()
bst.delete(6)
bst.print_elements()
