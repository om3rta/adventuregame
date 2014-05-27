#PYOA1.1: The Quest for the Crisp Princess

#import os version. For now, just to know what 'clear' command to use
import os

#Title screen w/ instructions
print"""
     #############                         #############
    ##            *##                     ##############*##
   #               **#                   ################**#
  #       %% %%    ***#                 ########  #  ####***#
 #       %%%%%%%   ****#               ########       ###****#
#         %%%%%    *****#             ##########     ####*****#
#   ###     %     ###***#             ####   ##### #####   ***#
#  # ####       #### #**#             ###      #######      **#
#  #     #     #     #**#             ###   X   #####   X   **#
#   #####  # #  #####***#             ####     ## # ##     ***#
#         #   #  *******#             ########## ### ##*******#
 ### #           **# ###               ### ############**# ###
     # - - - - - - #                       ##-#-#-#-#-#-##
      | | | | | | |                         | | | | | | |
       
       Choose Your Own Adventure 1:

       			The Quest for the Crisp Princess

       	Instructins:

       		You will be given a set of choices as you read. When prompted, type your choice and hit 'Enter'.

"""
#Story Parts
partone = "You find yourself in an empty room. You see see a note on the ground. What do?"
parttwo = "You pick up the note on the gound.\nOn the page is a bubbly, feminie script that reads: \n\nHelp!\nI'm trapped somewhere in this building. Please come find me.\nI'll make it worth your time. *wink wink*\n\n-Princess JB\n\nYou place the crumpled note in your pocket.\n You look around the room and see a door to your left, a door ahead, and a door to your right. What do?"

#meat and potatoes. Call this function for every correct direction traveled
def user_input(action_type, choices, option1, option2, text_output1, action_sub1, option_sub1, choices_sub1, text_sub1, text_sub2):
	error_text = "I have no clue what you've just said. Try again"
  while action_type != option1:
    action_type = raw_input([choices])
    action_type = action_type.lower()
  if action_type == option2:
    print "\n" + text_output1 + "\n"
  elif action_type != option1:
    print "\n" + error_text "\n"

#clear screen and part one
os.system('cls' if os.name=='nt' else 'clear')

print  "\n" + partone + "\n"
user_input(None, "choices: do nothing, pick up note", "pick up note", "do nothing", "You stand there for a bit.\nNothing happens.\nYour choices remain the same.", None, None, None, None, None)

#part two
os.system('cls' if os.name=='nt' else 'clear')
print "\n" + parttwo + "\n"
user_input(None, "choices: go left, go right, go straight", "go straight", "go left", "You enter an empty room with no other doors. What do?", None, "go back", "choices: do nothing, go back", "You can't stick around here forever. Go find Princess JB!", "You return to the previous room")
