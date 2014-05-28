#options
options_chapter_intro = {"option_1": "pick up note", "option_2": "do nothing"}
options_chapter_one = {"option_1": "go left", "option_2": "go right", "option_3": "go striaght"}
options_left_room = {"option_1": "do nothing", "option_2": "go back"}

#choices
choices_chapter_intro = {"ci0": "choices: do nothing, pick up note"}
choices_chapter_one = {"c10": "go left, go right, go straight.", "c11": "do nothing, go back"}

#text
text = {
	"text_intro": {
		"wake_up": "\nYou wake up in an empty room. You see a note on the ground. What do?\n",
		"do_nothing": "\nYou stand around for a bit.\nNothing happens.\nYour choices remain the same."
	},
	"text_chapeter_1": {
		"pick_up_note": "\nHelp!" + 
			"\nI'm trapped somewhere in this building. Please come find me" + 
			"\nI'll make it worth your time **wink wink**" + 
			"\n\n-Princes JB" +
			"\n\nYou place the crumpled note in your pocket." +
			"\nYou look around the room and see a door to your left, a door ahead, and a door to your right. What do?", 
		"left_room": "\nYou enter a room with nothing it it. What do"
		

	}
}

#Main Function
def user_input(options, choices):
	answer = ""
	exit = False
	option_3 = None
	option_number = len(options)
	option_1 = options["option_1"]
	option_2 = options["option_2"]
	if option_number > 2:
		option_3 = options["option_3"]
	error_text = "\nI have no clue what you've just said\n"
	while exit != True:
		answer = raw_input([choices])
		answer = answer.lower()
		if answer == option_1:
			exit = True
		if answer == option_2:
			exit = True
		if answer == option_3:
			exit = True
		if exit != True:#answer != option_1: #use loop here to account for unlimited opitons
			print error_text
	return answer	
	

#intro
print text["text_intro"]["wake_up"]
#pick up not exits while loop
answer = None
while answer != options_chapter_intro["option_1"]:
	answer = user_input(options_chapter_intro, choices_chapter_intro["ci0"])
	if answer == options_chapter_intro["option_2"]:
		print text["text_intro"]["do_nothing"]
	if answer == options_chapter_intro["option_1"]:
		print "\nyou picked up the note."
		print text["text_chapeter_1"]["pick_up_note"]		
#loop exits after note pickup. On to next part of game
while answer != options_chapter_one["option_3"]:
	answer = user_input(options_chapter_one, choices_chapter_one["c10"])
	if answer == options_chapter_one["option_1"]:
		print text["text_chapeter_1"]["left_room"]
		while answer != "go back":
			answer = user_input(options_left_room, choices_chapter_one["c11"])
			print answer

	if answer == options_chapter_one["option_2"]:
		print "you went right"
	if answer == options_chapter_one["option_3"]:
		print  "you went forward. Also, this answer should move you to then ext choice"
print "option 3"

