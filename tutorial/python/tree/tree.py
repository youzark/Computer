#!/usr/bin/env python
class tree_node:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        self.level = 0
        
    def get_level(self):
        return self.level

    def add_leaf(self,child):
        child.parent = self
        child.level = self.level + 1
        self.children.append(child)

    def print_tree(self):
        if not self.children:
            print('  '*self.level,'-',self.data)
        else:
            print('  '*self.level,'+',self.data)
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = tree_node("Electronics")
    Laptop = tree_node("Laptop")
    cell_phone = tree_node("Cell Phone")
    tv = tree_node("TV")
    root.add_leaf(Laptop)
    root.add_leaf(cell_phone)
    root.add_leaf(tv)
    Laptop.add_leaf(tree_node("ipad"))
    Laptop.add_leaf(tree_node("huawei"))
    Laptop.add_leaf(tree_node("surface"))
    return root

if __name__ == "__main__":
    root = build_product_tree()
    root.print_tree()
