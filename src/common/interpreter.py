class Interpreter:
    @staticmethod
    def yn(message):
        user_input = input(f"\n{message} (y/n) ")
        return user_input.lower() in ["y", "yes"]
