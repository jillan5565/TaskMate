import sys
from PyQt6.QtCore import QTimer
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, 
    QHBoxLayout, QLineEdit, QPushButton, QListWidget , QLabel
)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("TaskMate")
window.resize(350, 450)

# =========================
# العناصر
# =========================
theme1_btn = QPushButton("ليلكي")
theme2_btn = QPushButton("برغندي")

task_input = QLineEdit()
task_input.setPlaceholderText("اكتب المهمة هنا...")

add_button = QPushButton("إضافة")
delete_button = QPushButton("حذف المحددة")

task_list = QListWidget()

timer_seconds = 25*60
timer = QTimer()


timer_label = QLabel("25:00")
start_timer_btn = QPushButton("بدأ التركيز")
reset_timer_btn = QPushButton("إعادة ضبط")

# =========================
# الدوال (المنطق البرمجي)
# =========================
def set_Lilac_theme():
    window.setStyleSheet("background-color: #F5F0F6;")
    theme1_btn.setStyleSheet("background-color: #8A6B9D; color: white; padding: 6px; border-radius: 5px; font-weight: bold;")
    theme2_btn.setStyleSheet("background-color: #D5C6E0; color: #4A3B52; padding: 6px; border-radius: 5px;")
    task_input.setStyleSheet("background-color: #FFFFFF; color: #4A3B52; padding: 8px; border-radius: 6px; border: 1px solid #C8B6D6;")
    task_list.setStyleSheet("background-color: #FFFFFF; color: #4A3B52; border-radius: 6px; border: 1px solid #C8B6D6; font-size: 15px;")
    add_button.setStyleSheet("background-color: #8A6B9D; color: white; padding: 8px; border-radius: 6px; font-weight: bold;")
    delete_button.setStyleSheet("background-color: #BCA3CD; color: white; padding: 8px; border-radius: 6px; font-weight: bold;")
    start_timer_btn.setStyleSheet("background-color: #8A6B9D; color: black; padding: 6px; border-radius: 6px; font-weight: bold;")
    reset_timer_btn.setStyleSheet("background-color: #BCA3CD; color: black; padding: 6px; border-radius: 6px; font-weight: bold;")
    
def set_Burgundy_theme():
    window.setStyleSheet("background-color: #F8EDEC;")
    theme1_btn.setStyleSheet("background-color: #E2B6BD; color: #4A1521; padding: 6px; border-radius: 5px;")
    theme2_btn.setStyleSheet("background-color: #6B1D2F; color: white; padding: 6px; border-radius: 5px; font-weight: bold;")
    task_input.setStyleSheet("background-color: #FFFFFF; color: #4A1521; padding: 8px; border-radius: 6px; border: 1px solid #C2828D;")
    task_list.setStyleSheet("background-color: #FFFFFF; color: #4A1521; border-radius: 6px; border: 1px solid #C2828D; font-size: 15px;")
    add_button.setStyleSheet("background-color: #6B1D2F; color: white; padding: 8px; border-radius: 6px; font-weight: bold;")
    delete_button.setStyleSheet("background-color: #A24857; color: white; padding: 8px; border-radius: 6px; font-weight: bold;")
    timer_label.setStyleSheet("color: #4A3B52; font-size: 22px; font-weight: bold;")
    start_timer_btn.setStyleSheet("background-color: #8A6B9D; color: black; padding: 6px; border-radius: 6px; font-weight: bold;")
    reset_timer_btn.setStyleSheet("background-color: #BCA3CD; color: black; padding: 6px; border-radius: 6px; font-weight: bold;")

def add_task():
    text = task_input.text().strip()
    if text:  # نتأكد أن الخانة ليست فارغة
        task_list.addItem(text)
        task_input.clear()

def delete_task():
    selected_row = task_list.currentRow()
    if selected_row >= 0:  # نتأكد أن المستخدم محدد مهمة بالفعل
        task_list.takeItem(selected_row)

def update_timer():
    global timer_seconds
    if timer_seconds > 0:
        timer_seconds -= 1
        mins = timer_seconds // 60
        secs = timer_seconds % 60
        timer_label.setText(f"{mins:02d}:{secs:02d}")
    else:
        timer.stop()
        timer_label.setText("انتهى الوقت! 🎉")

def start_timer():
    if not timer.isActive():
        timer.start(1000)#ينبض كل ثانية

def reset_timer():

    global timer_seconds
    timer.stop()
    timer_seconds = 25* 60
    timer_label.setText("25:00")
def add_task():
    text = task_input.text().strip()
    if text:
        task_list.addItem(text)
        task_input.clear()

def delete_task():
    selected_row = task_list.currentRow()
    if selected_row >= 0:
        task_list.takeItem(selected_row)

#=============================
#ربط الازرار بالحداث
 #======================

theme1_btn.clicked.connect(set_Lilac_theme)
theme2_btn.clicked.connect(set_Burgundy_theme)


add_button.clicked.connect(add_task)
delete_button.clicked.connect(delete_task)
task_input.returnPressed.connect(add_task)

# ربط المؤقت
timer.timeout.connect(update_timer)
start_timer_btn.clicked.connect(start_timer)
reset_timer_btn.clicked.connect(reset_timer)

#تطبيق الثيم اليلكي كوضع افتراضي عند التشغيل
set_Lilac_theme()
# =========================
# ترتيب العناصر
# =========================
button_layout = QHBoxLayout()
button_layout.addWidget(add_button)
button_layout.addWidget(delete_button)

#منظم مؤقت البمودورو

pomodoro_layout = QHBoxLayout()
pomodoro_layout.addWidget(timer_label)
pomodoro_layout.addWidget(start_timer_btn)
pomodoro_layout.addWidget(reset_timer_btn)


main_layout = QVBoxLayout()
theme_layout = QHBoxLayout()
theme_layout.addWidget(theme1_btn)
theme_layout.addWidget(theme2_btn)
main_layout.addLayout(theme_layout)
main_layout.addWidget(task_input)
main_layout.addLayout(pomodoro_layout)
main_layout.addLayout(button_layout)
main_layout.addWidget(task_list)

window.setLayout(main_layout)
window.show()

sys.exit(app.exec())