from models import Players, Heroes, Teams
from engine_1 import get_session 


class PlayerManager():
    def __init__(self):
        self.session = get_session()
        self.model = Players 

    def create_player(self,nickname,rank,level):
        player = self.model(nickname=nickname,rank=rank,level=level)
        self.session.add(player)
        self.session.commit()
        return player
    
    def get_players(self):
        players = self.session.query(self.model).all()
        return players
    

class HeroManager():
    def __init__(self):
        self.session = get_session()
        self.model = Heroes

    def create_player(self, player_id, name, description, level, abilities):
        hero = self.model(players_id=player_id, name=name, description=description, level=level, abilities=abilities)
        self.session.add(hero)
        self.session.commit()
        return hero
    
    def get_players(self):
        players = self.session.query(self.model).all()
        return players
    

class TeamManager():
    def __init__(self):
        self.session = get_session()
        self.model = Teams

    def create_team(self,players_id, name, rating):
        team = self.model(players_id=players_id, name=name, rating=rating)
        self.session.add(team)
        self.session.commit()
        return team
    
    def get_teams(self):
        teams = self.session.query(self.model).all()
        return teams

team_manager = TeamManager()
team_manager.create_team(1,'Team Subat', 7)


# Miracle = PlayerManager()
# Miracle.create_player("Miracle", "Master", "1000")

# hero_manager = HeroManager()
# hero_manager.create_player(1,"Invoker", "Master of elements", 1000, "Quas Wex Exort")

