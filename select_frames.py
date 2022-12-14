import numpy as np

clip = np.random.random((100, 128, 128, 3))
frames = np.random.random((100, 128, 128))
trajectory = np.random.random((10, 2))

distances_frames = np.random.random((100, 1))

def calculate_distances(trajectory):
    """
    Input: trajectory - np.array of (x, y) points
    Task: Calculate the distances between the points
    Output: distances_points - np.array with the distances between points
    """
    distances_points = np.zeros(trajectory.shape[0])
    distances_points[1:] = np.sqrt(np.sum((trajectory[1:] - trajectory[:-1]) ** 2, axis=1))
    return distances_points

def calculate_distances_frames(frames):
    distances_frames = np.zeros((frames.shape[0], 1))
    for i in range(frames.shape[0]):
        distances_frames[i] = np.sum(np.abs(frames[i] - frames[i-1]))
    return distances_frames

def match_distance_frames_points(distances_frames, trajectory):
    """
    Input: distances_frames - np.array with the distances between frames
    Input: trajectory - np.array of (x, y) points
    Task: Select the distances between frames that match the distances between the trajectory points
    Output: selected frames
    """
    distances_points = calculate_distances(trajectory)
    selected_frames = []
    counter_frames = 0
    counter_points = 0
    while counter_points < len(distances_points) and counter_frames < len(distances_frames):
        if np.abs(distances_points[counter_points] - distances_frames[counter_frames]) < 0.1:
            selected_frames.append(counter_frames)
            counter_points += 1
        counter_frames += 1
    return np.array(selected_frames)

print(calculate_distances_frames(frames))