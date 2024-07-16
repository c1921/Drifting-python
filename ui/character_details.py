from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QCoreApplication

class CharacterDetails(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)

        self.name_label = QLabel(self)
        self.layout.addWidget(self.name_label)

        self.affinity_label = QLabel(self)
        self.layout.addWidget(self.affinity_label)

        self.attributes_title = QLabel(QCoreApplication.translate("CharacterDetails", "Attributes:"))
        self.layout.addWidget(self.attributes_title)

        self.strength_label = QLabel(self)
        self.agility_label = QLabel(self)
        self.charisma_label = QLabel(self)
        self.intelligence_label = QLabel(self)
        self.layout.addWidget(self.strength_label)
        self.layout.addWidget(self.agility_label)
        self.layout.addWidget(self.charisma_label)
        self.layout.addWidget(self.intelligence_label)

        self.skills_title = QLabel(QCoreApplication.translate("CharacterDetails", "Skills:"))
        self.layout.addWidget(self.skills_title)

        self.running_label = QLabel(self)
        self.riding_label = QLabel(self)
        self.management_label = QLabel(self)
        self.eloquence_label = QLabel(self)
        self.gathering_label = QLabel(self)
        self.layout.addWidget(self.running_label)
        self.layout.addWidget(self.riding_label)
        self.layout.addWidget(self.management_label)
        self.layout.addWidget(self.eloquence_label)
        self.layout.addWidget(self.gathering_label)

        self.traits_title = QLabel(QCoreApplication.translate("CharacterDetails", "Traits:"))
        self.layout.addWidget(self.traits_title)

        self.traits_labels = []

        self.setLayout(self.layout)

    def update_details(self, character, player_character):
        self.name_label.setText(QCoreApplication.translate("CharacterDetails", "Name: {name}").format(name=character.name))
        
        # 计算并显示好感度
        affinity_to_player = character.calculate_affinity(player_character)
        affinity_from_player = player_character.calculate_affinity(character)
        self.affinity_label.setText(QCoreApplication.translate("CharacterDetails", "Affinity: {to_player} | {from_player}").format(to_player=affinity_to_player, from_player=affinity_from_player))
        
        self.strength_label.setText(QCoreApplication.translate("CharacterDetails", "Strength: {value}").format(value=character.attributes["Strength"]))
        self.agility_label.setText(QCoreApplication.translate("CharacterDetails", "Agility: {value}").format(value=character.attributes["Agility"]))
        self.charisma_label.setText(QCoreApplication.translate("CharacterDetails", "Charisma: {value}").format(value=character.attributes["Charisma"]))
        self.intelligence_label.setText(QCoreApplication.translate("CharacterDetails", "Intelligence: {value}").format(value=character.attributes["Intelligence"]))
        self.running_label.setText(QCoreApplication.translate("CharacterDetails", "Running: {value}").format(value=character.skills["Running"]))
        self.riding_label.setText(QCoreApplication.translate("CharacterDetails", "Riding: {value}").format(value=character.skills["Riding"]))
        self.management_label.setText(QCoreApplication.translate("CharacterDetails", "Management: {value}").format(value=character.skills["Management"]))
        self.eloquence_label.setText(QCoreApplication.translate("CharacterDetails", "Eloquence: {value}").format(value=character.skills["Eloquence"]))
        self.gathering_label.setText(QCoreApplication.translate("CharacterDetails", "Gathering: {value}").format(value=character.skills["Gathering"]))

        # 更新特质显示
        for label in self.traits_labels:
            self.layout.removeWidget(label)
            label.deleteLater()
        self.traits_labels = []
        for trait in character.traits:
            label = QLabel(f"{trait.name}", self)
            self.traits_labels.append(label)
            self.layout.addWidget(label)
