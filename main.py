# Entry point for the AI Command Palette CLI
from intent_parser import parse_intent
from action_handlers import handle_action
from action_handlers.summarize_file import summarize_file

def main():
    print("Welcome to AI Command Palette!")
    while True:
        command = input("Enter a command (or 'exit' to quit): ").strip()
        if command.lower() == "exit":
            print("Goodbye!")
            break
        elif command.startswith("summarize "):
            # Extract the file path from the command
            file_path = command[len("summarize "):].strip().strip('"')
            summarize_file(file_path)
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()