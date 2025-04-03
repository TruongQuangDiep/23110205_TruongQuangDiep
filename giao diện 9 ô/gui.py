import tkinter as tk
from tkinter import Label, Canvas, PhotoImage, Frame, Scrollbar, Text
from bfs1 import *
from dfs1 import *
from iddfs1 import *
from ucs1 import *
from astar import *
from idastar import *
from SHC import *
from SAHC import *
from greedy_search import *
from utils import print_board

# Trạng thái bắt đầu
start = [[2, 6, 5], [0, 8, 7], [4, 3, 1]]
x, y = 1, 0  # Vị trí ô trống (0)

# Hàm cập nhật giao diện để hiển thị trạng thái
def update_display(text):
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text + "\n")
    output_text.config(state=tk.DISABLED)
    output_text.yview(tk.END)  # Tự động cuộn xuống cuối
 
# Hàm gọi BFS
def run_bfs():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)  # Xóa nội dung cũ
    output_text.config(state=tk.DISABLED)
    solve_puzzle_bfs(start, x, y, update_display)
    
# Hàm gọi DFS
def run_dfs():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_dfs(start, x, y, update_display)

# Hàm gọi IDDFS
def run_iddfs():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_iddfs(start, x, y, update_display)
    
def run_ucs():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_ucs(start, x, y, update_display)
    
def run_astar():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_astar(start, x, y, update_display)
    
def run_idastar():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_idastar(start, x, y, update_display)

def run_greedy():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_greedy(start, x, y, update_display)
    
def run_hill_climbing():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_hill_climbing(start, x, y, update_display)
    
def run_steepest_ascent():
    output_text.config(state=tk.NORMAL)
    output_text.delete("1.0", tk.END)
    output_text.config(state=tk.DISABLED)
    solve_puzzle_steepest_ascent(start, x, y, update_display)
    
text_widgets = []

root = tk.Tk()
root.title("8 Puzzle Solver")
window_width = 1200
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_x = (screen_width // 2) - (window_width // 2)
position_y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

root.configure(bg="lightblue")

label = Label(root, text="Chọn thuật toán để giải bài toán 8-Puzzle", font=("Arial", 14))
label.configure(bg="lightblue")
label.pack()

output_text = None
frame_main = None
output_scrollbar = None
canvas_frame = None  # Khai báo canvas_frame là None ban đầu
scrollbar = None  # Khai báo scrollbar là None ban đầu

def create_frame_main(root):
    global frame_main
    if frame_main:  # Nếu đã có Frame cũ, xóa nó trước
        frame_main.destroy()
    frame_main = tk.Frame(root)
    frame_main.pack(pady=10, fill=tk.BOTH, expand=True)

def create_main_text_widget(root, width=50, height=20):
    """Tạo Text widget và Scrollbar bên trong frame_main"""
    global output_text, output_scrollbar

    remove_main_text_widget()  # Xóa cái cũ nếu có
    create_frame_main(root)  # Tạo Frame trước

    # Tạo Text Widget
    output_text = Text(frame_main, wrap=tk.WORD, height=height)
    output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    output_text.config(state=tk.DISABLED)  # Vô hiệu hóa chỉnh sửa
    output_text.config(font=("Arial", 16))

    # Tạo Scrollbar
    output_scrollbar = Scrollbar(frame_main, command=output_text.yview)
    output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    output_text.config(yscrollcommand=output_scrollbar.set)
    
def remove_main_text_widget():
    """Xóa toàn bộ Frame chứa Text và Scrollbar"""
    global output_text, output_scrollbar, frame_main
    if frame_main:
        frame_main.destroy()
        frame_main = None  # Đặt lại biến
    if output_text:
        output_text.destroy()  # Xóa cả Frame, Text và Scrollbar
        output_text = None  # Đặt lại biến
    if output_scrollbar:
        output_scrollbar.destroy()
        output_scrollbar = None

create_main_text_widget(root)
        
def remove_text_widgets():
    """Xóa tất cả Text widget phụ"""
    global text_widgets, canvas_frame, scrollbar
    for widget in text_widgets:
        widget.destroy()
    text_widgets = []  # Đặt lại danh sách
    
    # Xóa canvas_frame nếu tồn tại
    if canvas_frame:
        canvas_frame.destroy()
        canvas_frame = None

    # Xóa scrollbar nếu tồn tại
    if scrollbar:
        scrollbar.destroy()
        scrollbar = None
    
text_widgets_output = []       

def create_text_widget(parent, width=25, height=15, x_offset=0,algorithm_name=""):
    remove_main_text_widget()
    """Tạo Text widget với thanh cuộn và đặt ở góc trái trên cùng"""
    """Tạo Text widget với thanh cuộn và đặt trong parent"""
    frame = tk.Frame(parent)
    frame.grid(row=0, column=x_offset // 210, padx=10, pady=10, sticky="nw")  # Sắp xếp theo cột

    # Tạo Text widget
    text_widget = tk.Text(frame, wrap=tk.WORD, width=width, height=height, font=("Arial", 14))
    text_widget.grid(row=0, column=0, sticky="nw")

    # Thanh cuộn
    scrollbar = tk.Scrollbar(frame, command=text_widget.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    text_widget.config(yscrollcommand=scrollbar.set)
    
    # Tạo Label bên dưới Text widget
    label = tk.Label(frame, text=algorithm_name, font=("Arial", 20), bg="lightgray")
    label.grid(row=1, column=0, columnspan=2, pady=5)  # Đặt Label bên dưới Text widget

    text_widgets.append(frame)
    return text_widget

def on_compare_click():
    """Xóa text lớn và tạo nhiều text widget phụ trên 1 hàng"""
    global text_widgets_output, canvas_frame
    remove_main_text_widget()  # Xóa text lớn
    remove_text_widgets()  # Xóa các widget phụ cũ
    
    # Tạo Canvas để chứa các frame
    canvas_frame = tk.Frame(root)
    canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    canvas = tk.Canvas(canvas_frame)
    scrollbar = tk.Scrollbar(canvas_frame, orient=tk.HORIZONTAL, command=canvas.xview)
    canvas.configure(xscrollcommand=scrollbar.set)

    canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

    # Tạo một frame bên trong Canvas
    inner_frame = tk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")
    
    # Danh sách tên thuật toán
    algorithm_names = [
        "BFS", "IDDFS", "UCS", "A*", "Greedy", "IDA*", "Hill Climbing", "Steepest Ascent"
    ]
    
    text_widgets_output = []
    for i, name in enumerate(algorithm_names):  # Số lượng có thể thay đổi
        x_offset = i * 210  # Mỗi Text widget cách nhau 250 pixel
        text_widget = create_text_widget(inner_frame, x_offset=x_offset, algorithm_name=name)
        text_widgets_output.append(text_widget)
        
    # Cập nhật kích thước của Canvas
    inner_frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

def compare_click():
    solve_puzzle_bfs(start, x, y, lambda text: (text_widgets_output[0].insert(tk.END, text + "\n"),text_widgets_output[0].see(tk.END)))
    solve_puzzle_iddfs(start, x, y, lambda text: (text_widgets_output[1].insert(tk.END, text + "\n"),text_widgets_output[1].see(tk.END)))
    solve_puzzle_ucs(start, x, y, lambda text: (text_widgets_output[2].insert(tk.END, text + "\n"),text_widgets_output[2].see(tk.END)))
    solve_puzzle_astar(start, x, y, lambda text: (text_widgets_output[3].insert(tk.END, text + "\n"),text_widgets_output[3].see(tk.END)))
    solve_puzzle_greedy(start, x, y, lambda text: (text_widgets_output[4].insert(tk.END, text + "\n"),text_widgets_output[4].see(tk.END)))
    solve_puzzle_idastar(start, x, y, lambda text: (text_widgets_output[5].insert(tk.END, text + "\n"),text_widgets_output[5].see(tk.END)))
    solve_puzzle_hill_climbing(start, x, y, lambda text: (text_widgets_output[6].insert(tk.END, text + "\n"),text_widgets_output[6].see(tk.END)))
    solve_puzzle_steepest_ascent(start, x, y, lambda text: (text_widgets_output[7].insert(tk.END, text + "\n"),text_widgets_output[7].see(tk.END)))
    #solve_puzzle_dfs(start, x, y, lambda text: (text_widgets_output[6].insert(tk.END, text + "\n"),text_widgets_output[6].see(tk.END)))
        
def restore_main_text_widget():
    """Xóa các text widget phụ và hiển thị lại text widget chính"""
    remove_text_widgets()

    global output_text, frame_main, output_scrollbar
    if frame_main is None:  # Nếu frame_main không tồn tại, tạo lại nó
        create_frame_main(root)

    if output_text is None:  # Nếu output_text không tồn tại, tạo lại nó
        output_text = Text(frame_main, wrap=tk.WORD, height=15)
        output_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        output_text.config(state=tk.DISABLED)
        output_text.config(font=("Arial", 16))

    if output_scrollbar is None:  # Nếu output_scrollbar không tồn tại, tạo lại nó
        output_scrollbar = Scrollbar(frame_main, command=output_text.yview)
        output_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        output_text.config(yscrollcommand=output_scrollbar.set)

    frame_main.pack(pady=10, fill=tk.BOTH, expand=True)

def update_display(text):
    """Cập nhật hiển thị nội dung thuật toán"""
    restore_main_text_widget()  # Khôi phục text chính trước khi hiển thị nội dung
    output_text.config(state=tk.NORMAL)
    output_text.insert(tk.END, text + "\n")
    output_text.config(state=tk.DISABLED)
    output_text.yview(tk.END)
    
# Tạo Canvas để chứa các nút
button_canvas = tk.Canvas(root, bg="lightgray", height=100)
button_canvas.pack(side=tk.BOTTOM, fill=tk.X)

# Thêm Scrollbar ngang
button_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=button_canvas.xview)
button_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

button_canvas.configure(xscrollcommand=button_scrollbar.set)

# Tạo Frame bên trong Canvas để chứa các nút
button_frame = tk.Frame(button_canvas, bg="lightgray")
button_canvas.create_window((0, 0), window=button_frame, anchor="nw")

# Hàm cập nhật kích thước của Canvas
def update_button_canvas():
    button_frame.update_idletasks()
    button_canvas.config(scrollregion=button_canvas.bbox("all"))

# Nút BFS từ ảnh
img_bfs = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\BFS.png")
btn_bfs = tk.Button(button_frame, image=img_bfs,  command=lambda: (restore_main_text_widget(), run_bfs(), solve_puzzle_bfs_giao_dien(start, x, y)))
btn_bfs.pack(side=tk.LEFT, padx=10)

# Nút DFS từ ảnh
img_dfs = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\DFS.png")
btn_dfs = tk.Button(button_frame, image=img_dfs, command=lambda: (restore_main_text_widget(), run_dfs(), solve_puzzle_dfs_giao_dien(start, x, y)))
btn_dfs.pack(side=tk.LEFT, padx=10)

# Nút IDDFS từ ảnh
img_iddfs = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\IDDFS.png")
btn_iddfs = tk.Button(button_frame, image=img_iddfs, command=lambda: (restore_main_text_widget(), run_iddfs(), solve_puzzle_iddfs_giao_dien(start, x, y)))
btn_iddfs.pack(side=tk.LEFT, padx=10)

# Nút UCS từ ảnh
img_ucs = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\\UCS.png")
btn_ucs = tk.Button(button_frame, image=img_ucs, command=lambda: (restore_main_text_widget(), run_ucs(), solve_puzzle_ucs_giao_dien(start, x, y)))
btn_ucs.pack(side=tk.LEFT, padx=10)

# Nút A* từ ảnh
img_astar = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\A STAR.png")
btn_astar = tk.Button(button_frame, image=img_astar, command=lambda: (restore_main_text_widget(), run_astar(), solve_puzzle_astar_giao_dien(start, x, y)))
btn_astar.pack(side=tk.LEFT, padx=10)

# Nút IDA* từ ảnh
img_idastar = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\IDA STAR.png")
btn_idastar = tk.Button(button_frame, image=img_idastar, command=lambda: (restore_main_text_widget(), run_idastar(), solve_puzzle_idastar_giao_dien(start, x, y)))
btn_idastar.pack(side=tk.LEFT, padx=10)

# Nút Greedy từ ảnh
img_greedy = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\\GREEDY SEARCH.png")
btn_greedy = tk.Button(button_frame, image=img_greedy, command=lambda: (restore_main_text_widget(), run_greedy(), solve_puzzle_greedy_giao_dien(start, x, y)))
btn_greedy.pack(side=tk.LEFT, padx=10)

img_hill_climbing = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\SHC.png")
btn_hill_climbing = tk.Button(button_frame, image=img_hill_climbing, command=lambda: (restore_main_text_widget(), run_hill_climbing(), solve_puzzle_hill_climbing_giao_dien(start, x, y)))
btn_hill_climbing.pack(side=tk.LEFT, padx=10)

img_steepest_ascent = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\SAHC.png")
btn_steepest_ascent = tk.Button(button_frame, image=img_steepest_ascent, command=lambda: (restore_main_text_widget(), run_steepest_ascent(), solve_puzzle_steepest_ascent_giao_dien(start, x, y)))
btn_steepest_ascent.pack(side=tk.LEFT, padx=10)

# Nút so sánh
img_compare = PhotoImage(file=r"D:\đồ án trí tuệ nhân tạo cá nhân\giao diện 9 ô\giao diện 8 puzzle png\Compare.png")
btn_compare = tk.Button(button_frame, image=img_compare, command=lambda: (on_compare_click(), compare_click()))
btn_compare.pack(side=tk.LEFT, padx=10)

# Chạy giao diện
root.mainloop()
