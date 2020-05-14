```python
from nbev3devsim import ev3devsim_nb as eds

#https://github.com/AaronWatters/jp_doodle/blob/master/notebooks/misc/JQueryUI%20dialogextend%20plugin%20demo.ipynb
#Load and initialise the jquery.dialogextend package
import jp_proxy_widget
cdn_url = "https://cdn.jsdelivr.net/npm/binary-com-jquery-dialogextended@1.0.0/jquery.dialogextend.js"
cdn_url = eds.get_file_path('js/jquery.dialogextend.js')
module_id = "dialogExtend"


# Load the module using a widget (any widget -- the module loads to the global jQuery object).
loader = jp_proxy_widget.JSProxyWidget()

# Configure the module to be loaded.
loader.require_js(module_id, cdn_url)

# Load the module
loader.js_init("""
    element.requirejs([module_identifier], function(module_value) {
        //element.html("loaded " + module_identifier + " : " + module_value);
    });
""", module_identifier=module_id)
loader

# I think we need to wait for this to load
# else we may get an error in next cell from dialogExtend not being available?
```

```python
!touch _load_requirements.py
!touch _load_nbev3devwidget.py
```

```python
# Run this cell to set up the robot simulator environment

#Load the nbtutor extension
%load_ext nbtutor

#Reset the notebook style
from IPython.core.display import display, HTML

display(HTML("<style>#notebook-container { width:50%; float:left !important;}</style>"))


#Launch the simulator
from nbev3devsim import ev3devsim_nb as eds
%load_ext nbev3devsim

roboSim = eds.Ev3DevWidget()

roboSim.set_element("response", '')
             
display(roboSim)
roboSim.element.dialog();


roboSim.js_init("""
element.dialog({ "title" : "Robot Simulator" }).dialogExtend({
        "maximizable" : true,
        "dblclick" : "maximize",
        "icons" : { "maximize" : "ui-icon-arrow-4-diag" }});
""")
```

```python
%%sim_magic
import ev3dev2_glue as g

print(g.showme())
```

```python

```

```javascript
//This allows us to resize this view
//Click on the right hand edge to drag
$( "#notebook-container" ).resizable({ghost: false})
```

# 4 Reasoning and the sense–think–act model


```python
%%sim_magic_preloaded

colorLeft = ColorSensor(INPUT_2)
colorRight = ColorSensor(INPUT_3)
 
while ((colorLeft.reflected_light_intensity>5) 
       and (colorLeft.reflected_light_intensity)>5):
    
    intensity_left = colorLeft.reflected_light_intensity
    intensity_right = colorRight.reflected_light_intensity
    intensity_left_pc = 100.0 * (intensity_left / 255.0)
    intensity_right_pc = 100.0 * (intensity_right / 255.0)

    print(intensity_left_pc, intensity_right_pc)
    
    left_motor_speed = SpeedPercent(intensity_left_pc)
    right_motor_speed = SpeedPercent(intensity_right_pc)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

## 4.1 Representing and using knowledge


Artificial intelligence and robotics have the major problem of *representing* facts and knowledge inside machines. We have a vast amount of knowledge in our brains. This knowledge is distributed over the brain, rather than each fact being neatly stored in a single memory unit.

The structure of the human brain is completely different from the structure of a robot's or a real computer’s "brain", and roboticists have found it very difficult to implant a wide range of experiences (real-world data) into robot brains. Significant progress has been made in Artificial Intelligence (AI) and Machine Learning (ML) approaches to machine vision in recent years by using ever more computational resources. Ever larger and more complex natural language processing (NLP) models are also proving effective in parsing natural language statements and generating natural language texts.

One way of *explicitly* trying to encode knowledge is to use a *rule based system*.


## Eliza

Athough written fifty or so years ago, Joseph Weizenbaum's *Eliza* programme is often referred to as one of the first great milestones in computational natural language interaction. You can see a copy of the original paper [here](https://github.com/wadetb/eliza/blob/master/p36-weizenabaum.pdf), which includes examples of the code used to programme the original Eliza engine. Eliza has been reimplemented several times, such as in the Lisp language by Peter Norvig's for his textbook *Paradigms of Artificial Intelligence Programming*, as well as in Python reimplementation of Norvig's code by Daniel Connelly ([*Paip-python: Peter Norvig's Paradigms of AI Programming implemented in Python*](http://dhconnelly.com/paip-python/)). 

A version of Connelly's code, updated to run in the version of Python used in these notebooks, is contained in the file [eliza.py](eliza.py).

You can try it out for yourself by running the following code cell and starting your converation with a *Hello*; end the conversation by starting your response with *Goodbye*):

```python
import eliza
eliza.hello_doctor()
```

<!-- #region -->
If you [look at the rules file](eliza.json), you will see that it contains a series of rules that have the form:

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

The `?*x` and `?*y` elements in the condition part of the rule are pattern matching operators that capture arbirtary text before and after the provided `KEYPHRASE`. A rule matches a provided input if the `KEYPHRASE` is contained in the text given to Eliza. The pattern matched content in the text can then be extracted from the input and used in the output response given by Eliza.

A rule matching engine, written in Python, takes the user input, tries to match it with one of the rules and then generates a response. If you are interested in how it works, Connelly provided a commentary [here](https://dhconnelly.com/paip-python/docs/paip/eliza.html) that explains how his version of the Eliza program works.
<!-- #endregion -->

<!-- #region -->
### Optional Activity

If you make a copy of the `eliza.json` file, for example, as `dr_me.json` and edit it to contain your own rules, you can run Eliza using your ruleset by running the command: `eliza.hello_doctor('dr_me.json')`.

You can also provide a set of custom default responses that Eliza will select between if no rules match by passing in them into the `hello_doctor()` function via the `default=` parameter. For example:

```python
eliza.hello_doctor('dr_me.json',
                   default = ["Very interesting",
                              "I am not sure I understand you fully"]
                  )
```

<!-- #endregion -->

### *Durable Rules Engine*

The [*Durable Rules Engine*](https://github.com/jruizgit/rules) is a *polyglot* framework for creating rule based systems capable of reasonng over large collections of factual statements.

To say that the framework is *polyglot* means that we can write programmes for the same framework using different ployglot languages, specifically Python, Node.js (a flavour of Javascript) and Ruby. Underneath, the same rules engine (which itself happens to be written in the C programming language) processes the facts and the rules to allow the system to reason.

Note that the *Durable Rules Engine* is *not* available directly within our robot simulator programmes.

The engine iself is rather more powerful than the engine used in the Eliza program example and can accept a wide range of rule definitions. It also makes use of a knowledge base of asserted facts (as well as ephemeral events) that are reasoned against using the rules.

To see how this more comprehensive version of a rule based system works, let's consider the example of reasoning over a set of "facts" that are asserted as *subject predicate object* statements. Separate rules parse one or more of these statements and then try to general additional statements as a logical consequence.

Facts might take the form *Sam is a student* where *Sam* is the subject of the statement, *student* is the object of the statement, and *is a* is a *predicate* that defines some sort of relationship between the subject and the object.

Rules test statements, and if they match the rule codition, the rule asserts another fact.

For example, *if Sam is a student, then Sam can use the module forums*.

Let's see how that works in practice. Note that the following treatment uses a simplification of the syntax used by default in the durable rules framework. (There is just too much clutter in the original syntax to see what's going on!)

Let's import the packages we need and enable some magic...

```python
#%pip install  --upgrade git+https://github.com/innovationOUtside/durable_rules_magic.git
```

```python
from durable.lang import ruleset, when_all, assert_fact, c, m
from durable_rules_tools.rules_utils import new_ruleset, SPO, Set, Subject
%reload_ext durable_rules_tools
```

<!-- #region -->
The ruleset definition syntax is little bewildering (the `@...` statements are known as Python *decorators*; but that's all you need to know in case you want to look them up them further, and further investigation is definitely *not required* and *not expected* of you for the purposes of this module.)

So take a deep breath, and let's dive in, using a slightly simpler, and more generalised, statement of the same rule we considered above:

```
if ?PERSON is student
    then ?PERSON can use forums
```

In this case, `?PERSON` is a variable representing the subject, *forums* is the object, and *can use* is the predicate.

We can encode this a formal rule as follows (remember, you don't need to understand what the `@...` decorator is or how it works, just regard it as "syntactic sugar" intended to make the rule a but more readable than it might otherwise have to be; go with the flow and tried to read the rule as some sort of structured pattern you can recognise).

```python
@when_all(Subject("is", "student"))
def cm_forum_use(c):
    Set(c, '? : can use : forums' )
```    
        
The rule has the form:

```python
@CONDITION
def RULENAME(TESTED_ASSERTION):
    ACTION
```

If you defocus your eyes, you can perhaps see how those elements might relate to a rule that coould perhaps be more logically presented as:

```
RULENAME:
  if TESTED_ASSERTION meets CONDITION
  then ACTION
```

The rule is used in the code cell below without further explanation, other than the commentary provided in the cell itself. What is important is that you see (if you close you eyes and squint hard enough!) the logical "shape" of the rule. The actual symbols used, and their placement, is "just syntax".

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

```python
when_all??
```

We can now assert a couple of facts, and see what conclusions can be draw about them from an application of the rules...

Facts are asserted in the form: `subject : predicate : object`.

We assert facts in the context of a particular ruleset via a cell block magic, `%%assert_facts -r RULESET_NAME`.

Run the following cell to assert some facts against the `RULESET_1` ruleset:

```python
%%assert_facts -r RULESET_1
Sam : is : student
Jo : is : course manager
```

We can't easily add rules to a pre-exsiting ruleset, so let's create another ruleset, building on the first, that contains another rule:

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

Let's test our assertions again:

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

At the next level of complexity, we might want to draw some conclusions about multiple facts. Suppose, for example, that we wish to identify people who have "engaged" with the forums. We might define such people as people who have read a forum post and who have posted to a forum. 

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

This is where things start getting trickier, and where we shall finish our quick introduction to creating rules with the *durable rules* framework. Briefly, we create a temporary reference when a fact matches a condition, and then compare those temporary references to see whether the same fact satisfied both conditions:

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

Let's now test the following assertions to see who has been identified as engaging with the forums:

```python
%%assert_facts -r RULESET_4

Al : has read : forum post
Al : has posted to : forum

Sam : has posted to : forum
```

Hopefully, from these examples and the earlier Eliza example, you have a feeling for how we can build up quite rich sequences of behaviour (conversations over time, logical reasoning over multiple facts, including over facts derived from earlier presented facts) using quite simple rules. But while each rule in and of itself might be quite simple, and the discrete actions performed by each rule might be quite simple, the emergent behaviour might be quite elaborate.


### Trying out another ruleset

eg from example on druable rules README

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
        Set(c, '? : is : bird')

    @when_all(Subject('is', 'frog'))
    def green(c):
        Set(c, '? : is : green')

    @when_all(Subject('is', 'chameleon'))
    def grey(c):
        Set(c, '? : is : grey')

    @when_all(Subject('is', 'bird'))
    def black(c):
        Set(c, '? :is : black')
        
    @when_all(Subject("is", "bird"))
    def can_fly(c):
        Set(c, '? : can : fly' )

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
```

```python
%%assert_facts -r RULESET
Kermit : eats : worms
```

### Facts versus Events

Facts persist, events are retracted once they have been evaluated. This then means we can also start counting over multiple events.


### How might rules be useful in a robot context?

?? could we use a variant of eliza code in simulator under skulpt to provide simple rules handling there?


### Using Python to Respond to and Control Events in the Simulator

Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 


The original RobotLab activities include examples of round-tripping, with the simulated robot passing state out to a remote application, which then returned a response to the simulated robot. I'm pretty sure we can do the same, either with a predefined application or a userdefined function. THe latter would be best becuase then we could have an activity to write a helper application in notebook python that is called on by the simulated robot.

At the moment, I have managed to send a message to Py from the simulator via messages sent to the simulator output window. THere is a callback that sends messages back from Py to the sim outpur window, but as yet the robot py code running in the simulator is oblivious to returned messages. (I need half a day, perhaps, a day, to actually get code into the simulator so the programme code can access it.)

The following recipe shows how to overwrite the default collaborative `responder()` function with a custom one.

```python
class CollabSim(eds.Ev3DevWidget):
     def responder(self, obj):
        """ Callback function that tries to respond to widget."""
        # obj is the message sent from the simulator
        #Generate a response
        response = f'pingpongBONG {obj}'
        #Send the response back to the simulator
        #At the moment, this is simply echoed in the simulator output window
        self.set_element("response", response)

# We now create an instance of the simulator with the custom collaborative callback function
roboSim = CollabSim()
```
