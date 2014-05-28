#import os version for screen clear
import os

#options
options_chapter_intro = {"option_1": "pick up note", "option_2": "do nothing"}
options_chapter_one = {"option_1": "go left", "option_2": "go right", "option_3": "go straight"}
options_left_room = {"option_1": "do nothing", "option_2": "go back"}
options_right_room = {"option_1": "do nothing", "option_2": "look out window", "option_3": "go back"}
options_chapter_two = {"option_1": "go left", "option_2": "go right", "option_3": "go straight"}
options_left_room_2 = {"option_1": "do nothing", "option_2": "go back"}
options_right_room_2 = {"option_1": "do nothing", "option_2": "check dresser", "option_3": "go back"}
options_chapter_three = {"option_1": "go left", "option_2": "go right"}
options_right_room_3 = {"option_1": "do nothing", "option_2": "go back"}
options_chapter_end = {"option_1": "do nothing", "option_2": "break door"}

#choices
choices_chapter_intro = {"ci0": "choices: do nothing, pick up note"}
choices_chapter_one = {"c10": "choices: go left, go right, go straight.", "c11": "choices: do nothing, go back", "c12": "choices: look out window, do nothing, go back"}
choices_chapter_two = {"c20": "choices: go left, go right, go straight", "c21": "choices: do nothing, go back", "c22": "choices: check dresser, do nothing, go back"}
choices_chapter_three = {"c30": "choices: go left, go right", "c31": "choices: do nothing, go back"}
choices_chapter_end = {"ce0": "choices: do nothing, break door"}

#text
text = {
	"text_intro": {
		"wake_up": "\nYou wake up in an empty room. You see a note on the ground. What do?\n",
		"do_nothing": "\nYou stand around for a bit.\nNothing happens.\nYour choices remain the same.\n"
	},
	"text_chapeter_1": {
		"pick_up_note": "\nThe note reads:\n\n" +
			"\nHelp!" + 
			"\nI'm trapped somewhere in this building. Please come find me" + 
			"\nI'll make it worth your time **wink wink**" + 
			"\n\n-Princes JB" +
			"\n\nYou place the crumpled note in your pocket." +
			"\nYou look around the room and see a door to your left, a door ahead, and a door to your right. What do?\n", 
		"left_room": "\nYou enter a room with nothing it it. What do?\n",
		"left_room_do_nothing": "\nYou can't stand around forever. Go find JB!\n",
		"right_room": "\nYou enter an empty room with a window. What do?\n",
		"right_room_do_nothing": "\nDon't just stand there. JB is waiting!\n",
		"right_room_window": "\nYou look out the window and see a thick forest in the distance.\n",
		"go back": "\nyou return to the previous room.\n"
	},
	"text_chapter_2": {
		"chapter_2_start": "\nYou enter a room with a door to the left, a door to the right, and a door straight ahead." + 
			"\nThe door behind you shuts, and you hear a loud click as if the door has been locked.\n",
		"left_room": "\nJust another empty room. This one smells like strawberries.\n",
		"left_room_do_nothing": "\nYou stay for a while and enjoy the scent of strawberries.\n",
		"right_room": "\nYou enter a bed chamber containing a bed, a vanity, and a very well crafted dresser.\n",
		"right_room_do_nothing": "\nPrincess JB is still waiting for you. Get going!\n",
		"right_room_dresser": "\nYou find a mix of boxer-briefs and frilly panties" +
			"\nAcross the butt of one of the frilly pairs is the word 'Crisp'" +
			"\nYou are mildly turned on.\n",
		"go back": "\nYou return to the previous room\n"
	},
	"text_chapter_3": {
		"chapter_three_start": "\nAfter passing through the door, it shuts and locks" +
			"\nYou see a door to your left and a door to your right\n",
		"right_room": "\nHey check it out. Another empty room.\n",
		"right_room_do_nothing": "\nYou really must not want to find JB...\n",
		"go back": "\nYou return to the previous room\n"
	},
	"text_chapter_end": {
		"chapter_end_start": "\nYou approach the door. On the other side you hear a low, sexy voice pleading for help.\n",
		"chapter_end_do_nothing": "\nJB is right on the other side of that door. Break it!\n",
		"chapter_end_break_door": "\nYou take a few steps back and charge the door." +
			"\nYou fall through the doorway as the door breaks from its hinges.\n" +
			"\nWhen you stand up, you see the one you came to rescue." +
			"\nTall, fit, cleanly shaved up top." +
			"\nPrincess JB leans down and offers you a hand.\n" +
			"\n'Thank you brave sir. That was very crisp. To reward your heroism, I offer you" +
			"\nunlimited handies for as long as we both shall live" + 
			"\n\nYou and princess JB lived happily ever after." + 
			"\n\n\nTHE END"
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
	
#screen clear
os.system('cls' if os.name == 'nt' else 'clear')

#Title Screen
print"""\n
                              .___.
          /)               ,-^     ^-. 
         //               /           
.-------| |--------------/  __     __  \-------------------.__
|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>
`-------| |--------------| \__/   \__/ |-------------------'^^
         \\   The Quest   \    /|\    / Instructions:
          \)    for JB     \   \_/   /     You will be given choices throughout the story,
                            |       |	   Type your choice and hit enter.
                            |+H+H+H+|
                            \       /
                             ^-----^

"""
#game start
start = None
while start != "yes":
	start = raw_input(["Start game? yes, no"])
	start = start.lower()
	if start != "yes":
		print "You know you want to play. Type 'yes'"
	if start == "yes":
		os.system('cls' if os.name == 'nt' else 'clear')

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
#start chapter one
os.system('cls' if os.name == 'nt' else 'clear')
print text["text_chapeter_1"]["pick_up_note"]		
while answer != options_chapter_one["option_3"]:
	answer = user_input(options_chapter_one, choices_chapter_one["c10"])
	answer = answer.lower()
	#left room
	if answer == options_chapter_one["option_1"]:
		print text["text_chapeter_1"]["left_room"]
		while answer != "go back":
			answer = user_input(options_left_room, choices_chapter_one["c11"])
			answer = answer.lower()
			if answer != "go back":
				print text["text_chapeter_1"]["left_room_do_nothing"]
			if answer == "go back":
				print text["text_chapeter_1"]["go back"]
	#right room
	if answer == options_chapter_one["option_2"]:
		print text["text_chapeter_1"]["right_room"]
		while answer != "go back":
			answer = user_input(options_right_room, choices_chapter_one["c12"])
			answer = answer.lower()
			if answer == options_right_room["option_1"]:
				print text["text_chapeter_1"]["right_room_do_nothing"]
			if answer == options_right_room["option_2"]:
				print text["text_chapeter_1"]["right_room_window"]
			if answer == "go back":
				print text["text_chapeter_1"]["go back"]
	#go striaght and exit loop
#start chapter two
os.system('cls' if os.name == 'nt' else 'clear')
print text["text_chapter_2"]["chapter_2_start"]
answer = None
while answer != options_chapter_two["option_3"]:
	answer = user_input(options_chapter_two, choices_chapter_two["c20"])
	answer = answer.lower()
	if answer == options_chapter_two["option_1"]:
		print text["text_chapter_2"]["left_room"]
		while answer != "go back":
			answer = user_input(options_left_room_2, choices_chapter_two["c21"])
			answer = answer.lower()
			if answer == options_left_room_2["option_1"]:
				print text["text_chapter_2"]["left_room_do_nothing"]
			if answer == options_left_room_2["option_2"]:
				print text["text_chapter_2"]["go back"]
	if answer == options_chapter_two["option_2"]:
		print text["text_chapter_2"]["right_room"]
		while answer != "go back":
			answer = user_input(options_right_room_2, choices_chapter_two["c22"])
			answer = answer.lower()
			if answer == options_right_room_2["option_1"]:
				print text["text_chapter_2"]["right_room_do_nothing"]
			if answer == options_right_room_2["option_2"]:
				print text["text_chapter_2"]["right_room_dresser"]
			if answer == options_right_room_2["option_3"]:
				print text["text_chapter_2"]["go back"]
		#go straight and exit loop
#start chapter three
os.system('cls' if os.name == 'nt' else 'clear')
print text["text_chapter_3"]["chapter_three_start"]
answer = None
while answer != options_chapter_three["option_1"]:
	answer = user_input(options_chapter_three, choices_chapter_three["c30"])
	answer = answer.lower()
	if answer == options_chapter_three["option_2"]:
		print text["text_chapter_3"]["right_room"]
		while answer != "go back":
			answer = user_input(options_right_room_3, choices_chapter_three["c31"])
			answer = answer.lower()
			if answer == options_right_room_3["option_1"]:
				print text["text_chapter_3"]["right_room_do_nothing"]
			if answer == options_right_room_3["option_2"]:
				print text["text_chapter_3"]["go back"]
		#go left and exit loop
#start chapter end
os.system('cls' if os.name == 'nt' else 'clear')
print text["text_chapter_end"]["chapter_end_start"]
answer = None
while answer != options_chapter_end["option_2"]:
	answer = user_input(options_chapter_end, choices_chapter_end["ce0"])
	answer = answer.lower()
	if answer == options_chapter_end["option_1"]:
		print text["text_chapter_end"]["chapter_end_do_nothing"]
	if answer == options_chapter_end["option_2"]:
		os.system('cls' if os.name == 'nt' else 'clear')
		print text["text_chapter_end"]["chapter_end_break_door"]