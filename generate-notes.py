import os
import importlib
import openai
import time
import re
import sys
from dotenv import load_dotenv

###########################################################
# TODO: XXXX
###########################################################

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
model = "gpt-3.5-turbo"
example_file = "input.json"
output_file = "notes.txt"
prompt_file = "prompt.txt"
example_input = open(example_file, "r").read()
example_input = example_input.replace("\n", " ")
backstory = f"""You are writing a professional presentation in academic style. You will be given a JSON file that defines various types of slide pages from which all slides will be generated, please generate speaker notes for each slide."""

def send_prompt(prompt):
    return openai.ChatCompletion.create(
        model=model,
        messages=[
            {"role": "system", "content": backstory},
            {"role": "user", "content": example_input},
            {"role": "user", "content": prompt}
        ],
        max_tokens=3500,
        n=1,
        temperature=0.2,
    ).choices[0].message.content.strip()


def main(prompt) -> None:
    # Start the timer
    start_time = time.time()
    print('Let me think about that...')

    if prompt == "":
        with open(prompt_file, 'r') as f:
            prompt = f.read()

    print(f"\nYour prompt: {prompt}\n")
    output = send_prompt(prompt)

    with open(output_file, "w") as f:
        f.write(output)
    end_time = time.time()
    duration = end_time - start_time
    duration = "{:.2f}".format(duration)
    print(f'Presentation data created in {duration} seconds!')

if __name__ == '__main__':
    prompt = ""
    if len(sys.argv) > 1:
        prompt = sys.argv[1]
    main(prompt)