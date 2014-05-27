#Python thinger with functions

"""def get_sum(var1, var2):
	total = var1 + var2
	result = "\n" + str(total) + "\n"
	return result

numbers = get_sum(7, 65)
print numbers"""

"""
def user_input(action_type, choices, option1, option2, text_output1):
	error_text = "I have no clue what you've just said. Try again"
	while action_type != option2:
		action_type = raw_input([choices])
		action_type = action_type.lower()
		if action_type == option1:
			print "\n" + text_output1 + "\n"
		elif action_type != option2:
			print "\n" + error_text + "\n"
"""


def user_input(choices, option1, option2, option3, text_output):
	action = None
	while action == None:
		action = raw_input([choices])
		decision = action
	if decision == option1:
		print 'option 1'
	if decision == option2:
		print 'option 2'
	elif decision == option3:
		print 'option 3'
	else:
		print text_output


user_input("choices: do nothing, pick up note, craddle balls", "do nothing", "pick up note", "craddle balls", "You stand around for a bit.Nothing happens.")



#user_input(None, "choices: do nothing, pick up note", "do nothing", "pick up note", "You stand around for a bit.Nothing happens.")
#user_input(None, "choices: go left, go right", "go left", "go right", "This room is empty")
