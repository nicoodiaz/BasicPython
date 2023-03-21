import random

answers = ['Yes - definitely.','It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

question = input('What is your question?: ')
magic_8_ball = random.choice(answers)
print(f'Question: {question}')
print(f'Answer: {magic_8_ball}')