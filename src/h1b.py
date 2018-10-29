import csv
import argparse

def read_csv(filename):
    '''
    :type filename:str
    :rtype: list 
    '''
    data = []
    with open(filename) as f:
        reader = csv.reader(f, delimiter = ';')
        for row in reader:
            data.append(row)
    return data

def column_select(data, filters):
    '''
    :type data: list
    :type filter: set #string of Column name needed
    :rtype:list
    '''
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
    '''
    :type records:list
    :rtype: list
    '''
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
    '''
    :type records: list
    :type target:str  #SOC_NAME if output top 10 occupation, WORKSITE_STATE if output top 10 state
    :rtype:list
    '''
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


def output_txt(records, filename, is_occupations):
    '''
    :type records: list
    :type filename: str
    '''
    with open(filename, 'w+') as f:
        if is_occupations:
            f.write('TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        else:
            f.write('TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n')
        for item in records:
            for i in range(2):
                f.write(item[i]+';')
            f.write('{:0.1f}%'.format(item[2]*100)+'\n')

def parse_args():
    args = argparse.ArgumentParser()
    args.add_argument('input', help='input file')
    args.add_argument('occupations_output', help='output file for occupations')
    args.add_argument('states_output', help='output file for states')
    return args.parse_args()

def main(args):
    df = read_csv(args.input)
    filters = ['CASE_STATUS','VISA_CLASS','WORKSITE_STATE','SOC_NAME']
    column_selected = column_select(df, filters)
    cer_records = certified_records(column_selected)
    occupation_ranked = get_rank(cer_records, 'SOC_NAME' )
    state_ranked = get_rank(cer_records, 'WORKSITE_STATE')
    output_txt(occupation_ranked, args.occupations_output, True)
    output_txt(state_ranked, args.states_output, False)

if __name__ == '__main__':
    args = parse_args()
    main(args)
