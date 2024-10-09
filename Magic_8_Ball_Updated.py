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
question = "What is your name?"
answer = ""
random_number = random.randint(1, 12)

# Determine the answer based on the random number
# Used a list instead of "if"
# Used .get to get information from answer list
answers = {1: "Yes - definitely", 2: "It is decidedly so", 3: " Without a doubt", 4: "Reply hazy, try again", 5: "Ask again later", 6: "Better not tell you now", 7: "My source say no", 8: "Outlook not so good", 9: "Very doubtful", 10: "Thinking", 11: "What is the question again?", 12: "Not enough power to answer"}
answer = answers.get(random_number)

# Control to ask user to add name and question
# used not... and .endswith instead of ==
if not question.endswith("?"):
  print("Please ask a Yes or No question.") 
elif name == "":
  print("Question: " + question)
  print("Magic 8-ball's answer: " + answer)
else:
  print(name + " asks: " + question) 
  print("Magic 8-Ball's answer: " + answer)

print("🎱")

