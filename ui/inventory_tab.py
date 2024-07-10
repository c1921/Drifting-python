from PyQt6.QtWidgets import (
    QLabel, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QAbstractItemView
)
from PyQt6.QtCore import Qt

class InventoryTab(QWidget):
    def __init__(self, game, show_context_menu):
        super().__init__()

        self.game = game
        self.show_context_menu = show_context_menu

        self.inventory_table = QTableWidget(self)
        self.inventory_table.setColumnCount(4)
        self.inventory_table.setHorizontalHeaderLabels(["Item", "Quantity", "Weight", "Value"])
        self.inventory_table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.inventory_table.customContextMenuRequested.connect(self.show_context_menu)
        self.inventory_table.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.inventory_table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

        self.weight_label = QLabel(self)
        self.max_weight = 100  # 设置负重上限
        self.update_weight_label()

        inventory_layout = QVBoxLayout()
        inventory_layout.addWidget(self.inventory_table)
        inventory_layout.addWidget(self.weight_label)

        self.setLayout(inventory_layout)

    def update_inventory(self):
        self.inventory_table.setRowCount(0)
        total_weight = 0
        for item in self.game.inventory.values():
            row_position = self.inventory_table.rowCount()
            self.inventory_table.insertRow(row_position)
            self.inventory_table.setItem(row_position, 0, QTableWidgetItem(item.name))
            self.inventory_table.setItem(row_position, 1, QTableWidgetItem(str(item.quantity)))
            self.inventory_table.setItem(row_position, 2, QTableWidgetItem(str(item.weight)))
            self.inventory_table.setItem(row_position, 3, QTableWidgetItem(str(item.value)))
            total_weight += item.weight * item.quantity
        self.update_weight_label(total_weight)

    def update_weight_label(self, current_weight=0):
        self.weight_label.setText(f"Weight: {current_weight} / {self.max_weight}")