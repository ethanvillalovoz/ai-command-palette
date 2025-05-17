# Entry point for the AI Command Palette CLI
from intent_parser import parse_intent
from action_handlers import handle_action

def main():
    print("Welcome to AI Command Palette!")
    while True:
        user_input = input("Enter a command (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Parse the intent
        intent = parse_intent(user_input)

        # Handle the action
        handle_action(intent)

if __name__ == "__main__":
    main()