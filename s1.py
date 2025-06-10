##### Problem 1
def welcome():
	print("Welcome to The Hundred Acre Wood!")
	
##### Problem 2
def greetings(name):
	print(f"Welcome to The Hundred Acre Wood {name} My name is Christopher Robin.")

##### Problem 3
def print_catchphrase(character):
	if character == "Pooh":
		print("Oh, bother!")
	elif character == "Tigger":
		print("TTFN: Ta-ta for now!")
	elif character == "Eeyore":
		print("Thanks for noticing me.")
	elif character == "Christoper Robin":
		print("Silly old bear.")
	else:
		print(f"Sorry! I dont know {character}'s catchphrase.")

#### Problem 4
def get_item(items, x):
	if x >= len(items):
		print(None)
		return
	
	print(items[x])

#### Problem 5
def doubled(hunny_jars):
    dub = [val *2 for val in hunny_jars]
    print(dub)

#### Problem 6
def count_less_than(race_times, threshold):
	amount = 0
	for x in race_times:
		if x < threshold:
			amount += 1
	print(amount)
	
#### Problem 7
def print_todo_list(task):
	print("Pooh's To-do List:")
	for i in range(len(task)):
		print(f"{i+1}. {task[i]}")

#### Problem 8
def can_pair(item_quantities):
	if len(item_quantities) == 0:
		print("True")
		return True
	else:
		for i in range(len(item_quantities)):
			if item_quantities[i] % 2 == 0:
				i = i
			else:
				print("False")
				return False
			
	print("True")
	return True
	
	# if len(item_quantities) == 0:
	# 	return True
    # for i in range(len(item_quantities) - 1):
    #     if item_quantities[i]  % 2 == 0:
	# 		return True
	# return False

# item_quantities = [2, 4, 6, 8]
# can_pair(item_quantities)

# item_quantities = [1, 2, 3, 4]
# can_pair(item_quantities)

# item_quantities = []
# can_pair(item_quantities)

# welcome()
# greetings("Michael")
# greetings("Winnie the Pooh")
# character = "Pooh"
# print_catchphrase(character)

# character = "Piglet"
# print_catchphrase(character)
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 2
# get_item(items, x)
# items = ["piglet", "pooh", "roo", "rabbit"]
# x = 5
# get_item(items, x)

# hunny_jars = [1, 2, 3]
# doubled(hunny_jars)

# race_times = [1, 2, 3, 4, 5, 6]
# threshold = 4
# count_less_than(race_times, threshold)

# race_times = []
# threshold = 4
# count_less_than(race_times, threshold)   
#task = ["Count all the bees in the hive", "Chase all the clouds from the sky", "Think", "Stoutness Exercises"]
# print_todo_list(task)

# task = []
# print_todo_list(task)



def mys_func(nums):
	count = 0
	max_coiunt = 0
	for i in range(len(nums)):
		if nums[i] > 0:
			count+=1
		else:
			if count > max_coiunt:
				max_coiunt = count
			count = 0
	if count > max_coiunt:
		max_coiunt = count
	print(max_coiunt)
	
mys_func([1,2,-3,4,5,-6,7,8,9])


def merge_sorted_lists(lst1, lst2):
	final_lst = []
	l1_idx = 0
	l2_idx = 0
	if lst1 == []:
		return lst2
	elif lst2 == []:
		return lst1
	else:
		while l1_idx < len(lst1) and l2_idx < len(lst2):
			if lst1[l1_idx] < lst2[l2_idx]:
				final_lst.append(lst1[l1_idx])
				l1_idx += 1
			else:
				final_lst.append(lst2[l2_idx])
				l2_idx += 1
		# Add remaining elements
		final_lst.extend(lst1[l1_idx:])
		final_lst.extend(lst2[l2_idx:])
		return final_lst