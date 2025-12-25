import sys
from PyQt6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

# Пример вложенной структуры данных с произвольной глубиной (списки, словари, простые объекты)
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
    if isinstance(items, dict):
        for key, value in items.items():
            item = QTreeWidgetItem([key])  # Просто имя, без типа
            parent_item.addChild(item)
            add_items_recursive(item, value)
    elif isinstance(items, list):
        for item_data in items:
            if isinstance(item_data, (dict, list)):
                # Для вложенных структур создаём "папку" или используем заголовок
                item = QTreeWidgetItem(["[Nested]"])  # Любая метка для вложенности
                parent_item.addChild(item)
                add_items_recursive(item, item_data)
            else:
                # Для простых объектов
                item = QTreeWidgetItem([str(item_data)])  # Преобразуем в строку
                parent_item.addChild(item)

app = QApplication(sys.argv)

tree = QTreeWidget()
tree.setColumnCount(1)  # Убираем столбец Type, оставляем только Name
tree.setHeaderLabels(["Name"])

root_item = QTreeWidgetItem(["TreeRoot"])  # Корневой элемент дерева
tree.insertTopLevelItem(0, root_item)
add_items_recursive(root_item, data)

tree.show()
sys.exit(app.exec())
