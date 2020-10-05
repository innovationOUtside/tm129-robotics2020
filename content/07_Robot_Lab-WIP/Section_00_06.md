---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.1
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# 6 Using a convolutional neural network to recognise images

In the previous notebooks, you saw how a neural network could partition points arranged in a two-dimensional space into distinct groups. In this notebook, you will explore how a neural network can be trained to recognise a variety of images, each of which is represented as a shape that extends across the whole extent of two dimensional space.

The dataset you will use is the MNIST database that you met in an earlier notebook.

Run the following cell to load in a simple interactive application that should be able to recognise a handwritten digit. Click in the canvas area, then with your mouse button held down, write a single digit in the range 0 to 9, then click on the *Predict* button. Does it recognise the digit correctly? Press the *Clear* button to clear the canvas and have another go.

*(The application may take a minute or two completely load because it needs to load a large model file into the browser. If it doesn't recognise your digit at first, wait a few moments and then try again. If for some reason it doesn't work at all, or the application doesn't display, then try the original version on the web here](https://bensonruan.com/handwritten-digit-recognition-with-tensorflow-js/).)* 

<font color='red'>JD: The following doesn't work (as there's no such file `nb_handwritten_digit` in this directory).</font>

```python
url='./nb_handwritten_digit/" width=500 height=300'

from IPython.display import IFrame
IFrame(url, width='100%', height=300)
```

## 6.1 Convolutional neural networks

Whilst an MLP can cope with distinguishing digits as a result of training on the MNIST handwritten digits datasets, it starts to struggle with more complex image recognition tasks.

In recent years, a different neural network model that is ideally suited to image recognition problems, has come to the fore. Known as a *convolutional neural network* (CNN), we will not explore its architecture in any formal way, other than to note a couple of differences to the MLP architecture.

In the first case, whereas the multi-layer perceptron is a fully connected network, the CNN is only sparsely connected.

In the second case, an MLP would typically present an image to a network in the form of a single column vector equal to the size of the the image in pixels, with each input pixel connected to every node in the first hidden layer. This means that every node in the first hidden layer sees every pixel in the image, no matter how far apart they are.

In a CNN, a smaller grid is used to filter localised areas of the image, preserving information about the local relationship between certain pixels. As we go deeper into the CNN's hidden layer, this filtering structure repeats, with each neuron only seeing outputs from a selection of neighbouring nodes in the previous layer.

Something else may also notice in what follows is the word "tensor" appearing again. A *tensor* is a multidimensional array of numbers (often, a *large* multidimensional array) and it hints at how the data is passed into, and flows through, a network. That is about as much as I'm going to tell you for the purposes of this module. If you want to know more, [T194 Engineering: mathematics, modelling, applications](http://www.open.ac.uk/courses/modules/t194) starts you on a gentle path by introducing the idea of matrices, ideas which are further developed in [MST210 Mathematical methods, models and modelling](http://www.open.ac.uk/courses/modules/mst210) (It's not for no reason that a lot of people who work with neural networks have a strong background in mathematics.) The third level module *TM358 Machine learning and artificial intelligence* looks in more detail about the machine-learning relevance.


## 6.2 Training a hand-written digit recogniser

Several researchers have created interactive, browser based demonstrations that are capable of training a neural network to recognise the MNIST digits.

The underlying code – and text – for these is licensed under an open license, which means we can redistribute them, and even edit the original versions, with due acknowledgement. Click on the first link in each list item to open the activity (or the second link if you are running this notebook on MyBinder).


<font color='red'>JD: Update links depending on how students will use/install the notebooks:</font>

- [__ConvNetJS MNIST demo__](./convnet_mnist/) [on MyBinder user [__this link__](../../../convnet_mnist/); the *OU installation* package can be found here: [`innovationOUtside/serverproxy_convnet_mnist`](https://github.com/innovationOUtside/serverproxy_convnet_mnist)]: this is fascinating example of training a network in the web browser using a Javascript based neural network package, and visualising the the effects as the network trains. The training should start automatically a moment or two after the pages loads. If you scroll down in the page, you will see in real time how the performance of the network improves as it is trained. It was originally developed by Andrej Karpathy whilst he was a PhD student at Stanford University. If you would like to visit the original, it is still available [here](https://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html).

- [__walked through training example__](./tfjs_mnist/) [on MyBinder user [__this link__](../../../tfjs_mnist/); the *OU installation* package can be found here: [`innovationOUtside/serverproxy_tfjs_demos`](https://github.com/innovationOUtside/serverproxy_tfjs_demos)]: this example is taken from the *tensorflow.js* "tfjs-vis" demos ([code](https://github.com/tensorflow/tfjs/tree/master/tfjs-vis); [original demo](https://storage.googleapis.com/tfjs-vis/mnist/dist/index.html)). It walks you through an example of training a neural network to recognise the MNIST digits, showing how the error value reduces over time.

Spend a few minutes looking through each of the demos. There is too much detail for us to review in this module, but it may give you a taste of what working with machine learning models at a technical level involves.


## 6.3 Inside the mind of a convolutional neural network MNIST handwritten digit recogniser

This final demonstration is an example of a three-dimensional interactive visualisation that allows you to explore how the a convolutional neural network filters certain features of an input image: [TensorSpace Playground - interaction guide](./nb_tensorspace_playground/) [on MyBinder, use [this link](../../../nb_tensorspace_playground/)].

- [TensorSpace Playground - trained MNIST demo](./nb_tensorspace_playground/LeNet/) [on MyBinder, use [this link](../../../nb_tensorspace_playground/LeNet/)]: in this first example, you can explore a trained network, providing your own hand written digit as an input to the network and then peering inside the network to see how it encodes, then decodes, various features in making its decision;
- [TensorSpace Playground - training demo](./nb_tensorspace_playground/LeNetTraining/) [on MyBinder, use [this link](../../../nb_tensorspace_playground/LeNetTraining/)]: in this example (which could take a few seconds to load the necessary training data before it will run) you can load a test example in, then reset and train the network. You know the network is being trained if you can see the *Training Metrics* values updating. If you look at the output layer of the network then you can see the network start to home in on the correct output result as the network is trained.


## 6.4 Summary

In this notebook, you have seen how we can train a different sort of neural network to the MLP, known as a convolutional neural network (CNN), to recognise handwritten images from a set of training examples. You have also had a peak inside the mind of such a network, exploring how each of the nodes in each of the layers recognises (and essentially looks for and ‘sees’ different abstract patterns of features in the input, before the network as a whole uses these recognisable (though not necessarily visually meaningful, to us at least) patterns to come to a decision about what the input image represents.

If you had to write a set of explicit, handwritten rules to perform such a discrimination task, I think you would find it very challenging indeed. But whilst we can see that each node of the network is recognising *something*, it may not be obvious to us what it is in any human meaningful way.
