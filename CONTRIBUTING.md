# Contributing to pySBD
Thanks for your interest in contributing to pySBD 🎉. The project is maintained by [@nipunsadvilkar](https://github.com/nipunsadvilkar), and I'll do my best to help you get started. This page will give you a quick overview of how things are organised and most importantly, how to get involved.

## Table of contents

1. [Issues and bug reports](#issues-and-bug-reports)</br>
    a. [Submitting issues](#submitting-issues)</br>
    b. [Issue labels](#issue-labels)
2. [Contributing to the code base](#contributing-to-the-code-base)</br>
    a. [Getting started](#getting-started)</br>
    b. [Add a new rule to existing *Golden Rules Set* (GRS)](#add-a-new-rule-to-existing-golden-rules-set-grs)</br>
    c. [Add new language support](#add-new-language-support)</br>
    d. [Add tests](#add-tests)</br>
    e. [Fix bugs](#fix-bugs)

## Issues and bug reports
First, do a [quick search](https://github.com/nipunsadvilkar/pySBD/issues?q=is%3Aissue+sort%3Aupdated-desc+is%3Aclosed+is%3Aopen) to see if the issue has already been reported or already open. If so, it's often better to just leave a comment on an existing issue, rather than creating a new one. Old issues also often include helpful tips and solutions to common problems.

Please understand that author won't be able to provide individual support via
email. Author also believe that help is much more valuable if it's **shared publicly**,
so that more people can benefit from it.

### Submitting issues

When opening an issue, use an **appropriate and descriptive title** and include your
**environment** (operating system, Python version, pySBD version). Choose the report type [from here](https://github.com/nipunsadvilkar/pySBD/issues/new/choose), if type is not available then open a [blank issue](https://github.com/nipunsadvilkar/pySBD/issues/new). The
[issue template](https://github.com/nipunsadvilkar/pySBD/issues/new?assignees=&labels=&template=bug_report.md&title=%3CAppropriate+title%3E) helps you
remember the most important details to include. If you've discovered a bug, you
can also submit a [regression test](#fix-bugs) straight away. When you're
opening an issue to report the bug, simply refer to your pull request in the
issue body. A few more tips:

-   **Describing your issue:** Try to provide as many details as possible. What
    exactly goes wrong? _How_ is it failing? Is there an error?
    "XY doesn't work" usually isn't that helpful for tracking down problems. Always
    remember to include the code you ran and if possible, extract only the relevant
    parts and don't just dump your entire script. Also, provide what was the expected output for given input. This will make it easier for contributors to
    reproduce the error.

-   **Getting info about your pySBD installation and environment:** You can use the command line interface to print details and copy-paste psybd verson along with python version into GitHub issues:
    `pip freeze|grep pysbd`.

-   **Sharing long blocks of code/logs/tracebacks:** If you need to include long code,
    logs or tracebacks, you can wrap them in `<details>` and `</details>`. This
    [collapses the content](https://developer.mozilla.org/en/docs/Web/HTML/Element/details)
    so it only becomes visible on click, making the issue easier to read and follow.

### Issue labels

[See this page](https://github.com/nipunsadvilkar/pySBD/labels) for an overview of
the system author uses to tag our issues and pull requests.

## Contributing to the code base

Happy to see you contibute to pySBD codebase. To help you get started and understand internals of pySBD, a good place to start is to refer to the implementation section of pySBD research paper (link to be added soon). Another great place for reference is to look at [merged pull requests](https://github.com/nipunsadvilkar/pySBD/pulls?q=is%3Apr+sort%3Aupdated-desc+is%3Amerged). Depending on the type of your contribution, refer to the assigned labels.

### Getting started
To make changes to pySBD's code base, you need to fork then clone the GitHub repository to your local machine. You'll need to make sure that you have a development environment consisting of a Python distribution including python 3+, pip and git installed.

```python
python -m pip install -U pip
git clone https://github.com/nipunsadvilkar/pySBD
cd pySBD
pip install -r requirements-dev.txt
```
Since pySBD is lightweight, it requires only python inbuilt modules, more specifically python `re` module to function. Development packages requiremment will be provided in `requirements-dev.txt`. If you want to use pySBD as a spacy component then install spacy in your environment.

### Add a new rule to existing *Golden Rules Set* (GRS)
The language specific *Golden Rules Set* are hand-constructed rules, designed to cover sentence boundaries across a variety of domains. The set is by no means complete and will evolve and expand over time. If you would like to report an issue in existing rule or report a new rule, please [open an issue.](#submitting-issues) If you want to contribute yourself then please go ahead and send pull request by referring to [add tests](#add-tests) section.

### Add new language support
Great to see you adding new language support to pySBD ✨.</br>
You would need following steps to add new language support:

^^ Please use already supported language commits - [Marathi](https://github.com/nipunsadvilkar/pySBD/commit/ab39442ece525285e5e83a80e2d2672bba467db7), [Spanish](https://github.com/nipunsadvilkar/pySBD/commit/ed6fb8672e30521e6e5d55bc86b779b2b4cf47dd), [Chinese](https://github.com/nipunsadvilkar/pySBD/commit/092764f896911bb97259720998b636f18980bb62) - as a frame of reference as you go through each steps below.

1. **New Language Specific *Golden Rules Set***</br>
You would require to create *Golden Rule Set* representing basic to complex sentence boundary variations as a test set. Assuming you know the language, its sentence syntax and other intricacies you can create a new file at `tests/lang/test_<language_name>.py` and enlist input text and expected output in the same way author has added support for existing^^ languages. You may want to refer to [adding tests](#adding-tests) section to know more details on how to add, run tests, adding language fixture. Next, run the tests using `pytest` and let it deliberately fail.

2. **Add your language module**</br>
Create a new file at `pysbd/lang/<language_name>.py` and define a new class `LanguageName` which should be inheriting from two base classes - `Common, Standard` - involving basic rules common across majority of languages. Try running tests to see your GRS passes or not. If fails, you would need to override `SENTENCE_BOUNDARY_REGEX`, `Punctuations` class variables and `AbbreviationReplacer` class to support your language specific punctuations, sentence boundaries.

 > Illustration: As you could see in [`Marathi`](https://github.com/nipunsadvilkar/pySBD/blob/master/pysbd/lang/marathi.py) language, `AbbreviationReplacer` & its `SENTENCE_STARTERS` are kept blank to override `Standard`'s [`SENTENCE_STARTERS`](https://github.com/nipunsadvilkar/pySBD/blob/master/pysbd/lang/common/standard.py#L111). Next, `Punctuations` are limited to  `['.', '!', '?']` and as per it `SENTENCE_BOUNDARY_REGEX` is constructed to make sure it would pass [Marathi GRS](https://github.com/nipunsadvilkar/pySBD/blob/master/tests/lang/test_marathi.py). Similar to the class variables, if you find any rule not pertaining to your language then you can override it in your language class.

3. **Add language code**<br>
Your language module & language GRS should be in place by now. Next step is to make it available to pySBD's [`languages`](https://github.com/nipunsadvilkar/pySBD/blob/master/pysbd/languages.py) module by importing your language module and adding a new key having [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) equivalent language code belonging to your language to the `LANGUAGE_CODES` dictionary and value as your language class you would have imported.

### Add tests
Author emphasizes on Test-Driven Development [(TDD)](https://testdriven.io/test-driven-development/) approach to ensure robustness of the pySBD module. You will follow a "<span style="color: red;">Red</span>-<span style="color: green;">Green</span>-<span style="color: orange;">Refactor</span>" cycle.

1. Make sure you have proper development environment [setup](#getting-started)
2. Depending on your type of contribution your test script would vary between [feature-specific](#add-new-language-support) / [bugfix-specific](#fix-bugs).
3. (<span style="color: red;">Red</span>) Once you add those tests, run `pytest` to make sure it fails deliberately.
4. (<span style="color: green;">Green</span>) Write just enough code to implement your logic in respective python script to pass the specific test which you added and got failed earlier.
5. Once it passes, run all the tests to see if your added code doesn't break existing code.
6. (<span style="color: orange;">Refactor</span>) Do necessary refactoring & cleaning to keep tests green.
7. Repeat 🔁

### Fix bug(s)

When fixing a bug, first create an
[issue](https://github.com/nipunsadvilkar/pySBD/issues) if one does not already exist.
The description text can be very short – don't need to be verbose.

Next, depending on your type of issue, add your test in `TEST_ISSUE_DATA` / `TEST_ISSUE_DATA_CHAR_SPANS` with a tuple `("#ISSUE_NUMBER", "<input_text>", <expected_output>)` in the
[`pysbd/tests/regression`](pysbd/tests/regression) folder. Test for the bug
you're fixing, and make sure the test fails. Next, add and commit your test file
referencing the issue number in the commit message. Finally, fix the bug, make
sure your test passes and reference the issue in your commit message.

Thank you for contributing! ✨ 🍰 ✨
