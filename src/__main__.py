from gpt_interface import GPTInterface

def main():
    prompt = "Hello World."
    response = GPTInterface.request(prompt)
    print(response)

if __name__ == "__main__":
    main()