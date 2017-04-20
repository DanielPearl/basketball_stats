# models.py

from app import app, db
from sqlalchemy import Column, Integer, String

class Player(db.Model):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    player_id = Column(String(255))
    team_id = Column(String(255))
    year = Column(Integer)
    games_played = Column(Integer)
    games_played = Column(Integer)
    minutes_played = Column(Integer)
    points = Column(Integer)
    o_rebounds = Column(Integer)
    d_rebounds = Column(Integer)
    assists = Column(Integer)
    steals = Column(Integer)
    blocks = Column(Integer)
    turnovers = Column(Integer)
    personal_fouls = Column(Integer)
    field_goal_attempts = Column(Integer)
    field_goals = Column(Integer)
    free_throw_attempts = Column(Integer)
    free_throws = Column(Integer)
    three_point_attempts = Column(Integer)
    three_points = Column(Integer)

class Series(db.Model):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    year = Column(Integer)
    winner = Column(String(255))
    loser = Column(String(255))
    games_won = Column(Integer)
    games_lost = Column(Integer)
