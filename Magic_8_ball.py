# Things need to be tackled 
  # Yes - definitely
  # It is decidely so 
  # Without a doubt
  # Reply hazy, try again
  # Ask again later
  # Better not tell you now
  # My sources say no
  # Outlook not so good
  # Not enough power to answer
  # Thinking 
  # What is the question again?
  # Very doubtful
  # [Name] asks: [Question] Magic 8-Ball’s answer: [Answer]

# Start code here
import random


name = "Sink"
question = "Monkey magic?"
answer = ""
random_number = random.randint(1, 12)

# Control for random of answer
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  asnwer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 8:
  answer = "Not enough power to answer"
elif random_number == 8:
  answer = "Thinking"
elif random_number == 8:
  answer = "What is the question again?"
else:
  answer = "Very doubtful"

#Control to ask user to add name and question
if question == "":
  print("Please ask a Yes or No question.") 
elif name == "":
  print("Question: " + question)
  print("Magic 8-ball's answer: " + answer)
else:
  print(name + " asks: " + question) 
  print("Magic 8-ball's answer: " + answer)

print("🎱")
