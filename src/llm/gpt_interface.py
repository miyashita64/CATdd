"""GPT仲介モジュール"""

import os
from openai import OpenAI
from common.log import Log


class GPTInterface:
    """GPTとの通信を行うクラス"""

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

    @classmethod
    def request(cls, model, user_prompt):
        """受け取ったpromptをOpenAI APIに送信し、レスポンスを返す."""
        available_models_request = {
            "text-davinci-003": cls.request_text_davinci_003,
            "gpt-3.5-turbo": cls.request_gpt_3_5_turbo,
            "gpt-4": cls.request_gpt_4
        }
        only_prompt_models = ["text-davinci-003"]
        system_prompt = "You are a helpful assistant. "
        try:
            if model in available_models_request:
                if model in only_prompt_models:
                    request_value = system_prompt + "\n" + user_prompt
                else:
                    request_value = [{'role': 'system', 'content': system_prompt},
                                {'role': 'user', 'content': user_prompt}]
                response = available_models_request[model](request_value)                
                return response
            else:
                raise Exception(f"Model \"{model}\" is undefined")
        except Exception as e:
            print(e)
            exit(1)

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
    res = GPTInterface.request_gpt_4(prompt)
    print(f"\033[36mres: {res}\033[0m")
