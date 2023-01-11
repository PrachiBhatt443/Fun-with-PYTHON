def remove_match_char(list1, list2):

	for i in range(len(list1)):
		for j in range(len(list2)):
			if list1[i] == list2[j]:
				c = list1[i]
				list1.remove(c)
				list2.remove(c)
				list3 = list1 + ["*"] + list2
				return [list3, True]

	# no common characters is found
	# return the concatenated list with False flag
	list3 = list1 + ["*"] + list2
	return [list3, False]


# Driver code
if __name__ == "__main__":

	p1 = input("Enter name 1 : ")
	p1 = p1.lower()
	p1.replace(" ", "")# replace any space with empty string
	p1_list = list(p1)

	p2 = input("Player 2 name : ")
	p2 = p2.lower()
	p2.replace(" ", "")
	p2_list = list(p2)

	# taking a flag as True initially
	proceed = True
	
	while proceed:
		ret_list = remove_match_char(p1_list, p2_list)
		con_list = ret_list[0]
		proceed = ret_list[1]
		star_index = con_list.index("*")

		# list slicing perform
		p1_list = con_list[: star_index]
		p2_list = con_list[star_index + 1:]

	# counting remaining characters
	count = len(p1_list) + len(p2_list)

	# list of FLAMES acronym
	result = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]

	# keep looping until only one item
	# is not remaining in the result list
	while len(result) > 1:

		# store that index value from
		# where we have to perform slicing.
		split_index = (count % len(result) - 1)

		# this steps is done for performing
		# anticlock-wise circular fashion counting.
		if split_index >= 0:

			# list slicing
			right = result[split_index + 1:]
			left = result[: split_index]

			# list concatenation
			result = right + left

		else:
			result = result[: len(result) - 1]

	# print final result
	print("Relationship status :", result[0])
