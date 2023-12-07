"""GPT仲介モジュール"""

import os
from openai import OpenAI
from common.log import Log


class GPTInterface:
    """GPTとの通信を行うクラス"""

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    @classmethod
    def request(cls, user_prompt):
        """受け取ったpromptをOpenAI APIに送信し、レスポンスを返す."""
        return GPTInterface.request_text_davinci_003(user_prompt)
    
    @classmethod
    def request_code(cls, user_prompt, assistant_prompt=""):
        """受け取った情報を送信し、ソースコードを返す."""
        system_prompt = "You are a programmer. Implement the source code as requested. Return the full code, including the non-fixed parts. Please return code only."
        messages = [{'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': user_prompt},
                    {'role': 'assistant', 'content': f"{assistant_prompt}\n"}]
        Log.debug(user_prompt)
        return GPTInterface.request_gpt_3_5_turbo(messages)

    @classmethod
    def request_text_davinci_003(cls, prompt):
        model = "text-davinci-003"
        response = cls.client.completions.create(model=model,
                                             prompt=prompt,
                                             max_tokens=1024,
                                             n=1,
                                             stop=None,
                                             temperature=0.8)
        return response.choices[0].text.strip()

    @classmethod
    def request_gpt_3_5_turbo(cls, messages):
        model = "gpt-3.5-turbo"
        response = cls.client.chat.completions.create(model=model, messages=messages)
        return response.choices[0].message.content

    @classmethod
    def request_gpt_4(cls, messages):
        model = "gpt-4"  # GPT-4のモデルを指定
        response = cls.client.chat.completions.create(model=model,
                                                  messages=messages,
                                                  max_tokens=1024,
                                                  n=1,
                                                  stop=None,
                                                  temperature=0.8)
        return response.choices[0].message.content

if __name__ == "__main__":
    prompt = input("prompt: ")
    res = GPTInterface.request_gpt_3_5_turbo(prompt)
    print(f"\033[36mres: {res}\033[0m")
