# queries.py

from app import app, models, session
from sqlalchemy import or_
from .models import *

def get_team_choices():
    """
    Selects distinct teams as a tuple and appends to a list
    """
    team_list = []
    teams = session.query(Player.team_id).distinct()
    for team in teams:
        team_tuple = (team[0], team[0])
        team_list.append(team_tuple)
    return team_list

def get_year_choices():
    """
    Selects all years as a tuple and appends to a list
    """
    year_list = []
    for year in range(1946,2012):
        year_tuple = (year, year)
        year_list.append(year_tuple)
    return year_list

def get_team_players(team, year):
    """
    Selects all players on a team during a specific year
    """
    player_list = []
    players = session.query(Player).filter(Player.team_id == team).filter(Player.year == year).all()
    for player in players:
        player_list.append(player.player_id)
    return player_list

def get_stats_dictionary():
    """
    Returns dictionary of team stats
    """
    return {'team_id':0, 'games_played': 0, 'minutes_played': 0, 'points': 0, 'o_rebounds': 0, 'd_rebounds': 0, 'assists': 0, 'steals': 0, 'blocks': 0, 'turnovers': 0, 'personal_fouls': 0, 'field_goal_attempts': 0, 'field_goals': 0, 'free_throw_attempts': 0, 'free_throws': 0, 'three_point_attempts': 0, 'three_points': 0}

def get_team_stats(team, year):
    """
    Selects stats on a team during a specific year
    """
    stats = session.query(Player).filter(Player.team_id == team).filter(Player.year == year).filter(Player.games_played != 0).all()

    team_dict = get_stats_dictionary()

    if stats != None and stats != 0:
        for stat in stats:
                team_dict['team_id'] += stat.games_played
                team_dict['games_played'] += stat.games_played
                team_dict['minutes_played'] += stat.minutes_played
                team_dict['points'] += stat.points
                team_dict['o_rebounds'] += stat.o_rebounds
                team_dict['d_rebounds'] += stat.d_rebounds
                team_dict['assists'] += stat.assists
                team_dict['steals'] += stat.steals
                team_dict['blocks'] += stat.blocks
                team_dict['turnovers'] += stat.turnovers
                # team_dict['field_goal_attempts'] += stat.field_goal_attempts
                team_dict['field_goals'] += stat.field_goals
                # team_dict['free_throw_attempts'] += stat.free_throw_attempts
                team_dict['free_throws'] += stat.free_throws
                # team_dict['three_point_attempts'] += stat.three_point_attempts
                team_dict['three_points'] += stat.three_points
    return team_dict

def get_game_results():
    results = session.query(Series.winner, Series.loser, Series.year)
    result_dict = {'predicted':0, 'total':0}

    for result in results:
        winner_stats = sum(get_team_stats(result.winner, result.year).values())
        loser_stats = sum(get_team_stats(result.loser, result.year).values())
        if winner_stats != 0 and loser_stats != 0:
            if winner_stats > loser_stats:
                result_dict['predicted'] += 1
            result_dict['total'] += 1
    return result_dict
