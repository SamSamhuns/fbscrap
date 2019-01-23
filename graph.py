import matplotlib.pyplot as plt
from datetime import datetime
from dateutil import tz
import seaborn as sns
# sns.set_style("whitegrid")

time_list = []
full_set = set()


def populate_list():
    """Populates the time list and the full friends set
    """
    exist_set = set()
    with open('active_friend_list.txt', 'r') as fdata:
        start = (fdata.readline()).strip().split(',')
        for line in fdata:
            nline = line.strip().split(',')
            if nline[0] not in exist_set:
                exist_set.add(nline[0])
                full_set.add(nline[0])
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
    """ Converets to utc_tiem to the selected 'time_zone'
    """
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz(time_zone)

    utc = datetime.strptime(utc_time, '%Y-%m-%d %H:%M:%S')

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc = utc.replace(tzinfo=from_zone)

    # Convert time zone
    new_tzone = utc.astimezone(to_zone)
    return new_tzone


def main():
    option = 0
    while True:
        print("1) Enter 1 to get the set of all friends with recorded status")
        print("2) Enter 2 to graph number of active friends \
            from the start of the recorded set")
        print("3) Enter 3 to select one friend and graph their activity")
        print("4) Enter 4 or q to exit")
        print("Input:", end='')
        option = input()

        if option == '1':
            for name in full_set:
                print(name)
        elif option == '2':
            pass
        elif option == '3':
            fname = 0
            while fname not in full_set:
                for name in full_set:
                    print(name)
                print("Enter friend name exactly as it appears in the list above: ", end="")
                fname = input()

            x_time = []
            y_status = []
            for time in time_list:
                    x_time.append(time[0])
                    if fname in time[1]:
                        y_status.append(1)
                    else:
                        y_status.append(0)
            plt.bar(x_time, y_status)
            plt.show()

        elif option == '4' or option.lower() == 'q':
            print("Quitting program")
            break
        else:
            print("Invalid option chosen.\n Options are 1, 2, 3 and 4.")


if __name__ == "__main__":
    populate_list()
    main()
