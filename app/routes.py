# routes.py

from flask import Response, render_template, request, url_for
from app import app, queries, forms

from .models import *

@app.route('/', methods=['GET', 'POST'])
def index():
    form = forms.TeamForm(request.form, csrf_enabled=True)
    stats, probability = None, None
    if request.method == 'POST':
        team1 = form.team1.data
        team2 = form.team2.data
        year = form.year.data

        sum1 = sum(queries.get_team_stats(form.team1.data, year).values())
        sum2 = sum(queries.get_team_stats(form.team2.data, year).values())

        stats = {team1: sum1, team2: sum2}

        results = queries.get_game_results()
        probability = round(100 * (results['predicted']/results['total']), 2)
    context = {'form':form, 'total':stats, 'probability':probability}
    return render_template('index.html', context=context)
