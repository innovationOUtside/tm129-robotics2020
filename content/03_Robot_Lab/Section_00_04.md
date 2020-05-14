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

An version of Connelly's code, updated to run in the version of Python used in these notebooks, is contained in the file [eliza.py](eliza.py).

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

```python
#%pip install git+https://github.com/innovationOUtside/durable_rules_magic.git
```

```python
One popular way of using rule based systems to reason about the wotk
```

![figure ../tm129-19J-images/tm129_rob_pa4_f5_1.png](../tm129-19J-images/tm129_rob_pa4_f5_1.png)


Figure 5.1 Listing: Facts_and_rules


comment : FACTS and RULES in RobotLab

const FALSE = 0

const TRUE = 1

const UNKNOWN = 2

const prepare_to_test_rule = 122

const the_rule_has_fired = 123

macro speak(words, wait_time)

      comment Add statements here...

      send words

      wait wait_time

macro tell_the_truth(phrase)

      comment Add statements here...

      call speak(118,260)

      var x = 119 + phrase

      call speak(x, 200)

main

      var you_are_a_student = TRUE

      var you_can_use_the_forum = UNKNOWN

      wait 200

      call tell_the_truth(you_can_use_the_forum)

      wait 200

      call speak(prepare_to_test_rule, 400)

      if you_are_a_student = TRUE

            then

                  call speak(the_rule_has_fired, 400)

                  set you_can_use_the_forum  = TRUE

                  wait 100

      call tell_the_truth(you_can_use_the_forum)

      comment : end of program

The program begins by declaring the constants `FALSE` and `TRUE` as discussed in Study week 3. For practical reasons we also need another constant, `UNKNOWN`.

This truth value `= UNKNOWN` allows a phrase to be in the fact database without the system being committed to it being true or false. This is used here as:

`you_can_use_the_forum = UNKNOWN`

as highlighted by the first arrow annotating the program above.

The program declares `prepare_to_test_rule` and `the_rule_has_fired` as constants. These are used later to make the program speak and can be ignored for the moment.

The program uses two *macros*. Macros are routines that can be ‘called’ from the main program. We’ll have more to say on these later, in Section 7. The first macro is called `speak` and is a convenient way to make the system speak and wait while the sound files are played. The second is called `tell_the_truth`. It is a convenient way for the system to speak the truth value of the phrase `you_can_use_the_forum`. You can minimise these macros using the [-] icon to their left if you don’t wish to be distracted by their detail.

When you run the program, the fourth command in the main part calls the `tell_the_truth` macro, which says ‘you can use the forum is unknown’.

The program then calls the `speak` macro and the system says ‘prepare to test rule’. The rule is:


```python
# Clear the state associated with a ruleset
def _delete_state(rs):
    try:
        delete_state(rs)
    except:
        pass

_delete_state(RULESET)
assert_fact(RULESET, { 'subject': 'Kermit',
                       'predicate': 'eats',
                       'object': 'flies' });
```

```python
from durable.lang import ruleset, when_all, m, assert_fact, retract_fact, delete_state, count, cap, c
import uuid

try:
    _delete_state(RULESET)
except:
    pass

RULESET = f'rs_{uuid.uuid4()}'

def spo(subj, pred, obj):
    """Return subject-predicate-object dict."""
    if not isinstance(subj, str):
        subj = subj.m.subject
    return { 'subject': subj, 'predicate': pred, 'object': obj }

def _assert_subj_is(c, obj):
    c.assert_fact(spo( c, 'is', obj ))
    
def _po(pred, obj):
    return (m.predicate == pred) & (m.object == obj)

def _when_is(obj):
    return (m.predicate == 'is') & (m.object == obj)

with ruleset(RULESET):
    # will be triggered by 'Kermit eats flies'
    @when_all(_po("eats", "flies"))
    def frog(c):
        c.assert_fact( spo(c, 'is', 'frog' ) )

    @when_all(_po('eats', 'worms'))
    def bird(c):
        c.assert_fact(spo( c, 'is', 'bird' ))

    # will be chained after asserting 'Kermit is frog'
    @when_all(_po('is', 'frog'))
    def green(c):
        c.assert_fact(spo( c, 'is', 'green' ))

    @when_all(_when_is('bird'))
    def black(c):
        _assert_subj_is(c, 'orange')

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
```

```python
from durable.engine import MessageObservedException

import warnings

RULESET = f'rs_{uuid.uuid4()}'

def spo2(c, statement):
    _statement = [x.strip() for x in statement.split(':')]
    subj = _statement[0] if  _statement[0]!='?' else c.m.subject
    pred = _statement[1]
    obj = _statement[2]
    try:
        c.assert_fact( spo(subj, pred, obj ) )
    except MessageObservedException:
        warnings.warn(f"Assertion error: is {statement} already asserted?")
    
with ruleset(RULESET):


    # how do we check multiple statements eg read and post to?
    @when_all(c.first << _po('can post to', 'forum discussions'),
              c.second << _po('can read', 'forum discussions') & (m.subject == c.first.subject))
    def forum_discussions(c):
        c.assert_fact({ 'subject': c.first.subject,
                       'predicate': 'can fully engage in',
                       'object': 'forum activity' })
    @when_all(_po("is", "student"))
    def student_forum_use(c):
        spo2(c, '? : can use : forums' )
    @when_all(_po("can use", "forums"))
    def forumpost(c):
        spo2(c, '? : can read : forum discussions' )
    @when_all(_po("can use", "forums"))
    def forumpost(c):
        spo2(c, '? : can post to : forum discussions' )
    @when_all(_po("is", "course manager"))
    def cm_forum_use(c):
        spo2(c, '? : can read : forum discussions' )
    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))
        
assert_fact(RULESET, { 'subject': 'Sam',
                       'predicate': 'is',
                       'object': 'course manager' })
assert_fact(RULESET, { 'subject': 'Jo',
                       'predicate': 'is',
                       'object': 'student' });

assert_fact(RULESET, { 'subject': 'Jo',
                       'predicate': 'is',
                       'object': 'student' });
```

```python
import durable.engine
dir(durable.engine)
```

```python
from IPython.core.magic import register_cell_magic
from IPython.core import magic_arguments


def quick_assert_fact(r, f):
    _statement = [t.strip() for t in f.split(':')]
    
    if len(_statement) != 3:
        return

    subj = _statement[0]
    pred = _statement[1]
    obj = _statement[2]
    #print('..', r, spo(subj, pred, obj ),'..' )
    try:
        assert_fact(r,  spo(subj, pred, obj ) )
    except MessageObservedException:
        warnings.warn(f"Assertion error: is {_statement} already asserted?")

@register_cell_magic
@magic_arguments.magic_arguments()
@magic_arguments.argument('--ruleset', '-r', help='Ruleset name.')
@magic_arguments.argument('--no-reset', action='store_false', help='Disable automatic state deletion.')
def assert_facts(line, cell):
    "Assert several facts."
    args = magic_arguments.parse_argstring(assert_facts, line)
    if not args.ruleset:
        warnings.warn("No ruleset reference (--ruleset/-r RULESET) provided.")
        return
    _ruleset = eval(args.ruleset)
    #print(_ruleset)
    if args.no_reset:
        _delete_state(_ruleset)

    for _assertion in cell.split('\n'):
        quick_assert_fact(_ruleset, _assertion)
```

We can add assertions in, `--no-reset` if you want to build on top of previous assertions

```python
%%assert_facts -r RULESET
James : is : student
Jane : is : course manager
```

```python3
# "Two rulesets with the same name cannot exist in the same process"
from durable.lang import *
with ruleset('animals'):
    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'water') & (m.subject == c.first.subject))
    def frog(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'frog' })

    @when_all(c.first << (m.predicate == 'eats') & (m.object == 'flies'),
              (m.predicate == 'lives') & (m.object == 'land') & (m.subject == c.first.subject))
    def chameleon(c):
        c.assert_fact({ 'subject': c.first.subject, 'predicate': 'is', 'object': 'chameleon' })

    @when_all((m.predicate == 'eats') & (m.object == 'worms'))
    def bird(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'bird' })

    @when_all((m.predicate == 'is') & (m.object == 'frog'))
    def green(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'green' })

    @when_all((m.predicate == 'is') & (m.object == 'chameleon'))
    def grey(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'grey' })

    @when_all((m.predicate == 'is') & (m.object == 'bird'))
    def black(c):
        c.assert_fact({ 'subject': c.m.subject, 'predicate': 'is', 'object': 'black' })

    @when_all(+m.subject)
    def output(c):
        print('Fact: {0} {1} {2}'.format(c.m.subject, c.m.predicate, c.m.object))


assert_fact('animals', { 'subject': 'Kermit', 'predicate': 'eats', 'object': 'flies' })
assert_fact('animals', { 'subject': 'Kermit', 'predicate': 'lives', 'object': 'water' })
assert_fact('animals', { 'subject': 'Greedy', 'predicate': 'eats', 'object': 'flies' })
assert_fact('animals', { 'subject': 'Greedy', 'predicate': 'lives', 'object': 'land' })
assert_fact('animals', { 'subject': 'Tweety', 'predicate': 'eats', 'object': 'worms' })  
```

How about we create some cell block magic for specifying facts as triples (so no space in a statement), else use a separator eg :, with one fact per line?, and perhaps also a ruleset definition magic, maybe with rules of the form `s : p :  `

```python
#_delete_state('animal6')
def _get_facts(rs):
    try:
        f = lang.get_facts(rs)
        return f
    except:
        print("No state?")

_get_facts('animal6')
```

### Using Python to Respond to and Control Events in the Simulator

Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 

```python

if you_are_a_student = TRUE

then you_can_use_the_forum = TRUE

```


The program then tests the *antecedent fact* in the rule `you_are_a_student` to see if it is true. It is true, so the rule *fires* and the *consequent fact* is true. Thus `you_can_use_the_forum` has its truth value updated to `= TRUE`.

The program ends by calling `tell_the_truth` again. This time it says ‘you can use the forum is true’.

The main sequence of events in this program is therefore:

1. 
Set `you_are_a_student` to `TRUE`.


2. 
Set `you_can_use_the_forum` to `UNKNOWN`.


3. 
Execute the rule; its antecedent fact matches `you_are_a_student = TRUE`, so it fires.


4. 
When the rule fires it updates the consequent fact `you_can_use_the_forum` to `TRUE`.


Thus the program can use the rule and the given fact that you are a student to deduce something it did not know before – that you can use the forum.

Run the program and listen to what it says. You should be able to follow the events as described above.

If you found the program hard to follow run it again in single-step mode. To do this open `Step_through_facts_and_rules`. Step through the program by repeatedly clicking the  ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f012.gif](../tm129-19J-images/tm129_rob_p4_f012.gif)  toolbar button or the `Run | Step` menu, <div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: F6</p></div> viewing each step in the Program window. Make sure you leave enough time for the sound files to play; otherwise they will run into each other.


## 4.2 Activity: Tiggy is happy


Open and run the program `Tiggy_is_happy`. In the `Simulator` window you will be given the following two options:

```python

```

![figure ../tm129-19J-images/tm129_rob_p4_f013.jpg](../tm129-19J-images/tm129_rob_p4_f013.jpg)

The simulator window which contains two square areas, one light grey and the other dark grey, on a white background. The light grey area is labelled ‘Tiggy is eating her dinner’. The dark grey area is labelled ‘Tiggy is in the swingboat’. 

If you place Simon over the pale grey square, `Tiggy_is_eating_her_dinner` is true, and the result should be shown in the `Simulator` window.

Run the program again to see what happens when you place Simon over the dark grey square. Stop the program first by clicking the Stop ![inlinefigure ../tm129-19J-images/tm129_rob_p4_f013a.gif](../tm129-19J-images/tm129_rob_p4_f013a.gif) button in the toolbar or using the `Run &gt; Stop` menu.<div xmlns:str="http://exslt.org/strings" style="background:lightblue"><p>Keyboard: F8</p></div> Then run the program, this time placing Simon on the dark square. In this case `Tiggy_is_in_the_swingboat` is true.

The program starts by defining three constants:

`FALSE = 0`

`TRUE = 1`

`UNKNOWN = 2`

The main part of the program you have just loaded begins with the potentially interesting, but currently unknown, possibilities:

`tiggy_is_eating_her_dinner = UNKNOWN`

`tiggy_is_in_the_swingboat = UNKNOWN`

`tiggy_is_wagging_her_tail = UNKNOWN`

When you place Simon over one of the squares it assigns the value `TRUE` to either `tiggy_is_eating_her_dinner` or `tiggy_is_in_the_swingboat`.

To do this the program has the command `call choose()`. This is another example of a macro.

The heart of the program is the rule:


![figure ../tm129-19J-images/tm129_rob_p4_f014.jpg](../tm129-19J-images/tm129_rob_p4_f014.jpg)

comment : Use the known rule to deduce a new fact

      if tiggy_is_eating_her_dinner = TRUE

            then

                  set tiggy_is_wagging_her_tail = TRUE

This rule will fire if the database contains the antecedent fact that `tiggy_is_eating_her_dinner = TRUE`, but it will not fire if `tiggy_is_eating_her_dinner = UNKNOWN`.

When the rule fires, it updates the fact database with the consequent fact `tiggy_is_wagging_her_tail = TRUE`

In this case, you have told Simon that Tiggy is eating her dinner, and Simon has deduced that Tiggy is wagging her tail.


## 4.3 The ‘choose’ macro


In the previous program I used a *macro* named `choose()`. As you learned in Section 5.1, a macro is a routine that can be ‘called’ from the main part of the program. Sometimes macros are used because they do something useful, or because they do something that is repeated many times. We’ll return to the macros later in this session.

The macro in the program `Tiggy_is_happy` has the following code:


![figure ../tm129-19J-images/tm129_rob_p4_f015.jpg](../tm129-19J-images/tm129_rob_p4_f015.jpg)

macro choose( )

      while choice &gt; 90

            set choice  = light_sensor

      if choice &lt; 50

            then

                  set tiggy_is_in_the_swingboat = TRUE

            else

                  set tiggy_is_eating_her_dinner = TRUE

On entering this macro, the program stays in a loop while `choice &gt; 90`. Note that when this variable was declared it was set to 100, so the condition of being greater than 90% is satisfied when the `while` condition is first encountered. The program then loops, resetting `choice` to the value of the `light_sensor` each time. When you place Simon on one of the squares, the value of the sensor drops below 90% and the program drops out of the loop.

After this, Simon tests to see if you have chosen the black square on the right (if the value of choice &lt; 50 then `Tiggy_is_in_the_swingboat = TRUE`), or the grey square on the left (else ` Tiggy_is_eating_her_dinner = TRUE`).

When one or other truth value is set, the program moves back to the command in the main part of the program after the call to the macro.


## 4.4 Simon plays detective


Simon has a problem. Its job is to keep the university clean and tidy. Some of the academics often work late and can be a bit messy. Sometimes they eat cake and sometimes they send out for pizza. Either way, Simon has to clear up the mess.

Let’s suppose that Simon is one of a new breed of robots, programmed with a personality. It has a special love for the four rooms – the lecture hall, theatre, laboratory and study – and likes them to be spick and span. Simon gets grumpy when they are not. Part of Simon’s personality has the robot playing detective, trying to find out who made the mess, so that it can give them a good telling off next time it sees them.


![figure ../tm129-19J-images/tm129_rob_p4_f016.gif](../tm129-19J-images/tm129_rob_p4_f016.gif)


Figure 5.2 The campus plan, suspects and food for Simon’s sleuthing


The campus plan which is represented as a square divided into four quadrants, each of which has a different pattern that gives each room a characteristic overall light level. At the top left is the Lecture Hall which is a light grey herringbone pattern. Top right is the Theatre which is a dark grey fish scale pattern. In the bottom right is the Laboratory which is mid grey with a diamond pattern. Finally in the bottom left is the Study which is white with black dots. Also shown in the figure are photos of the three suspects: Jon, Tony and Blaine; and of two foods: cake and pizza.

In order to find out what has been going on, Simon has to move from room to room looking for clues. The robot knows which room it is in from the colour of the floor, that is, the rooms are detected from the shade of grey, not the floor pattern.

Assume that each room has someone in it who has seen what has been going on. These people don’t like being quizzed by Simon, but if asked a direct question they have to tell the truth. So Simon might move to the laboratory and say ‘I suspect Jon with the cake in the laboratory’, and would be told which person, type of food and location were correct. By asking questions such as these Simon can deduce who the culprit is, what kind of food was involved and where the mess is located. Note that Simon can only nominate the room that it is currently in, so in order to nominate a different room it has to move to that room.

At the start of the game the culprit, food and room are selected using the `random` and `randomize` commands. The former gives random numbers and the latter initialises the process.

Open the `Simon_the_sleuth` program. Before you run it, take a look at the program code. An annotated version of the code is shown below.


![figure ../tm129-19J-images/tm129_rob_p4_f017.jpg](../tm129-19J-images/tm129_rob_p4_f017.jpg)


Figure 5.3 Listing: Simon_the_sleuth: setup


comment SIMON THE SLEUTH

__comment: set up light sensor__

sensor light_sensor on 2 is light as percent

__comment: assign motors to output ports__

output right_motor on C

output left_motor on A

__comment: define logical constants__

const TRUE = 1

const FALSE = 0

__comment: variables to test suspects__

var person_suspected = 1

var food_suspected = 1

var room_suspected = 1

__comment: random variables to be deduced__

var messy_person = 1

var trash = 1

var place = 1

__comment: logical variables__

var person_correct = FALSE

var food_correct = FALSE

var room_correct = FALSE

var uncertainty_remains = TRUE

__comment: audio file numbers for speaking__

const I_accuse = 114

const I_suspect = 115

const with_the = 116

const in_the = 117

[+] macro Move( )

[+] macro speak(x, y)

[+] macro I_Suspect( )

[+] main

The interesting parts of the program are variables to be deduced: `messy_person`, `trash` and `place`, and those that will be used to test suspects:
<table xmlns:str="http://exslt.org/strings">
<caption>Table 5.1 Interpretation of variable values</caption>
<tbody>
<tr>
<td class="highlight_" rowspan="" colspan="">
`messy_person = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Jon`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`messy_person = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Tony`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`messy_person = 3`
</td>
<td class="highlight_" rowspan="" colspan="">
`Blaine`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`trash = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Cake`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`trash = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Pizza`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`place = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Laboratory`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`place = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Theatre`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`place = 3`
</td>
<td class="highlight_" rowspan="" colspan="">
`Lecture hall`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`place = 4`
</td>
<td class="highlight_" rowspan="" colspan="">
`Study`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`person_suspected = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Jon`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`person_suspected = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Tony`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`person_suspected = 3`
</td>
<td class="highlight_" rowspan="" colspan="">
`Blaine`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`food_suspected = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Cake`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`food_suspected = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Pizza`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`room_suspected = 1`
</td>
<td class="highlight_" rowspan="" colspan="">
`Laboratory`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`room_suspected = 2`
</td>
<td class="highlight_" rowspan="" colspan="">
`Theatre`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`room_suspected = 3`
</td>
<td class="highlight_" rowspan="" colspan="">
`Lecture hall`
</td>
</tr>
<tr>
<td class="highlight_" rowspan="" colspan="">
`room_suspected = 4`
</td>
<td class="highlight_" rowspan="" colspan="">
`Study`
</td>
</tr>
</tbody>
</table>

The program has four macros:

`Move()`

The code in this macro rotates Simon through 90°, moves it forward and uses its downward-pointing sensor to identify the room colour, from which it deduces which room it is in.

`speak(x,y)`

This macro does the talking, by sending wav codes and waiting for them to be played.

`setScene()`

This macro assigns random values to `messy_person`, `place` and `trash`, and sets the scene. Simon then has to deduce what these values are.

`I_Suspect()`

This macro allows Simon to ask questions like ‘I suspect Tony with the cake in the study’, and gives the answers. The people are numbered 1, 2, 3 for Jon, Tony and Blaine respectively. In this case `person_suspected = 2`, so if `messy_person` is also 2, the rule:


```python

if person_suspected = messy_person

then set_person_correct = TRUE

```


will fire, and the phrase `set_person_correct` will be set to `TRUE`. Otherwise it is set to `FALSE`, and `uncertainty_remains` is set to `TRUE`.


![figure ../tm129-19J-images/tm129_rob_p4_f018.jpg](../tm129-19J-images/tm129_rob_p4_f018.jpg)


Figure 5.4 Listing: Simon_the_sleuth: the macro `I_suspect`


macro I_Suspect( )

      comment : Simon asks if his suspicions are correct

__comment: e.g. "I suspect Tony with the cake in the study"__

      call speak(I_suspect, 85)

      call speak((100+person_suspected), 90)

      call speak(with_the, 50)

      call speak(104+food_suspected, 90)

      call speak(in_the, 50)

      call speak(109 + room_suspected, 120)

      set uncertainty_remains = FALSE

      if person_suspected = messy_person

            then

                  comment : tell Simon it was this person 

                  set person_correct = TRUE

            else

                  comment : Tell Simon it was not this person

                  set person_correct = FALSE

__comment: reset uncertainty as TRUE__

                  set uncertainty_remains = TRUE

      if food_suspected = trash

            then

                  comment : Tell Simon it was this food

                  set food_correct = TRUE

            else

                  comment : Tell Simon it was not this food

                  set food_correct = FALSE

__comment: reset uncertainty as TRUE__

                  set uncertainty_remains = TRUE

      if room_suspected = place

            then

                  comment : Tell Simon it was this room

                  set room_correct = TRUE

            else

                  comment : Tell Simon it was not this room

                  set room_correct = FALSE

__comment: reset uncertainty as TRUE__

                  set uncertainty_remains = TRUE

This macro also tests the food suspected and the room suspected.

The main part of the program is as follows:


![figure ../tm129-19J-images/tm129_rob_p4_f019.jpg](../tm129-19J-images/tm129_rob_p4_f019.jpg)


Figure 5.5 Listing: Simon_the_sleuth: main program


main

      comment : start the main program

      call setScene( )

__comment: main loop starts here...__

      while uncertainty_remains = TRUE

            comment : keep going until everything is deduced

            call Move( )

            call I_Suspect( )

            comment -------------------------------

            if person_correct &lt;&gt;  TRUE

                  then

                        comment Add statements here...

                        set person_suspected = person_suspected + 1

            if food_correct &lt;&gt; TRUE

                  then

                        comment Add statements here...

                        set food_suspected = food_suspected + 1

__comment: ...main loop ends here__

      comment ...

__comment: give deduction, eg "I accuse Tony with the cake in the study"__

      call speak(81, 150)

      call speak(I_accuse, 80)

      call speak(100+person_suspected, 90)

      call speak(with_the,50)

      call speak(104+food_suspected, 90)

      call speak(in_the, 50)

      call speak(109+room_suspected, 100)

comment : end of program

The program uses the logical variable `uncertainty_remains` to control its main loop. Every time it calls the `I_Suspect()` macro, this variable is initially set to `FALSE`. If any of the suspected person, food or room is incorrect, this variable is set to `TRUE`. Thus, while uncertainty remains, Simon continues.

Recall that the `I_Suspect()` macro sets the `person_correct` variable to `TRUE` or `FALSE`. This is tested in the main loop. If it is not equal to `TRUE` (the expression `&lt;&gt;` means ‘not equal to’) then the value of the variable `person_suspected` is increased by 1. In this way the program can start with Jon (`person_suspected = 1`), move on to Tony (`person_suspected = 2`) and then Blaine (`person_suspected = 3`). Eventually it will find the right person, in which case the `person_correct` variable will be `TRUE` and the rule `if person_suspected &lt;&gt; TRUE then…` will not fire again.

The rule `if food_suspected &lt;&gt; TRUE then…` works in a similar way to allow Simon to discover if the food was cake (`food_suspected = 1`) or pizza (`food_suspected = 2`).

When Simon has deduced the person, the food and the room, `uncertainty_remains` becomes `FALSE` and the program drops out of the loop for Simon to make its accusation.



# 4.5 Challenge: A better sleuth

Suggest how Simon might finish off sleuth games sooner. Then modify the code to achieve this (this second part of the challenge is optional). 


## Round Tripping 

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
