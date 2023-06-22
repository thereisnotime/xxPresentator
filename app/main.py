import argparse
from generate_content import ContentGenerator
from generate_notes import NotesGenerator
from make_presentation import PresentationCreator

from constants import prompt


def main(content_flag, notes_flag, presentation_flag, prompt_text=None):

    if content_flag:
        content_generator = ContentGenerator()
        content_generator.generate_content(prompt_text or prompt)

    if notes_flag:
        notes_generator = NotesGenerator()
        notes_generator.generate_notes(prompt_text or prompt)

    if presentation_flag:
        presentation_creator = PresentationCreator()
        presentation_creator.generate_presentation()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate content, speaker notes, and presentation.")
    parser.add_argument("-c", "--content", action="store_true", help="Generate content")
    parser.add_argument("-n", "--notes", action="store_true", help="Generate speaker notes")
    parser.add_argument("-p", "--presentation", action="store_true", help="Generate presentation")
    parser.add_argument("--prompt", type=str, help="Specify a custom prompt")
    args = parser.parse_args()

    main(args.content, args.notes, args.presentation, args.prompt)
