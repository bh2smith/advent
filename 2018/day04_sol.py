from collections import defaultdict


def min_time(s):
    a, b = s.split(':')
    return 60 * (a == '00') + int(b)


def decreased_day(date):
    m, d = date.split('-')
    if int(d) > 1:
        return '-'.join([m, str(int(d) - 1).rjust(2, '0')])
    else:
        mapping = {
            '01': '31',
            '02': '28',
            '03': '31',
            '04': '30',
            '05': '31',
            '06': '30',
            '07': '31',
            '08': '31',
            '09': '30',
            '10': '31',
            '11': '30',
            '12': '31',
        }
        m = str(int(m) - 1).rjust(2, '0')
        d = mapping[m]
        return '-'.join([m, d])


def part1():

    def total_sleep(dates):
        res = 0
        for day in dates:
            clock = dates[day][1:]
            for i in range(0, len(clock), 2):
                res += clock[i+1] - clock[i]
        return res

    max_sleep = -1
    sleepiest_guard = ''
    for g in gd:
        if total_sleep(gd[g]) > max_sleep:
            max_sleep = total_sleep(gd[g])
            sleepiest_guard = g

    sg = gd[sleepiest_guard]

    counter = defaultdict(int)
    for d in sg:
        clock = sg[d][1:]
        for i in range(0, len(clock), 2):
            for time in range(clock[i], clock[i+1]):
                counter[time] += 1

    best_time = [k for k in counter if counter[k] == max(counter.values())]
    return (best_time[0] - 60) * int(sleepiest_guard[1:])


def part2():

    def most_frequent_minute_asleep(dates):
        counter = defaultdict(int)
        for day in dates:
            clock = dates[day][1:]
            for i in range(0, len(clock), 2):
                for time in range(clock[i], clock[i+1]):
                    counter[time] += 1
        if not counter:
            return 0, []
        mf = max(counter.values())
        res = [k for k in counter if counter[k] == mf]
        return mf, res

    m = -1
    for g in gd:
        time, minutes = most_frequent_minute_asleep(gd[g])
        if time > m:
            m = time
            ans = (g, minutes)

    return int(ans[0][1:]) * (ans[1][0]-60)


if __name__ == '__main__':
    with open('data/day04') as f:
        arr = []
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            d, t = line[:18][1:-1].split()
            d = d[5:]
            rest = line[19:].split()
            t = min_time(t)
            if t >= 60:
                d = decreased_day(d)
            arr.append((d, t, rest))

    arr.sort()

    gd = defaultdict(dict)
    for g in arr:
        day, time, action = g
        if action[0] == 'Guard':
            number = action[1]
            gd[number][day] = [time]
        else:
            gd[number][day].append(time)

    print(part1())
    print(part2())
