import numpy as np
import cv2
import math


# หมุนภาพ เพื่อลดปัญหาข้อผิดพลาดในการตัดตัวอักษร
class Rotate:

    def __init__(self):
        print("Rotate")
        img = cv2.imread("xx3.png")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        (thresh, self.BinaryImg) = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)
        W_BkGd, H_BkGd = 500, 500

        # สร้างภาพสำรองเพื่อเพิ่มขนาดของภาพ
        backgroundImg = np.zeros((H_BkGd, W_BkGd), dtype=np.uint8)
        (thresh, self.BinaryImgbk) = cv2.threshold(backgroundImg, 140, 255, cv2.THRESH_BINARY_INV)
        H, W = self.BinaryImg.shape
        BinaryImg = self.BinaryImg[15:H, 0:W]

        # หาขอบอังษรและเพิ่มขนาดของขอบตัวอักษร
        Image_MorphologyEx = self.UpLetterTo_MorphologyEx(BinaryImg)

        # สร้างเส้นตรงจากตากตัวอักษร
        LineRotate = self.find_lines(Image_MorphologyEx)

        try:
            self.Rasp_rotate = True
            # การหาลักษณะของเส้นตรงว่าอยู่ในโซนใด โดยแบ่งเป็น 4 โซน
            zone0, zone1, zone2, zone3 = self.Zone(LineRotate[1])
            # การหาเส้นตรงว่าเอียงในลักษณะ ติดลบ และ บวก ซึ่งจะพิจจารณาจากโซนที่ได้
            self.Direction(zone0, zone1, zone2, zone3)
            # คำนวณหามุมจากเส้นตรงที่ได้
            self.angle = self.AngleProcess(LineRotate[1])
            print(self.angle)
            # เปลี่ยนลักษณะรูปตัวอักษร
            # ImageLetterUpEdge = self.UpEdge_Image(BinaryImg)
            # บริดภาพตัวอักษรจากมุมที่คำนวนได้
            # self.ImgRotate = self.Rotate(ImageLetterUpEdge)
            # ตัดบรรทัดจากรูปตัวอักษร
            # self.ImgLetterTime1 = self.DetecLetter2(self.ImgRotate)
            # cv2.imwrite("Output_Rotate/OutputRotate.png", self.ImgLetterTime1)


        except:
            print("ไม่เจอชื่อข้อมูล")
            self.Rasp_rotate = False

    def UpLetterTo_MorphologyEx(self, img):
        edged = cv2.Canny(img, 10, 250)
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
        closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
        (thresh, closed) = cv2.threshold(closed, 140, 255, cv2.THRESH_BINARY_INV)
        return closed

    def find_lines(self, img):
        H, W = img.shape
        edges = cv2.Canny(img, 100, 200)
        threshold = 60
        minLineLength = 10
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold, 0, minLineLength, 50);
        if (lines is None or len(lines) == 0):
            return
        for line in lines[0]:
            cv2.line(self.BinaryImgbk, (line[0], line[1]), (line[2], line[3]), (0, 255, 0), 2)
        cv2.line(img, (line[0], line[1]), (line[2], line[3]), (0, 255, 255), 2)
        Cutimg = self.CutArea_UpperLowwer(self.BinaryImgbk)
        Cutimg = self.CutArea_LeftRight(Cutimg)
        return img, Cutimg

    def Zone(self, img):
        img = self.CutArea_UpperLowwer(img)
        img = self.CutArea_LeftRight(img)
        H, W = img.shape
        X1 = int(W / 2) - 1
        X2 = int(W / 2) - 1
        X3 = int(W / 2) - 1
        X4 = int(W / 2) - 1

        Y1 = int(H / 2)
        Y2 = int(H / 2)
        Y3 = int(H / 2)
        Y4 = int(H / 2)

        scoreZone0 = 0
        scoreZone1 = 0
        scoreZone2 = 0
        scoreZone3 = 0
        for i1 in range(0, Y1, +1):
            for j1 in range(0, X1, +1):
                if img[i1][j1] == 0:
                    scoreZone0 += 1
        for i2 in range(0, Y2, +1):
            for j2 in range(X1, X1 + X2, +1):
                if img[i2][j2] == 0:
                    scoreZone1 += 1
        for i3 in range(Y1, H, +1):
            for j3 in range(0, X3, +1):
                if img[i3][j3] == 0:
                    scoreZone2 += 1
        for i4 in range(Y1, H, +1):
            for j4 in range(X1, W, +1):
                if img[i4][j4] == 0:
                    scoreZone3 += 1
        for i in range(0, H, +1):
            img[i][X1] = 0
        for j in range(0, W, +1):
            img[Y1][j] = 0
        return scoreZone0, scoreZone1, scoreZone2, scoreZone3

    def Direction(self, Z1, Z2, Z3, Z4):
        ArrayZone = [Z1, Z2, Z3, Z4]
        getMax = [0] * 2
        index = [0] * 2
        self.Clock = 0
        for j in range(0, ArrayZone.__len__(), +1):
            if ArrayZone[j] > getMax[0]:
                getMax[0] = ArrayZone[j]
                index[0] = j
        for i in range(0, ArrayZone.__len__(), +1):
            if i == index[0]:
                i += 1
            elif ArrayZone[i] > getMax[1]:
                getMax[1] = ArrayZone[i]
                index[1] = i
        if ((index[0] == 1) & (index[1] == 2)) | ((index[0] == 2) & (index[1] == 1)):
            self.Clock = -1
        else:
            self.Clock = 1

    def AngleProcess(self, imgLine):
        H, W = imgLine.shape
        pstUpper = 0
        pstLowwer = 0
        if self.Clock == -1:
            for j in range(0, W, +1):
                if imgLine[0][j] == 0:
                    pstUpper += j
                    break
            for i in range(0, H, +1):
                if imgLine[i][0] == 0:
                    pstLowwer += i
                    break
            if (H <= 5) and (pstUpper <= 2) and (pstLowwer <= 2):
                return 0
            else:
                Sum = (pstLowwer / pstUpper)
                agle = math.degrees(math.atan(Sum))
                return -agle
        else:
            for j in range(0, W, +1):
                if imgLine[H - 1][j] == 0:
                    pstUpper += j
                    break
            for i in range(0, H, +1):
                if imgLine[i][W - 1] == 0:
                    pstLowwer += i
                    break
            if (H <= 5) and (pstUpper <= 2) and (pstLowwer <= 2):
                return 0
            else:
                Sum = (pstLowwer / pstUpper)
                agle = math.degrees(math.atan(Sum))
                return agle

    def CutArea_LeftRight(self, imgArray):
        H, W = imgArray.shape
        SumPixel_Ver = np.array([H - (y / 255) for y in imgArray.sum(axis=0)])
        Position_Begin = 0
        Position_End = 0
        chk1 = False
        chk2 = False

        for i in range(0, SumPixel_Ver.__len__(), +1):
            if i == SumPixel_Ver.__len__() - 2:
                chk1 = True
                Position_Begin = 0
                break
            elif SumPixel_Ver[i] == 0:
                i = + 1
            else:
                Position_Begin = + i
                break

        for j in range(SumPixel_Ver.__len__(), 0, -1):
            if j == 1:
                chk2 = True
                Position_End = SumPixel_Ver.__len__()
                break

            if SumPixel_Ver[j - 1] == 0:
                j = +1
            else:
                Position_End = +j
                break
        NewImg_CutLeftRight = imgArray[0:H, Position_Begin:Position_End]

        if (chk1 == True) & (chk2 == True):
            self.CheckLetterInImge = False
        return NewImg_CutLeftRight

    def CutArea_UpperLowwer(self, imgArray):
        H, W = imgArray.shape
        SumPixel_Horizontal = np.array([W - (y / 255) for y in imgArray.sum(axis=1)])
        Position_Begin = 0
        Position_End = 0

        for i in range(0, SumPixel_Horizontal.__len__(), +1):
            if i == SumPixel_Horizontal.__len__() - 1:
                Position_Begin = 0
                break
            elif SumPixel_Horizontal[i] == 0:
                i = +1
            else:
                Position_Begin = + i
                break

        for j in range(SumPixel_Horizontal.__len__(), 0, -1):
            if j == 1:
                Position_End = SumPixel_Horizontal.__len__()
                break
            if SumPixel_Horizontal[j - 1] == 0:
                j = +1
            else:
                Position_End = +j
                break
        NewImg = imgArray[Position_Begin:Position_End, 0:W]

        return NewImg

    # def UpEdge_Image(self, img):
    #     W_BkGd, H_BkGd = 800, 600
    #     backgroundImg = np.zeros((H_BkGd, W_BkGd), dtype=np.uint8)
    #     (thresh, BinaryImgbk) = cv2.threshold(backgroundImg, 140, 255, cv2.THRESH_BINARY_INV)
    #     Hbk, Wbk = BinaryImgbk.shape
    #     PstY = int(Hbk / 5)
    #     PstX = int(Wbk / 20)
    #     H, W = img.shape
    #     for i in range(0, H, +1):
    #         for j in range(0, W, +1):
    #             BinaryImgbk[i + PstY][j + PstX] = img[i][j]
    #     return BinaryImgbk
    # def Rotate(self, ImageLetterUpEdge):
    #
    #     (h, w) = ImageLetterUpEdge.shape[:2]
    #     center = (w // 2, h // 2)
    #     M = cv2.getRotationMatrix2D(center, self.angle, 1.0)
    #     rotated = cv2.warpAffine(ImageLetterUpEdge, M, (w, h), flags=cv2.INTER_CUBIC,
    #                              borderMode=cv2.BORDER_REPLICATE)
    #     (thresh, BinaryImg) = cv2.threshold(rotated, 140, 255, cv2.THRESH_BINARY)
    #     return BinaryImg



    # def DetecLetter2(self, img):
    #     img = self.CutArea_UpperLowwer(img)
    #     # กำจัดสิ่งแปลกปลอม
    #     img = self.DetecNois(img)
    #     H, W = img.shape
    #     SumPixel = np.array([W - (y / 255) for y in img.sum(axis=1)])
    #     ScoreNois = 0
    #     fist = 0
    #     end = 0
    #     loop = True
    #     checkLine = 0
    #     getDetecLetter = []
    #     getAllLetterLine = []
    #     ZeroPixelNois = 0
    #
    #     while loop:
    #         for i in range(fist, SumPixel.__len__(), +1):
    #             if i == SumPixel.__len__() - 1:
    #                 end += SumPixel.__len__() - 1
    #                 loop = False
    #                 break
    #             if SumPixel[i] != 0:
    #                 if (ScoreNois >= 1) & (ScoreNois <= 5):
    #                     i += ScoreNois - 1
    #                     ScoreNois = 0
    #                 elif ScoreNois >= 6:
    #                     end += i - ScoreNois
    #                     checkLine = i
    #                     break
    #                 i += 1
    #                 ZeroPixelNois += 1
    #             if SumPixel[i] == 0:
    #                 ScoreNois += 1
    #         imgg = img[fist:end, 0:W]
    #         getAllLetterLine.append(imgg)
    #         pst = [fist, end]
    #         Hdt, Wdt = imgg.shape
    #         SumPixel_CheckDepth = np.array([Wdt - (y / 255) for y in imgg.sum(axis=1)])
    #         ScoreDepth = 0
    #         for i_Depth in range(0, SumPixel_CheckDepth.__len__(), +1):
    #             ScoreDepth += SumPixel_CheckDepth[i_Depth]
    #         Raspone = [ScoreDepth, pst]
    #         getDetecLetter.append(Raspone)
    #         if end <= SumPixel.__len__() - 5:
    #             fist = checkLine
    #             ScoreNois = 0
    #             end = 0
    #         elif end >= SumPixel.__len__() - 5:
    #             end = SumPixel.__len__() - 5
    #             loop = False
    #     getDepthSumpixelLetter = []
    #     getIndex = []
    #     getImg = []
    #     for i_sr in range(0, getDetecLetter.__len__(), +1):
    #         if (getDetecLetter[i_sr][0] >= 800) & (getDetecLetter[i_sr][1][0] == 0):
    #             getIndex.append(i_sr)
    #             sum = [getDetecLetter[i_sr][0], getDetecLetter[i_sr][1]]
    #             getDepthSumpixelLetter.append(sum)
    #             getImg.append(getAllLetterLine[i_sr])
    #     try:
    #         return getImg[0]
    #     except:
    #         for i_sr in range(0, getDetecLetter.__len__(), +1):
    #             if (getDetecLetter[i_sr][0] >= 800):
    #                 getIndex.append(i_sr)
    #                 sum = [getDetecLetter[i_sr][0], getDetecLetter[i_sr][1]]
    #                 getDepthSumpixelLetter.append(sum)
    #                 getImg.append(getAllLetterLine[i_sr])
    #                 break
    #         return getImg[0]

    # def DetecNois(self, img):
    #     H, W = img.shape
    #     SumPixel = np.array([W - (y / 255) for y in img.sum(axis=1)])
    #     Nois = 0
    #     self.fistNois = 0
    #     self.endNois = 0
    #     PstPixelZero = []
    #     swicth1 = True
    #     getNois = [0, 0]
    #     for i in range(0, SumPixel.__len__(), +1):
    #         if SumPixel[i] != 0:
    #             if i == SumPixel.__len__() - 1:
    #                 self.endNois = SumPixel.__len__()
    #                 getNois = [self.fistNois, self.endNois]
    #                 PstPixelZero.append(getNois)
    #             elif swicth1 == True:
    #                 self.fistNois = i
    #                 swicth1 = False
    #         elif SumPixel[i] == 0:
    #             if swicth1 == False:
    #                 self.endNois = i
    #                 getNois = [self.fistNois, self.endNois]
    #                 PstPixelZero.append(getNois)
    #                 swicth1 = True
    #     indexDel = []
    #     for st in range(0, PstPixelZero.__len__(), +1):
    #         Sum = PstPixelZero[st][1] - PstPixelZero[st][0]
    #         if Sum <= 5:
    #             indexDel.append(st)
    #     countDel = 0
    #     for i_del in range(0, indexDel.__len__(), +1):
    #         PstPixelZero.pop(indexDel[i_del] - countDel)
    #         countDel += 1
    #     fist = PstPixelZero[0][0]
    #     length = len(PstPixelZero) - 1
    #     end = PstPixelZero[length][1]
    #     imgg = img[fist:end, 0:W]
    #     return imgg
    #



Rotate()

