import csv,json
import io
from math import floor, inf

scores = {'100m':[25.4347,18,1.81],
          'lj':[0.14354,220,1.4],
          'sp':[51.39,1.5,1.05],
          'hj':[0.8465,75,1.42],
          '400m':[1.53775,82,1.81],
          '110m':[5.74352,28.5,1.92],
          'dt':[12.91,4,1.1],
          'pv':[0.2797,100,1.35],
          'jt':[10.14,7,1.08],
          '1500m':[0.03768,480,1.85]}
output = []

def json_parse(file):
    output = _read_data(file)
    [_score(i) for i in output]
    _compute_position(output)
    return output

def _compute_position(data):
    data.sort(key=lambda x: x['total'],reverse=True)
    position = 1
    current = 0
    for i in data:
        if i['total'] < current:
            position += 1
        i['position'] = position
        current = i['total']

def _score(val):
    track = ['100m','400m','110m','1500m']
    jumps = ['lj','hj','pv']
    
    ts = 0
    for i in scores:
        if i == '1500m':
            temp = val[i].split('.',1)
            x = float(temp[0])*60 + float(temp[1])
        else:
            x = float(val[i])
            
        if i in track:
            ts += floor(scores[i][0] * (scores[i][1] - x) ** scores[i][2])
        elif i in jumps:
            ts += floor(scores[i][0] * (100*x-scores[i][1]) ** scores[i][2])
        else:
            ts += floor(scores[i][0] * (x - scores[i][1]) ** scores[i][2])
        val['total'] = ts
    return ts

def _read_data(filename):
    file = filename.read().decode('utf-8')
    io_string = io.StringIO(file)
    #delimiter semicolon used, change to ',' to suit your needs if error
    reader = csv.reader(io_string,delimiter=';' )
    for row in reader:
        dic = {}
        dic['name'] = row.pop(0)
        counter = 0
        for i in scores:
            dic[i] = row[counter]
            counter += 1
        output.append(dic)
    return output

