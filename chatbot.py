import random

# Responses for different types of user inputs
greetings = ["hello", "hi", "hey", "welcome"]
menu = ["menu", "options", "what do you have", "offerings"]
order = ["order", "place an order", "I want to order"]
thanks = ["thank you", "thanks", "great", "awesome"]

# Coffee shop menu
coffee_menu = {
    "espresso": 3.0,
    "cappuccino": 4.0,
    "latte": 4.5,
    "americano": 3.5,
    "mocha": 4.5,
    "macchiato": 4.0
}

# Function to generate a random response from a list of responses
def get_random_response(responses):
    return random.choice(responses)

# Function to display the coffee shop menu
def display_menu():
    print("Here's our menu:")
    for item, price in coffee_menu.items():
        print(f"- {item.capitalize()}: ${price}")

# Function to take the user's order
def take_order():
    print("Sure! What would you like to order?")
    order = input("> ").lower()
    if order in coffee_menu:
        price = coffee_menu[order]
        print(f"Great choice! Your {order} will be ${price}.")
    else:
        print("Sorry, we don't have that on our menu.")

# Main chatbot loop
def chat():
    print("Welcome to the Coffee Shop!")
    print("How can I assist you today?")

    while True:
        user_input = input("> ").lower()

        if user_input in greetings:
            response = get_random_response(greetings)
            print(response)
        elif user_input in menu:
            display_menu()
        elif user_input in order:
            take_order()
        elif user_input in thanks:
            print("You're welcome!")
        elif user_input == "bye":
            print("Thank you for visiting the Coffee Shop. Have a great day!")
            break
        else:
            print("I'm sorry, I didn't understand that. Can you please rephrase?")

# Start the chatbot
chat()
