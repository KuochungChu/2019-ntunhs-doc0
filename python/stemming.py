from nltk.stem import PorterStemmer

result = []
with open('/root/exchange-hdfs/key-points.txt', 'r') as f:
    for line in f:
        singles = []
        stemmer = PorterStemmer()
        for plural in line.split():
            singles.append(stemmer.stem(plural))
            sentence=' '.join(singles)
        result.append(sentence)

with open('/root/exchange-hdfs/key-points-stem.txt', 'w') as f:
    for item in result:
        f.write("%s\n" % item)
