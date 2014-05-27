#Dictionaries for intro
options_chapter_intro = {"option_1": "pick up note", "option_2": "do nothing"}
choices_chapter_intro = {"ci0": "choices: do nothing, pick up note"}
text_intro = {
"ti0": "\nYou wake up in an empty room. You see a note on the ground. What do?\n",
"ti1": "\nYou stand around for a bit.\nNothing happens.\nYour choices remain the same."
}

#Main Function
def user_input(options, choices, text_output):
	answer = ""
	jet = False
	option_1 = options["option_1"]
	option_2 = options["option_2"]
	error_text = "\nI have no clue what you've just said\n"
	#print "xxxxx" + option_1
	while jet != True:
		answer = raw_input([choices])
		answer = answer.lower()
		if answer == option_1:
			jet = True
		if answer == option_2:
			jet = True
		if jet != True:#answer != option_1: #use loop here to account for unlimited opitons
			print error_text

	print "function exit"
	return answer	
	

#intro
print text_intro["ti0"]
answer = user_input(options_chapter_intro, choices_chapter_intro["ci0"], None)
print "xxxxxxx"
print answer
while answer != options_chapter_intro["option_1"]:
	answer = user_input(options_chapter_intro, choices_chapter_intro["ci0"], None)
	if answer == options_chapter_intro["option_2"]:
		print text_intro["ti1"]
	if answer == options_chapter_intro["option_1"]:
		print "you picked up the note."		


#while answer != options_chapter_intro["option_1"]:
	#print "xxxxxx" + answer
	#print text_intro["ti1"]
	#user_input(options_chapter_intro, choices_chapter_intro["ci0"], None)
	#if answer != options_chapter_intro["option_1"]:
		#answer = None




