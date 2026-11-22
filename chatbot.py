print("Hi, this is Elena, your personal chat assistant.")
name = input("Please provide your name for further assistance: ")
print("Welcome, "+name+"! How can I help you")
while True:
    message = input().lower()
    if "bye" in message:
        print("Goodbye! Have a great day.")
        break
    elif "order status" in message:
        print("View your order via the app using your provided tracking ID.")
    elif "refund" in message:
        print("View refund information on the website.")
    elif "delivery" in message:
        print("View your delivery information on this site.")
    elif "help" in message:
        print("What can I do for you?")
    elif "thanks" in message :
        print("You're welcome!")
    else:
        print("Please contact us via email or phone.")
    

