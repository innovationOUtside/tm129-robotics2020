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

In this session, you will get hands-on experience of using a variety of neural networks, and you will build and train neural networks to perform specific tasks.


<!-- #region activity=true -->
## Activity — Recognising A Static Pose in An Image

As well as tagging images, properly trained models can recognise individual people's faces in photos (and not just of celebrities!) and human poses within a photograph.

Click through to the following web location to see an example of a netural network model running in your web browser to the recognise the pose of several different people across a set of images: https://pose-animator-demo.firebaseapp.com/static_image.html


<!-- #endregion -->

<!-- #region tags=["todo", "alter-danger"] -->
TO DO - Add a local example with additional ability to upload your own photo.
<!-- #endregion -->

<!-- #region activity=true -->
## Optional Activity — Distinguishing Between Two Of Your Own Poses From a Live Video Feed
Although is can take *a lot* of data and *a lot* of computational effort to train a model, topping up a model with transfer learning applied to a previously trained model can be achieved quite simply.

This optional activity allows you to top-up a pre-trained model to recognise of an image of you with your hand raised, and an image of you without you hand raised. Feeding a live image into the model allows it to detect in real time whether you have your hand or arm raised or not.

__ TO DO _ need to package this as a jupyter_server_proxy thing.__
__`demo-video-arm-pose` dir__

*This activity requires that you have a camera attached to your computer and that your web browser has permission access the camera feed. The captured images do not leave your computer.*
<!-- #endregion -->

<!-- #region activity=true -->
## Optional Activity — Training Your Own Image or Audio Classifier


If you have a camera or microphone attached to your computer, the following activity will show you how you can top-up a pre-trained model to distinguish between two or more categories of image or sound of your own devising:

- upload your own images (or capture some images from a camera attached to your computer) and assign them to two or more categories you have defined yourself, then train the model to distinguish between them: https://teachablemachine.withgoogle.com/train/image

- upload your own audio files (or capture some audio from a microphone attached to your computer) and assign them to two or more categories you have defined yourself, then train the model to distinguish between them: https://teachablemachine.withgoogle.com/train/audio
<!-- #endregion -->

## Summary

In this notebook you have seen how we can use a third party application to recognise different objects within an image and return human readable labels that can be used to "tag" the image. These applications use large, pretrained neural networks to perform the object recognition task.

You have also seen how we can take a pretrained neural network model and use an approach called *transfer learning* "top it up" with a bit of extra learning so that it recognises particular sorts of different between two classes of input image that we have provided it with.

In the next set of activities, you will have an opportunity to train your own neural netwrok, from scratch, on a simple classification task.