# xxPresentator

A helper utility to generate presentations quickly.

## Table of Contents

- [xxPresentator](#xxpresentator)
  - [Table of Contents](#table-of-contents)
  - [Preresquisites](#preresquisites)
  - [Installation](#installation)
    - [Usage](#usage)
      - [Makefile](#makefile)
      - [Docker](#docker)
      - [Python](#python)
    - [Output](#output)
    - [Slide options](#slide-options)
  - [Demo](#demo)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)

## Preresquisites

- make
- git
- Docker
- Python3
- pip3
- python3-venv

## Installation

```bash
git clone https://github.com/thereisnotime/xxPresentator
cd xxPresentator
```

## Usage

- There are several different ways to use xxPresentator:
- - Makefile
- - Docker
- - Python

### Makefile

The Makefile is the easiest way to use xxPresentator.
- It will automatically install all dependencies and run the script.
- It will also automatically clean up after itself.

```bash
make presentation ARGS="-arg -arg -arg -arg"
```

When you are running the Makefile, you can pass arguments to the script by using the ARGS variable.
You can specify:

- -c / --content - for generating content;
- -n / --notes - for generating notes;
- -p / --presentation - for generating presentation;
-  --prompt "string" - for overriding the default prompt.

_A default prompt is used when no prompt is specified._

- Options

```bash
xxPresentator - v1.01 - available targets:
    help         Shows the help menu
    run          Generates the presentation
    presentation Generates the presentation and open it
    clean        Deletes all artifacts and presentation
    build        Prepares the base image
```

### Docker

1.Build the image:
```bash
docker build -t image_name .
```

2. Run the image:
```bash
docker run -v "$pwd/output:/output" image_name -arg -arg -arg
```

### Python
1. Create a virtual environment:
```bash
virtualenv venv
```

2. Activate the virtual environment:
```bash
source venv/bin/activate
```

3. Install dependencies:
```bash
pip3 install -r requirements.txt
```

4. Run the script:
```bash
python3 main.py -arg -arg -arg -arg
```

_You can also run every script individually._
```bash
python3 generate_content.py
python3 generate_notes.py
python3 make_presentation.py
```

## Output

The output is a .pptx file with the name "output.pptx" inside the output directory.

## Slide options

Take a look at the input.example.json file to see all the options available.

## Demo

- Generate the JSON source file (with ChatGPT or any other tool):

TIP: You can use the prompt: "Generate a presentation on the topic of XXX with at least 20 slides following this example JSON input".

[![Screenshot](/media/screenshot00.png "This is an example JSON")](https://raw.githubusercontent.com/thereisnotime/xxPresentator/master/screenshots/screenshot01.png)

- Generate the presentation:

[![Screenshot](/media/screenshot01.png "This is an example presentation")](https://raw.githubusercontent.com/thereisnotime/xxPresentator/master/screenshots/screenshot01.png)

- Output presentation:

[![Screenshot](/media/screenshot02.png "This is an example presentation")](https://raw.githubusercontent.com/thereisnotime/xxPresentator/master/screenshots/screenshot02.png)

- Change template/theme:

TIP: You can import the output presentation in Google and then just apply a nice theme.

[![Screenshot](/media/screenshot03.png "This is an example presentation")](https://raw.githubusercontent.com/thereisnotime/xxPresentator/master/screenshots/screenshot03.png)

And now all you have to do is to style the presentation to your liking.

## Roadmap

This is a small tool that I made for myself to generate presentations quickly. I will add more features as I need them. If you have any suggestions, please open an issue

- [ ] Add more slide templates.
- [ ] Add random variation to the slide layouts.
- [ ] Add more text formats.
- [ ] Modify Makefile and Dockerfiles for the three different functions.
- [ ] Add random image picker/generator for backgrounds and for slides.
- [ ] Add pretty first slide with title, author and stylization.
- [ ] Add pretty last slide with thanks, author and stylization.
- [ ] Add option for footer and header on each slide except first and last.
- [ ] Add integration with OpenAI to generate the JSON from a prompt.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. The same goes for suggestions and feature requests.

## License

For more information, please refer to the [GNUv3](LICENSE.md) file.
