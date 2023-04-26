"""GPT仲介モジュール"""

import openai
import os

class GPTInterface:
    """GPTとの通信を行うクラス"""

    @staticmethod
    def request(prompt):
        # APIキーの設定
        openai.api_key = os.environ["OPENAI_API_KEY"]
        model_engine = "text-davinci-003"

        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        return response.choices[0].text.strip()