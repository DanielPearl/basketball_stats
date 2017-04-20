# routes.py

from flask import Response, render_template, request, url_for
from app import app, queries, forms

from .models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.TeamForm(request.form, csrf_enabled=True)
    sum1, sum2, team1_wins, team2_wins, results = None, None, None, None, None
    if request.method == 'POST':
        team1 = form.team1.data
        team2 = form.team2.data

        year = form.year.data

        stats1 = queries.get_team_stats(team1, year)
        stats2 = queries.get_team_stats(team2, year)

        sum1 = sum(stats1.values())
        sum2 = sum(stats2.values())
        stats = {team1: sum1, team2: sum2}

        results = queries.get_game_results(team1, team2, year)

    context = {'form':form, 'total':stats, 'results':results}
    return render_template('index.html', context=context)
