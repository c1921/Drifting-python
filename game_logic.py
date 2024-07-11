import random
from items import Item, Food, Armor, Weapon
from character import Character
import config
from PyQt6.QtCore import QTime

class GameLogic:
    def __init__(self):
        # 初始化游戏状态
        self.character = Character("Hero")  # 初始化角色
        self.speed_per_minute = config.SPEED_PER_MINUTE
        self.hunger = config.INITIAL_HUNGER
        self.thirst = config.INITIAL_THIRST
        self.fatigue = config.INITIAL_FATIGUE
        self.mood = config.INITIAL_MOOD
        self.is_traveling = True
        self.day_count = 1
        self.distance = 0.0
        self.inventory = self.initialize_inventory()
        self.log = []
        self.game_time = QTime(0, 0)  # 初始化时间
        self.companions = []  # 新增同路人列表

    def initialize_inventory(self):
        inventory = {}
        for item_name, quantity in config.INITIAL_INVENTORY.items():
            for item_type, items in config.ITEM_DEFINITIONS.items():
                if item_name in items:
                    item_data = items[item_name]
                    if item_type == "Food":
                        hunger_restore, thirst_restore, weight, value = item_data
                        inventory[item_name] = Food(item_name, quantity, hunger_restore, thirst_restore, weight, value)
                    elif item_type == "Weapon":
                        attack = item_data["attack"]
                        weight = item_data["weight"]
                        value = item_data["value"]
                        inventory[item_name] = Weapon(item_name, quantity, attack, weight, value)
                    # 可根据需要添加其他类型
        return inventory

    def update_time_and_distance(self):
        if self.is_traveling:
            self.distance += self.speed_per_minute
            self.thirst -= 0.1
            self.hunger -= 0.2
            self.fatigue -= 0.5
            self.mood -= 0.1
            self.random_event()
        else:
            self.thirst -= 0.01
            self.hunger -= 0.02
            self.fatigue -= 0.05
            self.mood -= 0.05

        self.thirst = max(self.thirst, 0)
        self.hunger = max(self.hunger, 0)
        self.fatigue = max(self.fatigue, 0)
        self.mood = max(self.mood, 0)

    def random_event(self):
        # 50%概率获得一个苹果
        if random.random() < 0.5:
            if "Apple" in self.inventory:
                self.inventory["Apple"].quantity += 1
            else:
                hunger_restore, thirst_restore, weight, value = config.ITEM_DEFINITIONS["Food"]["Apple"]
                self.inventory["Apple"] = Food("Apple", 1, hunger_restore, thirst_restore, weight, value)
            self.log.append("You found an apple!")
        
        # 10%概率遇到新角色
        if random.random() < 0.1:
            new_companion = Character.random_character()
            self.companions.append(new_companion)
            self.log.append(f"You met {new_companion.name}!")

    def discard_item(self, item_name):
        if item_name in self.inventory:
            del self.inventory[item_name]
            self.log.append(f"You discarded {item_name}")

    def eat_item(self, item_name):
        if item_name in self.inventory and isinstance(self.inventory[item_name], Food):
            food = self.inventory[item_name]
            self.hunger = min(self.hunger + food.hunger_restore, 100)
            self.thirst = min(self.thirst + food.thirst_restore, 100)
            food.quantity -= 1
            if food.quantity <= 0:
                del self.inventory[item_name]
            self.log.append(f"You ate an {item_name}")
