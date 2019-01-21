from datetime import datetime
from dateutil import tz

time_list = []


def main():
    exist_set = set()
    with open('active_friend_list.txt', 'r') as fdata:
        start = (fdata.readline()).strip().split(',')
        for line in fdata:
            nline = line.strip().split(',')
            if nline[0] not in exist_set:
                exist_set.add(nline[0])
            if start[1] != nline[1]:
                exist_set = set()
                unix_epoch_time = int(((start[1]).split('.'))[0])
                utc_time = (datetime.utcfromtimestamp(
                    unix_epoch_time).strftime('%Y-%m-%d %H:%M:%S'))
                time_list.append([(utc_convert(
                    utc_time, 'Asia/Dubai')).strftime(
                    '%Y-%m-%d %H:%M:%S'), exist_set])
            start = nline


def utc_convert(utc_time, time_zone):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(time_zone)

    utc = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)

    # Convert time zone
    gst = utc.astimezone(to_zone)

    return gst


if __name__ == "__main__":
    main()
