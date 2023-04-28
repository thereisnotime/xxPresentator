# xxPresentator

A helper utility to generate presentations quickly.

## Table of Contents

- [xxPresentator](#xxpresentator)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Generate a presentation](#generate-a-presentation)
    - [Options](#options)
    - [Slide options](#slide-options)
  - [Demo](#demo)
  - [Roadmap](#roadmap)
  - [Contributing](#contributing)
  - [License](#license)

## Installation

1. Make sure to have make, git and Docker installed.
2. Run the following commands:

```bash
git clone https://github.com/thereisnotime/xxPresentator
cd xxPresentator
```

## Usage

### Generate a presentation

1. Copy input.example.json to input.json and edit the contents to your liking.
2. Run the following command:

```bash
make presentation
```

You now have "output.pptx" with your presentation.

### Options

```bash
xxPresentator - v1.01 - available targets:
    help         Shows the help menu
    run          Generates the presentation
    presentation Generates the presentation and open it
    clean        Deletes all artifacts and presentation
    build        Prepares the base image
```

### Slide options

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
- [ ] Add random image picker/generator for backgrounds and for slides.
- [ ] Add pretty first slide with title, author and stylization.
- [ ] Add pretty last slide with thanks, author and stylization.
- [ ] Add option for footer and header on each slide except first and last.
- [ ] Add integration with OpenAI to generate the JSON from a prompt.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. The same goes for suggestions and feature requests.

## License

For more information, please refer to the [GNUv3](LICENSE.md) file.
