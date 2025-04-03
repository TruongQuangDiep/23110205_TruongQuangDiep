import time
from function import run_gui
from utils import is_goal_state, is_valid, row, col

def heuristic(board):
    """ Hàm heuristic: Đếm số ô sai vị trí """
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return sum(1 for i in range(3) for j in range(3) if board[i][j] and board[i][j] != goal[i][j])

def solve_puzzle_steepest_ascent_core(start, x, y, display_mode=None, update_display=None):
    """Hàm chung cho Steepest-Ascent Hill Climbing, hỗ trợ cả hiển thị text và giao diện"""
    start_time = time.time()
    current_board = start
    current_x, current_y = x, y
    current_heuristic = heuristic(current_board)
    path = [current_board]
    visited = set()
    visited.add(tuple(map(tuple, current_board)))

    while not is_goal_state(current_board):
        best_board = None
        best_x, best_y = -1, -1
        best_heuristic = current_heuristic

        for i in range(4):
            new_x, new_y = current_x + row[i], current_y + col[i]
            if is_valid(new_x, new_y):
                new_board = [r[:] for r in current_board]
                new_board[current_x][current_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[current_x][current_y]
                board_tuple = tuple(map(tuple, new_board))
                new_h = heuristic(new_board)

                # Chọn nước đi có heuristic tốt nhất trong tất cả các lựa chọn
                if board_tuple not in visited and new_h < best_heuristic:
                    best_board, best_x, best_y, best_heuristic = new_board, new_x, new_y, new_h

        # Nếu không có bước đi nào tốt hơn, dừng lại (mắc kẹt tại cực đại cục bộ)
        if best_board is None:
            if display_mode == "text" and update_display:
                update_display('No improvement found, stuck in local optimum (Steepest-Ascent Hill Climbing)')
            return

        # Cập nhật trạng thái tốt nhất tìm được
        current_board, current_x, current_y, current_heuristic = best_board, best_x, best_y, best_heuristic
        path.append(current_board)
        visited.add(tuple(map(tuple, current_board)))

    end_time = time.time()

    if display_mode == "text" and update_display:
        for step, state in enumerate(path):
            display_text = f"Step {step}:\n"
            display_text += "\n".join([" ".join(map(str, row)) for row in state]) + "\n------"
            update_display(display_text)

        update_display(f'Solution found in {len(path) - 1} steps (Steepest-Ascent Hill Climbing)')
        update_display(f'Time taken: {end_time - start_time:.6f} seconds')
        update_display(f'Nodes expanded: {len(visited)}')
    elif display_mode == "gui":
        run_gui(path)  # Gửi danh sách trạng thái để hiển thị
        
def solve_puzzle_steepest_ascent(start, x, y, update_display):
    """Steepest-Ascent Hill Climbing hiển thị qua text"""
    solve_puzzle_steepest_ascent_core(start, x, y, display_mode="text", update_display=update_display)
    
def solve_puzzle_steepest_ascent_giao_dien(start, x, y):
    """Steepest-Ascent Hill Climbing hiển thị qua giao diện"""
    solve_puzzle_steepest_ascent_core(start, x, y, display_mode="gui")
