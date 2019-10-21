# let user input age and country, output is whether the user can drive or not
country = input('Which country are you from: ')
age = input('Please enter your age:')
age = int(age)	# casting very important
if country == 'Taiwan':
	if age >= 18:
		print('You can take driving licence test')
	else:
		print('You can not take driving licence test yet')
elif country == 'America':
	if age >= 16:
		print('You can take driving licence test')
	else:
		print('You can not take driving licence test yet')
else:
	print('You can only enter Taiwan or America')