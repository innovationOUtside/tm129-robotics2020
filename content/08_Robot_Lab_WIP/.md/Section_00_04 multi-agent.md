---
jupyter:
  jupytext:
    cell_metadata_filter: -all
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

<!-- #region -->
# 4 Multi-agent systems

In the previous notebooks in the session, we synchronised data collected in the simulator with the notebook's Python environment, and then analysed the data in the notebook environment as and when it was convenient. In particular, we could view the data as images, and present the data to a pre-trained multilayer perceptron (MLP) or a pre-trained convolutional neural network (CNN) to try to classify them.

We could also capture and decode test labels for the images,


TO DO.
<!-- #endregion -->

To simplify data collection matters, we positioned the robot at specific locations, rather than expecting the robot to explore the environment and try to detect images on its own. In this notebook, we will try to make things a little more dynamic in two ways. Firstly, we will set the robot free to drive over the digits rather than magically teleporting it around the environment. Secondly, we will make use of a communication mechanism where the robot can send data back to the notebook environment for analysis, and then when the analysis is complete, have a message sent back to the robot identifying how a potential image was classified.

<!-- #region -->
## 4.1 ROS — the Robot Operating System

*ROS*, the *Robot Operating System*, provides one possible architecture for implementing a dynamic message passing architecture. In a ROS environment, separate *nodes* publish details of one or more *services* they can perform along with *topics* that act act as the nodes address that other nodes can subscribe. Nodes then pass messages between each other in order to perform a particular task. The ROS architecture is rather elaborate for our needs, however, so we shall use a much simpler and more direct approach.

The approach we will use, although much simpler approach than the full ROS architecture, will also be based on a message passing approach. To begin with, we will train a simple MLP network using the MNIST digits data in the Python environment attached to the notebook. We will then log image sensor data from the simulated robot and copy it into the notebook data log. From the data in the data log, we will then see if the MLP can recognise the digits.

After testing this approach, we will then explore a simple message passing protocol where the simulated robot sends a message to the Python environment containing the image sensor data, the data is run through the MLP, and the classification response is sent back to the simulated robot.

### 3.1.1 Communicating between the notebook and the robot


![A diagram showing a robot and computer connected by a double ended arrow labelled ‘messages between the agents’.](../tm129-19J-images/tm129_rob_p9_f002.jpg)


Figure 1.1 The robot and the PC as a simple example of a two-agent system

The combination of just two agents like this creates a powerful example of a multi-agent system in which the performance of the agents is enhanced due to their interaction.

Communication between the agents is very important. The Lego RCX and PC can communicate with each other using infrared messages, similar to those sent by a TV remote control. An exchange of messages needs to be governed by a *protocol* that defines what the messages mean, and how the agents should take turns in sending and receiving. It should also handle cases where messages get lost, since no communication channel is fully reliable. For example, infrared messages could be lost if the robot wanders out of range or just faces the wrong way. We will consider a simple protocol in this session.

As always, in this session you will be working with Simon, our simulated autonomous robot, rather than a real mobile robot. Our two agents will therefore be Simon and RoboLab itself. Rather confusingly, both the simulation of Simon and RoboLab will be running on the same computer, so you will have to take it on trust that they are effectively independent and only communicate with the simple messages I explain below. There is no cheating, no hidden channel of communication!

In Robot Lab Session 8 you will experiment using the neural network on the PC to classify data on fruit, gathered by Simon. You will also experiment by training your own network to be used remotely by the robot.
<div xmlns:str="http://exslt.org/strings" style="background:lightgreen">
<!--Heading: 
            Tip-->
Before running any of the programs in this session we recommend that you first switch off the ‘trace’ function. Do this with the `Run | Trace` menu item.<div style="background:lightblue"><p>Keyboard: Alt, R, A</p></div> (You will need to remember to do this each time you open a new program.) With the trace on, RoboLab will highlight the current statement, but this can be distracting with the long programs used here.
</div>

<!-- #endregion -->

*Set up a handshake between the robot seeing data, sending it to notebook, getting a response back and then eg saying the number aloud?*


## Multi agent


Can we find a way of getting the robot to post a message to Python, and Python to respond with a message back to the robot that the robot can respond to? 

The original RoboLab activities include examples of round-tripping, with the simulated robot passing state out to a remote application, which then returned a response to the simulated robot. I'm pretty sure we can do the same, either with a predefined application or a user defined function. The latter would be best because then we could have an activity to write a helper application in notebook python that is called on by the simulated robot.

At the moment, I have managed to send a message to Py from the simulator via messages sent to the simulator output window. There is a callback that sends messages back from Py to the sim output window, but as yet the robot py code running in the simulator is oblivious to returned messages. (I need half a day, perhaps, a day, to actually get code into the simulator so the program code can access it.)

The following recipe shows how to overwrite the default collaborative `responder()` function with a custom one.

```python
#Get the simulator
from nbev3devsim.load_nbev3devwidget import roboSim, eds
%load_ext nbev3devsim

```

We can create custom handlers on the Python notebook side that can pick up messages sent from the simulator and return a response to the simulator.

```python
def responder(obj):
    """ Callback function that tries to respond to widget."""
    response = f'I SAW> {obj} >that...'
    return response
```

```python
roboSim.pyresponder = responder
%sim_magic --refresh
```

```python
%%sim_magic -RO
print("five")
print("six")
import time

for i in range(10):
    print(str(i))
    if not i%4:
        print("PY::"+str(i))
    time.sleep(0.1)
```

```python

```

```python
def live_image_handler(i):
    """ Callback function that tries to respond to logged image."""
    response = f'I SAW> {i} >that image...'
    return response

roboSim.live_image_handler = live_image_handler
%sim_magic --refresh
```

```python
%%sim_magic_preloaded -b Simple_Shapes --collab -ARO -x 760 -y 700 -O

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

# This is essentially a command invocation
# not just a print statement!
print("image_data both")

import time
for i in range(5):
    print(i)
    time.sleep(0.1)
```

```python

```

```python
%%sim_magic_preloaded
import time
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_C)

gyro = GyroSensor(INPUT_4)


tank_drive.on(SpeedPercent(50), SpeedPercent(30))
time.sleep(0.1)

#print('left_motor_count'+tank_drive.left_motor.position_sp)
while int(tank_drive.right_motor.position)<1000:
    time.sleep(0.1)
    print('left_motor_count'+str(tank_drive.left_motor.position))
    print('right_motor_count'+str(tank_drive.right_motor.position))

```

```python

```
## ??

In this section I will explain the details of how the simulated robot and the notebook Python environment can work together as a *multi-agent system*.

To overcome the (simulated) autonomous robot’s limited processing abilities, and to exploit the much greater power of your PC and the full power of a rich Python environment, we have created a protocol in which the simulated robot sends data to code running in the notebook Python environment, the notebook processes that information using a pre-trained neural network or rule based system and then sends the result back to the robot.

The model is a bit asking a research librarian for some specific information, the research librarian researching the topic, perhaps using resources you don't have direct access to, and then the research librarian providing you with the information you requested.

In computational terms, *agents* are long-lived computational systems that can deliberate on the actions they may take in pursuit of their own goals based on their own internal state (often referred to as "beliefs") and sensory inputs. Their actions are then performed by means of some sort of effector system that can act on to change the state of the environment within which they reside.

In a multi-agent system, two or more agents may work together to combine to perform some task that not only meets the (sub)goals of each individual agent, but that might also strive to attain some goal agreed upon by each member of the multi-agent system.

In a multi-agent system, agents may communicate by making changes to the environment, for example, by leaving a trail that other agents may follow (*stigmergy*), or by passing messages between themselves directly.

To a limited extent, we may view our robot / Python system as a model for a simple multi-agent system where two agents — the robot, and the classifying neural network or deliberative rule based system — work together to perform the task classifying and identifying patterns in some environment that the individual agents could not achieve by themselves.





![figure ../tm129-19J-images/tm129_rob_p9_f006.png](../tm129-19J-images/tm129_rob_p9_f006.png)


Figure 3.1 The robot–PC communication protocol


## ??

## Logging lots of data


```python
%%sim_magic_preloaded

# how do we log the raw light sensor data to the datalog?


# Configure a light sensor
colorLeft = ColorSensor(INPUT_2)

# Start the robot driving forwards
tank_drive.on(SpeedPercent(50), SpeedPercent(50))

#Sample the light sensor reading
sensor_value = colorLeft.reflected_light_intensity

#Check the light sensor reading
while True:
    # Whilst we are on the white background
    # update the reading
    sensor_value = colorLeft.reflected_light_intensity_pc
    # and display it
    if sensor_value < 50:
        print("image_data left")
```

```python
data = roboSim.image_data
data[0]
```

```python

df = pd.DataFrame(columns=['side', 'vals', 'clock'])
for r in data:
    _r = r.split()
    if len(_r)==3:
        tmp=_r[1].split(',')
        k=4
        del tmp[k-1::k]
        df = pd.concat([df, pd.DataFrame([{'side':_r[0],
                                          'vals': ','.join(tmp),
                                          'clock':_r[2]}])])
df.reset_index(drop=True,inplace=True)
df
```

```python
tmp=df.iloc[14]['vals'].split(',')
#k=4
#del tmp[k-1::k]

vv = np.array(tmp).reshape(20, 20, 3).astype(np.uint8)
vvi = Image.fromarray(vv, 'RGB')
vvi
```

```python
#vvx = vvi.crop((3, 3, 19, 19)) 
vvx =vvi.resize((28, 28), Image.LANCZOS)
vvx
```


## ??

```python
# co-operative mode

# previous is a "pull" model where we essentially pull data into the notebook environment
# But what if we automatically push data from the robot to the notebook pyhtion environment and then 
# that automatically sends a response to the pyhton environment?
```

A communication diagram showing the messages passed between mobile robot and a computer. The robot is shown on the right and the computer on the left; reading down the page shows the successive images of robot and computer at different times. Messages are shown by labelled arrows between participants. The diagram is read from the top. The starting point is the robot which has taken measurements (here 8 and 11). The first message runs from robot to computer, shown as an arrow labelled ‘send 255; upload my data and classify it’. An arrow labelled ‘prepare to upload data’ leads from the computer to another image of the computer placed in the line below. The computer then sends a message shown as an arrow labelled ‘upload your datalog’ to the robot. An arrow labelled ‘upload datalog’ leads from the robot to another image of the robot in the next line. A further message, labelled ‘8 11; here is my datalog’ is passed from robot back to the computer. Finally, an arrow from the computer to another image of the computer in the following line is labelled ‘neural network classification’; the image of the computer is now accompanied by one of a strawberry.

When you open the `Simon_recognises_fruit` program, RoboLab automatically loads the appropriate trained neural network, at which point it is ready to classify unseen data. When it receives the uploaded data RoboLab puts these data through the neural network and obtains a classification, such as ‘strawberry’ in Figure 3.1.

The robot, Simon, first measures the long and short axis of the fruit. We’ll use a strawberry for this example, with measurements 8 and 11. Simon now initiates the communication with the `send 255` command. The code 255 tells RoboLab to initiate its neural network procedures. It starts by uploading Simon’s data log. Here, the data log contains two numbers, 8 and 11, which are the short and long measurements of the strawberry respectively. These are used as inputs to the neural network.

Having made a classification, RoboLab sends a code back to Simon to say what this class was – i.e. strawberry. The code RoboLab sends back corresponds to the first character of the class name given to the neural network during training – in this case, ‘s’, which is represented by the ASCII code 83 (<a xmlns:str="http://exslt.org/strings" href="">Table 7.1 in Appendix 1</a>).

How can Simon be sure to receive the information from RoboLab? In our protocol, Simon will wait in a loop until it receives a message. When RoboLab sends a message, Simon will pick it up.


![figure ../tm129-19J-images/tm129_rob_p9_f007.png](../tm129-19J-images/tm129_rob_p9_f007.png)


Figure 3.2 The robot gets the classification back as a coded message


A further stage in the message passing between mobile robot and computer. This starts with the robot sending the message labelled ‘which class did you recognise?’ The computer, accompanied by a picture of a strawberry, receives that and an arrow labelled ‘send back 83 the code for S’ leads to another image of the computer in the following line. The final message is sent from computer to robot, labelled ‘83; the message 83 is the code for S; S is the first letter of strawberry’. The robot is now accompanied by a picture of a strawberry.

The message protocol is now complete and our mobile agent, Simon, has now been told that the object it measured was a strawberry. It could then go on to do something with that information. Here, Simon simply sends an appropriate message back to RoboLab using the `send` command as we have done in several other programs. This makes RoboLab announce ‘strawberry’, confirming that Simon now knows it has found a strawberry (Figure 3.2). (Look in the RoboLab help file for a full list of `send` codes).

The full message protocol is shown in Figure 3.3. We can use exactly the same protocol with a Lego RCX robot exchanging infrared messages with RoboLab.


![figure ../tm129-19J-images/tm129_rob_p9_f008.png](../tm129-19J-images/tm129_rob_p9_f008.png)


Figure 3.3 The entire two-agent neural network classification process


A communication diagram for the entire exchange between robot and computer. This merges the two previous diagrams; the complete description is repeated here. 

 The robot is shown on the right and the computer on the left; reading down the page shows the successive images of robot and computer at different times. Messages are shown by labelled arrows between participants. The diagram is read from the top. The starting point is the robot which has taken measurements (here 8 and 11). The first message runs from robot to computer, shown as an arrow labelled ‘send 255; upload my data and classify it’. An arrow labelled ‘prepare to upload data’ leads from the computer to another image of the computer placed in the line below. The computer then sends a message shown as an arrow labelled ‘upload your datalog’ to the robot. An arrow labelled ‘upload datalog’ leads from the robot to another image of the robot in the next line. A further message, labelled ‘8 11; here is my datalog’ is passed from robot back to the computer. An arrow from the computer to another image of the computer in the following line is labelled ‘neural network classification’; the image of the computer is now accompanied by one of a strawberry. At the same stage, an arrow from the robot is labelled ‘wait 150’ and leads to another image of the robot. 

 At this point, the robot sends the message labelled ‘which class did you recognise?’ The computer, accompanied by a picture of a strawberry, receives that and an arrow labelled ‘send back 83 the code for S’ leads to another image of the computer in the following line. The final message is send from computer to robot, labelled ’83; the message 83 is the code for S; S is the first letter of strawberry’. The robot is now accompanied by a picture of a strawberry. 

