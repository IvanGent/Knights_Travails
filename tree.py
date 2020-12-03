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

    def add_child(self, node):
        if node not in self._children:
            self._children.append(node)
            node.parent = self

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value
        if value is not None:
            self.parent.add_child(self)

    def remove_child(self, node):
        self._children.remove(node)
        node.parent = None
