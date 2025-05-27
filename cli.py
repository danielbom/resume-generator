import json

from argparse import ArgumentParser
from pathlib import Path

import src.templates.base.runner as base

import src.colors.rxresume as rxresume

schemas = {
    "rxresume": rxresume
}

templates = {
    "base": base.RunnerT
}


def generate_pdf(args):
    with args.data_path.open(encoding="utf-8") as file:
        data = json.load(file)

    if args.headline:
        data['basics']['headline'] = args.headline

    RunnerT = templates["base"] # TODO: Create new templates
    runner = RunnerT(
        output_path=str(args.output_path),
        primary=args.primary,
    )
    runner.run(data)


def json_path(path: str) -> Path:
    p = Path(path)
    if not p.is_file() or p.suffix != '.json':
        raise ValueError("'data_path' expects a valid JSON file")
    return p


def primary_color(color: str | None) -> str:
    if color is None:
        return 'black'
    if '_' in color:
        schema, idx = color.split('_')
        idx = int(idx)
        if schema not in schemas:
            raise ValueError('invalid color schema')
        return schemas[schema].primary[idx]
    return color


def main():
    parser = ArgumentParser('resume-generator')
    parser.add_argument("data_path", type=json_path)
    parser.add_argument("-o", "--output_path", type=Path,
                        default="resume.pdf", help="output pdf path (default: resume.pdf)")
    parser.add_argument("--primary", type=primary_color,
                        default="black", help="primary color (default: black)")
    parser.add_argument("--headline", help="change the HEADLINE value")
    args = parser.parse_args()
    generate_pdf(args)


if __name__ == "__main__":
    main()

