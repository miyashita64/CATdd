class Interpreter:
    """ユーザの入力を受け付ける."""
    @staticmethod
    def yn(message):
        """y/nの入力を受け付ける."""
        user_input = input(f"\n{message} (y/n) ")
        return user_input.lower() in ["y", "yes"]
