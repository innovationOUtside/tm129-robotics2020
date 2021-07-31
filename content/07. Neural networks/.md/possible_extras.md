---
jupyter:
  jupytext:
    cell_metadata_filter: -all
    formats: ipynb,.md//md
    main_language: python
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.11.4
---

NOTES - anyhting we can pull outof these? 

[Tools for visualising networks](https://github.com/ashishpatel26/Tools-to-Design-or-Visualize-Architecture-of-Neural-Network)

Single layer perceptron trainer - https://github.com/niinpatel/Single-Layer-Perceptron/ Could be useful to fork / extend; eg show weights?

Convolutional net - stepwise https://github.com/vicolab/neural-network-intro/blob/master/3-convnet/convolutional-network.ipynb

Observable MNIST demo https://observablehq.com/@tpreusse/interactive-convolutional-neural-network

Network structure visualisation: https://github.com/voletiv/myPythonNeuralNetwork (1_Neural_Network_Tutorial_Visualizations.ipynb); my own cribbed structure visualiser https://github.com/jarusgnuj/ioctm358/blob/TH-fn-to-plot-NN/notebooks/py/draw_neural_net.py

Simple interactives: [perceptrons](https://github.com/trsvchn/interactive-perceptrons) - possibly useful with explanation, but not very responsive? Some explanation of perceptron as logic blocks: https://medium.com/@stanleydukor/neural-representation-of-and-or-not-xor-and-xnor-logic-gates-perceptron-algorithm-b0275375fea1 ;  How about building using ipywidgets? There's also a simple weight visualiser with table inputs here: http://jalammar.github.io/feedforward-neural-networks-visual-interactive/#prediction-calculation Could be interesting if we also had weight sliders? What does that data look like on a scatter plot?

(simple MNIST code example - tensorflow - https://github.com/aymericdamien/TensorFlow-Examples/blob/master/notebooks/3_NeuralNetworks/neural_network_raw.ipynb ) 

MNIST layer visualisation (tensorflow) https://medium.com/@awjuliani/visualizing-neural-network-layer-activation-tensorflow-tutorial-d45f8bf7bbc4 -  simple Python code, showing what each node sees for MNIST figure input; there is a 3d take on something similar at https://blog.terencebroad.com/archive/convnetvis/vis.html - change input at top (hover near top and offered 'press for new example') <- not overly useful?


https://pair.withgoogle.com/explorables/

scrollytelling https://web.archive.org/web/20180705105310/https://google-developers.appspot.com/machine-learning/crash-course/backprop-scroll/

http://demofox.org/NN2D.html https://blog.demofox.org/2017/02/07/a-geometric-interpretation-of-neural-networks/

V powerful visualisation but perhaps hard to use; may be worth an explanatory video? Or could we automate it somehow? Tensorspace.js visualise layers in 3d https://tensorspace.org/html/playground/index.html ( - Tensorspace could be interesting to play with; 


https://github.com/dv-fenix/NNVisualizer - streamlit also https://github.com/Joyoshish/Neural-Network-Visualiser-for-MNIST (seems to be from a coursera course?)

- https://github.com/microsoft/tensorwatch teaser is interesting (pytorch) (MNIST, https://github.com/microsoft/tensorwatch/blob/master/notebooks/mnist.ipynb), fruit https://github.com/microsoft/tensorwatch/blob/master/notebooks/fruits_analysis.ipynb ). But how slow will this be? Works ish on MyBinder (slow; `%conda install pytorch cpuonly -c pytorch; %conda install pandas`) eg with MNIST; could we do a really simple training activity on small dataset and instrument it using Tensorwatch for better performance?

"Cool" web demos: https://teachablemachine.withgoogle.com/, https://openai.com/blog/microscope/, https://github.com/tensorflow/lucid (eg activation atlas)

