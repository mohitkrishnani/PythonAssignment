color_list_1 = set(["White","Black", "Red"])

color_list_2 = set(["Red","Green"])

ans_set = set()
for a in color_list_1:
  if a not in color_list_2:
    ans_set.add(a)
print(ans_set)

'''OUTPUT
{'White', 'Black'}'''