from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QHeaderView, QMenu
from PyQt6.QtCore import Qt, QCoreApplication, pyqtSignal

class TeamTab(QWidget):
    character_selected = pyqtSignal(object)

    def __init__(self, game):
        super().__init__()

        self.game = game

        self.layout = QVBoxLayout(self)
        self.team_table = QTableWidget(self)
        self.team_table.setColumnCount(4)
        self.team_table.setHorizontalHeaderLabels([
            QCoreApplication.translate("TeamTab", "Name"),
            QCoreApplication.translate("TeamTab", "Gender"),
            QCoreApplication.translate("TeamTab", "Affinity to Player"),
            QCoreApplication.translate("TeamTab", "Affinity from Player")
        ])
        self.team_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.team_table.cellClicked.connect(self.on_cell_clicked)

        self.layout.addWidget(self.team_table)
        self.setLayout(self.layout)

        self.update_team_table()

    def update_team_table(self):
        # 保存当前选中单元格
        selected_items = self.team_table.selectedItems()
        selected_cell = None
        if selected_items:
            selected_cell = (self.team_table.row(selected_items[0]), self.team_table.column(selected_items[0]))

        self.team_table.setRowCount(0)

        # 插入玩家角色
        self.insert_character_to_table(self.game.character, 0)

        # 插入团队角色
        for i, companion in enumerate(self.game.team[1:], start=1):  # 排除玩家角色
            self.insert_character_to_table(companion, i)

        # 恢复之前的选中单元格
        if selected_cell:
            self.team_table.setCurrentCell(selected_cell[0], selected_cell[1])

    def insert_character_to_table(self, character, row):
        self.team_table.insertRow(row)

        name_item = QTableWidgetItem(character.name)
        name_item.setData(Qt.ItemDataRole.UserRole, character.id)
        name_item.setFlags(name_item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # 不可编辑

        gender_symbol = "♂" if character.gender == "male" else "♀"
        gender_item = QTableWidgetItem(gender_symbol)
        gender_item.setFlags(gender_item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # 不可编辑

        affinity_to_player = character.calculate_affinity(self.game.character, self.game.character)
        affinity_to_player_item = QTableWidgetItem(str(affinity_to_player))
        affinity_to_player_item.setFlags(affinity_to_player_item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # 不可编辑

        affinity_from_player = self.game.character.calculate_affinity(character, character)
        affinity_from_player_item = QTableWidgetItem(str(affinity_from_player))
        affinity_from_player_item.setFlags(affinity_from_player_item.flags() ^ Qt.ItemFlag.ItemIsEditable)  # 不可编辑

        self.team_table.setItem(row, 0, name_item)
        self.team_table.setItem(row, 1, gender_item)
        self.team_table.setItem(row, 2, affinity_to_player_item)
        self.team_table.setItem(row, 3, affinity_from_player_item)

    def on_cell_clicked(self, row, column):
        character_id = self.team_table.item(row, 0).data(Qt.ItemDataRole.UserRole)
        character = next((comp for comp in self.game.team if comp.id == character_id), self.game.character)
        self.character_selected.emit(character)
