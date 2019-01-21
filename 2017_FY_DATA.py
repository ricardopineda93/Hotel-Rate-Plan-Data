import csv
import pygal as pg
from datetime import datetime, timedelta

filename = '2017_daybyday.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    master_date, dow, rate_code, mkt_code, rate_desc, rns,\
    revenue, adr = [], [], [], [], [], [], [], []

    weekday= ['Monday', 'Tuesday', 'Wednesday',
               'Thursday', 'Friday', 'Saturday', 'Sunday']

    for row in reader:
        indv_date = datetime.strptime(row[0], "%m/%d/%Y").date()
        master_date.append(indv_date)

        rt_cd = str(row[2])
        rate_code.append(rt_cd)

        mkt_cd = str(row[3])
        mkt_code.append(mkt_cd)

        rt_dsc = str(row[4])
        rate_desc.append(rt_dsc)

        rooms = int(row[5])
        rns.append(rooms)

        rev = float(row[6])
        revenue.append(rev)

        try:
            calc_adr = rev / rooms
        except ZeroDivisionError:
            calc_adr = 0
            adr.append(calc_adr)
        else:
            adr.append(calc_adr)

date_set = list(sorted(set(master_date)))
mkt_set = list(set(mkt_code))
rate_set = list(set(rate_code))



def set_from_date():
    while True:
        try:
            from_date = datetime.strptime(input('From date (mm/dd/yyyy format): '), "%m/%d/%Y").date()
        except:
            print('Error - please input correct date format (mm/dd/yyyy)')
            continue
        else:
            try:
                if from_date not in date_set:
                    raise(ValueError)
            except:
                print('Start date not in data range, earliest date is ',
                      str(date_set[0]), ', please try again.')
                continue
            else:
                return from_date

def set_to_date():
    while True:
        try:
            to_date = datetime.strptime(input('To date (mm/dd/yyyy format): '), "%m/%d/%Y").date() \
                      + timedelta(days=1)
        except:
            print('Error - please input correct date format (mm/dd/yyyy)')
            continue
        else:
            try:
                if to_date not in date_set:
                    raise (ValueError)
            except:
                print('End date not in data range, earliest date is ',
                      str(date_set[-1]), ', please try again.')
                continue
            else:
                return to_date

def set_date_range(from_date, to_date):
    date_range = []

    for days in range(int((to_date - from_date).days)):
        date_range.append(from_date + timedelta(days=days))
    return date_range

def rate_plan_input():
    while True:
        try:
            rc = input(str('RATEPLAN?: ')).upper()
            if rc not in rate_code:
                raise(LookupError)
        except:
            print('Error - invalid rate plan.')
            continue
        else:
            return rc

def display_metric_input():
    while True:
        try:
            display_metric = input('What metric do you wish to plot? RN, REVENUE, or ADR?: ').lower()
            if display_metric not in ['rn', 'adr', 'revenue']:
                raise(LookupError)
        except:
            print('Invalid selection, please try again.')
            continue
        else:
            return display_metric

def line_display(display_metric_input):
    if display_metric_input == 'rn':
        return rns
    elif display_metric_input == 'revenue':
        return revenue
    elif display_metric_input == 'adr':
        return adr

def data_by_rateplan():

    selected_rp = rate_plan_input()
    dmi = display_metric_input()
    l_display = line_display(dmi)
    dates = set_date_range(set_from_date(),set_to_date()) 

    rate_dicts = []
    for i, rate in enumerate(rate_code):
        if rate == selected_rp:
            if master_date[i] in dates:
                rate_dict = {
                    'value': l_display[i],
                    'description': rate_desc[i]
                }
                rate_dicts.append(rate_dict)
        else:
            continue

    line = pg.Line(x_label_rotation=45)
    line.title = '2017 ' + selected_rp + ' ' + dmi.upper() + ' by Date'
    line.x_labels = dates
    line.x_title = 'Date'
    line.y_title = dmi.upper()

    line.add(selected_rp + ' ' + dmi.upper(),rate_dicts)
    line.render_in_browser()

data_by_rateplan()

