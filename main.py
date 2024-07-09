import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget, QListWidget, QListWidgetItem
from PyQt6.QtCore import QTimer, QTime

class AdventureRPG(QMainWindow):
    def __init__(self):
        super().__init__()

        # 初始化时间和距离
        self.game_time = QTime(0, 0)
        self.day_count = 1
        self.distance = 0.0
        self.speed_per_minute = 80

        # 初始化物品栏
        self.inventory = {"Apple": 10}

        # 设置窗口
        self.setWindowTitle("Adventure RPG")
        self.setGeometry(100, 100, 400, 300)

        # 创建标签
        self.time_label = QLabel(self)
        self.distance_label = QLabel(self)
        self.update_labels()

        # 创建物品栏列表
        self.inventory_list = QListWidget(self)
        self.update_inventory()

        # 布局
        layout = QVBoxLayout()
        layout.addWidget(self.time_label)
        layout.addWidget(self.distance_label)
        layout.addWidget(self.inventory_list)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # 设置计时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time_and_distance)
        self.timer.start(1000)  # 每秒触发一次

    def update_time_and_distance(self):
        # 更新游戏时间
        self.game_time = self.game_time.addSecs(60)
        if self.game_time.hour() == 0 and self.game_time.minute() == 0:
            self.day_count += 1

        # 更新距离
        self.distance += self.speed_per_minute

        # 更新标签显示
        self.update_labels()

    def update_labels(self):
        time_text = f"Day {self.day_count}, {self.game_time.toString('HH:mm')}"
        distance_text = f"Distance traveled: {self.distance:.2f} meters"
        self.time_label.setText(time_text)
        self.distance_label.setText(distance_text)

    def update_inventory(self):
        self.inventory_list.clear()
        for item, quantity in self.inventory.items():
            self.inventory_list.addItem(f"{item}: {quantity}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    rpg = AdventureRPG()
    rpg.show()
    sys.exit(app.exec())
