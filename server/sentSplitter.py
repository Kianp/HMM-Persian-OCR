import os 
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

sents = tuple(open(sys.argv[1] , "r"))
out = open(sys.argv[1].split('.')[0] + "_2split_.txt" , "w")

o = []  

for s in sents :
    pred = s.split(" ")
    #for idx , w in enumerate(pred) :
	#if len(w) >= 4 :
	    #o.append(w)

	#out.write(w +  ("\n" if idx != len(pred)-1 else "" ) ) 
    for i in range(2 , 3) :
	step  = i
	curr = 0
	while curr + step <= len(pred) :
	    disc = ""
	    for ch in pred[curr:curr+step] :
		disc += ch
		disc += " "
	    out.write(disc + "\n") 
	    o.append(disc)
	    curr += step
	s = ""
	for j in range(i) :
	    s += pred[j] + " "
        o.append(s)
	out.write(s + ("\n" if j != len(pred) else "" )) 
 
for l in o :
    out.write(l.replace('\n' , '').replace("  " , " ").strip() + "\n" )
