# Spatial-Que-Numpy
Write a function to select indices of frames given a clip of the car driving.

#### `calculate_distances`

```python
def calculate_distances(trajectory):
    """
    Input: trajectory - np.array of (x, y) points
    Task: Calculate the distances between the points
    Output: distances_points - np.array with the distances between points
    """
    distances_points = np.zeros(trajectory.shape[0])
    distances_points[1:] = np.sqrt(np.sum((trajectory[1:] - trajectory[:-1]) ** 2, axis=1))
    return distances_points
```

#### `match_distance_frames_points`

```python
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
```