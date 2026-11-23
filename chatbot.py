print("Hi, this is Elena, your personal chat assistant.")
name = input("Please provide your name for further assistance: ")
print("Welcome, " + name + "! How can I help you")
while True:
    message = input().lower().strip().split()
    if ("don't" in message or "dont" in message or "not" in message) and "want" in message:
        print("Okay, no problem! How else can I help?")
    elif "bye" in message or "goodbye" in message:
        print("Goodbye! Have a great day.")
        break
    elif "order" in message or ("track" in message and "package" in message):
        print("View your order via the app using your provided tracking ID.")
    elif "refund" in message or "return" in message or ("money" in message and "back" in message):
        print("View refund information on the website.")
    elif "delivery" in message or "shipping" in message or "arrival" in message:
        print("View your delivery information on this site.")
    elif "help" in message:
        print("What can I do for you?")
    elif "thanks" in message:
        print("You're welcome!")
    else:
        print("Please contact us via email or phone.")