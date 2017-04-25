from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine
import models

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = {
    'db': 'bar_app',
    'username': '',
    'password': ''
}

mongo = MongoEngine(app)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getbars')
def get_bars():
    monday = models.Bar.objects(deals__dow='Monday')
    tuesday = models.Bar.objects(deals__dow='Tuesday')
    wednesday = models.Bar.objects(deals__dow='Wednesday')
    thursday = models.Bar.objects(deals__dow='Thursday')
    friday = models.Bar.objects(deals__dow='Friday')
    saturday = models.Bar.objects(deals__dow='Saturday')
    sunday = models.Bar.objects(deals__dow='Sunday')

    deals = [[],[],[],[],[],[],[]]

    for bar in monday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Monday':
                dtext = deal.deal_text
        deals[0].append(bar.name + ' - ' + dtext)
    for bar in tuesday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Tuesday':
                dtext = deal.deal_text
        deals[1].append(bar.name + ' - ' + dtext)
    for bar in wednesday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Wednesday':
                dtext = deal.deal_text
        deals[2].append(bar.name + ' - ' + dtext)
    for bar in thursday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Thursday':
                dtext = deal.deal_text
        deals[3].append(bar.name + ' - ' + dtext)
    for bar in friday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Friday':
                dtext = deal.deal_text
        deals[4].append(bar.name + ' - ' + dtext)
    for bar in saturday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Saturday':
                dtext = deal.deal_text
        deals[5].append(bar.name + ' - ' + dtext)
    for bar in sunday:
        dtext = ''
        for deal in bar.deals:
            if deal.dow == 'Sunday':
                dtext = deal.deal_text
        deals[6].append(bar.name + ' - ' + dtext)


    return jsonify(deals)


@app.route('/get_bar/<bar>')
def get_bar(bar):
    bar = ' '.join(bar.split('+'))
    bar = bar.split(' - ')[0]
    bar = models.Bar.objects(name=bar).first()
    hours = []
    for h in bar.hours:
        hours.append(h.dow + '-' + h.hours)
    deals = []
    for d in bar.deals:
        deals.append(d.dow + '-' + d.deal_text)
    result = [bar.name, bar.logo, bar.description, hours, deals]
    return jsonify(result)


@app.route('/getallbars')
def getallbars():
    bars = []
    for bar in models.Bar.objects():
        bars.append(bar.name)
    return jsonify(bars)


if __name__ == '__main__':
    app.run(host='0.0.0.0')




