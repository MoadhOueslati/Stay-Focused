from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer
from PyQt5.uic import loadUi


class TasksWindow(QMainWindow):
    def __init__(self, pomofocuswindow):
        super().__init__()
        loadUi('styles/task.ui', self)
        self.pomowindow = pomofocuswindow

        self.cancelButton.clicked.connect(lambda: self.close())
        
        self.saveButton.clicked.connect(self.saveTask)
    
    def saveTask(self):
        task_text = " ".join(self.taskLineEdit.text().split())
        if task_text:
            self.pomowindow.addTask(task_text) 
            self.close()       

class PomoFocus(QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.mw = mainwindow

        ''''This is responsible for decreasing the timer once the user
        hits the start button , the button handls stop/start signals.'''
        self.pomodoro_timer = QTimer()
        self.mw.startStopButton.clicked.connect(self.start_stop_timer)  # if else for stop/start
        self.pomodoro_timer.timeout.connect(self.updateTimer)
        self.work_duration = 200 * 60   # this is chosen by the user
        self.remaining_time = self.work_duration

        # open add task window
        self.mw.addTaskButton.clicked.connect(self.showTaskWindow)


    def showTaskWindow(self):
        self.taskswindow = TasksWindow(self)
        self.taskswindow.setWindowTitle("Task")
        self.taskswindow.setFixedSize(600, 260)
        self.taskswindow.show()

    def addTask(self, task_text):
        self.mw.label_2.setStyleSheet("font-size: 40px")
        if len(task_text) > 100:
            self.mw.label_2.setStyleSheet("font-size: 20px")
        self.mw.label_2.setText(task_text)

    def start_stop_timer(self):
        if self.pomodoro_timer.isActive():
            self.mw.startStopButton.setText('Start')
            self.pomodoro_timer.stop()
        else:
            self.mw.startStopButton.setText('Stop')
            self.pomodoro_timer.start(1000)  # timer ticks every 1 second
            
        
    def updateTimer(self):
        self.remaining_time -= 1
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        self.mw.timerLabel.setText(f"{minutes:02}:{seconds:02}")


        
        
        
