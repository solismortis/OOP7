import sys
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


data = {
    "Root1": [
        {"Sub1": ["obj1", "obj2", {"Deep1": ["deeper1", "deeper2"]}]},
        "obj3",
        {"Sub2": ["obj4", "obj5"]}
    ],
    "Root2": [
        "obj6",
        {"Sub3": ["obj7", {"Deep2": ["deeper3", "deeper4", "even_deeper"]}]},
        "obj8"
    ]
}


def add_items_recursive(parent_item, items):
    if str(type(items)) == "<class 'dict'>":
        for key, value in items.items():
            item = QTreeWidgetItem([key, str(type(key))])
            parent_item.addChild(item)
            add_items_recursive(item, value)
    elif str(type(items)) == "<class 'list'>":
        for value in items:
            item = QTreeWidgetItem([str(value), str(type(value))])
            parent_item.addChild(item)
            add_items_recursive(item, value)


app = QApplication(sys.argv)

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])

root_item = QTreeWidgetItem(["TreeRoot", str(type(data))])
tree.insertTopLevelItem(0, root_item)
add_items_recursive(root_item, data)

tree.show()
sys.exit(app.exec())
