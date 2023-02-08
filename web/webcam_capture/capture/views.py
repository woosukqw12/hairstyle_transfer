from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip
import cv2
import threading

# Create your views here.
def index(request):
    return render(request, 'capture/base.html')
    return HttpResponse("Hello! ")
@csrf_exempt
def page1(request):
    #return HttpResponse("Hello! ")
    return render(request, 'capture/page1.html')
@csrf_exempt
def page2(request):
    photo1  = "../source.jpg"
    photo2 = "../target.jpg"
    return render(request, 'capture/page2.html', {'source': photo1, 'target': photo2})

#카메라 관련 클래스
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


def gen(camera):
    while True:
        frame = camera.get_frame()
        # frame단위로 이미지를 계속 반환한다. (yield)
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


# detectme를 띄우는 코드(여기서 웹캠을 킨다.)
@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera() #웹캠 호출
        # frame단위로 이미지를 계속 송출한다
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        print("에러입니다...")
        pass