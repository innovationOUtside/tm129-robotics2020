```python
import sys
sys.path.insert(0,'..')
import _load_nbev3devwidget_requirements
```

```javascript
//This allows us to resize this view
//Click on the right hand edge to drag
$( "#notebook-container" ).resizable({ghost: false})
```

```python
from _load_nbev3devwidget import roboSim, eds

%load_ext nbev3devsim
%load_ext nbtutor
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

    print(intensity_left, intensity_right)
    
    left_motor_speed = SpeedPercent(intensity_left)
    right_motor_speed = SpeedPercent(intensity_right)
    
    tank_drive.on(left_motor_speed, right_motor_speed)
 
```

## 4.1 Representing and using knowledge


Artificial intelligence and robotics have the major problem of *representing* facts and knowledge inside machines. We have a vast amount of knowledge in our brains. This knowledge is distributed over the brain, rather than each fact being neatly stored in a single memory unit.

The structure of the human brain is completely different from the structure of a robot's or a real computer’s "brain", and roboticists have found it very difficult to implant a wide range of experiences (real-world data) into robot brains. Significant progress has been made in Artificial Intelligence (AI) and Machine Learning (ML) approaches to machine vision in recent years by using ever more computational resources. Ever larger and more complex natural language processing (NLP) models are also proving effective in parsing natural language statements and generating natural language texts.

One way of *explicitly* trying to encode knowledge is to use a *rule based system*.


## Eliza

Athough written fifty or so years ago, Joseph Weizenbaum's *Eliza* programme is often referred to as one of the first great milestones in computational natural language interaction. You can see a copy of the original paper [here](https://github.com/wadetb/eliza/blob/master/p36-weizenabaum.pdf), which includes examples of the code used to programme the original Eliza engine. Eliza has been reimplemented several times, such as in the Lisp language by Peter Norvig's for his textbook *Paradigms of Artificial Intelligence Programming*, as well as in Python reimplementation of Norvig's code by Daniel Connelly ([*Paip-python: Peter Norvig's Paradigms of AI Programming implemented in Python*](http://dhconnelly.com/paip-python/)). 

A version of Connelly's code, updated to run in the version of Python used in these notebooks, is contained in the file [eliza.py](eliza.py).

You can try it out for yourself by running the following code cell and starting your conversation with a *Hello*; end the conversation by starting your response with *Goodbye*):

```python
import eliza
eliza.hello_doctor()
```

If you want to hear Eliza speak the responses aloud to you, start the programme by passing in the parameter `aloud=True` in the following way: `eliza.hello_doctor(aloud=True)`.

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
eliza.hello_doctor('doolittle.json',
                   default = ["Very interesting",
                              "I am not sure I understand you fully"]
                  )
```

If you come up with an interesting script, please fee free to share it in the module forums.
<!-- #endregion -->

### Durable Rules Engine

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


We can define a really simple Python speech class that allows us to speak from code contained in a notebook using the browser's Javascript speech engine:

```python
from IPython.display import Javascript

class Speech():
    def say(self, txt):
        display(Javascript(f'speechSynthesis.speak(new SpeechSynthesisUtterance("{txt}"))'))
        
speaker = Speech()
speaker.say('hello')
```

Building on the simple speech class for taling via the browser, I have created a class that keeps track of how many messages have been posted and returns a visual count of utterances, alongside a transcript of the utterance.

```python
from IPython.display import Javascript

class Speech():
    def __init__(self, voice=None, reset=True):
        if reset:
            self.count = 1
        self.voice = voice
        self._get_voices()
        self.voicelist = ''

    def set_voice(self, voicenum):
        """Set voice number."""
        self.voice = voicenum

    def say(self, txt, showtext = True):
        """Speak an utterance."""
        js = f'''
        var utterance = new SpeechSynthesisUtterance("{txt}");
        '''
        if self.voice:
            js = js + f'''
            utterance.voice = window.speechSynthesis.getVoices()[{self.voice}];
            '''
        js = js + 'speechSynthesis.speak(utterance);'
        display(Javascript(js))
        
        if showtext:
            print(f'{self.count}: {txt}')
        self.count = self.count +1
        
    def reset_count(self):
        """Reset the counter."""
        self.count = 1
        
    def _get_voices(self):
        """Show a list of supported voices."""
        # via https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis/getVoices
        js = '''
        var voices =  window.speechSynthesis.getVoices();
    var voicelist = '';
   for(var i = 0; i < voices.length; i++) {
   voicelist = voicelist+i+': '+ voices[i].name + ' ('+ voices[i].lang +')';
    if(voices[i].default) {
      voicelist += ' -- DEFAULT';
    }
   voicelist = voicelist + '*'
  }

IPython.notebook.kernel.execute("_browser_voicelist = '"+ voicelist+"'");
        '''
        display(Javascript(js))
        
    def show_voices(self):
        self.voicelist = _browser_voicelist
        
        outlist = '\n'.join([s.strip() for s in _browser_voicelist.split('*')])
        print(outlist)
        #return self.voicelist
    
```

```python
speaker = Speech()

#speaker.set_voice(49)
speaker.say('hello how are you')
```

We can also show the list of voices.

```python
speaker.show_voices()
```

You can use the folowing command to reset the message count:

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

## More General Forms of Rules

So far we have focused on reasoning about "facts" in the form of statements with the form  *subject predicate object*.

But this actally represents a more complicated form of reasoning than the rules engine actually employs because the *atomic* smallest possible facts are not the *subject predicate object* triples at all, they are the individual properties: `{subject: SUBJECT}`, `{'predicate': PREDICATE}` and `{object: OBJECT}`.



### Facts versus Events

Facts persist, events are retracted once they have been evaluated. Events are particularly useful in a robotics context, where we may want to respond to repeated sensor events.

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

```python
post(RULESET, {'color': 'red' });
```

```python
post(RULESET, {'color': 'green' });
```

```python
post(RULESET, {'color': 'red' });
post(RULESET, {'color': 'green' });
```

### How might rules be useful in a robot context?

Although we can easily create our own `if...` statements in the programme downloaded to the simulator, and control the robot's behaviour that way, it may more convenient to develop, and test, a large and possibly complex rule based set of behaviours using a framework such as a *Durable Rules*.

This may be achieved by capturing sensor values from the robot in the simulator, passing them back to the notebook's Python context, passing them as events to the Durable Rules ruleset, applying the rules to create some statement of a desired motor action, and then returning this instruction to the simulated robot for execution there.

We will not pursue this approach further, here. However, you will have an opportunity to control the simulated robot in a similar way using a neural network running in the notebook context, rather than a rule based system, in a later notebook.

<!-- #region -->
### Addendum - Using Python to Respond to and Control Events in the Simulator


__THESE ARE JUST MY WORKING NOTES AS I TRY TO FIGURE STUFF OUT...__

Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 
<!-- #endregion -->

The original RobotLab activities include examples of round-tripping, with the simulated robot passing state out to a remote application, which then returned a response to the simulated robot. I'm pretty sure we can do the same, either with a predefined application or a user defined function. The latter would be best because then we could have an activity to write a helper application in notebook python that is called on by the simulated robot.

At the moment, I have managed to send a message to Py from the simulator via messages sent to the simulator output window. There is a callback that sends messages back from Py to the sim output window, but as yet the robot py code running in the simulator is oblivious to returned messages. (I need half a day, perhaps, a day, to actually get code into the simulator so the programme code can access it.)

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
