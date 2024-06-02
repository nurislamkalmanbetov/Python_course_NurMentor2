# from utils import create_tables
# from manager import hero_manager #, Miracle
# from sys import argv



# if __name__ == '__main__':
#     data = argv
#     print(data)
#     if data[1] == "create":
#         create_tables()
#     elif data[1] == "player":
#         # Miracle.create_player("Miracle", "Master", "1000")
#         hero_manager.create_player(1,"Invoker", "Master of elements", 1000, "Quas Wex Exort")


# № 1 
# from utils import create_tables
# from manager import HeroManager
# from sys import argv

# if __name__ == '__main__':
#     data = argv
#     print(data)
#     if len(data) < 2:
#         print("Usage: python3 main.py <action>")
#     elif data[1] == "create":
#         create_tables()
#     elif data[1] == "player":
#         hero_manager = HeroManager()
#         # Assuming player_id is 1
#         hero_manager.create_player(1, "Invoker", "Master of elements", 1000, "Quas Wex Exort")

#2 
from utils import create_tables
from manager import TeamManager
from sys import argv

if __name__ == '__main__':
    data = argv
    print(data)
    if len(data) < 2:
        print("Usage: python3 main.py <action>")
    elif data[1] == "create":
        create_tables()
    elif data[1] == "teams":
        team_manager = TeamManager()
        # Assuming player_id is 1
        team_manager.create_team(1,'Otchayannye botaniki', 7)
