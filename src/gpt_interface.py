"""GPT仲介モジュール"""

import os
import openai
from janome.tokenizer import Tokenizer

class GPTInterface:
    """GPTとの通信を行うクラス"""

    @staticmethod
    def request(prompt):
        """受け取ったpromptをGPTに送信し、レスポンスを返す.

        Args:
            prompt: String
        Return:
            GPTから返ってきた文字列: String
        """
        # APIキーの設定
        openai.api_key = os.environ["OPENAI_API_KEY"]
        model_engine = "text-davinci-003"

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.8,
        )
        return response.choices[0].text.strip()

    @staticmethod
    def count_tokens(text):
        t = Tokenizer()
        tokens = t.tokenize(text)
        return len(list(tokens))

    @staticmethod
    def sub_japanese(text):
        return re.sub('[ぁ-んァ-ン一-龥]', '', text)