# Image Caption WebApp Using Flask-Bootstrap
### share_project: Flask project
Made by Trinh, Thu, Hung, Huy and Luc

## Experiment
[!title](/image/experiment.png)

##Dependencies
* Python3
* Flask-Bootstrap
* Tensorflow
* Requests

## Installing

### Step 1: Clone this git
	
> git clone https://github.com/2t2hl/share_project/tree/master/ImageCaptionWebApp
> cd ImageCaptionWebApp

### Step 2: Install environment

> pip install -r requirements.txt

### Step 3: Dowbload Vocabulary dict and pretrained model
[Vocabulary](https://raw.githubusercontent.com/ColeMurray/medium-show-and-tell-caption-generator/master/etc/word_counts.txt)
[Pretrained Model](https://drive.google.com/uc?export=download&id=15Juh0gaYR0qv8GjRL1EvsigErdQXTmnt)

* And then, let's move **word_counts.txt** to data folder and **show-and-tell.pb** to models folder (both of them at ImageCaptionWebApp)

### Step 4: Run Web App (I recommend we should run app on virtual Env )

> python3 inference.py

## Reference

[Deploy Keras Model with Flask as Web App in 10 Minutes](https://github.com/mtobeiyf/keras-flask-deploy-webapp)


