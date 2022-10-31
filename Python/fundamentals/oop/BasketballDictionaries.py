class Player:
    def __init__(self, player_dict):
        self.name = player_dict["name"]
        self.age = player_dict["age"]
        self.position = player_dict["position"]
        self.team = player_dict["team"]


kevin = {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
}
player_kevin = Player(kevin)
print(player_kevin.name)
print(player_kevin.age)
print(player_kevin.position)
print(player_kevin.team)

jason = {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
}
player_jason = Player(jason)
print(player_jason.name)
print(player_jason.age)
print(player_jason.position)
print(player_jason.team)

kyrie = {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
}
player_kyrie = Player(kyrie)
print(player_kyrie.name)
print(player_kyrie.age)
print(player_kyrie.position)
print(player_kyrie.team)


players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32, "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33, "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32, "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "", 
        "age":16, 
        "position": "P", 
        "team": "en"
    }
]

new_team = []
for player in players:
    player_dict = Player(player)
    new_team.append(player_dict)

print(new_team)





