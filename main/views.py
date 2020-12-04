from flask import render_template, redirect, url_for, abort, flash, request
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Achievement
from .forms import AchievementForm

@main.route('/')
def signup():
	return render_template('signup.html')

@main.route('/db', methods = ['GET', 'POST'])
def index():

	# ----- more db stuff probably goes here ------

	return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
	return render_template('profile.html', name=current_user.name)

# ------ CRUD functions ------
@main.route('/delete/<int:id>')
def delete(id):
    achievement_to_delete = Achievement.query.get_or_404(id)

    try:
        db.session.delete(achievement_to_delete)
        db.session.commit()
        return redirect('/')
        
    except:
        return "There was a problem deleting the achievement"

@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    achievement_to_update = Achievement.query.get_or_404(id)

    if request.method == 'POST':
        achievement_to_update.achievement = request.form['achievement']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was a problem updating the achievement'
    else:
        return render_template('update.html', achievement_to_update=achievement_to_update)

@login_required
@main.route('/', methods=['GET', 'POST'])
def achievements():
    achievement = None
    form = AchievementForm()

    if request.method == "POST":
        achievement = form.achievement.data
        new_achievement = Achievement(achievement=achievement)
        try:
            db.session.add(new_achievement)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error adding an achievement'    
    else:
        achieve = Achievement.query.order_by(Achievement.date_created)
        return render_template('index.html', form=form, achieve=achieve)