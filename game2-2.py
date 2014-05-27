options = {
"move": { "m0": "go straight", "m1": "go left", "m2": "go right", "m3": "go back"},
"spec": { "s0": "do nothing", "s1": "pick up note", "s2": "look out window", "s3": "check dresser"}	
}

text_strings = {
"story": {"st0": "You wake up in an empty room. There is a note on the ground. What do?", "st1": "\nYou stand around for a bit.\nNothing happens.\nYour choices remain the same"},
"choice": {"ch0": "choices: do nothing, pick up note", "ch1": "choices: go left, go right, go straight", "ch2": "choices: do nothing, go back", "ch3": "choices: go back, look out window"},
"room": {"r0": "You enter another empty rooom", "r1": "You enter a room with only a window"}
}


def user_input(choices, secondary_choices, third_choices, option1, option2, option3, text_output1, text_output2, nested_options):
	error_text = "I have no clue what you've just said. Try again"
	action_type = None
	
	while action_type != option2:
		action_type = raw_input([choices])
		action_type = action_type.lower()
		if action_type == option1:
			print "\n" + text_output1 + "\n"
			if nested_options == 1:
				next_choice = raw_input([secondary_choices])
		elif action_type == option2:
			print "\n" + text_output2 + "\n"
			if nested_options == 1:
				next_choice = raw_input([third_choices])
		elif action_type != option2:
			print "\n" + error_text + "\n"

user_input(text_strings["choice"]["ch0"],None, None, options["spec"]["s0"], options["spec"]["s1"], None, text_strings["story"]["st1"],"", 0)
user_input(text_strings["choice"]["ch1"], text_strings["choice"]["ch2"], text_strings["choice"]["ch3"], options["move"]["m1"], options["move"]["m0"], options["move"]["m2"], text_strings["room"]["r0"], text_strings["room"]["r1"], 1)






"""
choices_intro = {}
choices_chapter_1 = {
		'choice_one':'do something',
		'choice_two':'do something else',
		'choice_three': 'finally, do this'
}
choices_chaptyer_2 = {}

choices_list = [1:'choice', ]



def user_input(choices, options, text_output ):
	pass

user_input(choices_chapter_1, options_intro, text_output_intro)
	# parse out my choices
	choices_chapter_1['choice_one']
	choice_two = choices_chapter_1['choice_two']

	# parse out my options
	# up to you
	# start my loop

	# THIS LOOP NEEDS TO DO THE FOLLOWING:
		# 1. ASK A QUESTION
		# 2. RETURN A RESPONSE (TEXT)
		# 3. EXIT LOOP
		# 4. RETURN USER CHOICE


what_they_did = user_input(one, two, three)

if what_they_did == 'aweawe':
	user_inpuit(bla, bla bla)
if what_they_did == 'achghyyyyy':
	user_input(waeawe, awegawe,awetgawet)

"""








print "end"