def compare(u1, u2):
	if u1 == u2:
		return("It's a tie!")
	elif u1 == 'rock':
		if u2 == 'scissors':
			return("Rock wins!")
		else:
			return("Paper wins!")
	elif u1 == 'scissors':
		if u2 == 'paper':
			return("Scissors win!")
		else:
			return("Rock wins!")
	elif u1 == 'paper':
		if u2 == 'rock':
			return("Paper wins!")
		else:
			return("Scissors win!")

again = True
while again != False:
	kontrola = False
	while kontrola != True:
		print ('Player one please enter rock/paper/scissors:')
		player1 = input()
		if player1 == 'rock' or player1 == 'paper' or player1 == 'scissors':
			kontrola1 = True
		else:
			print ('You have entered wrong object. Enter again')
			kontrola1 = False

		print ('Player two please enter rock/paper/scissors:')
		player2 = input()
		if player2 == 'rock' or player2 == 'paper' or player2 == 'scissors':
			kontrola2 = True
		else:
			print ('You have entered wrong object. Enter again')
			kontrola2 = False

		if kontrola1 == True and kontrola2 == True:
			kontrola = True

		print ("player1 entered {}".format(player1))
		print ("player2 entered {}".format(player2))

		print(compare(player1,player2))

		print ('Do you want to play again? (Y/N)')
		if input() == 'Y':
			again = True
		else:
			again = False
