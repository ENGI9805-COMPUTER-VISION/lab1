import numpy as np

def group_by_angle(lines):
    """Group lines based on their angles.

    For this problem, since the grid only contains vertical and
    horizontal lines. We can safely divide the lines into two groups,
    namely vertical lines and horizontal lines.

    For complex situations, we can use k-means method to separate the lines.
    """

    v_lines = []
    h_lines = []

    for line in lines:
        if 0.875 < line[0][1] < 2.356:
            v_lines.append(line)
        else:
            h_lines.append(line)

    return v_lines, h_lines


def find_intersection(line1, line2):
    """Finds the intersection of two lines."""

    rho1, theta1 = line1[0]
    rho2, theta2 = line2[0]
    A = np.array([
        [np.cos(theta1), np.sin(theta1)],
        [np.cos(theta2), np.sin(theta2)]
    ])
    b = np.array([[rho1], [rho2]])
    x, y = np.linalg.solve(A, b)
    x, y = int(np.round(x)), int(np.round(y))

    return (x, y)


def find_group_intersections(group1, group2):
    """Finds the intersections between two groups of lines."""

    intersections = []

    for line1 in group1:
        for line2 in group2:
            intersections.append(find_intersection(line1, line2))

    return intersections
