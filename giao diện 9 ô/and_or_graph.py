import time
from function import run_gui
from utils import is_goal_state, is_valid, row, col

def and_or_graph_search_core(start, x, y, display_mode=None, update_display=None):
    start_time = time.time()

    def AND_OR_GRAPH_SEARCH(state, x, y, path):
        if is_goal_state(state):
            return [state]

        state_key = tuple(map(tuple, state))
        if state_key in path:
            return None  # Tránh vòng lặp

        for i in range(4):
            nx, ny = x + row[i], y + col[i]
            if is_valid(nx, ny):
                new_state = [r[:] for r in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]

                result = AND_OR_GRAPH_SEARCH(new_state, nx, ny, path + [state_key])
                if result:
                    return [state] + result
        path.remove(state_key)
        return None

    result = AND_OR_GRAPH_SEARCH(start, x, y, [])

    end_time = time.time()

    if result:
        if display_mode == "text" and update_display:
            for step, state in enumerate(result):
                text = f"Step {step}:\n" + "\n".join(" ".join(map(str, r)) for r in state) + "\n------"
                update_display(text)
            update_display(f'Solution found in {len(result) - 1} steps (AND-OR)')
            update_display(f'Time taken: {end_time - start_time:.6f} seconds')
            update_display(f'Nodes expanded: {len(result)}')
        elif display_mode == "gui":
            run_gui(result)
    else:
        if display_mode == "text" and update_display:
            update_display('No solution found (AND-OR)')


def solve_puzzle_and_or(start, x, y, update_display):
    and_or_graph_search_core(start, x, y, display_mode="text", update_display=update_display)


def solve_puzzle_and_or_giao_dien(start, x, y):
    and_or_graph_search_core(start, x, y, display_mode="gui")
