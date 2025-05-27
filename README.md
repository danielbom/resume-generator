# Resume Generator

This project was inspired by an [article](https://www.linkedin.com/posts/marcia-agostinho-developer_como-perdi-a-vaga-antes-mesmo-de-ser-lido-activity-7330572028774629378-ylcF/) I read on LinkedIn. I took a screenshot of it, which you can find [here](./extras/linkedIn-about-resumes.pdf).

I didn’t invent the idea of generating resumes — there are many tools out there (some of which I’ve used and listed in the References section). However, I ran into problems like page breaks, multilingual formatting, and maintaining a consistent structure. So, I built this project mainly for my own needs.

It provides a command-line interface (CLI), so it’s mostly intended for people comfortable working in the terminal. If you’d like to make it more accessible for non-technical users, feel free to submit a pull request or fork the project and adapt it however you like.

## Usage

### Requirements

- Python 3.10+
- uv

### Installation

```bash
# Install 'uv'
pip install uv

# Install dependencies
uv venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
uv install
```

### Generating Resumes

```bash
uv run cli.py ./data/info-pt.json --primary "rxresume_13" -o ./data/resume-pt.pdf
uv run cli.py ./data/info-en.json --primary "rxresume_3" -o ./data/resume-en.pdf
```

Open the files to see the result:
- [Resume PT](./data/resume-pt.pdf)
- [Resume EN](./data/resume-en.pdf)

### See help

```bash
uv run cli.py --help
```

```
usage: resume-generator [-h] [-o OUTPUT_PATH] [--primary PRIMARY] [--headline HEADLINE] data_path

positional arguments:
  data_path

options:
  -h, --help            show this help message and exit
  -o, --output_path     output pdf path (default: resume.pdf)
  --primary PRIMARY     primary color (default: black)
  --headline HEADLINE   change the HEADLINE value
```

#### Notes

- Use --headline to tailor the resume for a particular job or role.
- Use --primary to set the main color and visually distinguish between different resume versions.

## Contributing

Feel free to open issues or submit pull requests!

## License

MIT License.

## References

- [RxResume](https://rxresu.me/)
- [Gerador de Curriculo](https://ats-curriculo.vercel.app/)
- [CEFR Levels: A1, A2, B1, B2, C1 and C2](https://www.europassitalian.com/blog/cefr-levels/)
- [MIT LIcense](https://mit-license.org/)
