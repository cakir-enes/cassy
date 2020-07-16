import csv

def parse(inFile, outFile, fun, delimiter):
    out = open(outFile, 'w')
    with open(inFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        for row in csv_reader:
            try:
                print(','.join([str(e) for e in fun(row)]), file=out)
            except:
                pass
    out.close()


def ckim_mapper(row):
    userId = row[0]
    twitId = row[1]
    twit = row[2]
    time = row[3]
    return [userId, twitId, twit, time]

def twitter_ckim():
    print('Starting ckim parsing')
    parse('twitter_cikm_2010/training_set_tweets.txt', 'cikm2010.csv', ckim_mapper, '\t')
    print('Done.')

if __name__ == '__main__':
    twitter_ckim()

