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
            self._childen.append(node)
            node.parent = self
        

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        if value is not None:
            self._parent = value
    
    def remove_child(self, node):
        self._children.remove(node)
        node.parent = None
    