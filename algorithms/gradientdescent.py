from utils.gradient import calculate_grad


def GD(dim, func, x_0, num_iter, step_size):
    history = [x_0]
    old_pt = x_0
    for _ in range(num_iter):
        new_pt = old_pt - step_size*calculate_grad(func, old_pt, dim)
        history.append(new_pt)
        old_pt = new_pt
    return history
