

questions ={1: {'noob': {1: 'Python is a _______ that takes your code and executes your instructions.',
			2: 'Python is very strict about its _______, your code must be clean and tidy.',
			3: 'A _______ is also called a routine or method.',
			4: "These routines are also known as _______'s.",
			5: 'Functions are important and necessary to simplify _______ tasks.'},
		    'rookie': {1: 'In Python Grammar for Arithmetic, numbers are known as an _______.',
			2: 'In Python Arithmetic an asterix * is called a _______.',
			3: 'Is this the correct , true or false?  _______ Operator Expression Expression',
			4: 'Is this the correct , true or false?  _______ Expression Expression Operator',
			5: 'Is this the correct , true or false?  _______ Operator Expression Operator'},
			'jedi': {1: 'You can not _______ strings and numbers together.',
			2: 'You can however _______ strings and numbers together.',
			3: 'Code with a hash tag in front is called _______ code.',
			4: 'Printing  "4" + "4" would produce the result _______.',
			5: 'The above is an example of _______'}},
			2: {'noob': {1: 'Programming is grounded in _______.',
			2: 'Python is a high level _______',
			3: 'We can not use natural languages to program because they are _______.',
			4: "Natural languages are very _______.",
			5: 'The word ambiguous means open to more than one _______.'},
		    'rookie': {1: '_______ is a valid expression; 3  (1*(2*(3*4))  + 33  ((7)))  ((3)',
			2: '(1*(2*(3*4)) is valid code. true or false? _______.',
			3: '(((7)))  is valid code. true or false? _______.',
			4: 'Type the symbol you would use to assign _______.',
			5: 'What is the difference between: 2 + 3 = 5 and: my_variable = 5? _______'},
			'jedi': {1: 'We often need to make _______ between values',
			2: 'We can do the above by using an _______ statement.',
			3: 'We can also do equality comparisons with _______ (not equal) and ==.',
			4: 'Complete this line of code; if a == b _______ b == c:',
			5: 'What is missing in this line?; def someThing() _______'}},
			3: {'noob': {1: '_______, using more words than needed; wordiness.',
			2: 'John Bakus created the _______ form.',
			3: 'This form uses _______ replacement.',
			4: 'This uses a method called _______.',
			5: 'non-terminal rules are one side and terminal rules are on the _______ side.'},
		    'rookie': {1: 'Programmers use _______ to represent values in their code.',
			2: 'We sometimes call numbers without a variable "_______".',
			3: 'It is best to _______ the amount of "magic numbers" in our code.',
			4: 'You must always _______ a variable before you can use it.',
			5: 'Strings contain _______ and must be enclosed with quotes or double quotes.'},
			'jedi': {1: 'True or False is considered type _______.',
			2: 'A _______ loop has an end and will not loop for ever.',
			3: 'A _______ loop can loop forever.',
			4: 'Witch one of the above loops is the preferred method of coding, _______.',
			5: 'Witch of the following is mutable, dictionary or string, _______.'}}}

answers ={1: {'noob': {1: 'interpreter', 2: 'indentation', 3: 'function', 4: 'algorithm', 5: 'repetitive'},
		  'rookie': {1: 'expression', 2: 'operator', 3: 'false', 4: 'false', 5: 'false'},
		  'jedi': {1: 'add', 2: 'multiply', 3: 'pseudo', 4: '44', 5: 'concatenation'}},
		  2: {'noob': {1: 'arithmetic', 2: 'language', 3: 'ambiguous', 4: 'verbose', 5: 'interpretation'},
		  'rookie': {1: '3', 2: 'true', 3: 'true', 4: '==', 5: 'nothing'},
		  'jedi': {1: 'comparisons', 2: 'if', 3: '!=', 4: 'and', 5: ':'}},
		  3: {'noob': {1: 'verbose', 2: 'backus-naur', 3: 'non-terminal', 4: 'derivation', 5: 'right'},
		  'rookie': {1: 'variables', 2: 'magic numbers', 3: 'reduce', 4: 'introduce', 5: 'characters'},
		  'jedi': {1: 'boolean', 2: 'for', 3: 'while', 4: 'for', 5: 'dictionary'}}}

# note when I forgot the last bracket above, I got an error saying def below was invalid syntax.

def success():
 	# this function is to keep from printing success over and over.
	print 'Success that is correct!'

def failure():
 	# this function is like the one above.
	print 'That is incorrect, please try again.'

def levelInfo(level, dif):
	# confirms the level you are on, and cuts down on repetition
	print 'You are on level', level, dif + ',', ' Good luck.'

def question(level, dif, q_num):
	# this will call questions up to 5 and then go to  play()
	print questions[level][dif][q_num]
	if raw_input('Type here. >> ') == answers[level][dif][q_num]:
		success()
		string = questions[level][dif][q_num]
		string = string.replace('_______', answers[level][dif][q_num])
		q_num = q_num + 1
		if q_num > 5:
			play()
		else:
			print string
			question(level, dif, q_num)
	else:
		failure()
		question(level, dif, q_num)

def chooseLevel(level, dif):
	# this sets the level and difficulty variables, the original was much bigger.
	# I discovered it was cleaner to state not equal too then equal too. Less lines of code.

	if level !='1' and level != '2' and level != '3':
	 # I used the same concept below, code looks much better.
		play()
	else:
		q_num = 1
		levelInfo(level, dif)
		question(int(level), dif, q_num)

def play():
	# we pick our difficulty and level and give it to chooseLevel(level, dif)
	print 'What difficulty, noob, rookie or jedi?'
	dif = raw_input('Type here. >> ')
	if dif != 'noob' and dif != 'rookie' and dif != 'jedi':
		play()

	print 'What level 1, 2 or 3'
	level = raw_input('Type here. >> ')
	if level != '1' and level != '2' and level != '3':
		play()

	chooseLevel(level, dif)

play()
