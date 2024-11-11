import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem


# Define a dictionary with project structures to display the information as a tree, with files belonging to each project
data = {"Project A": ["file_a.py", "file_a.txt", "something.xls"],
        "Project B": ["file_b.csv", "photo.jpg"],
        "Project C": []}

# initialize the QApplication sigleton
app = QApplication()

tree = QTreeWidget()
tree.setColumnCount(2)
tree.setHeaderLabels(["Name", "Type"])


items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split(".")[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)

tree.insertTopLevelItems(0, items)

# show the tree and execute the QApplication
tree.show()
sys.exit(app.exec())