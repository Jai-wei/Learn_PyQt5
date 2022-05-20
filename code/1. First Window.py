from PyQt5.Qt import *
import sys

# 创建QApplication实例,argv为了将命令行参数传入
app = QApplication(sys.argv)

# 控件：创建控件、设置控件、展示控件
# 创建窗口
window = QWidget()
# 设置窗口标题
window.setWindowTitle('The First Window')
# 设置窗口尺寸
window.resize(200,200)
# 移动窗口
window.move(300,300)

# 创建lable标签，并且将window做为父控件
lable = QLabel(window)
lable.setText('Lable')
lable.move(100,100)

# 显示窗口(一个控件如果没有父控件，默认不被展示，必须使用show进行调用)
# 若控件有父控件，当父控件展示时将被一同展示
window.show()
# 进入程序主循环，并通过exit确保主循环安全结束，鉴证错误码
sys.exit(app.exec_())





