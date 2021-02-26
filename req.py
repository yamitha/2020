#import pywhatkit
from terminaltables import AsciiTable
import os
from terminaltables import SingleTable
from inventory import vehicles_needed as cars
#pywhatkit.sendwhatmsg_to_group('J8yK5GB3MWqCO7mQ7AewXa', 'Testing automated messages', 22, 22)
#pywhatkit.sendwhatmsg_to_group('J8yK5GB3MWqCO7mQ7AewXa', 'Testing automated messages 2', 22, 24)

class Inventory:
    def table(self):
        #cars = ['Axio', 'Premio', 'Alto', 'Hilux', 'Prado', 'Montero', 'wagonR', 'Lancer', 'Silvia', 'Elantra', 'Kia Sportage', 'Kia Sorento']

        rows, columns = os.popen('stty size', 'r').read().split()

        columns = round(int(columns) / 30)
        table_data = []
        #heading = []
        title = 'Vehicles Needed'
        #for x in range(0, columns):
        #    heading.append('###')

        rows = round(len(cars) / columns) + 2
        #row1 = [0:columns]
        #table_data.append(heading)

        for v in range(1, rows):
            row = []
            if v == 1:
                #row.append(cars[0:columns])
                for i in range(columns):
                    row.append(cars[i])
            elif v == rows - 1:
                y = (v - 1) * columns
                z = len(cars)
                #row.append(cars[y:])
                for i in range(y, z):
                    row.append(cars[i])
                #print(z, y, v)
            else:
                y = (v - 1) * columns
                z = v * columns
                #row.append(cars[y:z])
                for i in range(y, z):
                    row.append(cars[i])
                #print(z, y, v)
            
            table_data.append(row)


        #table = AsciiTable(table_data, title)
        table_instance = SingleTable(table_data, title)
        table_instance.inner_heading_row_border = False
        table_instance.inner_row_border = True
        #print(columns, rows)
        print('')
        print(table_instance.table)
    
    def insert(self):
        print('Wanted Car :')
        car = input('')
        contact = input('Contact: ')
        cars.append('{}:{}'.format(car, contact))
        save = int(input('1.Save or 2.skip : '))
        if save == 1:
            self.save()
            self.table()
        else:
            print('Skipped')
            self.insert()

    def save(self):
        with open('inventory.py', 'w+') as f:
            f.write('vehicles_needed = %s' % cars)
    

bot = Inventory()
bot.table()
bot.insert()