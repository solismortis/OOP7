import sys
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

# Change data to lists of lists (no dictionaries)
test_data = [
    [["obj1", "obj2", ["deeper1", "deeper2"]], "obj3", ["obj4", "obj5"]],
    ["obj6", ["obj7", ["deeper3", "deeper4", "even_deeper"]], "obj8"]
]

def add_items_recursive(parent_item, items):
    if isinstance(items, list):
        for value in items:
            item = QTreeWidgetItem([str(value), str(type(value))])
            parent_item.addChild(item)
            add_items_recursive(item, value)

def update_tree(tree, new_data):
    # Clear all existing top-level items
    tree.clear()
    # Create a new root item
    root_item = QTreeWidgetItem(["TreeRoot", str(type(new_data))])
    tree.insertTopLevelItem(0, root_item)
    # Add new data recursively
    add_items_recursive(root_item, new_data)

app = QApplication(sys.argv)

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

# Initial population
update_tree(tree, test_data)

# Example: Update with new data later (replace with your logic)
new_data = [
    ["new_obj1", ["new_sub", ["even_newer"]]],
    ["another_obj"]
]
# To update when container changes, call update_tree(tree, new_data)
update_tree(tree, new_data)
tree.show()
sys.exit(app.exec())
