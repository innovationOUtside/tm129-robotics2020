---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.4.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

```python
from nbev3devsim.load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
```
<font color='red'>JD: Rename notebook if first and second notebooks for this week are combined.</font>

# 4 Reasoning and the sense–think–act model

In the sense–act model, agents (or robots) typically perform an action as a direct response of a sensory input. In the ‘sense–think–act’ model, there is an element of deliberation in which the agent makes a *choice* about what action to perform based not just on the sensory input but also other factors. In the simplest case, this might be a value against which the input is compared, or it might be a much more elaborate decision process involving a wide range of factors.


## 4.1 Representing and using knowledge and beliefs

Artificial intelligence and robotics have the major problem of *representing* facts and *knowledge*, or at least, *beliefs* inside machines. We have a vast amount of knowledge in our brains. This knowledge is distributed over the brain, rather than each fact being neatly stored in a single memory unit.

<!-- #region tags=["alert-success"] -->
In many formal studies of intelligent agents, ‘knowledge’ is defined as ‘justified true belief’. An agent may ‘believe’ a fact, but that is only classed as ‘knowledge’:

- if the fact is true
- if the agent is justified in having the belief (that is, there is a good reason why it has that belief).
<!-- #endregion -->

The structure of the human brain is completely different from the structure of a robot’s or a real computer’s ‘brain’, and roboticists have found it very difficult to implant a wide range of experiences (real-world data) into robot brains. Whilst significant progress has been made in artificial intelligence (AI) and machine learning (ML) approaches in recent years by using ever-more computational resources, these achievements are often quite limited in terms of domain or general applicability. They can also be hugely expensive in terms of the amount of data and computational effort, as well as the energy used to power the underlying computers that are required to create them. Ever larger and more complex natural-language processing (NLP) models are also proving effective in parsing natural-language statements and generating natural-language texts, albeit often in a ‘free-writing’ sense.

An alternative to the ‘self-learning’ neural network style of artificial intelligence, which you will meet later in the block, are approaches in which we try to *explicitly* encode knowledge using an approach known as *rule-based systems*.

In this notebook you will meet two such examples: the classic *Eliza* rule-based conversational agent, and a more general rule-based architecture, *durable-rules*, which can be used to develop a wide range of rulesets that can be used to reason more generally over a set of provided ‘facts’.


## 4.2 Eliza

Athough written fifty or so years ago, Joseph Weizenbaum’s *Eliza* program is often referred to as one of the first great milestones in computational natural-language interaction. [This copy of the original paper](https://github.com/wadetb/eliza/blob/master/p36-weizenabaum.pdf) includes examples of the code used to program the original Eliza engine.

Eliza has been reimplemented several times, such as in the *Lisp* programming language by Peter Norvig for his textbook *Paradigms of Artificial Intelligence Programming*, as well as a Python reimplementation of Norvig’s code by Daniel Connelly ([Paip-python: Peter Norvig's Paradigms of AI Programming implemented in Python](http://dhconnelly.com/paip-python/)). 

A version of Connelly’s code, updated to run in the version of Python used in these notebooks, is contained in the file [eliza.py](eliza.py).

<!-- #region activity=true -->
### Activity – Chatting to ‘Eliza’

Relive the past, perhaps in more ways than one – depending on how your conversation goes! – by chatting to Eliza for two or three minutes.

Run the following code cell to import the `eliza` package:
<!-- #endregion -->

```python
import eliza
```

Run the following code cell to enter Eliza’s treatment room. Start your conversation with a *Hello*; end the conversation by starting your response with *Goodbye* or force an exit to the program by clicking the *stop* button in the notebook toolbar.

```python activity=true
eliza.hello_doctor()
```

<!-- #region activity=true -->
If you want to hear Eliza speak the responses aloud to you then start the program by passing in the parameter `aloud=True` in the following way: `eliza.hello_doctor(aloud=True)`.
<!-- #endregion -->

<!-- #region -->
### What makes Eliza tick?

If you look at the [rules file](eliza.json), you will see that it contains a series of rules that have the form:

```
CONDITION: [
    POSSIBLE_RESPONSE_1,
    POSSIBLE_RESPONSE_2,
    ...
    ]
```

or more completely:

```
"?*x KEYPHRASE ?*y": [
        "RESPONSE_1 ?y?",
        "RESPONSE_2 ?y?",
        ...
        ]
```

For example:

```python
    "?*x I want ?*y": [
        "What would it mean if you got ?y?",
        "Why do you want ?y?",
        "Suppose you got ?y soon."
        ]
```

The `?*x` and `?*y` elements in the condition part of the rule are pattern-matching operators that capture arbirtary text before and after the provided `KEYPHRASE`. A rule matches a provided input if the `KEYPHRASE` is contained in the text given to Eliza. The pattern-matched content in the text can then be extracted from the input and used in the output response given by Eliza.

A rule-matching engine, written in Python, takes the user input, tries to match it with one of the rules and then generates a response. If you are interested in the details, [Connelly provides a commentary](https://dhconnelly.com/paip-python/docs/paip/eliza.html) that explains how his version of the Eliza program works.
<!-- #endregion -->

<!-- #region activity=true -->
### Optional activity

If you make a copy of the `eliza.json` file, for example, as `dr_me.json` and edit it to contain your own rules, then you can run Eliza using your ruleset by running the command: `eliza.hello_doctor('dr_me.json')`.

You can also provide a set of custom default responses that Eliza will select between if no rules match by passing them into the `hello_doctor()` function via the `default=` parameter. For example:

```python
eliza.hello_doctor('doolittle.json',
                   default = ["Very interesting",
                              "I am not sure I understand you fully"]
                  )
```

If you come up with an interesting script, then share it in your Cluster group forum.
<!-- #endregion -->

## 4.3 Durable Rules Engine

The [Durable Rules Engine](https://github.com/jruizgit/rules) is a *polyglot* framework for creating rule-based systems capable of reasonng over large collections of factual statements.

To say that the framework is *polyglot* means that we can write programs for the same framework using different programming languages, specifically Python, Node.js (a flavour of JavaScript) and Ruby. Underneath, the same rules engine (which itself happens to be written in the C programming language) processes the facts and the rules to allow the system to reason.

Note that the Durable Rules Engine (durable-rules) is *not* available directly within our robot simulator programs. Instead, we call on it via the full Python environment associated with code cells that are not prefaced by the simulator magic.

The engine itself is rather more powerful than the engine used in the Eliza program example and can accept a wide range of rule definitions. It also makes use of a knowledge base of asserted facts (as well as ephemeral events) that are reasoned against using the rules.

To see how this more comprehensive version of a rule-based system works, let’s consider the example of reasoning over a set of ‘facts’ that are asserted as *subject predicate object* statements. Separate rules parse one or more of these statements and then try to make general additional statements as a logical consequence.

Facts might take the form *Sam is a student* where *Sam* is the subject of the statement, *student* is the object of the statement, and *is a* is a *predicate* that defines some sort of relationship between the subject and the object.

Rules test statements, and if they match the rule condition then the rule asserts another fact.

For example, *if Sam is a student, then Sam can use the module forums*.

Let’s see how that works in practice. Note that the following treatment uses a simplification of the syntax used by default in the durable-rules framework. (There is just too much clutter in the original syntax to see what’s going on!)

Let’s import the packages we need and enable some magic:

<font color='red'>JD: Does the following code cell do anything? Is it needed?</font>

```python
#%pip install  --upgrade git+https://github.com/innovationOUtside/durable_rules_magic.git
```

```python
from durable.lang import ruleset, when_all, assert_fact, c, m
from durable_rules_tools.rules_utils import new_ruleset, SPO, Set, Subject
%reload_ext durable_rules_tools
```

<!-- #region -->
The ruleset definition syntax is little bewildering, so just try to see the structural patterns that the various bits of syntax make.

So, let’s take a deep breath and dive in, looking at this pseudo-code abstraction of a possible rule:

```
if ?PERSON is student
    then ?PERSON can use forums
```

In this case, `?PERSON` is a variable representing the subject, *forums* is the object, and *can use* is the predicate.

We can encode this formal rule using the durable-rules framework as follows:

```python
@when_all(Subject("is", "student"))
def cm_forum_use(c):
    Set(c, '? : can use : forums' )
```    
<!-- #endregion -->

<!-- #region tags=["alert-danger"] -->
The `@...` statements are known as Python *decorators*; but that’s all you need to know in case you want to look them up them further (further investigation is definitely *not required* and *not expected* of you for the purposes of this module). Just regard it as ‘syntactic sugar’ intended to make the rule a bit more readable than it might otherwise be. So go with the flow and just try to read the rules as some sort of structured pattern you can recognise as performing some sort of magic...
<!-- #endregion -->

<!-- #region -->
The rule has the form:

```python
@CONDITION
def RULENAME(TESTED_ASSERTION):
    ACTION
```

If you defocus your eyes, you can perhaps see how those elements might relate to a rule that could perhaps be more logically presented as:

```
RULENAME:
  if TESTED_ASSERTION meets CONDITION
  then ACTION
```

The rule is used in the code cell below without further explanation, other than the commentary provided in the cell itself. What is important is that you see (if you close you eyes and squint hard enough!) the logical ‘shape’ of the rule. The actual symbols used, and their placement, is ‘just syntax’.

Run the following cell to define a new ruleset:
<!-- #endregion -->

```python
# Get a unique identifier for the ruleset
RULESET_1 = new_ruleset()

# Add rules to the ruleset
with ruleset(RULESET_1):
    
    # Rule condition (the "if" part)
    @when_all(Subject("is", "student"))
    # Rule body (the "then" part)
    # - cm_forum_use is can be viewed as the name of the rule
    # - c is an assertion that is being tested by the rule
    def cm_forum_use(c):
        # This is what we actually do when the rule condition is satisfied
        # The ? in the first position says:
        #   """use the original value in this position (i.e. the subject)
        #      from the tested statement when creating the asserted statement"""
        Set(c, '? : can use : forums' )

    #A "utility" rule that displays all asserted facts
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
     
```

We can now assert a couple of facts, and see what conclusions can be draw about them from an application of the rules.

Facts are asserted in the form: `subject : predicate : object`.

We assert facts in the context of a particular ruleset via a cell block magic, `%%assert_facts -r RULESET_NAME`.

Run the following cell to assert some facts against the `RULESET_1` ruleset:

```python
%%assert_facts -r RULESET_1
Sam : is : student
Jo : is : course manager
```

We can’t easily add rules to a pre-exsiting ruleset, so let’s create another ruleset, building on the first, that contains another rule:

```python
RULESET_2 = new_ruleset()
with ruleset(RULESET_2):
    
    @when_all(Subject("is", "course manager"))
    def cm_forum_use(c):
        Set(c, '? : can read : forum discussions' )


    # -- PREVIOUS RULES --

    @when_all(Subject("is", "student"))
    def cm_forum_use(c):
        Set(c, '? : can use : forums' )

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
 
```

Let’s test our assertions again:

```python
%%assert_facts -r RULESET_2
Sam : is : student
Jo : is : course manager
```

So, course managers can *read* forum discussions, but students can *use* forums. What might that entail?

In the following set, we define two rules that test the same condition, but with different actions:

```python
RULESET_3 = new_ruleset()
with ruleset(RULESET_3):
    
    @when_all(Subject("can use", "forums"))
    def forum_read(c):
        Set(c, '? : can read : forum discussions' )
        
    @when_all(Subject("can use", "forums"))
    def forum_post(c):
        Set(c, '? : can post to : forum discussions' )
        
    
    # -- PREVIOUS RULES --
    @when_all(Subject("is", "course manager"))
    def cm_forum_use(c):
        Set(c, '? : can read : forum discussions' )

    @when_all(Subject("is", "student"))
    def student_forum_use(c):
        Set(c, '? : can use : forums' )

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
 
```

What can we determine now? 

```python
%%assert_facts -r RULESET_3
Sam : is : student
Jo : is : course manager
```

At the next level of complexity, we might want to draw some conclusions about multiple facts. Suppose, for example, that we wish to identify people who have ‘engaged’ with the forums. We might define such people as people who have read a forum post and who have posted to a forum. 

```python
%%assert_facts -r RULESET_3

Al : has read : forum post
Al : has posted to : forum

Sam : has posted to : forum
```

The rules we have seen so far test just a single condition, so how do we test *two* conditions?

```
if ?PERSON has read forum post AND ?PERSON has posted to forum
then ?PERSON has engaged with forum
```

This is where things start getting trickier, and where we shall finish our quick introduction to creating rules with the durable-rules framework. Briefly, we create a temporary reference when a fact matches a condition, and then compare those temporary references to see whether the same fact satisfied both conditions:

```python
RULESET_4 = new_ruleset()
with ruleset(RULESET_4):
    
    @when_all(c.first << Subject('has read', 'forum post'),
              c.second << Subject('has posted to', 'forum') & (m.subject == c.first.subject))
    def forum_discussions(c):
        c.assert_fact({ 'subject': c.first.subject,
                       'predicate': 'has engaged with',
                       'object': 'forum' })

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
 
```

Let’s now test the following assertions to see who has been identified as engaging with the forums:

```python
%%assert_facts -r RULESET_4

Al : has read : forum post
Al : has posted to : forum

Sam : has posted to : forum
```

Hopefully, from these examples and the earlier Eliza example you have a feeling for how we can build up quite rich sequences of behaviour (conversations over time, logical reasoning over multiple facts, including over facts derived from earlier-presented facts) using quite simple rules. But while each rule might be quite simple, and the discrete actions performed by each rule might be quite simple, the emergent behaviour might be quite elaborate.


### Trying out another ruleset

Let’s try another example, this time using one of the example rulesets provided in the durable-rules documentation.

We’ll also see how we can add another dimension to the rules and create a ruleset that speaks back to us.

You’ve already seen how we can get the simulated robot to speak, but how might we go about getting our notebooks to talk to us?


### Talking notebooks

To get the robot to speak in the simulator, we make use of the browser’s JavaScript speech engine. This speech engine was also used to allow Eliza to speak. It’s not too hard to pull together a simple Python package, intended for use in Jupyter notebooks, that makes it easy for us to call this engine from a single line of Python code running via a notebook code cell that is not prefixed with the simulator magic.  


The following example demonstrates one such approach. The Python object that manages the speech actions also keeps track of how many messages have been posted and returns a visual count of utterances, alongside a transcript of each utterance.

```python
from nb_simple_speech import Speech
```

Create a speaker...

```python
speaker = Speech()
```

And listen to them talk:

```python
speaker.say('Hello, how are you?')
speaker.say('All well, I hope?')
```

You can list the available voices by running the following code cell:

```python
print(browser_voicelist)
```
<font color='red'>JD: This doesn't print out anything (maybe an empty list?) so presumbly I don't have alternative voices :¬( </font>

Change the voice by setting the desired voice number: 

```python
speaker.set_voice(49)
speaker.say('I can change my voice')
```

You can use the following command to reset the message count in the transcript:

```python
speaker.reset_count()
speaker.say('hello again')
```

Now we can listen to the rules as they are fired, as well as seeing a report that shows the order in which they were fired.

```python
RULESET = new_ruleset()
with ruleset(RULESET):
    @when_all(c.first << Subject('eats', 'flies'),
              Subject('lives', 'water') & (m.subject == c.first.subject))
    def frog(c):
        c.assert_fact(SPO(c.first.subject, 'is', 'frog'))

    @when_all(c.first << Subject('eats', 'flies'),
              Subject('lives', 'land') & (m.subject == c.first.subject))
    def chameleon(c):
        c.assert_fact(SPO(c.first.subject, 'is', 'chameleon'))
        
    @when_all(Subject('eats', 'worms'))
    def bird(c):
        speaker.say(f'if {c.m.subject} eats worms')
        Set(c, '? : is : bird')
        speaker.say(f'{c.m.subject} is a bird')

    @when_all(Subject('is', 'frog'))
    def green(c):
        Set(c, '? : is : green')

    @when_all(Subject('is', 'chameleon'))
    def grey(c):
        Set(c, '? : is : grey')

    @when_all(Subject('is', 'bird'))
    def black(c):
        speaker.say(f'if {c.m.subject} is a bird')
        Set(c, '? :is : black')
        speaker.say(f'{c.m.subject} is black')
        
    @when_all(Subject("is", "bird"))
    def can_fly(c):
        speaker.say(f'if {c.m.subject} is a bird')
        Set(c, '? : can : fly' )
        speaker.say(f'{c.m.subject} can fly')

    @when_all(+m.subject)
    def output(c):
        print('\nFact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
```

```python
%%assert_facts -r RULESET
Kermit : eats : worms
```

## More general forms of rules

So far we have focused on reasoning about ‘facts’ in the form of statements with the form *subject predicate object*.

But this actally represents a more complicated form of reasoning than the rules engine actually employs because the *atomic* smallest possible facts are not the *subject predicate object* triples at all, they are the individual properties: `{subject: SUBJECT}`, `{'predicate': PREDICATE}` and `{object: OBJECT}`.
<font color='red'>JD: in the above, in `{'predicate': PREDICATE}` should predicate be in quote marks? (Compare with subject and object.)</font>


### Facts versus events

Facts persist, whereas events are retracted once they have been evaluated. Events are particularly useful in a robotics context, where we may want to respond to repeated sensor events.

For example, imagine a case where we want to avoid a red line, because red lines indicate danger.


```python
from durable.lang import post

RULESET = new_ruleset()
with ruleset(RULESET):
    # this rule will trigger as soon as three events match the condition
    @when_all(m.color=='red')
    def see_red(c):
        speaker.say(f'I see red')
        c.assert_fact({'status': 'danger'})
        
    @when_all(m.color!='red')
    def not_red(c):
        speaker.say(f'I see {c.m.color}')
        c.assert_fact({'status': 'safe'})

    @when_all( m.status == 'danger')
    def dangerous(c):
        speaker.say(f'That is dangerous.')
        c.retract_fact({'status': 'danger'})
        
    @when_all( m.status == 'safe')
    def safe(c):
        speaker.say(f'That is safe.')
        c.retract_fact({'status': 'safe'})
          

```

What happens when if we detect a red colour?

```python
post(RULESET, {'color': 'red' });
```

How about if we detect a green colour?

```python
post(RULESET, {'color': 'green' });
```

What if we see red, then green quickly after?

```python
post(RULESET, {'color': 'red' });
post(RULESET, {'color': 'green' });
```

### How might rules be useful in a robot context?

Although we can easily create our own `if...` statements in the program downloaded to the simulator and control the robot’s behaviour that way, it may be more convenient to develop, and test, a large and possibly complex rule-based set of behaviours using a framework such as durable-rules.

This may be achieved by capturing sensor values from the robot in the simulator, passing them back to the notebook’s Python context, passing them as events to the durable-rules ruleset, applying the rules to create some statement of a desired motor action, and then returning this instruction to the simulated robot for execution there.

We will not pursue this approach further, here. However, you will have an opportunity to control the simulated robot in a similar way using a neural network running in the notebook context, rather than a rule-based system, in a later notebook.


## Summary

In this notebook, you have seen how a rule-based agent originally created over fifty years ago can still hold a conversation (of sorts!) today. By providing different scripts containing only a few dozen rules, quite wide-ranging conversations are possible if the human conversant adds the detail.

The durable-rules framework provides an example of a system that can be used to generate a more powerful rule-based system. Reasoning about a set of persistent facts, or ephemeral events, rule-based systems constructed using framweorks such as this can be used to implement a wide range of systems, from fraud-detection systems to systems that implement complex sets of business rules in a corporate context. Such systems can also be developed to implement actual robot controllers, with rules accepting events based on incoming sensor data as well as higher-level beliefs (that is, ‘facts’) derived from sensor data events and other facts.

In a later part of the block, you will have an opportunity to see how a multi-agent system can be built where the simulated robot can pass sensor readings to an external rule-based system, which will process the data and return some sort of response that the robot can then act on.

<!-- #region heading_collapsed=true -->
## Addendum

Adding a simple Python speech utility in a Jupyter notebook is quite easy if we make use of the JavaScript speech engine in the browser used to render the notebook. This addendum shows how.

*(You are not required to study this addendum for the purposes of the module.)*
<!-- #endregion -->

<!-- #region hidden=true -->
To create a simple Python speech function, we need to import the `IPython.display.Javascript` package that lets us run JavaScript code in the browser from Python.
<!-- #endregion -->

```python hidden=true
from IPython.display import Javascript, display
```

<!-- #region hidden=true -->
Then we can define a simple function that invokes the JavaScript speech engine with a provided piece of text:
<!-- #endregion -->

```python hidden=true
def say(txt):
    """Say a provided text sentence out loud."""
    display(Javascript(f'speechSynthesis.speak(new SpeechSynthesisUtterance("{str(txt)}"))'))
```

<!-- #region hidden=true -->
We can create a further level of abstraction by putting the function inside a Python `class`:
<!-- #endregion -->

```python hidden=true
class Speech():
    def say(self, txt):
        """Say a provided text sentence out loud."""
        display(Javascript(f'speechSynthesis.speak(new SpeechSynthesisUtterance("{str(txt)}"))'))
        
speaker = Speech()
speaker.say('hello')
```
