---
jupyter:
  jupytext:
    formats: ipynb,.md//md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Flow Chart Generator

```python
from jp_flowchartjs.jp_flowchartjs import FlowchartWidget
```

*An [issue](https://github.com/adrai/flowchart.js/issues/186) has been filed regarding the misaligned return path in the flow diagram in `jp_flowchartjs`.*


## 03_1_1

Mermaid code https://mermaid-js.github.io/mermaid-live-editor/
The mermaid editor is supposed to encode/decode base 64 strings
but I can't get my own encoder/decoder to work to encode/decode things the same way?

graph LR
    A(Start) --> B[Set the count to 0]
    B --> C[Swim a length]
    C --> D[Add 1 to the count]
    D --> E{Is the<br/>count less<br/>than 20?}
    E --> |Yes| C
    E --> |No| F(End)
    
Long description:

A flow chart for a person swimming 20 lengths of a pool. The flow chart starts with an oval shape labelled ‘Start’. From here there are sequences of boxes connected by arrows: first ‘Set the count to 0’, then ‘Swim a length’ and last ‘Add 1 to the count’. From this box an arrow leads to a decision diamond labelled ‘Is the count less than 20?’ Two arrows lead from this: one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch leads back to rejoin the box ‘Swim a length’. The ‘No’ branch leads directly to an oval shape labelled ‘End’. There is thus a loop in the chart which includes the steps ‘Swim a length’ and ‘Add 1 to the count’ and ends with the decision ‘Is the count less than 20?’

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Set the count to 0
op2=>operation: Swim a length
op3=>operation: Add 1 to the count
cond=>condition: Is the count less than 20?
st(right)->op1(right)->op2(right)->op3(right)->cond
cond(yes,right)->op2
cond(no)->e
```

### Ironing

Mermaid drawing (this is far from ideal...Maybe better to use draw.io?)<font color='red'>JD: To be resolved.</font>

graph LR
    A(Start) --> B{Any clothes<br>left in<br/>basket?}
    B --> |Yes| C[Take out<br/>item and<br/>iron]
    C --> D[Put it on pile<br/>of ironed<br/>clothes]
    D --> B
    B --> |No| E(End)
    
Long description:

A flow chart for a person ironing clothes. This starts with an oval ‘Start’. An arrow leads to a decision diamond ‘Any clothes left in basket?’ Two arrows lead from this: one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch continues in turn to two boxes ‘Take out item and iron’ and ‘Put it on pile of ironed clothes’; an arrow leads back from this box to rejoin the decision ‘Any clothes left in basket?’ The ‘No’ branch leads directly to an oval ‘End’. There is thus a loop in the chart which begins with the decision ‘Any clothes left in basket?’ and includes the steps ‘Take out item and iron’ and ‘Put it on pile of ironed clothes’.

```python
%%flowchart_magic
st=>start: Start
e=>end: End
cond=>condition: Any clothes left in basket?
op2=>operation: Take out item and iron
op3=>operation: Put it on pile of ironed clothes
st(right)->cond
cond(yes, right)->op2
op2(right)->op3(top)->cond
cond(no, bottom)->e
```

graph TD
    A(Start) --> B[Set counter to 0]
    B --> C[# Draw side<br/>...code...]
    C --> D[# Turn ninety degrees<br/>...code...]
    D --> E[Add 1 to counter]
    E --> F{Is counter < 4?}
    F --> |Yes| C
    F --> |No| G(End)
    
Long description:

A flow chart for a robot program with a loop. This starts with an oval ‘Start’. An arrow leads first to a box ‘Set counter to 0’ and then to a sequence of further boxes: ‘# Draw side’ with an implication of the code associated with that, ‘# Turn ninety degrees’, again with a hint regarding the presence of code associated with that activity, and lastly ‘Add 1 to counter’. The arrow from this box leads to a decision diamond ‘Is counter < 4?’ Two arrows lead from this, one labelled ‘Yes’, the other ‘No’. The ‘Yes’ branch loops back to rejoin the sequence at ‘# Draw side code’. The ‘No’ branch leads directly to an oval ‘End’. There is thus a loop in the chart which includes the sequence of motor control commands, incrementing the counter and ends with the decision ‘Is counter < 4?’.

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Set counter to 0
op2=>operation: Draw side code
op3=>operation: Turn ninety degrees code
op4=>operation: Add 1 to counter
cond=>condition: Is counter < 4?
st(right)->op1(right)->op2->op3->cond
cond(yes, right)->op2
cond(no, bottom)->e
```

### 02_Robot_Lab/Section_00_02.md

![](https://mermaid.ink/img/eyJjb2RlIjoiXG5ncmFwaCBURFxuICAgIEEoU3RhcnQpIC0tPiBCW01vdmUgZm9yd2FyZHNdXG4gICAgQiAtLT4gQ3tMaWdodCA9PSAyNTV9XG4gICAgQyAtLT4gfFllc3wgRFtEaXNwbGF5IHJlYWRpbmddXG4gICAgRCAtLT4gQ1xuICAgIEMgLS0-IHxOb3wgRVtEcml2ZSBmb3J3YXJkPGJyLz5hIHNob3J0IHdheV1cbiAgICBFIC0tPiBGe0xpZ2h0IDwgMTI4P31cbiAgICBGIC0tPiB8WWVzfCBHW1NheSAnYmxhY2snXVxuICAgIEYgLS0-IHxOb3wgSFtTYXkgJ2dyZXknXVxuICAgIEcgLS0-IEkoRW5kKVxuICAgIEggLS0-IElcbiAgICBcbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2V9)

```python
%%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Start moving forwards
cond1=>condition: Light < 100?
op2=>parallel: Display reading (continue drive forwards)
op3=>operation: Drive forward a short way
cond2=>condition: Light < 50?
op4=>operation: Say "grey"
op5=>operation: Say "black"

st(right)->op1(right)->cond1({'flowstate':{'cond1':{'yes-text' : 'ssno', 'no-text' : 'yes'}}} )
cond1(no,right)->op2(path1, top)->cond1
cond1(yes)->op3->cond2
cond2(no)->op4->e
cond2(yes)->op5->e
```

<div class='alert alert-warning'>The flowchart.js layout algorithm will allow us to change yes/no labels on conditions, but the magic does not currently provide a way to pass alternative values in (eg swapping yes/no labels to change the sense of the decision as drawn). Also, the layout algorithm seems to be broken when swapping yes and no.</div>

```python
## # Mermaid.js code

graph TD
    A(Start) --> B[Move forwards]
    B --> C{Light == 100}
    C --> |Yes| D[Display reading]
    D --> C
    C --> |No| E[Drive forward<br/>a short way]
    E --> F{Light < 50?}
    F --> |Yes| G[Say 'black']
    F --> |No| H[Say 'grey']
    G --> I(End)
    H --> I
```

We can do checklists in notebooks:

- [ ] item 1
- [ ] item 2

```python
# %%flowchart_magic
st=>start: Start
e=>end: End
op1=>operation: Start moving forwards
cond1=>condition: Light < 100?
op2=>parallel: Display reading (continue drive forwards)
op3=>operation: Drive forward a short way
cond2=>condition: Light < 50?
op4=>operation: Say "grey"
op5=>operation: Say "black"

st(right)->op1(right)->cond1({'flowstate':{'cond1':{'yes-text' : 'ssno', 'no-text' : 'yes'}}} )
cond1(no,right)->op2(path1, top)->cond1
cond1(yes)->op3->cond2
cond2(no)->op4->e
cond2(yes)->op5->e

```

The flow chart starts with a *Start* label followed by a rectangular *Start moving forwards* step. An initial diamond shaped decision block tests the condition "Light < 100". If false ("no"), the program continues with a rectangular "Display reading (continue drive forwards)" step which then returns control back to the first decision block. If true ("yes") control progresses via a rectangular "Drive forward a short way" step and then another diamond shaped decision step which tests the condition "Light < 50". If "no", control passes to a rectangular "Say 'grey'" step and then a terminating "End" condition. If "yes", control passes to a rectangular "Say 'black'" step and then also connects to the terminating "End" condition.


## Design cycle

<!-- #raw -->
# st=>start: Start
e=>end: End
op1=>operation: Generate
op2=>parallel: Evaluate
st(right)->op1(right)->op2
op2(path1, top)->op1
op2(path2, right)->e
<!-- #endraw -->
