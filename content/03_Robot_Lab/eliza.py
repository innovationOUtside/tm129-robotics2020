'''Copyright (c) 2015, Daniel Connelly
All rights reserved.

Source: https://github.com/dhconnelly/paip-python
Code explication: https://dhconnelly.com/paip-python/docs/paip/eliza.html

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import json
import sys
#!/usr/bin/env python

"""
**Eliza** is a pattern-matching automated psychiatrist.  Given a set of rules
in the form of input/output patterns, Eliza will attempt to recognize user input
phrases and generate relevant psychobabble responses.
Each rule is specified by an input pattern and a list of output patterns.  A
pattern is a sentence consisting of space-separated words and variables.  Input
pattern variables come in two forms: single variables and segment variables;
single variables (which take the form `?x`) match a single word, while segment
variables (which take the form `?*x`) can match a phrase.  Output pattern
variables are only single variables.  The variable names contained in an input
pattern should be the same as those in the corresponding output pattern, and
each segment variable `?*x` in an input pattern corresponds to the single
variable `?x` in the output pattern.
The conversation proceeds by reading a sentence from the user, searching through
the rules to find an input pattern that matches, replacing variables in the
output pattern, and printing the results to the user.
For examples of using this scheme, see the following programs:
- [Eliza](examples/eliza/eliza.html)
- [Automated technical support system](examples/eliza/support.html)
This implementation is inspired by Chapter 5 of "Paradigms of Artificial
Intelligence Programming" by Peter Norvig.
"""

import random
import string

## Talking to the computer

def interact(prompt, rules, default_responses):
    """Have a conversation with a user."""
    # Read a line, process it, and print the results until no input remains.
    while True:
        try:
            # Remove the punctuation from the input and convert to upper-case
            # to simplify matching.
            _input = input(prompt)
            _input = remove_punct(_input.upper())
            if not _input:
                continue
        except:
            break
            
        #Stopping condition
        if _input.startswith('GOODBYE'):
            print("Oh, okay. It was nice talking to you. Goodbye.")
            break
        print(respond(rules, _input, default_responses))


def respond(rules, input, default_responses):
    """Respond to an input sentence according to the given rules."""

    input = input.split() # match_pattern expects a list of tokens

    # Look through rules and find input patterns that matches the input.
    matching_rules = []
    for pattern, transforms in rules:
        pattern = pattern.split()
        replacements = match_pattern(pattern, input)
        if replacements:
            matching_rules.append((transforms, replacements))

    # When rules are found, choose one and one of its responses at random.
    # If no rule applies, we use the default rule.
    if matching_rules:
        responses, replacements = random.choice(matching_rules)
        response = random.choice(responses)
    else:
        replacements = {}
        response = random.choice(default_responses)

    # Replace the variables in the output pattern with the values matched from
    # the input string.
    for variable, replacement in replacements.items():
        replacement = ' '.join(switch_viewpoint(replacement))
        if replacement:
            response = response.replace('?' + variable, replacement)
    
    return response
    

## Pattern matching

def match_pattern(pattern, input, bindings=None):
    """
    Determine if the input string matches the given pattern.
    Expects pattern and input to be lists of tokens, where each token is a word
    or a variable.
    Returns a dictionary containing the bindings of variables in the input
    pattern to values in the input string, or False when the input doesn't match
    the pattern.
    """

    # Check to see if matching failed before we got here.
    if bindings is False:
        return False
    
    # When the pattern and the input are identical, we have a match, and
    # no more bindings need to be found.
    if pattern == input:
        return bindings

    bindings = bindings or {}

    # Match input and pattern according to their types.
    if is_segment(pattern):
        token = pattern[0] # segment variable is the first token
        var = token[2:] # segment variable is of the form ?*x
        return match_segment(var, pattern[1:], input, bindings)
    elif is_variable(pattern):
        var = pattern[1:] # single variables are of the form ?foo
        return match_variable(var, [input], bindings)
    elif contains_tokens(pattern) and contains_tokens(input):
        # Recurse:
        # try to match the first tokens of both pattern and input.  The bindings
        # that result are used to match the remainder of both lists.
        return match_pattern(pattern[1:],
                             input[1:],
                             match_pattern(pattern[0], input[0], bindings))
    else:
        return False


def match_segment(var, pattern, input, bindings, start=0):
    """
    Match the segment variable against the input.
    pattern and input should be lists of tokens.
    Looks for a substring of input that begins at start and is immediately
    followed by the first word in pattern.  If such a substring exists,
    matching continues recursively and the resulting bindings are returned;
    otherwise returns False.
    """

    # If there are no words in pattern following var, we can just match var
    # to the remainder of the input.
    if not pattern:
        return match_variable(var, input, bindings)

    # Get the segment boundary word and look for the first occurrence in
    # the input starting from index start.
    word = pattern[0]
    try:
        pos = start + input[start:].index(word)
    except ValueError:
        # When the boundary word doesn't appear in the input, no match.
        return False

    # Match the located substring to the segment variable and recursively
    # pattern match using the resulting bindings.
    var_match = match_variable(var, input[:pos], dict(bindings))
    match = match_pattern(pattern, input[pos:], var_match)

    # If pattern matching fails with this substring, try a longer one.
    if not match:
        return match_segment(var, pattern, input, bindings, start + 1)
    
    return match


def match_variable(var, replacement, bindings):
    """Bind the input to the variable and update the bindings."""
    binding = bindings.get(var)
    if not binding:
        # The variable isn't yet bound.
        bindings.update({var: replacement})
        return bindings
    if replacement == bindings[var]:
        # The variable is already bound to that input.
        return bindings

    # The variable is already bound, but not to that input--fail.
    return False


## Pattern matching utilities

def contains_tokens(pattern):
    """Test if pattern is a list of subpatterns."""
    return type(pattern) is list and len(pattern) > 0


def is_variable(pattern):
    """Test if pattern is a single variable."""
    return (type(pattern) is str
            and pattern[0] == '?'
            and len(pattern) > 1
            and pattern[1] != '*'
            and pattern[1] in string.ascii_letters
            and ' ' not in pattern)


def is_segment(pattern):
    """Test if pattern begins with a segment variable."""
    return (type(pattern) is list
            and pattern
            and len(pattern[0]) > 2
            and pattern[0][0] == '?'
            and pattern[0][1] == '*'
            and pattern[0][2] in string.ascii_letters
            and ' ' not in pattern[0])


## Translating user input

def replace(word, replacements):
    """Replace word with rep if (word, rep) occurs in replacements."""
    for old, new in replacements:
        if word == old:
            return new
    return word


def switch_viewpoint(words):
    """Swap some common pronouns for interacting with a robot."""
    replacements = [('I', 'YOU'),
                    ('YOU', 'I'),
                    ('ME', 'YOU'),
                    ('MY', 'YOUR'),
                    ('AM', 'ARE'),
                    ('ARE', 'AM')]
    return [replace(word, replacements) for word in words]


def remove_punct(string):
    """Remove common punctuation marks."""
    if string.endswith('?'):
        string = string[:-1]
    return (string.replace(',', '')
            .replace('.', '')
            .replace(';', '')
            .replace('!', ''))

default_responses = [
    "Very interesting",
    "I am not sure I understand you fully",
    "What does that suggest to you?",
    "Please continue",
    "Go on",
    "Do you feel strongly about discussing such things?",
    ]


# TH
def hello_doctor(rules_file='eliza.json', default=None):
    if default is not None:
        default_responses = default
    with open(rules_file, 'r') as f:
        rules = json.load(f)
    rules_list = []
    for pattern, transforms in rules.items():
        pattern = remove_punct(str(pattern.upper())) # kill unicode
        transforms = [str(t).upper() for t in transforms]
        rules_list.append((pattern, transforms))
    interact('ELIZA> ', rules_list, list(map(str.upper, default_responses)))
