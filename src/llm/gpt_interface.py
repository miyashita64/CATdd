"""GPT仲介モジュール"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

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
        
        model = "text-davinci-003"

        response = client.completions.create(model=model,
                                             prompt=prompt,
                                             max_tokens=1024,
                                             n=1,
                                             stop=None,
                                             temperature=0.8)
        return response.choices[0].text.strip()

    @staticmethod
    def request_turbo(messages):
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=messages)

        #返信のみを出力
        return response["choices"][0]["message"]["content"]

    @staticmethod
    def request_gpt_4(messages):
        """GPT-4にリクエストを送信し、レスポンスを返す静的メソッド。
        Args:
            prompt: String
        Return:
            GPT-4から返ってきた文字列: String
        """
        # APIキーの設定
        
        model = "gpt-4"  # GPT-4のモデルを指定
        response = client.chat.completions.create(model=model,
                                                  messages=messages,
                                                  max_tokens=1024,
                                                  n=1,
                                                  stop=None,
                                                  temperature=0.8)
        return response.choices[0].message.content

if __name__ == "__main__":
    # """
    # prompt = input("prompt: ")
    prompt = "hello world."
    res = GPTInterface.request(prompt)
    print(f"\033[36mres: {res}\033[0m")

    messages = [{'role': 'system', 'content': 'You are a helpful assistant.'},                                                                                      
                {'role': 'user', 'content': prompt}]

    res = GPTInterface.request_turbo(messages)
    print(f"\033[36mres: {res}\033[0m")
    # res = GPTInterface.request_gpt_4(messages)
    # print(f"\033[36mres: {res}\033[0m")
