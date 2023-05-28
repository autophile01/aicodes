import random

# Function to generate a random greeting
def get_greeting():
    greetings = ["Hello!", "Hi there!", "Welcome!", "Greetings!"]
    return random.choice(greetings)

# Function to analyze user input and generate a response
def generate_response(user_input):
    # Example response generation based on user input
    if "product" in user_input:
        return "We have a wide range of products available. How can I assist you in finding a specific product?"
    elif "price" in user_input:
        return "Our prices vary depending on the product. Could you please provide more details so that I can assist you better?"
    elif "delivery" in user_input:
        return "We offer various delivery options. To provide accurate information, could you please provide your location?"
    elif "booking" in user_input:
        return "Sure! I can help you with that. May I know the destination and travel date?"
    elif "account" in user_input:
        return "If you need assistance with your account, please visit our website and go to the account section."
    elif "help" in user_input:
        return "I'm here to help! Please let me know how I can assist you."
    else:
        return "I'm sorry, but I couldn't understand your request. Could you please rephrase or provide more information?"

# Main program loop
def main():
    print(get_greeting())
    while True:
        user_input = input("> ")
        response = generate_response(user_input.lower())
        print(response)

        # Break the loop if user wants to exit
        if "bye" in user_input.lower() or "quit" in user_input.lower():
            print("Thank you for using our chatbot. Goodbye!")
            break

# Run the main program
if __name__ == "__main__":
    main()