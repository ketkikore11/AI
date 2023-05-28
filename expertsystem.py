# Dictionary of common issues and their corresponding solutions
knowledge_base = {
    "printer": "Please check if the printer is properly connected and has enough paper. If the issue persists, try restarting the printer.",
    "network": "Make sure you are connected to the correct network. If you are still having trouble, contact your network administrator.",
    "password": "To reset your password, please visit our password reset page at example.com/reset.",
    "software": "Try uninstalling and reinstalling the software. If that doesn't work, please contact our support team for further assistance.",
    "hardware": "If it's a hardware issue, please provide more details about the problem so that we can assist you better.",
    "email": "Make sure you have entered the correct email address and password. If you are still unable to access your email, please contact our support team."
}

# Function to handle user inquiries
def handle_inquiry(inquiry):
    inquiry = inquiry.lower()
    
    for keyword, solution in knowledge_base.items():
        if keyword in inquiry:
            return solution
    
    return "I'm sorry, I couldn't find a solution for your issue. Please contact our support team for further assistance."

# Main function to handle the conversation
def chat():
    print("Welcome to the Help Desk Management Expert System!")
    print("How can I assist you today?")
    
    while True:
        user_input = input("> ")
        
        if user_input.lower() == 'bye':
            print("Thank you for using our Expert System. Have a great day!")
            break
        
        response = handle_inquiry(user_input)
        print(response)

# Start the expert system
chat()
