import numpy as np


def _make_resize_transition_matrix(c):
    return _make_shrink_transition_matrix(c, c, c)


def _make_move_transition_matrix(x, y, z):
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [x, y, z, 1]
    ])


def _make_rotate_transition_matrix(axis, angle):
    angle = np.radians(angle)
    if axis == 0:
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(angle), np.sin(angle), 0],
            [0, -1 * np.sin(angle), np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    if axis == 1:
        return np.array([
            [np.cos(angle), 0, -1 * np.sin(angle), 0],
            [0, 1, 0, 0],
            [np.sin(angle), 0, np.cos(angle), 0],
            [0, 0, 0, 1]
        ])
    return np.array([
        [np.cos(angle), np.sin(angle), 0, 0],
        [-1 * np.sin(angle), np.cos(angle), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])


def _make_shrink_transition_matrix(cx, cy, cz):
    return np.array([
        [cx, 0, 0, 0],
        [0, cy, 0, 0],
        [0, 0, cz, 0],
        [0, 0, 0, 1]
    ])


def _make_rotate_along_free_axis_transformation_matrix(point_x, point_y, point_z, angle):
    angle = np.radians(angle)

    d = np.sqrt(np.power(point_x, 2) + np.power(point_y, 2) + np.power(point_z, 2))
    n1 = point_x / d
    n2 = point_y / d
    n3 = point_z / d

    return np.array([
        [np.power(n1, 2) + (1 - np.power(n1, 2)) * np.cos(angle), n1 * n2 * (1 - np.cos(angle)) + n3 * np.sin(angle),
         n1 * n3 * (1 - np.cos(angle)) - n2 * np.sin(angle), 0],
        [n1 * n2 * (1 - np.cos(angle)) - n3 * np.sin(angle), np.power(n2, 2) + (1 - np.power(n2, 2)) * np.cos(angle),
         n2 * n3 * (1 - np.cos(angle)) + n1 * np.sin(angle), 0],
        [n1 * n3 * (1 - np.cos(angle)) + n2 * np.sin(angle), n2 * n3 * (1 - np.cos(angle)) - n1 * np.sin(angle),
         np.power(n3, 2) + (1 - np.power(n3, 2)) * np.cos(angle), 0],
        [0, 0, 0, 1]
    ])


def _make_shrink_along_free_axis_transition_matrix(point_x, point_y, point_z, cx, cy, cz):
    return np.array([
        [cx, 0, 0, 0],
        [0, cy, 0, 0],
        [0, 0, cz, 0],
        [(1 - cx) * point_x, (1 - cy) * point_y, (1 - cz) * point_z, 1]
    ])
