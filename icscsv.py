import vobject
import csv

with open('calendar2020.csv', mode='w') as csv_out:
    csv_writer = csv.writer(csv_out, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow(['WHAT', 'FROM', 'TO', 'DESCRIPTION', 'LOCATION'])

        # read the data from the file
    data = open("calendar.ics").read()

        # iterate through the contents
    for cal in vobject.readComponents(data):
        for component in cal.components():
            if component.name == "VEVENT":

                csv_writer.writerow([component.summary.valueRepr(),component.dtstart.valueRepr(),component.dtend.valueRepr(),component.description.valueRepr(),component.location.valueRepr()])
   
