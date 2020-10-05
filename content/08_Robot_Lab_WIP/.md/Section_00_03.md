---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,.md//md
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
---

# 3 Multi-agent systems


*Set up a handshake between the robot seeing data, sending it to notebook, getting a response back and then eg saying the number aloud?*


*Maybe example with CNN and durable rules?*

??architecture

In this section I will explain the details of how the simulated robot and the notebook Python environment can work together as a *multi-agent system*.

To overcome the (simulated) autonomous robot’s limited processing abilities, and to exploit the much greater power of your PC and the full power of a rich Python environment, we have created a protocol in which the simulated robot sends data to code running in the notebook Python environment, the notebook processes that information using a pre-trained neural network or rule based system and then sends the result back to the robot.

The model is a bit asking a research librarian for some specific information, the research librarian researching the topic, perhaps using resources you don't have direct access to, and then the research librarian providing you with the information you requested.

In computational terms, *agents* are long-lived computational systems that can deliberate on the actions they may take in pursuit of their own goals based on their own internal state (often referred to as "beliefs") and sensory inputs. Their actions are then performed by means of some sort of effector system that can act on to change the state of the environment within which they reside.

In a multi-agent system, two or more agents may work together to combine to perform some task that not only meets the (sub)goals of each individual agent, but that might also strive to attain some goal agreed upon by each member of the multi-agent system.

In a multi-agent system, agents may communicate by making changes to the environment, for example, by leaving a trail that other agents may follow (*stigmergy*), or by passing messages between themselves directly.

To a limited extent, we may view our robot / Python system as a model for a simple multi-agent system where two agents — the robot, and the classifying neural network or deliberative rule based system — work together to perform the task classifying and identifying patterns in some environment that the individual agents could not achieve by themselves.





![figure ../tm129-19J-images/tm129_rob_p9_f006.png](../tm129-19J-images/tm129_rob_p9_f006.png)


Figure 3.1 The robot–PC communication protocol


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

