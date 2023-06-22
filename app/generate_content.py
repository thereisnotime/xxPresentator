import os
import sys
import time
from dotenv import load_dotenv
import openai

from constants import backstory_content


class ContentGenerator:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.model = "gpt-3.5-turbo"
        self.example_file = "../input/input.example.json"
        self.output_file = "../input/input.json"
        self.prompt_file = "prompt.txt"
        self.example_input = open(self.example_file, "r").read()
        self.example_input = self.example_input.replace("\n", " ")
        self.backstory = backstory_content

    def send_prompt(self, prompt):
        return openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "system", "content": self.backstory},
                {"role": "user", "content": self.example_input},
                {"role": "user", "content": prompt}
            ],
            max_tokens=3500,
            n=1,
            temperature=0.2,
        ).choices[0].message.content.strip()

    def generate_content(self, prompt):
        start_time = time.time()
        print('Generating presentation data...')

        if prompt == "":
            with open(self.prompt_file, 'r') as f:
                prompt = f.read()

        print(f"\nYour prompt: {prompt}\n")
        output = self.send_prompt(prompt)

        with open(self.output_file, "w") as f:
            f.write(output)

        end_time = time.time()
        duration = end_time - start_time
        duration = "{:.2f}".format(duration)
        print(f'Presentation data created in {duration} seconds!')


if __name__ == '__main__':
    generator = ContentGenerator()
    prompt = ""
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    generator.generate_content(prompt)
