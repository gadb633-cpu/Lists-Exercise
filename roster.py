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
