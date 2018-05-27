# %load q06_bowled_players/build.py
# Default Imports
from greyatomlib.python_getting_started.q01_read_data.build import read_data
data = read_data()

# Your Solution
def bowled_out(data=data):
    bowled_players = []
    deliveries = data['innings'][1]['2nd innings']['deliveries']
    for b in (deliveries):
        data1=list(b.values())
        if 'wicket' in data1[0].keys():
            if data1[0]['wicket']['kind']=='bowled':
                bowled_players.append(data1[0]['batsman'])

    return bowled_players

bowled_out()




