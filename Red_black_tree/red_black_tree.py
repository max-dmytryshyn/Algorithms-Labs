from colorama import Fore


class Node:

    def __init__(self, value, parent=None, left_child=None, right_child=None, is_red=True):
        self.value = value
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.is_red = is_red


class RedBlackTree:

    def __init__(self):
        self.root = None

    def _left_rotate(self, node):
        if node.parent:
            if node.parent.left_child == node:
                node.parent.left_child = node.right_child
            else:
                node.parent.right_child = node.right_child
        else:
            self.root = node.right_child

        node.right_child.parent = node.parent
        node.parent = node.right_child
        node.right_child = node.right_child.left_child
        node.parent.left_child = node
        if node.right_child:
            node.right_child.parent = node

    def _right_rotate(self, node):
        if node.parent:
            if node.parent.left_child == node:
                node.parent.left_child = node.left_child
            else:
                node.parent.right_child = node.left_child
        else:
            self.root = node.left_child

        node.left_child.parent = node.parent
        node.parent = node.left_child
        node.left_child = node.left_child.right_child
        node.parent.right_child = node
        if node.left_child:
            node.left_child.parent = node

    def _find_brother(self, node):
        if node.parent is None:
            return None

        if node.parent.left_child == node:
            return node.parent.right_child
        else:
            return node.parent.left_child

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
            self.root = Node(value, is_red=False)
            return

        new_node = self._insert(self.root, value)
        print("Inserting node", new_node.value)
        self._insert_balance(new_node)

    def _insert(self, current_node, value):
        if value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = Node(value, parent = current_node)
            return self._insert(current_node.right_child, value)

        if value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value, parent = current_node)
            return self._insert(current_node.left_child, value)

        return current_node

    def _insert_balance(self, node):
        if not node.parent:
            self.root.is_red = False
            return

        if not node.parent.parent or not node.parent.is_red:
            return

        if self._find_brother(node.parent) and self._find_brother(node.parent).is_red:
            node.parent.is_red = False
            self._find_brother(node.parent).is_red = False
            node.parent.parent.is_red = True
            self._insert_balance(node.parent.parent)

        else:
            if node.parent.parent.left_child == node.parent:
                if node.parent.right_child == node:
                    self._left_rotate(node.parent)
                    node = node.left_child
                    print("left rotation")
                self._right_rotate(node.parent.parent)
                print("right rotation")
                node.parent.is_red, self._find_brother(node).is_red = self._find_brother(
                    node).is_red, node.parent.is_red

            else:
                if node.parent.left_child == node:
                    self._right_rotate(node.parent)
                    print("right rotation")
                    node = node.right_child
                self._left_rotate(node.parent.parent)
                print("left rotation")
                node.parent.is_red, self._find_brother(node).is_red = self._find_brother(
                    node).is_red, node.parent.is_red

    def delete(self, value):
        print("Deleting", value)
        node_to_delete = self._search(self.root, value)
        if not node_to_delete:
            raise KeyError()

        if not node_to_delete.left_child and not node_to_delete.right_child:
            self._delete_leaf(node_to_delete)

        elif not node_to_delete.left_child or not node_to_delete.right_child:
            self._delete_node_with_one_child(node_to_delete)

        else:
            self._delete_node_with_two_children(node_to_delete)

    def _balance_double_black_node(self, double_black_node):
        if not double_black_node.parent:
            return

        brother = self._find_brother(double_black_node)
        if not brother.is_red:
            if brother.parent.left_child == brother:
                if brother.left_child and brother.left_child.is_red:
                    brother.left_child.is_red = False
                    self._right_rotate(brother.parent)
                    print("right rotation")

                elif brother.right_child and brother.right_child.is_red:
                    brother.right_child.is_red = False
                    brother.is_red = True
                    self._left_rotate(brother)
                    print("left rotation")
                    brother = brother.parent
                    brother.left_child.is_red = False
                    self._right_rotate(brother.parent)
                    print("right rotation")

                else:
                    brother.is_red = True
                    if brother.parent.is_red:
                        brother.parent.is_red = False
                    else:
                        self._balance_double_black_node(double_black_node.parent)

            else:
                if brother.right_child and brother.right_child.is_red:
                    brother.right_child.is_red = False
                    self._left_rotate(brother.parent)
                    print("left rotation")

                elif brother.left_child and brother.left_child.is_red:
                    brother.left_child.is_red = False
                    brother.is_red = True
                    self._right_rotate(brother)
                    print("right rotation")
                    brother = brother.parent
                    brother.right_child.is_red = False
                    self._left_rotate(brother.parent)
                    print("left rotation")

                else:
                    brother.is_red = True
                    if brother.parent.is_red:
                        brother.parent.is_red = False
                    else:
                        self._balance_double_black_node(double_black_node.parent)

        else:
            brother.is_red = not brother.is_red
            brother.parent.is_red = not brother.parent.is_red

            if brother.parent.left_child == brother:
                self._right_rotate(brother.parent)
                brother = brother.right_child

            else:
                self._left_rotate(brother.parent)
                brother = brother.left_child

            self._balance_double_black_node(double_black_node)

    def _delete_leaf(self, node):
        if not node.parent:
            self.root = None
            return

        if not node.is_red:
            self._balance_double_black_node(node)

        if node.parent.left_child == node:
            node.parent.left_child = None
        else:
            node.parent.right_child = None

    def _delete_node_with_one_child(self, node):
        if node.left_child:
            node.left_child.is_red = False
            node.left_child.parent = node.parent

            if node.parent:
                if node.parent.left_child == node:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child
            else:
                self.root = node.left_child

        else:
            node.right_child.is_red = False
            node.right_child.parent = node.parent

            if node.parent:
                if node.parent.left_child == node:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child
            else:
                self.root = node.right_child

    def _delete_node_with_two_children(self, node):
        node_to_swap = self._max_node(node.left_child)
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

    def depth(self):
        return self._depth(self.root, 0)

    def _depth(self, node, depth):
        max_depth = depth
        if node.left_child is not None:
            max_depth = max(max_depth, self._depth(node.left_child, depth + 1))
        if node.right_child is not None:
            max_depth = max(max_depth, self._depth(node.right_child, depth + 1))
        return max_depth

    def print_level_order(self):
        if self.root is None:
            print("Tree is empty")
            return

        queue = [self.root]
        current_depth = 0

        while current_depth <= self.depth():
            current_level_length = len(queue)
            current_level_counter = 0
            #print(3 * (2 ** (self.depth() - current_depth)) * " ", end="")

            while current_level_counter < current_level_length:
                node = queue.pop(0)

                if node:
                    if node.is_red:
                        print(Fore.RED, end="")
                        print((str(node.value) + "(" + str(node.parent.value) + ")"), end= "")
                        #print((6 * (2 ** (self.depth() - current_depth) - 1) + 1) * " ", end="")
                        print(Fore.RESET, end=" ")
                    else:

                        if node.parent:
                            print((str(node.value)+"(" + str(node.parent.value) + ")"), end=" ")
                        else:
                            print(str(node.value).center(5), end=" ")

                        #print((6 * (2 ** (self.depth() - current_depth) - 1) + 1) * " ", end="")

                    if node.left_child:
                        queue.append(node.left_child)
                    else:
                        queue.append(None)

                    if node.right_child:
                        queue.append(node.right_child)
                    else:
                        queue.append(None)
                else:
                    pass
                    #print((6 * (2 ** (self.depth() - current_depth) - 1) + 5) * " ", end=" ")

                current_level_counter += 1

            print()
            current_depth += 1


rdt = RedBlackTree()
elements = [2,4,6,8,10,12,14,16,18,20,17]
for elem in elements:
    rdt.insert(elem)
    rdt.print_level_order()
    print("----------------------------")

for elem in elements[::-1]:
    rdt.delete(elem)
    rdt.print_level_order()
    print("----------------------------")


