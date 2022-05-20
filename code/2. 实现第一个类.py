from PyQt5.Qt import *

# 继承QWidget类
class Window(QWidget):
    def __init__(self):
        # 在子类里调用父类的方法，防止父类的方法都不运行
        super().__init__()
        # 原本是window. 但是由于window也是自己创建的，所以使用self.:调用自己
        self.setWindowTitle("实现第一个类")
        self.resize(500, 500)
        self.setup_label()

    def setup_label(self):
        label = QLabel(self)
        label.setText('xxx')

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())