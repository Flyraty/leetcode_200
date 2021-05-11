import sys
import datetime


def gen_date_range(from_date, to_date):
    dates = []
    dt = datetime.datetime.strptime(from_date, "%Y%m%d")
    date = from_date[:]
    while date <= to_date:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    return dates


if __name__ == '__main__':
    from_date = sys.argv[1]
    to_date = sys.argv[2]
    print(' '.join(gen_date_range(from_date, to_date)))
