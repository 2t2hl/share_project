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
```
###### Next, clone the repo:
```javascript
$ git clone https://github.com/jrosebr1/simple-keras-rest-api.git
```

###### Run to build server
```javascript
python run_keras_server.py
```
