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

# 1 Introduction


You have already been introduced the idea of neural networks in the VLE study materials: now you are going to have an opportunity to play with them in practice.

Neural networks can solve subtle pattern recognition problems, which are very important in robotics. Although many of the activities are presented outside the robotics context, we will also try to show how they can be used to support robotics related problems.

In recent years, great advances have been made in generating powerful neural networks based models often referred to as "deep learning" models. But neural networks have been around for over 50 years, with advances every few years, often reflecting advances in computing availability, and then long periods of "AI Winter" when not much progress appeared to be being made.

The following XKCD cartoon, *Tasks*, was first published in 2014. As is typical of XKCD cartoons, hovering over the cartoon revealed some hidden caption text. In this particular case: *[i]n the 60s, Marvin Minsky assigned a couple of undergrads to spend the summer programming a computer to use a camera to identify objects in a scene. He figured they'd have the problem solved by the end of the summer. Half a century later, we're still working on it*. 

![](https://imgs.xkcd.com/comics/tasks.png)

At the time (this is only a few short years ago remember), recognising arbitrary items in images was still a hard task and the sentiment of this cartoon rang true. But within a few months, advances in neural network research meant that AI models capable of performing similar tasks, albeit crudely and with limited success, had started to appear. Today, photographs are routinely tagged with labels that identify what can be seen in the photograph using much larger, much more powerful, and much more effective AI models.

However, identifying individual objects in an image on the one hand, and being able to generate a sensible caption that describes the image, is a different matter. A quick web search today will undoubtedly turn up some very enticing demos out there of automated caption generators. But "reading the scene" presented by a picture and generating a caption from a set or keywords or tags associated with items that can be recognised in the image is an altogether more complex task: as well as performing the object recognition task correctly, we also need to be able to identify the relationships that hold between the different parts of the image; and do that in a meaningful way.

<!-- #region activity=true -->
### Activity - Example Image Tagging Demo

There are many commercial image tagging services available on the web that are capable are tagging uploaded images or images that can be identified by a web URL.

Try one or more of the following services to get a feel for what sorts of service are available and how effective they are at tagging an image based on its visual content: 

- [Algorithmia](https://demos.algorithmia.com/image-tagger)
- [Imagga](https://imagga.com/auto-tagging-demo)
- [Pixolution](https://pixolution.io/keyword-suggestion)
- [Sensifai](https://demo.sensifai.com/)
- [Ximilar (demo1 - generic tagging)](https://demo.ximilar.com/)
- [Ximilar (demo2 - fashion tagging)](https://demo.ximilar.com/fashion/fashion-tagging)

__Do not spend more than 10 minutes on this activity.__

*If you discover any additional demo services, or if you find that any of the above services seem have either stipped working, or disappeared, please let us know via the module forums.*
<!-- #endregion -->

## Transfer Learning

Creating a neural network capable of recognising a particular image can take a lot of data and a lot of computing power. The training process typically involves showing the network being trained:

- an image;
- a label that says how we want the image to be recognised.

The neural network, which is often referred to as *a model* (that is, a *statistical model*) is presented with the image and asked what label is associated with that image. If the network's suggested label matches the training label, the network model is "rewarded" so that it is more like to give that answer for that sort of image in future. If the prediction does not match the training label, the model parameters are updated so that the model is less likely to make that incorrect prediction in future and more likely to assign the correct training label.

The effectiveness of the model is then tested on images it has not seen before, and it's predictions checked against the correct labels.

A process known as "transfer learning" allows a model trained on one set of images to be "topped up" with additional training based on image/label pairs from images it has not seen or been trained on before. 

The pre-trained model already knows how to identify lots of different unique "features" that might be contained within an image. When you further train the model, it uses combinations of the features it can already detect as components of different feature collections that it can use to distinguish between the different object types you train it to recognise specifically.

In Robot Lab Session 7 you will get hands-on experience of using a variety of neural networks, and you will build and train neural networks to perform specific tasks.


<!-- #region activity=true -->
## Activity — Recognising A Static Pose in An Image

As well as tagging images, properly trained models can recognise individual people's faces in photos (and not just of celebrities!) and human poses within a photograph.

Click through to the following web location to see an example of a netural netwrok model running in your web browser to the recognise the pose of several different people across a set of images: https://pose-animator-demo.firebaseapp.com/static_image.html


<!-- #endregion -->

<!-- #region tags=["todo", "alter-danger"] -->
TO DO - Add a local example with additional ability to upload your own photo.
<!-- #endregion -->

<!-- #region activity=true -->
## Optional Activity — Distinguishing Between Two Of Your Own Poses From a Live Video Feed
Although is can take *a lot* of data and *a lot* of computational effort to train a model, topping up a model with transfer learning applied to a previously trained model can be achieved quite simply.

This optional activity allows you to top-up a pre-trained model to recognise of an image of you with your hand raised, and an image of you without you hand raised. Feeding a live image into the model allows it to detect in real time whether you have your hand or arm raised or not.

__ TO DO _ need to package this as a jupyter_server_proxy thing.__

*This activity requires that you have a camera attached to your computer and that your web browser has permission access the camera feed. The captured images do not leave your computer.*
<!-- #endregion -->

<!-- #region activity=true -->
## Optional Activity — Training Your Own Image or Audio Classifier


If you have a camera or microphone attached to your computer, the following activity will show you how you can top-up a pre-trained model to distinguish between two or more categories of image or sound of your own devising:

- upload your own images (or capture some images from a camera attached to your computer) and assign them to two or more categories you have defined yourself, then train the model to distinguish between them: https://teachablemachine.withgoogle.com/train/image

- upload your own audio files (or capture some audio from a microphone attached to your computer) and assign them to two or more categories you have defined yourself, then train the model to distinguish between them: https://teachablemachine.withgoogle.com/train/audio
<!-- #endregion -->

### IFrame demo of tensorflow playground

Need jupyter-server-proxy
Need a server: python3 -m http.server 8999

```
from IPython.display import IFrame
IFrame('http://localhost:8129/proxy/8999/dist/index.html#activation=tanh&batchSize=10&dataset=circle&regDataset=reg-plane&learningRate=0.03&regularizationRate=0&noise=0&networkShape=4,2&seed=0.70538&showTestData=false&discretize=false&percTrainData=50&x=true&y=true&xTimesY=false&xSquared=false&ySquared=false&cosX=false&sinX=false&cosY=false&sinY=false&collectStats=false&problem=classification&initZero=false&hideText=false',width=1000, height=600)
```


[Tools for visualising networks](https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network)

Single layer perceptron trainer - https://github.com/niinpatel/Single-Layer-Perceptron/ Could be useful to fork / extend; eg show weights?

Convolutional net - stepwise https://github.com/vicolab/neural-network-intro/blob/master/3-convnet/convolutional-network.ipynb

Observable MNIST demo https://observablehq.com/@tpreusse/interactive-convolutional-neural-network

Network structure visualisation: https://github.com/voletiv/myPythonNeuralNetwork (1_Neural_Network_Tutorial_Visualizations.ipynb); my own cribbed structure visualiser https://github.com/jarusgnuj/ioctm358/blob/TH-fn-to-plot-NN/notebooks/py/draw_neural_net.py

Simple interactives: [perceptrons](https://github.com/trsvchn/interactive-perceptrons) - possibly useful with explanation, but not very responsive? Some explanation of perceptron as logic blocks: https://medium.com/@stanleydukor/neural-representation-of-and-or-not-xor-and-xnor-logic-gates-perceptron-algorithm-b0275375fea1 ;  How about building using ipywidgets? There's also a simple weight visualiser with table inputs here: http://jalammar.github.io/feedforward-neural-networks-visual-interactive/#prediction-calculation Could be interesting if we also had weight sliders? What does that data look like on a scatter plot?

Useful viz demos (old) https://cs.stanford.edu/people/karpathy/convnetjs/demo/classify2d.html and repo: https://github.com/karpathy/convnetjs

(simple MNIST code example - tensorflow - https://github.com/aymericdamien/TensorFlow-Examples/blob/master/notebooks/3_NeuralNetworks/neural_network_raw.ipynb ) 

MNIST layer visualisation (tensorflow) https://medium.com/@awjuliani/visualizing-neural-network-layer-activation-tensorflow-tutorial-d45f8bf7bbc4 -  simple Python code, showing what each node sees for MNIST figure input; there is a 3d take on something similar at https://blog.terencebroad.com/archive/convnetvis/vis.html - change input at top (hover near top and offered 'press for new example') <- not overly useful?

There's also this MNIST interactive for writing a digit and recognising it https://bensonruan.com/handwritten-digit-recognition-with-tensorflow-js/ / https://github.com/bensonruan/Hand-Written-Digit-Recognition This has a Python trainer and then a js recogniser. We could maybe widgetise this? Interesting if we could then integrate one of the layer visualisers too?
Wrapped as server_proxy app: https://github.com/ouseful-PR/Hand-Written-Digit-Recognition/

https://pair.withgoogle.com/explorables/


scrollytelling https://web.archive.org/web/20180705105310/https://google-developers.appspot.com/machine-learning/crash-course/backprop-scroll/


http://demofox.org/NN2D.html https://blog.demofox.org/2017/02/07/a-geometric-interpretation-of-neural-networks/


V powerful visualisation but perhaps hard to use; may be worth an explanatory video? Or could we automate it somehow? Tensorspace.js visualise layers in 3d https://tensorspace.org/html/playground/index.html ( - Tensorspace could be interesting to play with; 
Platforms:


https://github.com/dv-fenix/NNVisualizer - streamlit also https://github.com/Joyoshish/Neural-Network-Visualiser-for-MNIST (seems to be from a coursera course?)


MNIST on a page - live training js https://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html 


- https://github.com/microsoft/tensorwatch teaser is interesting (pytorch) (MNIST, https://github.com/microsoft/tensorwatch/blob/master/notebooks/mnist.ipynb), fruit https://github.com/microsoft/tensorwatch/blob/master/notebooks/fruits_analysis.ipynb ). But how slow will this be? Works ish on MyBinder (slow; `%conda install pytorch cpuonly -c pytorch; %conda install pandas`) eg with MNIST; could we do a really simple training activity on small dataset and instrument it using Tensorwatch for better performance?

"Cool" web demos: https://teachablemachine.withgoogle.com/, https://openai.com/blog/microscope/, https://github.com/tensorflow/lucid (eg activation atlas)


