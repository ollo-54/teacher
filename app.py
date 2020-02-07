from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)


def read_json(file_name):
    with open(file_name, 'r', encoding='utf8') as r_data:
        data_json = json.load(r_data)
    return data_json


def write_json(file_name, data_json):
    with open(file_name, 'w', encoding='utf8') as w_data:
        json.dump(data_json, w_data)


profiles = read_json('data.json')


@app.route('/')
@app.route('/index/')
def main():
    choice_teacher = []
    for i in profiles['teachers']:
        choice_teacher.append(i)
    choice_teachers = random.sample(choice_teacher, 6)
    main_page = render_template('index.html', choice_teachers=choice_teachers, profiles=profiles)
    return main_page


@app.route('/goals/<goal>/')
def goals(goal):
    teacher_for_goal = []
    all_teacher = profiles['teachers']

    for teacher in all_teacher:
        if goal in teacher['goals']:
            teacher_for_goal.append(teacher)

    goal_page = render_template('goal.html', goal=goal, teacher_for_goal=teacher_for_goal, profiles=profiles)
    return goal_page


@app.route('/profiles/<int:id>/')
def profile(id):
    profile_page = render_template('profile.html', id=id, profiles=profiles)
    return profile_page


@app.route('/select_teacher/')
def select_teacher():
    select_teacher_page = render_template('select_teacher.html', profiles=profiles)
    return select_teacher_page


@app.route('/select_done/', methods=['GET'])
def select_done():
    goal = request.args['goal']
    time = request.args['time']
    name = request.args['clientName']
    phone = request.args['clientPhone']

    selects = read_json('select.json')
    selects = ({'goal': goal, 'time': time, 'user_name': name, 'user_phone': phone})
    write_json('select.json', selects)

    select_done_page = render_template('select_done.html', selects=selects, profiles=profiles)
    return select_done_page


@app.route('/booking/<int:id>/<day>/<time>/')
def booking(id, day, time):
    booking_page = render_template('booking.html', id=id, day=day, time=time, profiles=profiles)
    return booking_page


@app.route('/booking_done/', methods=['GET'])
def booking_done():
    id = request.args['id']
    day = request.args['day']
    time = request.args['time']
    name = request.args['clientName']
    phone = request.args['clientPhone']

    bookings = read_json('booking.json')
    bookings = ({'id': id, 'day': day, 'time': time, 'user_name': name, 'user_phone': phone})
    write_json('booking.json', bookings)

    booking_done_page = render_template('booking_done.html', bookings=bookings, profiles=profiles)
    return booking_done_page


@app.errorhandler(404)
def not_found(e):
   return 'У нас такого нет. Попробуйте вернуться на главную и выбрать что-то другое.'


@app.errorhandler(500)
def server_error(e):
   return 'Что-то не так, но мы ЭТО уже скоро починим.'


if __name__ == '__main__':
   app.run()
