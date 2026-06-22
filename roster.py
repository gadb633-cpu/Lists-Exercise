# Part 1
# 1
agents = ["alpha", "bravo", "charlie", "delta", "echo"]
print(agents)
# 2
print(agents[0], agents[4])
# 3
print(agents[2])
# 4
print(agents[1:4])
# 5
agents.append("Foxtrot")
print(agents)
# 6
agents.insert(2,"zulu")
print(agents)
# 7
agents.remove("bravo")
print(agents)
# 8
print(len(agents))
# 9
scores = [42,17,95,8,61]
print(max(scores), min(scores))
# 10
copy_agents = agents.copy()
# print(copy_agents)
print(agents)
copy_agents[0] = "ALPHA"
print(copy_agents)

# Part 2
# 1 
numbers_1 = [3,1,4,1,5,9,2,6]
numbers_1.sort()
print(numbers_1)
numbers_2 = [3,1,4,1,5,9,2,6]
print(numbers_2)
copy_list = sorted(numbers_2)
print(copy_list)
# 2
a = [1,2,3]
b = [4,5,6]
print(a+b)
a.extend(b)
print(a)
# 3
items = ["x","y","z","x","y","x"]
x_items = items.count("x")
print(x_items)
items.remove("x")
print(items)
items.remove("x")
print(items)
items.remove("x")
print(items)
