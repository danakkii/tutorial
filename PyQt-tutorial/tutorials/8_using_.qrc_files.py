
from PySide6.QtGui import QIcon, QKeySequence, QPixmap
playIcon = QIcon(QPixmap(":/icons/play.png"))
previousIcon = QIcon(QPixmap(":/icons/previous.png"))
pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
nextIcon = QIcon(QPixmap(":/icons/forward.png"))
stopIcon = QIcon(QPixmap(":/icons/stop.png"))

import rc_icons

def __init__(self):
    super(MainWindow, self).__init__()

    self.playlist = QMediaPlaylist()
    self.player = QMediaPlayer()

    toolBar = QToolBar()
    self.addToolBar(toolBar)

    fileMenu = self.menuBar().addMenu("&File")
    openAction = QAction(QIcon.fromTheme("document-open"),
                         "&Open...", self, shortcut=QKeySequence.Open,
                         triggered=self.open)
    fileMenu.addAction(openAction)
    exitAction = QAction(QIcon.fromTheme("application-exit"), "E&xit",
                         self, shortcut="Ctrl+Q", triggered=self.close)
    fileMenu.addAction(exitAction)

    playMenu = self.menuBar().addMenu("&Play")
    playIcon = QIcon(QPixmap(":/icons/play.png"))
    self.playAction = toolBar.addAction(playIcon, "Play")
    self.playAction.triggered.connect(self.player.play)
    playMenu.addAction(self.playAction)

    previousIcon = QIcon(QPixmap(":/icons/previous.png"))
    self.previousAction = toolBar.addAction(previousIcon, "Previous")
    self.previousAction.triggered.connect(self.previousClicked)
    playMenu.addAction(self.previousAction)

    pauseIcon = QIcon(QPixmap(":/icons/pause.png"))
    self.pauseAction = toolBar.addAction(pauseIcon, "Pause")
    self.pauseAction.triggered.connect(self.player.pause)
    playMenu.addAction(self.pauseAction)

    nextIcon = QIcon(QPixmap(":/icons/forward.png"))
    self.nextAction = toolBar.addAction(nextIcon, "Next")
    self.nextAction.triggered.connect(self.playlist.next)
    playMenu.addAction(self.nextAction)

    stopIcon = QIcon(QPixmap(":/icons/stop.png"))
    self.stopAction = toolBar.addAction(stopIcon, "Stop")
    self.stopAction.triggered.connect(self.player.stop)
    playMenu.addAction(self.stopAction)

    # many lines were omitted