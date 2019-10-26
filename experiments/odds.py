
import csv

m1 = [0,1,1,2,2,3]
m2 = [1,2,2,3,3,4]
m3 = [2,3,3,4,4,5]
mc = [4,4,4,5,5,5]
ai = [4,5,6,7,0,0]
qu = [2,2,2,3,5,10]
max_flops = 20


def get_result(a, b):
	out = []
	for sidea in a:
		for sideb in b:
			out.append(sidea + sideb)
	return out

def get_combinations (dice):	
	result = [0]
	for die in dice:
		result = get_result(result, die)
		
	# result now has all possabilities
	return result

def get_counts(combinations):
	out = []
	for t in range(max_flops+1):
		out.append(combinations.count(t))
	
	return out

def get_odds(counts):
	out = []
	total = sum(counts)
	running_total = 1.0
	for c in counts:
		part = (c / total)
		out.append(running_total)
		running_total -= part
	return out
	
def odds(dice):
	return get_odds(get_counts(get_combinations(dice)))

	
out = []
out.append(["Combo"]+list(range(max_flops+1)))
out.append(["m1"]+odds([m1]))
out.append(["m2"]+odds([m2]))
out.append(["m3"]+odds([m3]))
out.append(["m1,m1"]+odds([m1,m1]))
out.append(["m1,m2"]+odds([m1,m2]))
out.append(["m2,m2"]+odds([m2,m2]))
out.append(["m2,m3"]+odds([m2,m3]))
out.append(["m3,m3"]+odds([m3,m3]))
out.append(["m1,m1,m1"]+odds([m1,m1,m1]))
out.append(["m1,m1,m2"]+odds([m1,m1,m2]))
out.append(["m1,m2,m2"]+odds([m1,m2,m2]))
out.append(["m2,m2,m2"]+odds([m2,m2,m2]))
out.append(["m2,m2,m3"]+odds([m2,m2,m3]))
out.append(["m2,m3,m3"]+odds([m2,m3,m3]))
out.append(["m3,m3,m3"]+odds([m3,m3,m3]))
out.append(["m1,m1,m1,m1"]+odds([m1,m1,m1,m1]))
out.append(["m2,m2,m2,m2"]+odds([m2,m2,m2,m2]))
out.append(["m3,m3,m3,m3"]+odds([m3,m3,m3,m3]))
out.append(["m1,m1,m1,m1,m1"]+odds([m1,m1,m1,m1,m1]))
out.append(["m2,m2,m2,m2,m2"]+odds([m2,m2,m2,m2,m2]))
out.append(["m3,m3,m3,m3,m3"]+odds([m3,m3,m3,m3,m3]))
out.append(["m1,m1,m1,m1,m1,m1"]+odds([m1,m1,m1,m1,m1,m1]))
out.append(["m2,m2,m2,m2,m2,m2"]+odds([m2,m2,m2,m2,m2,m2]))
out.append(["m3,m3,m3,m3,m3,m3"]+odds([m3,m3,m3,m3,m3,m3]))

#clean commas
for r in range(len(out)):
	out[r][0] = out[r][0].replace(",", "|")
	

print(out)
	
with open("odds.csv","w+",newline='') as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(out)



