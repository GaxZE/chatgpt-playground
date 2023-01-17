import os
import openai
from dotenv import load_dotenv
load_dotenv()


def main():
    # Set the API key
    openai.api_key = os.environ.get("OPENAI_TOKEN")

    # Use the `Completion` class to generate a response
    model_engine = "text-davinci-002"
    prompt = input("What would you like to ask?: \n")
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.7,
    )

    # Print the response
    print(response.choices[0].text)


if __name__ == "__main__":
    main()
