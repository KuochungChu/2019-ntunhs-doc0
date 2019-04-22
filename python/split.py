lines = open('/root/exchange-hdfs/key-points-stem.txt').read().splitlines()

i=0
	
for n in lines:
    filename="/root/exchange-hdfs/key-points-stem-%d.txt" %i
    with open(filename, 'w') as f:
            f.write(n)
    i=i+1