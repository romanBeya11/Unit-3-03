'''
Created by: Roman Beya
Created on: 16-oct-2017
Created for: ICS3U
This program plays rock, paper, scissors depending on a random number which is then compared to the user input
'''
import ui
from numpy import random
	
def rock_touch_up_inside(sender):
	# generates a random number to decide between rock,paper, or scissors
	random_integer = random.randint(1, 4)
	if random_integer == 1: # Computer chooses rock
		view['output_label'].text = "Computer choice:ROCK\nYour choice: ROCK\nROCK clashes with Rock! YOU TIE! Play again?"
		
	elif random_integer == 2: # Computer chooses paper
		view['output_label'].text = "Computer choice: PAPER\nYour choice: ROCK\nPAPER covers Rock! YOU LOSE! Play again?"
		
	else: # Only option left is scissors
		view['output_label'].text = "Computer choice: SCISSORS\nYour choice: ROCK\nROCK crushes Scissors! YOU WIN! Play again?"

def paper_touch_up_inside(sender):
	# generates a random number to decide between rock,paper, or scissors
	random_integer = random.randint(1, 4)
	if random_integer == 1: # Computer chooses rock
		view['output_label'].text = "Computer choice: ROCK\nYour choice: PAPER\nPaper covers Rock! YOU WIN! Play again?"
		
	elif random_integer == 2: # Computer chooses paper
		view['output_label'].text = "Computer choice: PAPER\nYour choice: PAPER\nPaper covers Paper! YOU TIE! Play again?"
		
	else: # Only option left is scissors
		view['output_label'].text = "Computer choice: SCISSORS\nYour choice: PAPER\nScissors cuts Paper! YOU LOSE! Play again?"
		
def scissors_touch_up_inside(sender):
	# generates a random number to decide between rock,paper, or scissors
	random_integer = random.randint(1, 4)
	if random_integer == 1: 
		view['output_label'].text = "Computer choice: ROCK\nYour choice: SCISSORS\nRock crushes Scissors! YOU LOSE! Play again?"
		
	elif random_integer == 2: # Computer chooses paper
		view['output_label'].text = "Computer choice: PAPER\nYour choice: SCISSORS\nScissors cuts Paper! YOU WIN! Play again?"
		
	else: # Only option left is scissors
		view['output_label'].text = "Computer choice: SCISSORS\nYour choice: SCISSORS\nScissors cuts Scissors! YOU TIE! Play again?"
	
	
view = ui.load_view()
view.present('sheet')
