from flask import render_template, redirect, url_for, abort, flash, request
from flask_login import login_required, current_user
from . import main
from .. import db
from ..models import User, Achievement
from .forms import AchievementForm, EditAchievementForm

#@main.route('/')
#def signup():
#	return render_template('signup.html')

#@main.route('/db', methods = ['GET', 'POST'])
#def index():

	# ----- more db stuff probably goes here ------

#	return render_template('index.html')

@login_required
@main.route('/profile')
def profile():
    achievement = Achievement.query.order_by(Achievement.date_created).count()
    completed = Achievement.query.filter(Achievement.isComplete).count()

    inProgress = achievement - completed 

    return render_template('profile.html', name=current_user.name, achievement=achievement, completed=completed, inProgress=inProgress)

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

@login_required
@main.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    achievement = Achievement.query.get_or_404(id)
    form = EditAchievementForm(achievement=achievement)

    if form.validate_on_submit():
        if form.submit.data:
            achievement.achievement = form.achievement.data
            achievement.progress = form.progress.data
            achievement.isComplete = form.isComplete.data
            db.session.add(achievement)
            db.session.commit()
            flash('Achievement updated.')
            return redirect(url_for('.index'))
        else:
            return redirect(url_for('.index'))

    form.achievement.data = achievement.achievement
    form.progress.data = achievement.progress
    form.isComplete.data = achievement.isComplete

    return render_template('update.html', form=form)

@login_required
@main.route('/add', methods=['GET', 'POST'])
def achievements():
    achievement = None
    form = AchievementForm()
    if form.validate_on_submit():
        achievement = Achievement(achievement=form.achievement.data,
                                  progress=form.progress.data,
                                  isComplete=form.isComplete.data)
        db.session.add(achievement)
        db.session.commit()
        return redirect(url_for('.index'))

    return render_template('new.html', form=form)

@main.route('/', methods=['GET', 'POST'])
def index():
    achievements = Achievement.query.order_by(Achievement.date_created)
    return render_template("index.html", achievements=achievements)