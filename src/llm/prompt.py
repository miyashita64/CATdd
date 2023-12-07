import tiktoken

class Prompt:
    def __init__(self, elms, max_token):
        self.elms = elms
        self.max_token = max_token
        self.value = self.join_elms()

    def join_elms(self):
        while self.calc_total_token() > self.max_token:
            for elm in self.elms:
                elm.priority -= 1
        return "\n".join([elm.value for elm in self.elms])

    def calc_total_token(self):
        return sum([elm.token for elm in self.elms])


class PromptElement:
    def __init__(self, value, priority=0):
        self.priority = priority if value != "" else -1
        self._value = value
        self._token = self.calc_token()

    @property
    def value(self):
        return self._value if self.priority > 0 else ""

    @property
    def token(self):
        return self._token if self.priority > 0 else 0

    def calc_token(self):
        # トークン数を算出する
        encoding_35 = tiktoken.encoding_for_model("gpt-3.5-turbo-0301")
        encoding = tiktoken.get_encoding(encoding_35.name)
        num_tokens = len(encoding.encode(self.value))
        return num_tokens