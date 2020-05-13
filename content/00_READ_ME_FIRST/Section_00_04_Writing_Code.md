## 1.4 Writing Style Compliant Code

__NOTE TO CRITICAL READERS: THIS IS INTENDED AS GENERIC TO JUPYTER ENVTS AND AIMS TO NUDGE STUDENTS TOWARDS GOOD CODE STYLE PRACTICE IF THEY WANT NUDGING.__

Whilst this is not specifically a programming course, this may well be the first time you have done any sort of programming at all, let alone any programming in Python.

The style of programming we are teaching is geared towards helping you understand how we might be able to control robots through programme code, rather than formally teaching you programming in general, or Python coding in particular.

However, we will try to to demonstrate code examples that are well written and that comply with the popular [PEP 8 — Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/). This guide sets out a set of stylistic convention for writing clear Python code.

There are many tools available that can be used to support code authors and we have installed some of them into the RoboLab environment.

One particular tool is know as a "linter". When you run a code cell, this tool can post warnings about where the code diverges from PEP-8 guidelines.

Error codes are described via the following links:

- `E*`, `W*`: [show code lookups](https://pycodestyle.readthedocs.io/en/latest/intro.html#error-codes);
- `D*`: [show code lookups](http://www.pydocstyle.org/en/2.1.1/error_codes.html);
- `F*`: [show code lookups](http://flake8.pycqa.org/en/3.7.9/user/error-codes.html).

The linter can be enabled in a notebook by running the following magic:

`%flake8_on --ignore D100`

__TO DO: flake seems to be broken atm tho pycodestyle ok; also note probably only works with native code cells, not magic ones, though I may be able to fix that by tweaking magic to ignore the `%%sim_magic` call...__

When you run a code cell, if the linter detects a difference from the style guide, it will display a warning of the form:

TO DO 

??show line numbers
??fix 
??rerun


Another useful extension that is installed, but not enabled, is the `Autopep8` extension. You can enable the extension from the `nbextensions Configurator` [[direct link](/nbextensions/?nbextension=code_prettify/autopep8)]. Enabling this extension provides a "hammer" toolbar button that you can use to prettify your code in accord with some PEP-8 recommendations at least. Simply select a code select, and hit the button; it will prettify the code, if it can, in a more PEP-8 compliant way. (But it won't change the way your code executes, so it won't tend to fix bugs in your code for you...)

One way of using the `flake8` linter and `Autopep8` button together is to let the linter raise a warning (if you do make an error), use the button to try to fix the code, then run the cell again to invoke the linter and see if the warning(s) were addressed. If they were, *inspect the fixed code to see what change the `Autopep8` tool made* (`CTRL-z` (Win), `CMD-z` (Mac) will undo the last cell edit; `SHIFT-CTRL-z` (Win), `SHFT-CMD-z` (Mac) will then redo it).

Tools are also available to support writing markdown text in markdoan cells. For example, enabling the `livemdpreview` extension will display an inline live preview of the rendered markdown directly beneath a markdown cell as you edit it [[direct link](/nbextensions/?nbextension=livemdpreview/livemdpreview)].

Spell checkers are also available, either as the `spellchecker` notebook extension [[direct link](https://hub.gke.mybinder.org/user/innovationoutsi-29-robotics2020-o5z3lwky/nbextensions/?nbextension=spellchecker/main)) or via the Accessibility toolbar.
