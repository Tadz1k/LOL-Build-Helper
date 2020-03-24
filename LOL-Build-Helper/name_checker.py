champion_list = ["Vi", "Aphelios", "Jinx", "Lux", "Evelynn"]
current_champion = "None"
selected = False


class NameResolver:
    @staticmethod
    def check_name(name):
        print(name)
        for champion in champion_list:
            global selected
            global current_champion
            if champion.upper() == name.upper():
                current_champion = champion
                selected = True
                print("OK")
                break
            else:
                selected = False

    @staticmethod
    def get_champion():
        global current_champion
        return current_champion

    @staticmethod
    def is_selected():
        global selected
        return selected

    @staticmethod
    def false_selected():
        global selected
        selected = False


