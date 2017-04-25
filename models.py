from hobokenbarapp import mongo
from datetime import datetime
import csv
db = mongo


class Hours(db.EmbeddedDocument):
    dow = db.StringField()
    hours = db.StringField()


class Deals(db.EmbeddedDocument):
    dow = db.StringField()
    deal_text = db.StringField()


class Bar(db.DynamicDocument):
    meta = {
        'collection': 'bars'
    }
    name = db.StringField(primary_key=True)
    hours = db.EmbeddedDocumentListField(Hours)
    deals = db.EmbeddedDocumentListField(Deals)
    location = db.PointField()
    website = db.StringField()
    logo = db.StringField()
    description = db.StringField()

with open("D:\\temptrans\\hobokenbarapp\\Bars.csv", 'rt') as csvfile:
    sreader = csv.DictReader(csvfile)
    for row in sreader:
        hoursM = Hours(
            dow='Monday',
            hours=row['Hours M']
        )
        hoursT = Hours(
            dow='Tuesday',
            hours=row['Hours T']
        )
        hoursW = Hours(
            dow='Wednesday',
            hours=row['Hours W']
        )
        hoursR = Hours(
            dow='Thursday',
            hours=row['Hours R']
        )
        hoursF = Hours(
            dow='Friday',
            hours=row['Hours F']
        )
        hoursS = Hours(
            dow='Saturday',
            hours=row['Hours S']
        )
        hoursU = Hours(
            dow='Sunday',
            hours=row['Hours U']
        )
        deals = []
        if row['Deals M'] != '':
            deals.append(Deals(
                dow='Monday',
                deal_text=row['Deals M']
            ))
        if row['Deals T'] != '':
            deals.append(Deals(
                dow='Tuesday',
                deal_text=row['Deals T']
            ))
        if row['Deals W'] != '':
            deals.append(Deals(
                dow='Wednesday',
                deal_text=row['Deals W']
            ))
        if row['Deals R'] != '':
            deals.append(Deals(
                dow='Thursday',
                deal_text=row['Deals R']
            ))
        if row['Deals F'] != '':
            deals.append(Deals(
                dow='Friday',
                deal_text=row['Deals F']
            ))
        if row['Deals S'] != '':
            deals.append(Deals(
                dow='Saturday',
                deal_text=row['Deals S']
            ))
        if row['Deals U'] != '':
            deals.append(Deals(
                dow='Sunday',
                deal_text=row['Deals U']
            ))
        newBar = Bar(
            name=row["Name"],
            website=row['Website'],
            description=row['Description'],
            logo=row['Link to Logo'],
            location=[float(row['Location Lat']), float(row['Location Lon'])],
            hours=[hoursM, hoursT, hoursW, hoursR, hoursF, hoursS, hoursU],
            deals=deals
        )
        newBar.save()



