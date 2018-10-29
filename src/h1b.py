import csv

def read_csv(w):
    f = open(w)
    reader = csv.reader(f,delimiter = ';')
    data = []
    for row in reader:
        data.append(row)
    f.close()
    #for i in range(len(data)):
     #   data[i] = data[i][0].split(';')
    return data

def column_select(data, filters):
    records = [[] for _ in range(len(data))]
    filter_index = []
    for i in range(len(data[0])):
        if data[0][i] in filters:
            records[0].append(data[0][i])
            filter_index.append(i)
    for i in range(1,len(data)):
        for j in filter_index:
            records[i].append(data[i][j])
    return records

def certified_records(records):
    t = 0
    certied_r = [records[0]]
    for i in range(len(records[0])):
        if records[0][i] == 'CASE_STATUS':
            t = i
            break
    for i in range(1, len(records)):
        if records[i][t] == 'CERTIFIED':
            certied_r.append(records[i])
    return certied_r

def get_rank(records, target):
    index = 0
    n = len(records)
    for i in range(len(records[0])):
        if records[0][i] == target:
            index = i
            break
    d = dict()
    for i in range(1,n):
        state = records[i][index]
        if state in d:
            d[state] += 1
        else:
            d[state] = 1
    rank = []
    val_nodup = sorted(list(set(d.values())), reverse = True)[:10]
    d1 = dict()
    for key, val in d.items():
        if val in d1:
            d1[val].append(key)
        else:
            d1[val] = [key] 
    for i in range(len(val_nodup)):
        numbers = val_nodup[i]
        sorted_alpha = sorted(d1[numbers])
        for x in sorted_alpha:
            tmp = [x, str(numbers), numbers/(n-1)]
            rank.append(tmp)
    return rank


def output_txt(records, filename):
    f = open(filename, 'w+')
    if filename == 'top_10_occupations.txt':
        f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    else:
        f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
    for item in records:
        for i in range(2):
            f.write(item[i]+';')
        f.write('{:0.1f}%'.format(item[2]*100)+'\n')
    f.close()


#w = '/Users/xyn/Documents/project/h1banalysis/2016n200.csv'
w = '/Users/xyn/Documents/project/h1banalysis/H1B_FY_2016.csv'
df = read_csv(w)
filters = {'CASE_STATUS','VISA_CLASS','WORKSITE_STATE','SOC_NAME'}
column_selected = column_select(df, filters)
cer_records = certified_records(column_selected)
occupation_ranked = get_rank(cer_records, 'SOC_NAME' )
state_ranked = get_rank(cer_records,'WORKSITE_STATE')
output_txt(occupation_ranked, 'top_10_occupations.txt')
output_txt(state_ranked,'top_10_states.txt' )