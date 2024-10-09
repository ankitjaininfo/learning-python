p1=input("enter the 1st person's name: ")
p2=input("enter the 2nd person's name: ")
p3=input("enter the 3rd person's name: ")
p4=input("enter the 4th person's name: ")
score1=0
score2=0
score3=0
score4=0
for i in range(10):
	print("----- Starting Game ", i+1 , "--------")
	w=float(input("Enter [" + p1 + "]'s score: "))
	x=float(input("Enter [" + p2 + "]'s score: "))
	y=float(input("Enter [" + p3 +"]'s score: "))
	z=float(input("Enter [" + p4 + "]'s score: "))
	if w not in [0, 200, 500, 1000]:
	    print("Try again.",p1,"Invalid score:", w)
	    continue
	if x not in [0, 200, 500, 1000]:
	    print("Try again.",p2,"Invalid score:", x)
	    continue
	if y not in [0, 200, 500, 1000]:
	    print("Try again.",p3,"Invalid score:", y)
	    continue
	if z not in [0, 200, 500, 1000]:
	    print("Try again.",p4,"Invalid score:", z)
	    continue

	score1=score1+w
	score2=score2+x
	score3=score3+y
	score4=score4+z

highest_score = max(score1,score2,score3,score4)

print("---------------------------------------")
print("this is the highest score: ", highest_score)
if highest_score==score1:
    print(p1,"is the winner. good job!")
elif highest_score==score2:
    print(p2,"is the winner. good job!")
elif highest_score==score3:
    print(p3,"is the winner .good job!")
elif highest_score==score4:
    print(p4," is the winner .good job!")
else:
    print("ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR-ERROR")