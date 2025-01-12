from flask import Flask, render_template,Response
import cv2

#creating the app
app=Flask(__name__)

camera=cv2.VideoCapture(0) #this captures the video 
def generate_frames():
    while True:
        success,frame=camera.read()  #reading from the camera frame
        if not success:
            break
            
        else:
            ret,buffer=cv2.imencode('.jpeg',frame) #encoding the video
            frame=buffer.tobytes() #converts to bytes 
        yield(b'--frame\r\n' b'Content-Type: image\jpeg\r\n\r\n'+frame+b'\r\n') #returning the video


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')  #video functionality, returns the image
def video():
    return Response(generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__=='__main__':
    app.run(debug=True)
