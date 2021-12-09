from projet import solution
import timeit

def check():
	start = timeit.timeit()
	l=[[[[1,0,0],[1,0,0],[0,1,0]],[[0,0,0],[0,0,0],[0,0,1]]],[[[-1,1,-1],[-1,1,-1],[-1,0,-1]],[[-1,0,-1],[-1,0,-1],[-1,1,-1]]],[[[0,1,0,-1],[1,1,1,1],[0,-1,1,1]],[[0,0,0,-1],[0,1,0,1],[1,-1,0,1]]],[[[-1,-1,-1,1,-1,-1,-1],[-1,-1,0,1,0,-1,-1],[-1,0,0,0,1,0,-1],[1,1,0,0,0,1,0],[0,0,1,0,1,0,0],[-1,1,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]],[[-1,-1,-1,0,-1,-1,-1],[-1,-1,0,0,0,-1,-1],[-1,0,0,0,0,0,-1],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,-1],[-1,-1,0,0,0,-1,-1],[-1,-1,-1,0,-1,-1,-1]]],[[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[1,1,0,1,0,0,0],[0,0,1,0,0,1,1],[-1,1,1,0,0,0,-1],[-1,-1,0,0,0,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,0,0,1,0,0,-1],[0,0,1,0,1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[-1,0,1,1,0,0,-1],[-1,-1,0,0,0,-1,-1]]]]
	s=[[[[1,0],[1,0]],[[0,1],[0,0]]],[[[1,1,0],[1,1,0],[0,0,1]],[[0,0,0],[0,1,0],[1,0,1]]],[[[1,0,-1,1],[1,-1,0,1],[1,1,0,0],[1,0,-1,1]],[[1,0,-1,0],[1,-1,0,1],[0,0,0,0],[0,0,-1,0]]],[[[-1,1,1,-1],[1,0,1,1],[1,1,1,1],[-1,1,1,-1]],[[-1,0,0,-1],[0,1,0,0],[0,0,0,0],[-1,0,0,-1]]]]
	for m in l:
		pos1 = timeit.timeit()
		if solution(m[0],m[1])!=True:
			print("Votre programme échoue sur le couple:")
		else:
			print("Votre programme marche sur le couple:")
		print((m[0],m[1]))
		pos2 = timeit.timeit()
		print("\n")
		print("Elapsed time: ")
		print(pos2 - pos1)
	for m in s:
		pos1 = timeit.timeit()
		if solution(m[0],m[1])==True:
			print("Votre programme échoue sur le couple:")
		else:
			print("Votre programme marche sur le couple:")
		print((m[0],m[1]))
		pos2 = timeit.timeit()
		print("\n")
		print("Elapsed time: ")
		print(pos2 - pos1)
	m1=[[[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1],[1,1,1,1,1,1,1],[1,1,1,0,1,1,1],[1,1,1,1,1,1,1],[-1,-1,1,1,1,-1,-1],[-1,-1,1,1,1,-1,-1]],[[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[-1,-1,0,0,0,-1,-1],[-1,-1,0,0,0,-1,-1]]]
	pos1 = timeit.timeit()
	if solution(m1[0],m1[1])!=True:
		print("Votre programme échoue sur le couple:")
	else:
		print("Votre programme marche sur le couple:")
	print((m1[0],m1[1]))
	pos2 = timeit.timeit()
	print("\n")
	print("Elapsed time: ")
	print(pos2 - pos1)
	m2=[[[-1,1,1,1,-1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1],[-1,1,1,1,-1]],[[-1,0,0,0,-1],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[-1,0,0,0,-1]]]
	pos1 = timeit.timeit()
	if solution(m2[0],m2[1])==True:
		print("Votre programme échoue sur le couple:")
	else:
		print("Votre programme marche sur le couple:")
	print((m2[0],m2[1]))
	pos2 = timeit.timeit()
	print("\n")
	print("Elapsed time: ")
	print(pos2 - pos1)

check()
