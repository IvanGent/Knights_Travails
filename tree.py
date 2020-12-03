class Node:
    def __init__ (self, value):
        self._value = value
        self._parent = None
        self._children = []

    @property
    def value (self):
        return self._value

    @property
    def children (self):
        return self._children

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if self._parent is node:
            return
        if self._parent is not None:
            self._parent.remove_child(self)
        self._parent = node
        if node is not None:
            node.add_child(self)

    def add_child(self, node):
        if node not in self.children:
            self._children.append(node)
            if node.parent != self:
                node.parent = self

    def remove_child(self, node):
        if node in self._children:
            self._children.remove(node)
            node.parent = None

    def depth_search(self, value):
        if self._value == value:
            return self
        if not len(self._children):
            return None
        for child in self._children:
            result = child.depth_search(value)
            if result != None:
                return result
        return None

    def breadth_search(self, value):
        queue = []
        queue.append(self)
        currNode = None
        while queue:
            currNode = queue.pop(0)
            if currNode.value == value:
                return currNode
            for child in currNode.children:
                queue.append(child)
        return None


# node1 = Node("root1")
# print(node1.parent)
# print(node1.child)
# print(node1.value)
# node2 = Node("root2")
# node3 = Node("root3")
# '''
# node1, [value="root1", parent=None, children=[]]
# node2, [value="root2", parent=None, children=[]]
# node3, [value="root3", parent=None, children=[]]

# node1, [value="root1", parent=None, children=[node3]]
# node3, [value="root3", parent=node1, children=[]]
# parentSetter (self=node3, value=node1)
# '''


# node3.parent = node1
# node3.parent = node2

# print(node1.children)
# print(node2.children)
