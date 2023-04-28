import json
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE
from pptx.util import Inches

input_file = "input.json"
output_file = "output.pptx"

def load_slide_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data

def create_slide(presentation, title):
    slide_layout = presentation.slide_layouts[5]  # Choosing a layout
    slide = presentation.slides.add_slide(slide_layout)
    shapes = slide.shapes

    title_shape = slide.shapes.title
    title_shape.text = title

    return slide

if __name__ == "__main__":
    data = load_slide_data(input_file)
    slide_titles = data["slide_titles"]

    presentation = Presentation()
    for title in slide_titles:
        create_slide(presentation, title)

    presentation.save(output_file)