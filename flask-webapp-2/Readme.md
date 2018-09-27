###### Asume you have anaconda, then run below command to create development environtment.
```javascript
conda create --name flask-webapp python==3.6
```

###### To activate this environment, use:
```javascript
source activate flask-webapp
```
###### To deactivate an active environment, use:
```javascript
source deactivate
```
###### Install keras and the relevent library
```javascript
pip install keras
pip install tensorflow
pip install flask gevent requests pillow
pip install sklearn
```

###### Run to build server
```javascript
python app.py
```
###### Reference URL
https://www.pyimagesearch.com/2018/01/29/scalable-keras-deep-learning-rest-api/