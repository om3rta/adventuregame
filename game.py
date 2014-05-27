#PYOA game
#What do?
#Present choice, user input, result

story = {
	"choices": {
		"intro":{
			"first_set": "choices: bla bla bla",
			"second_set": "choices: bla balaba "
		}
		"the note":{
			""
		}
	}
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

#user_input(None, "choices: do nothing, pick up note", "do nothing", "pick up note", "You stand around for a bit.Nothing happens.")
#user_input(None, "choices: go left, go right", "go left", "go right", "This room is empty")



"""
	Need overall error reporting when user types something not recognized
		- wrap this in a single function that you can use everywhere
	While actionX != loop is used a lot of times:
		- put this functionality into one function and call it each time you need it
			this function will also probably user the error function you defined above.
	Also add comments to functions and variables
		ex. def function blaBLABLA():
			\""" This tells me what the function does \"""
		ex. var1 = '4' # This is a comment about my variable
"""
print "You wake up in an empty room. You see a note on the ground. What do?"

user_input("choices: do nothing, pick up note", None, None, "do nothing", "pick up note", None, "You stand around for a bit.Nothing happens.", "", 0)


# Wow. Such Plot. Much deep. Very Princess JB
print
print """You pick up the crumpled note.
On the page is a bubbly, feminine script that reads:"""
print
print """Dear traveler
Help!
I'm trapped somewhere in this building. Please come find me
I'll make it worth your time **wink wink**

-Princes JB

you see a map on the bottom of the note

 ___ ___ ___
|JB |   | X |
 ___ ___ ___
| X |   |   |
 ___ ___ ___
| X |_E_| W |

You place the crumpled note in your pocket

You look around the room and see a door to your left, a door ahead, and a door to your right. What do?
"""



#action 2: looking for JB. Go left, right, or straight
action2 = ""
action2a = ""
action2b = ""

# looking for JB
#user_input(stuff, ae,awet,awe,tawet,)
#user_input(awe,we,awe,awe,wae)

user_input("choices: go left, go right, go straight", "choices: do nothing, go back", "choices: do nothing, look out window, go back", "go left", "go right", "go straight", "You enter an empty room with no doors. What do?", "You enter a room with only a window. What do?", 1)

"""
while action2 != "go straight":
	action2 = raw_input(["choices: go left, go right, go straight"])
	action2 = action2.lower()
	if action2 == "go left":
		print
		print "You enter an empty room with no doors. What do?"
		print
		action2a = ""
		"""

while action2a != "go back":
	action2a = raw_input(["choices: go back"])
	action2a = action2a.lower()
	if action2a != "go back":
		print
		print "You can't stick around here forever. Go find Princess JB!"
		print
		action2a = ""
	elif action2a == "go back":
		print
		print"You return to the previous room."
		print
	elif action2 == "go right":
		print
		print "You enter a room with only a window. What do?"
		print
		action2b = ""
		while action2b != "go back":
			action2b = raw_input(["choices: look out window, go back"])
			action2b = action2b.lower()
			if action2b == "look out window":
				print
				print "It's dark out. Not too far in the distance you see a dence forest"
				print
				action2b = ""
			elif action2b == "go back":
				print
				print "You return to the previous room."
				print
			elif action2b != "go back" or "look out window":
				print
				print "Come on. We need to go save Princess JB!"
				print
				action2b = ""
	elif action2 != "go straight":
		print
		print "That's not one of your choices."
		print

#go striaght
print
print"""As you enter the room, the door behind you slams shut.
You hear a loud click as the door is locked behind you

As you look around the room, you see a door to your left, a door to your right, and a door straight ahead

What do?"""
print

action3 = ""
action3a = ""
action3b = ""

while action3 != "go straight":
	action3 = raw_input(["choices: go left, go right, go straight"])
	action3 = action3.lower()
	if action3 == "go left":
		print
		print "Just another empty room. This one smells like strawberries."
		print
		while action3a != "go back":
			action3a = raw_input(["choices: go back"])
			action3a = action3a.lower()
			if action3a == "go back":
				print
				print "You return to the previous room."
				print
			elif action3a != "go back":
				print
				print "Sure. Just sit around while the hhhhoooooootest of princesses waits for you to save her."
				print
				action3a = ""
	if action3 == "go right":
		print
		print "You enter a bed chamber containing a bed, a vanity, and a dresser"
		print
		action3b = ""
		while action3b != "go back":
			action3b = raw_input(["choices: go back, check dresser"])
			action3b = action3b.lower()
			if action3b == "check dresser":
				print
				print "You open a drawer that contains a mix of boxer-briefs and frilly panties"
				print "Across one of the butts of the frilly pairs is the word 'Crisp'."
				print
				action3b = ""
			elif action3b == "go back":
				print
				print "You return to the previous room"
				print
			elif action3b != "go back" or "check dresser":
				print
				print "You can't give up now. Make your choice!"
				print
	if action3 != "go straight":
		print
		print "That's not one of your choices"
		print
#go straight
print
print """As you enter the room, the door behind you shuts and locks.

Why does this keep happening?

It's almost as if the programmer of this game didn't want to wirte what happened if you went back.

What a lazy shit."""
print
print """Anyways... You see a locked door to your left and a door to your
right."""
print

action4 = ""
action4a = ""

while action4 != "go left":
	action4 = raw_input(["choices: go left, go right"])
	action4 = action4.lower()
	if action4 == "go right":
		print
		print"You enter a room with nothing in it."
		print
		action4a = ""
		while action4a != "go back":
			action4a = raw_input(["choices: go back"])
			action4a = action4a.lower()
			if action4a == "go back":
				print
				print "You return to the previous room."
				print
			elif action4a != "go back":
				print
				print "Don't give up now!"
				print
				action4a = ""

#go left"
print
print "You come to a locked door. What should you do?"
print

action5 = ""
action5a = ""
action5b = ""

while action5 != "break door":
	action5 = raw_input(["choices: break door, knock"])
	action5 = action5.lower()
	if action5 == "knock":
		print
		print "You hear a low, sexy voice respond 'Please, help me!'"
		print
		action5 = ""
	elif action5 != "break door":
		print
		print "What are you going to do about this door?"
		print

print
print"""You take a few steps back and charge the door.
You fall through the doorway as the door breaks from its hinges.

When you stand up, you see the one you cam to rescue.
Tall, fit, cleanly shaved up top.

Princess JB leans down and offers you a hand.

'Thank you brave sir. That was very crisp. To reward your heroism, I offer you 
unlimited handies for
as long as we both shall live'

You and princess JB lived happily ever after.

THE END
 """
print


#Old version stuff:

#first action. Do nothing, or pick up note
"""
while action1 != "pick up note":
	action1 = raw_input(["choices: do nothing, pick up note"])
	action1 = action1.lower()
	if action1 == "do nothing":
		print
		print \"""You stand around for a bit.
Nothing happens.
Your choices remain the same\"""
		print
	elif action1 != "pick up note":
		print
		print "I have no clue what you've just said. Try again"
		print
"""