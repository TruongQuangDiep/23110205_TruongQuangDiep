import random
import time
from function import run_gui
from utils import is_goal_state, heuristic

def generate_random_board():
    """Tạo trạng thái ngẫu nhiên"""
    numbers = list(range(9))
    random.shuffle(numbers)
    return [numbers[i:i+3] for i in range(0, 9, 3)]

def flatten_board(board):
    """Chuyển ma trận 3x3 thành danh sách 1 chiều"""
    return [num for row in board for num in row]

def unflatten_board(flat_board):
    """Chuyển danh sách 1 chiều thành ma trận 3x3"""
    return [flat_board[i:i+3] for i in range(0, 9, 3)]

def fitness(board):
    """Hàm fitness: Sử dụng heuristic để đánh giá trạng thái"""
    return -heuristic(board)  # Giá trị càng cao càng tốt (heuristic càng thấp)

def mutate(board):
    """Đột biến: Hoán đổi hai ô bất kỳ"""
    flat_board = flatten_board(board)
    i, j = random.sample(range(9), 2)
    flat_board[i], flat_board[j] = flat_board[j], flat_board[i]
    return unflatten_board(flat_board)

def crossover(parent1, parent2):
    """Lai ghép: Kết hợp hai cha mẹ để tạo con"""
    flat1 = flatten_board(parent1)
    flat2 = flatten_board(parent2)
    crossover_point = random.randint(1, 8)
    child_flat = flat1[:crossover_point] + [num for num in flat2 if num not in flat1[:crossover_point]]
    return unflatten_board(child_flat)

def solve_puzzle_genetic_algorithm_core(start, x, y, population_size=100, generations=1000, mutation_rate=0.1, display_mode=None, update_display=None):
    """Hàm chung cho Genetic Algorithm, hỗ trợ cả hiển thị text và giao diện"""
    start_time = time.time()
    population = [generate_random_board() for _ in range(population_size)]
    population[0] = start  # Đảm bảo trạng thái đầu tiên là trạng thái đầu vào

    for generation in range(generations):
        # Đánh giá fitness của quần thể
        population = sorted(population, key=lambda board: fitness(board), reverse=True)

        # Nếu tìm thấy lời giải
        if is_goal_state(population[0]):
            end_time = time.time()
            if display_mode == "text" and update_display:
                update_display(f'Solution found in generation {generation} (Genetic Algorithm)')
                update_display(f'Time taken: {end_time - start_time:.6f} seconds')
                update_display(f'Best board:\n' + "\n".join([" ".join(map(str, row)) for row in population[0]]))
            elif display_mode == "gui":
                run_gui([population[0]])  # Hiển thị trạng thái cuối cùng
            return

        # Chọn lọc: Giữ lại một phần quần thể tốt nhất
        next_population = population[:population_size // 2]

        # Lai ghép: Tạo thế hệ mới
        while len(next_population) < population_size:
            parent1, parent2 = random.sample(population[:population_size // 2], 2)
            child = crossover(parent1, parent2)
            next_population.append(child)

        # Đột biến
        for i in range(len(next_population)):
            if random.random() < mutation_rate:
                next_population[i] = mutate(next_population[i])

        population = next_population

    # Nếu không tìm thấy lời giải
    if display_mode == "text" and update_display:
        update_display('No solution found (Genetic Algorithm)')

def solve_puzzle_genetic_algorithm(start, x, y, update_display):
    """Genetic Algorithm hiển thị qua text"""
    solve_puzzle_genetic_algorithm_core(start, x, y, display_mode="text", update_display=update_display)

def solve_puzzle_genetic_algorithm_giao_dien(start, x, y):
    """Genetic Algorithm hiển thị qua giao diện"""
    solve_puzzle_genetic_algorithm_core(start, x, y, display_mode="gui")