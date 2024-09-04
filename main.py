import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    originalTileSize = 16
    scale = 6
    tileSize = originalTileSize * scale
    screenRow = 6
    screenCol = 8
    WIDTH = screenCol * tileSize
    HEIGHT = screenRow * tileSize
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tier Lister")
        self.setGeometry(550, 300, self.WIDTH, self.HEIGHT)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()