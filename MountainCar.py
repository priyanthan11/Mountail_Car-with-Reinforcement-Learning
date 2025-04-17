# https://www.youtube.com/watch?v=TiAXhVAZQl8 (Q-Learning Explained)

import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
min_position = -1.5
max_position = 1.8  # Change this to see more or less of the right hill
goal_position_hill = math.pi/6
goal_position_valley = 3*math.pi/6  # Task 3 onwards
force = 0.001
gravity = 0.0025
max_speed = 0.07


# Initialize car
start_position = -1*math.pi/6  # Start position
position = start_position
velocity = 0.0  # Start velocity
actions = [-1, 0, 1]  # Left, Neutral, Right

# Hill function (for visualization)


def hill(x):
    return np.sin(3 * x) * 0.5


# Simulation parameters
num_steps = 1000  # change if needed
positions = []

# Data
state_action_pair = ([], [])

# Initialize figure
fig, ax = plt.subplots()
x = np.linspace(min_position, max_position, 100)
y = hill(x)
ax.plot(x, y, 'k')  # Draws the hill
car, = ax.plot([start_position], [hill(start_position)],
               'ro', markersize=10)  # Car marker


# Animation update function
def update(frame):
    global position, velocity, outcome

    # This should not be random :)
    # action = np.random.choice([-1, 1])  # Random force direction
    action = np.random.choice(actions)
    # print("Action: ", action)

    # Edit this block for later data/state changes and perhaps make this an actual good data structure
    state_action_pair[0].append(position)
    state_action_pair[1].append(action)
    # print("State Action Pair: ", state_action_pair)

    applied_force = action * force
    gradient = np.cos(3 * position)

    # Update velocity
    velocity += applied_force - (gravity * gradient)
    velocity = np.clip(velocity, -max_speed, max_speed)

    # Update position
    position += velocity
    position = np.clip(position, min_position, max_position)

    # Reset if going over the wrong hill
    if position <= -1.5:
        position = start_position
        # ani.event_source.stop() # You could also stop the simulation, perhaps consider this if you get bad results
        # outcome = "Failure"

    # Stops once on the hill with Success
    if goal_position_hill - 0.005 < position < goal_position_hill + 0.005:
        ani.event_source.stop()
        outcome = "Success"

    # Garage case
    # This is needed for task3 onwards
    # if goal_position_valley - 0.005 < position < goal_position_valley + 0.005 and abs(velocity) < 0.005:
    #    ani.event_source.stop()
    #    outcome = "Success"

    # Safe the current position for later analysis (if wanted)
    positions.append(position)
    car.set_data([position], [hill(position)])  # Update car position

    return car,


# Set plot limits
ax.set_xlim(min_position, max_position)
ax.set_ylim(-0.6, 0.6)
ax.set_xlabel("Position")
ax.set_ylabel("Height")
ax.set_title("Mountain Car Simulation")
car.set_color("Red")

# Create animation
ani = animation.FuncAnimation(
    fig, update, frames=num_steps, interval=1, blit=True)
plt.show()
