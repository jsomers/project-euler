# Prim's algorithm
lines = open('network.txt', 'rU').readlines()

edges = []
for i, row in enumerate(lines):
	for j, col in enumerate(row.split(',')):
		if col != '-' and col != '-\n':
			edges.append((int(col), i, j))
edges.sort()
original = sum([e[0] for e in edges]) / 2

V_new = [12]
E_new = []
while len(V_new) < 40:
	for edge in edges:
		if edge[1] in V_new and edge[2] not in V_new:
			V_new.append(edge[2])
			E_new.append(edge)
			break
			
print original - sum([e[0] for e in E_new])