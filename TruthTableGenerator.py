# -*- coding: utf-8 -*-
# Copyright (c) 2020, xehoth
# All rights reserved.
#
# @file TruthTableGenerator.py
# @author: xehoth
from typing import List
import re
import sys


class Proposition:
    def __init__(self, value=False):
        self.value = value

    # ->
    def __rshift__(self, rhs):
        return Proposition(not (self.value and not rhs.value))

    # or
    def __add__(self, rhs):
        return Proposition(self.value or rhs.value)

    # and
    def __mul__(self, rhs):
        return Proposition(self.value and rhs.value)

    # not
    def __invert__(self):
        return Proposition(not self.value)

    # <->
    def __eq__(self, rhs):
        return Proposition((self.value and rhs.value) or (not self.value and not rhs.value))

    # ^
    def __ne__(self, rhs):
        return Proposition(self.value != rhs.value)


def getTableElement(s: str, markdown=False) -> str:
    if markdown:
        s = "$" + s + "$"
    s = s.center(len(s) + 2)
    return s + "|" if markdown else s


def getPropositions(s: str) -> List[str]:
    return list(sorted(set(re.findall(r'\w+', s.replace("T", "").replace("F", "")))))


def getEvalExpression(s: str):
    # not
    s = s.replace("!", "~").replace("not", "~").replace(
        "¬", "~").replace(r"\neg", "~")
    # and
    s = s.replace("&", "*").replace(r"\wedge", "*").replace("and",
                                                            "*").replace("∧", "*")
    # or
    s = s.replace("|", "+").replace(r"\vee", "+").replace("or",
                                                          "+").replace("∨", "+").replace("v", "+")
    # <->
    s = s.replace("<->", "==").replace("↔",
                                       "==").replace(r"\leftrightarrow", "==")
    # ->
    s = s.replace("->", ">>").replace("→", ">>").replace(r"\rightarrow", ">>")

    # ^
    s = s.replace("^", "!=").replace("⊕", "!=")
    return s


def getLatexExpression(s: str) -> str:
    return s.replace("~", r" \neg ").replace("*", r" \wedge ").replace(
        "+", r" \vee ").replace("==", r" \leftrightarrow ").replace(">>", r" \rightarrow ").replace("!=", r" \oplus")


def generateTruthTable(expression: str, reverse=False, markdown=False, file=sys.stdout) -> None:
    # True
    T = Proposition(True)
    # False
    F = Proposition(False)
    # strip
    expression = expression.strip()
    # eval string
    s = getEvalExpression(expression)

    if markdown:
        expression = getLatexExpression(s)

    props = getPropositions(s)
    n = len(props)
    # prop eval buffer
    buf = [Proposition() for i in range(n)] + [T, F]

    if markdown:
        print("|", end='', file=file)

    for i in props + [expression]:
        print(getTableElement(i, markdown=markdown), sep='', end='', file=file)
    print(file=file)
    if markdown:
        print("|", end='', file=file)
        for i in range(n + 1):
            print(" :--: |", end='', file=file)
        print()

    states = range(0, 1 << n)

    for state in reversed(states) if reverse else states:
        if markdown:
            print("|", end='', file=file)
        for i in range(n):
            buf[i].value = (state >> (n - i - 1)) & 1 == 1
            print(getTableElement(
                "FT"[buf[i].value], markdown=markdown), end='', file=file)
        print(getTableElement("FT"[eval("(" + s + ").value",
                                        {v: buf[i] for i, v in enumerate(props + ['T', 'F'])})], markdown=markdown), file=file)


def main(inputFile=sys.stdin, outputFile=sys.stdout, reverse=False, markdown=False) -> None:
    for s in inputFile:
        generateTruthTable(s, reverse=reverse,
                           markdown=markdown, file=outputFile)


def printHelp() -> None:
    print("""Truth Table Generator
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
    """)


if __name__ == "__main__":
    args = sys.argv
    if len(args) == 1:
        main()
    elif "-h" in args or "--help" in args:
        printHelp()
    elif "-c" in args or "--console" in args:
        main()
    else:
        markdown = "-m" in args or "--markdown" in args
        reverse = "-r" in args or "--reverse" in args
        inputFile = ''
        outputFile = ''
        if "-i" in args:
            inputFile = args[args.index("-i") + 1]
        if "--input" in args:
            inputFile = args[args.index("--input") + 1]
        if "-o" in args:
            outputFile = args[args.index("-o") + 1]
        if "--output" in args:
            outputFile = args[args.index("--output") + 1]
        if not inputFile and not outputFile:
            main(reverse=reverse, markdown=markdown)
        elif not inputFile and outputFile:
            with open(outputFile, "w", encoding='utf-8') as o:
                main(outputFile=o, reverse=reverse, markdown=markdown)
        elif inputFile and not outputFile:
            with open(inputFile, "r", encoding='utf-8') as i:
                main(inputFile=i, reverse=reverse, markdown=markdown)
        else:
            with open(inputFile, "r", encoding='utf-8') as i, open(outputFile, "w", encoding='utf-8') as o:
                main(inputFile=i, outputFile=o,
                     reverse=reverse, markdown=markdown)
