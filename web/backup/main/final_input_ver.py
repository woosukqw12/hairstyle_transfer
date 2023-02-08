import cv2
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import numpy as np

def Resize(Bg,sample): #얘 아직 안씀
    Board = cv2.imread('Board4.jpg')
    x = Board.shape[1]
    y = Board.shape[0] #퍼즐판의 xy좌표
    Boardsize = [x/9,y/7] #[퍼즐개수+1,퍼즐개수+1] 여기부분은 나중에 판 퍼
    sam = cv2.imread(sample)
    x1 = sam.shape[1]
    y1 = sam.shape[0] #퍼즐조각의 xy좌표
    fx = Boardsize[0]/x1#퍼즐1개가로길이/판의 퍼즐가로길이 해서 같은 1개의 퍼즐인데 픽셀차이나는것을 맞춰줄거임
    fy = Boardsize[1]/y1#동일
    shrinked_picture = cv2.resize(sam, None,fx=fx,fy=fy,interpolation=cv2.INTER_AREA)#fx,fy는 줄이는 비율
    #cv2.imshow('shrinked',shrink)
    #cv2.imshow('ori',Board)
    cv2.imwrite('main/static/edgesam.jpg',shrinked_picture)
    cv2.imwrite('edgesam.jpg',shrinked_picture)

def tmpMatching(bgString, String):
    img = cv2.imread(bgString)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #cvt == convert
    template = cv2.imread(String,0)#String들어간다
    
    #global img2 없어도 오류안생김
    ret, img2 = cv2.threshold(template,100,255,cv2.THRESH_BINARY)
    #cv2.imwrite('sample2.png',img2) 굳이 필요없을
    w, h = template.shape[::-1]
    #print(template.shape[::-1]) => (51,41)

    result = cv2.matchTemplate(imgray, img2, cv2.TM_CCOEFF_NORMED) #matchTemplate(InputArray image, InputArray templ, OutputArray result, int method)
    percent = result.max()

    loc = np.where(result >= percent) # -0.01안하면 안나옴
    if bgString == 'temsambg.jpg':
        loc = np.where(result >= percent-0.003)
    print(String)
    print(loc[::-1])

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,pt, (pt[0]+w, pt[1]+h), (255,57,95),10)
        
    cv2.imwrite('main/static/Resulted_'+String, img)
    cv2.imwrite('Resulted_'+String, img)

#===============================================================================
#위: 색상으로 판별 || 아래: edge detection이용 판별
#===============================================================================

def auto_canny(image, sigma=0.33):
    v = np.median(image)
 
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)

    print('lower: %d  upper: %d' % (lower, upper))
 
    # return the edged image
    return edged

def canny_run(BgImage, TmpImage):
    ##배경사진 디텍팅
    image = cv2.imread(BgImage) ####입력사진
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10, 200)
    auto = auto_canny(blurred)

    cv2.imwrite('Temsambg.jpg',auto) ####저장사진

    ##템플릿사진 디텍팅
    image = cv2.imread(TmpImage) ####입력사진
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10, 200)
    auto = auto_canny(blurred)

    cv2.imwrite('temsam.jpg',wide) ####저장사진

#######################################
#print('도움말: Board4 입력 ')
bg = 'Board4.jpg' #input() + '.jpg' #bg: 'Board4.jpg'
#######################################
def play(samname):
    bg = 'Board4.jpg' #임시
    #==============================
    #print('도움말: sam2 입력')
    print(samname)
    sam = samname
    #sam= input() + '.jpg' #sam: 'sam.jpg'
    Resize(bg, sam)

    ##배경사진 디텍팅
    image1 = cv2.imread(bg) ####입력사진
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10, 200)
    auto = auto_canny(blurred)

    cv2.imwrite('temsambg.jpg',auto) ####저장사진

    ##템플릿사진 디텍팅
    image2 = cv2.imread('edgesam.jpg') ####입력사진
    gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)

    wide = cv2.Canny(blurred, 10, 200)
    auto = auto_canny(blurred)

    cv2.imwrite('main/static/temsam.jpg',wide) ####저장사진
    cv2.imwrite('temsam.jpg',wide)

    #===============================================================================
    #TmpMatching
    #===============================================================================

    tmpMatching(bg, 'edgesam.jpg') #색상으로 판별 bg: 'Board4.jpg'
    tmpMatching('temsambg.jpg', 'temsam.jpg') #디텍팅이용판별

    #===============================================================================
    #결과 출력
    #===============================================================================
'''
    img1 = cv2.imread('Resulted_edgesam.jpg', cv2.IMREAD_COLOR)
    img2 = cv2.imread('Resulted_temsam.jpg', cv2.IMREAD_COLOR)

    b, g, r = cv2.split(img1)   # img파일을 b,g,r로 분리
    img3 = cv2.merge([r,g,b]) # b, r을 바꿔서 Merge
    b, g, r = cv2.split(img2)
    img4 = cv2.merge([r,g,b])

    plt.subplot(121),plt.imshow(img3,cmap = 'gray')
    plt.title('Color_detected'), plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img4,cmap = 'gray')
    plt.title('Edge_detected'), plt.xticks([]), plt.yticks([])
    plt.suptitle('Result')

    plt.show()
    print('finished')
'''
