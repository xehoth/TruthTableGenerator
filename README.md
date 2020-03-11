# TruthTableGenerator

Generate truth table according to logic expressions.

## Logic Expressions

- `!`, `~`, `not`, `¬` are the same.
- `&`, `*`, `and`, `∧`, `^` are the same.
- `|`, `+`, `or`, `∨`, `v` are the same.
- `<->`, `↔` are the same.
- `->`  `→` are the same.

## Usage

Python3 is required. See help using `python TruthTableGenerator.py` or `python3 TruthTableGenerator.py`

``` bash
usage: [-h | --help] [-i | --input <file path>]
           [-o | --output <file path>] [-c | --console]
           [-m | --markdown] [-r | --reverse ]
    [-i | --input <file path>]
        input from <file path>
    [-o | --output <file path>]
        output the result to <file path>
    [-c | --console]
        console mode (default)
    [-m | --markdown]
        generate markdown table
    [-r | --reverse]
        reverse the enumerate order (default F -> T)
```

## Feature

- It can input expressions from a file and generate tables for expressions in each line.
- It can generate a markdown table.
