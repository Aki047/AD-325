class TextOperation:
    def __init__(self, operation_type, character=None):
        self.operation_type = operation_type
        self.character = character

class TextEditor:
    def __init__(self):
        self.text = ""
        self.operation_stack = []

    def add_character(self, character):
        self.text += character
        self.operation_stack.append(TextOperation("add", character))
        self.display_text()

    def delete_last_character(self):
        if self.text:
            deleted_character = self.text[-1]
            self.text = self.text[:-1]
            self.operation_stack.append(TextOperation("delete", deleted_character))
            self.display_text()
        else:
            print("Text is empty. Nothing to delete.")

    def undo_last_operation(self):
        if self.operation_stack:
            last_operation = self.operation_stack.pop()
            if last_operation.operation_type == "add":
                self.text = self.text[:-1]
            elif last_operation.operation_type == "delete":
                self.text += last_operation.character
            self.display_text()
        else:
            print("No operation to undo.")

    def display_text(self):
        print("Current Text:", self.text)

def main():
    text_editor = TextEditor()

    while True:
        print("\nSelect an option:")
        print("1. Add character")
        print("2. Delete last character")
        print("3. Undo")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            character = input("Enter character to add: ")
            text_editor.add_character(character)
        elif choice == "2":
            text_editor.delete_last_character()
        elif choice == "3":
            text_editor.undo_last_operation()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
