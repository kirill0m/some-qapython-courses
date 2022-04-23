import operator
import re
from collections import Counter


def apache_log_reader(logfile):
    parts = [
        r'(?P<host>\S+)',
        r'\S+',
        r'(?P<user>\S+)',
        r'\[(?P<time>.+)\]',
        r'"(?P<request>.+)"',
        r'(?P<status>[0-9]+)',
        r'(?P<size>\S+)',
        r'"(?P<referer>.*)"',
        r'"(?P<agent>.*)"',
    ]
    pattern = re.compile(r'\s+'.join(parts) + r'\s*\Z')
    items = []

    with open(logfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            m = pattern.match(line)
            items.append(m.groupdict())
        f.close()

    [item.pop(key) for key in ('user', 'time', 'referer', 'agent') for item in items]

    #Общее количество запросов
    req_count = len(items)

    #Общее количество запросов по типу
    methods = ['GET', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH', 'HEAD']
    method_freq = Counter(item['request'].split(' ')[0] for item in items if item['request'].split(' ')[0] in methods)
    method_freq = method_freq.most_common(5)

    #Топ 10 самых частых запросов
    top_reqs = Counter(item['request'].split(' ')[1] for item in items)
    top_reqs = top_reqs.most_common(10)

    #Топ 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой
    uniq_reqs_4XX = sorted([item for item in items if item['status'].startswith('4')],
                            key=operator.itemgetter('request'))
    bgst_reqs_4XX = sorted(uniq_reqs_4XX, key=lambda item: int(item['size']) if item['size'].isdigit() else 0,
                                 reverse=True)[:5]

    #Топ 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой
    top_users_5XX = Counter(item['host'] for item in items if item['status'].startswith('5'))
    top_users_5XX = top_users_5XX.most_common(5)

    with open(fr'result_python.txt', 'w') as res:
        res.write(f'Общее количество запросов:\n{req_count}\n')
        res.write('\nОбщее количество запросов по типу:\n')
        for i in method_freq:
            res.write(' - '.join(str(s) for s in i) + '\n')
        res.write('\nТоп 10 самых частых запросов:\n')
        for i in top_reqs:
            res.write(' - '.join(str(s) for s in i) + '\n')
        res.write('\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n')
        for i in bgst_reqs_4XX:
            i['request'] = i['request'].split()[1]
            res.write(' - '.join(i.values()) + '\n')
        res.write('\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой:\n')
        for i in top_users_5XX:
            res.write(' - '.join(str(s) for s in i) + '\n')
        res.close()


if __name__ == '__main__':
    apache_log_reader('access.log')
