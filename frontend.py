import time
from wx import *
import backend


# ------------- 화면 패널 -------------
# 시작 화면
class startPanel(Panel):

    def __init__(self, parent):
        Panel.__init__(self, parent=parent)
        self.titleImage = Bitmap("resources/title.jpg")
        self.Bind(EVT_PAINT, self.onPaint)

        # 게임 시작, 종료 버튼
        self.startButton = Button(self, label="시작")
        self.startButton.SetSize((100, 50))
        self.startButton.SetPosition((360, 380))
        self.endButton = Button(self, label="종료")
        self.endButton.SetSize((100, 50))
        self.endButton.SetPosition((360, 430))

    # 별도의 시작 화면 파일을 불러와 화면에 그려냈음
    def onPaint(self, event):
        dc = PaintDC(self)
        dc.DrawBitmap(self.titleImage, 0, 0)


# 게임 진행 화면
class gamePanel(Panel):
    # 기본적인 게임 화면 구성
    def __init__(self, parent):

        global stage, life
        Panel.__init__(self, parent=parent)
        # self.lifeImage = Bitmap("resources/life.png")
        self.SetBackgroundColour(Colour(255, 255, 255, 3))

        # 백엔드를 활용한 이미지 및 틀린그림찾기 정보 초기화
        self.imageNum = 0
        self.answerPoints = []
        self.path = images[0]
        self.image, self.answerPoints, self.t = backend.get_next_quiz(self.path)
        self.pointsCenter = backend.get_pts_center(self.answerPoints)
        self.gameImage = StaticBitmap(self, -1, backend.create_wx_bitmap(self.image), (0, 0))

        # 게임 인터페이스(스테이지, 목숨 수)
        self.font = Font(FontInfo(32).AntiAliased(True).FaceName("NanumGothic"))
        self.SetFont(self.font)
        self.stageString = StaticText(self, -1, "Stage " + str(stage), (5, 0))
        self.lifeString = StaticText(self, -1, "Life : " + ("♥" * life), (585, 0))

        # 비트맵 대신 text label로 구현했음
        # self.Bind(EVT_PAINT, self.paintUI)

    # 목숨 수를 하트 모양 비트맵으로 표현
    def paintUI(self, event):
        pass
        # global life
        # image = backend.create_wx_bitmap(self.image)
        # self.gameImage.SetBitmap(image)
        # dc = PaintDC(self)
        # dc.Clear()
        # dc.DrawBitmap(image, 0, 0)
        # for i in range(life+1) :
        #   dc.DrawBitmap(self.lifeImage, (784-50*i, 0))

    # 처음 실행 후 게임 시작, 게임 오버 후 게임 초기화 후 다시 시작
    def resetAndStartGame(self):

        # 전역 변수 초기화
        global stage, answerCount, life, goalCount
        stage = 1
        answerCount = 0
        life = 3
        images = backend.load_images()

        # 이미지 정보 초기화
        self.imageNum = 0
        self.answerPoints = []
        self.path = images[0]
        self.image, self.answerPoints, self.t = backend.get_next_quiz(self.path)
        self.pointsCenter = backend.get_pts_center(self.answerPoints)

        # 틀린 부분이 3개를 초과할 경우 3개로 고정
        goalCount = len(self.pointsCenter)
        if goalCount > 3:
            goalCount = 3

        # 화면 표시
        self.gameImage.SetBitmap(backend.create_wx_bitmap(self.image))
        self.stageString.SetLabel("Stage " + str(stage))
        self.stageString.Hide()
        self.stageString.Show()
        self.lifeString.SetLabel("Life : " + ("♥" * life))
        self.lifeString.Hide()
        self.lifeString.Show()

    # 클리어 시 다음 스테이지로 넘어가는 과정 처리
    def goToNextStage(self):

        # 목숨, 정답 개수 초기화
        global stage, answerCount, life, goalCount
        life = 3
        answerCount = 0

        # 다음 이미지 정보 불러오기
        self.imageNum += 1
        self.path = images[self.imageNum]
        self.image, self.answerPoints, self.t = backend.get_next_quiz(self.path)
        self.pointsCenter = backend.get_pts_center(self.answerPoints)

        # 틀린 부분이 3개를 초과할 경우 3개로 고정
        goalCount = len(self.pointsCenter)
        if goalCount > 3:
            goalCount = 3

        # 화면 표시
        self.gameImage.SetBitmap(backend.create_wx_bitmap(self.image))
        self.stageString.SetLabel("Stage " + str(stage))
        self.lifeString.SetLabel("Life : " + ("♥" * life))
        self.gameImage.Hide()
        self.gameImage.Show()


# 게임 결과 화면
class gameOverPanel(Panel):

    def __init__(self, parent):
        Panel.__init__(self, parent=parent)
        self.resultImage = Bitmap("resources/gameover.jpg")
        self.Bind(EVT_PAINT, self.onPaint)

        # 시작 화면으로 돌아가기, 종료 버튼
        self.returnToStartButton = Button(self, label="돌아가기")
        self.returnToStartButton.SetSize((100, 50))
        self.returnToStartButton.SetPosition((360, 380))
        self.endButton = Button(self, label="종료")
        self.endButton.SetSize((100, 50))
        self.endButton.SetPosition((360, 430))

    # 별도의 게임 오버 화면 파일을 불러와 화면에 그려냈음
    def onPaint(self, event):
        dc = PaintDC(self)
        dc.DrawBitmap(self.resultImage, 0, 0)


# 게임 결과 화면
class clearPanel(Panel):

    def __init__(self, parent):
        Panel.__init__(self, parent=parent)
        self.resultImage = Bitmap("resources/clear.jpg")
        self.Bind(EVT_PAINT, self.onPaint)

        # 게임 오버 화면 버튼과 같음
        self.returnToStartButton = Button(self, label="돌아가기")
        self.returnToStartButton.SetSize((100, 50))
        self.returnToStartButton.SetPosition((360, 380))
        self.endButton = Button(self, label="종료")
        self.endButton.SetSize((100, 50))
        self.endButton.SetPosition((360, 430))

    # 별도의 클리어 화면 파일을 불러와 화면에 그려냈음
    def onPaint(self, event):
        dc = PaintDC(self)
        dc.DrawBitmap(self.resultImage, 0, 0)


# 각 패널들이 표시되는 윈도우 프레임
class mainFrame(Frame):

    def __init__(self):

        # 창 초기화(최대화, 크기 변경 불가)
        Frame.__init__(self, None, ID_ANY, "틀린그림찾기", size=(825, 650),
                       style=DEFAULT_FRAME_STYLE & ~RESIZE_BORDER & ~MAXIMIZE_BOX)

        # 정답 시 원을 그려주기 위한 동그라미 그림
        # self.circle = Image("resources/circle.png", BITMAP_TYPE_ANY)

        # 화면에 표시되는 패널 초기화
        self.startPanel = startPanel(self)
        self.gamePanel = gamePanel(self)
        self.gameOverPanel = gameOverPanel(self)
        self.clearPanel = clearPanel(self)
        self.gamePanel.Hide()
        self.gameOverPanel.Hide()
        self.clearPanel.Hide()

        # 패널을 한 sizer에 추가하여 관리
        self.sizer = BoxSizer(VERTICAL)
        self.sizer.Add(self.startPanel, 1, EXPAND)
        self.sizer.Add(self.gamePanel, 1, EXPAND)
        self.sizer.Add(self.gameOverPanel, 1, EXPAND)
        self.sizer.Add(self.clearPanel, 1, EXPAND)
        self.SetSizer(self.sizer)

        # 각종 버튼 작동 기능 할당
        self.startPanel.endButton.Bind(EVT_BUTTON, self.closeGame)
        self.startPanel.startButton.Bind(EVT_BUTTON, self.startGame)
        self.gameOverPanel.returnToStartButton.Bind(EVT_BUTTON, self.returnToStart)
        self.gameOverPanel.endButton.Bind(EVT_BUTTON, self.closeGame)
        self.clearPanel.returnToStartButton.Bind(EVT_BUTTON, self.returnToStart)
        self.clearPanel.endButton.Bind(EVT_BUTTON, self.closeGame)

        # 이미지를 왼쪽 마우스로 클릭하여 게임 진행 처리
        self.gamePanel.gameImage.Bind(EVT_LEFT_DOWN, self.gameProgress)

        # 정오답 및 결과를 알려주는 상태 바
        self.statusBar = StatusBar(self)
        self.SetStatusBar(self.statusBar)
        self.statusBar.Hide()

    # 게임 진행 처리
    def gameProgress(self, event):

        global stage, answerCount, life, goalCount
        # 유클리드 좌표계 거리로 정답 좌표가 30 이내일때 정답으로 처리
        maxDistance = 30 * 30
        # 정답 오답 처리를 위한 변수
        isCorrect = False

        # 정답 찾는 과정
        # 정답의 중점 좌표를 활용
        # 이미지 처리 과정에서 이미지가 이동한 값 t를 이용하여 좌표 보정
        pointsCenter = self.gamePanel.pointsCenter
        (x, y) = (event.x - self.gamePanel.t[0], event.y - self.gamePanel.t[1])

        for point in pointsCenter:
            interval = backend.interval
            # 원본 그림과 틀린 그림 둘 다 확인
            x1 = point[0] - x
            y1 = point[1] - y
            x2 = point[0] + 400 - x + interval
            y2 = point[1] - y + interval

            d1 = x1 * x1 + y1 * y1
            d2 = x2 * x2 + y2 * y2

            if d1 <= maxDistance or d2 <= maxDistance:
                # 정답인 경우 정답으로 처리하고, 이미 정답으로 확인했다는 값 설정
                # 정답 확인 값은 pointsCenter의 마지막 원소로 저장되어 있음
                # 클릭하여 정답으로 처리한 적 있는 좌표면 1, 아닐시 0
                isCorrect = True
                if point[2] == 0:
                    answerCount += 1
                    point[2] = 1

                    # 정답일 시 상태 바의 표시 변경
                    self.statusBar.SetStatusText("정답입니다. 앞으로 %d개 남았습니다."
                                                 % (goalCount - answerCount))

                    # 화면에 원 그리기 (미구현, 상태 바로 대체)
                    # StaticBitmap(self, -1, self.circle.ConvertToBitmap(), ((point[0] +400 - 32), (point[1] + 32)))

                # 이미 정답으로 처리된 좌표 처리
                else:
                    self.statusBar.SetStatusText("이미 정답으로 찾아낸 곳입니다.")
            else:
                continue

        # 오답 처리
        if not isCorrect:
            # 목숨 감소 및 상태 바, 화면 업데이트
            life -= 1
            self.statusBar.SetStatusText("오답입니다.")
            self.gamePanel.lifeString.SetLabel("Life : " + ("♥" * life))
            self.gamePanel.stageString.Hide()
            self.gamePanel.stageString.Show()

            # 게임 오버 시 처리
            if life == 0:
                # 전체 정답 공개(화면 확장 및 이미지 업데이트)
                time.sleep(1)
                self.statusBar.SetStatusText("게임 오버입니다. 전체 정답을 공개합니다.")
                self.SetSize(1220, 650)
                self.gamePanel.gameImage.SetBitmap(backend.create_wx_bitmap(self.gamePanel.image))
                time.sleep(3)

                # 게임 오버 화면으로 이동
                self.showGameover(self)
                self.SetSize(825, 650)

        # 3개를 찾았을 시 다음 스테이지로 이동에 대한 처리
        if answerCount == goalCount:
            # 전체 정답 공개(화면 확장 및 이미지 업데이트)
            time.sleep(1)
            self.SetSize(1220, 650)
            self.gamePanel.gameImage.SetBitmap(backend.create_wx_bitmap(self.gamePanel.image))
            self.statusBar.SetStatusText("3개를 찾았습니다! 전체 정답을 공개합니다.")
            stage += 1
            time.sleep(3)

            # 다음 스테이지로 넘어감
            # 모든 스테이지를 클리어 했을 시 클리어 화면으로 변경
            if stage > len(images):
                self.statusBar.SetStatusText("모든 스테이지를 클리어했습니다! 3초 후 클리어 화면이 출력됩니다.")
                time.sleep(3)
                self.showClear(self)
            else:
                self.gamePanel.goToNextStage()
                self.statusBar.SetStatusText("다음 문제 로드 완료")
            self.SetSize(825, 650)

    # 시작 버튼을 눌렀을 때
    def startGame(self, event):
        self.gamePanel.resetAndStartGame()
        self.startPanel.Hide()
        self.gamePanel.Show()
        self.statusBar.Show()
        self.Layout()

    # 게임 오버 화면 전환
    def showGameover(self, event):
        self.gamePanel.Hide()
        self.gameOverPanel.Show()
        self.statusBar.Hide()
        self.Layout()

    # 클리어 화면 전환
    def showClear(self, event):
        self.gamePanel.Hide()
        self.clearPanel.Show()
        self.statusBar.Hide()
        self.Layout()

    # 시작 화면으로 돌아가기(게임 오버, 클리어 공통)
    def returnToStart(self, event):
        self.statusBar.SetLabel("")
        if self.gameOverPanel.IsShown():
            self.gameOverPanel.Hide()
        elif self.clearPanel.IsShown():
            self.clearPanel.Hide()
        self.startPanel.Show()
        self.Layout()

    # 게임 종료 메세지 창 출력, 확인 시 종료
    def closeGame(self, event):
        answer = MessageBox('게임을 종료할까요?', '종료',
                            YES_NO | NO_DEFAULT, self)
        if answer == YES:
            self.Close()


# ------------- 각종 화면 -------------

# ------------- 전역 변수 및 main 함수 -------------

# 목숨, 스테이지, 현재 정답 개수, 목표 정답 개수, 이미지 파일 (전역 변수)
life = 3
stage = 1
answerCount = 0
goalCount = 0
images = backend.load_images()

# main 실행 부분
if __name__ == "__main__":
    app = App(False)
    frame = mainFrame()
    frame.Show()
    app.MainLoop()

# ------------- 전역 변수 및 main 함수 -------------