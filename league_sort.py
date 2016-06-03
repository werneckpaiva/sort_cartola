import random
import collections
from counting import Counting

NUM_TEAMS = 5000000
NUM_LEAGUES = 500000
MAX_LEAGUES = 10
random.seed(1)

def str_team(team, with_leagues=False):
    return u"%s - %.2f $%.2f [%s]" % (team.key, team.points, team.budget, ", ".join([str(l) for l in team.leagues]) if with_leagues else "")

def retrieve_global_league():
    Team = collections.namedtuple('Team', 'key points budget leagues') # mor memory efficient
    leagues = range(1, NUM_LEAGUES+1)
    data = [Team(key=i,
                 points=random.uniform(1, 80), 
                 budget=random.uniform(50, 150),
                 leagues = random.sample(leagues, random.randint(1, MAX_LEAGUES))
                 )
            for i in xrange(NUM_TEAMS)]
    return data


def sort_league(league):
    league.sort(key=lambda l:l.points, reverse=True)


def generate_sorted_leagues(global_league):
    leagues = [[] for _ in xrange(NUM_LEAGUES)]
    for t in global_league:
        for l in t.leagues:
            leagues[l-1].append(t)
    return leagues

def print_league(league, with_leagues=False):
    for t in league[:10]:
        print str_team(t, with_leagues)

counting = Counting()

def main():
    print "Generating data..."
    print "Num teams: %s" % NUM_TEAMS
    print "Num leagues: %s" % NUM_LEAGUES
    print "MAX leagues per team: %s" % MAX_LEAGUES
    with counting:
        global_league = retrieve_global_league()
    print "Sorting global league..."
    with counting:
        sort_league(global_league)
    print "Sorting all leagues..."
    with counting:
        sorted_leagues = generate_sorted_leagues(global_league)
    print ""
    print "Liga 1"
    print_league(sorted_leagues[2])


main()