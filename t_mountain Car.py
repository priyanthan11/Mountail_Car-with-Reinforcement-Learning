import numpy as np
import math
import matplotlib.pyplot as plt


# Env Constraints
min_position = -1.5
max_position = 1.8
goal_position_hill = math.pi/6
force = 0.001
gravity = 0.0025
max_speed = 0.07
start_position = -1 * math.pi / 6
actions = [-1, 0, 1]  # Left, Neutral, Right

# Q-Learning parameters
n_bins = 30
alpha = 0.1
gamma = 0.99
epsilon = 0.1
epsilon_min = 0.05
epsilon_decay = 0.995
episodes = 500

# Discretize position
'''
🍕 Real-World Analogy: Pizza Delivery
Imagine you're a pizza delivery driver, and your GPS gives you your location as a decimal:

You are at: 2.34 km from the city center.

But your boss doesn’t want that level of detail. He says:
 
“Just tell me which zone you're in. We’ve split the city into 5 zones.”

Each zone covers 1 km, like:

Zone 0: 0.0 - 1.0
Zone 1: 1.0 - 2.0
Zone 2: 2.0 - 3.0
Zone 3: 3.0 - 4.0
Zone 4: 4.0 - 5.0

So if you're at 2.34 km, your zone = 2 ✅

This is called discretization: taking a precise value and converting it into a category or bin.

🚗 Mountain Car Example
1. 📐 Position Range:
The car’s position can be from -1.5 to 1.8.

2. 📦 Let's say we use 6 bins:
We'll split the range into 6 intervals:

python
Copy
Edit
position_bins = np.linspace(-1.5, 1.8, 6)
# Result: [-1.5, -0.84, -0.18, 0.48, 1.14, 1.8]
3. 🧮 Now take some example positions:

Position	Falls In Range	Bin Index
-1.3	between -1.5 and -0.84	bin 1
-0.5	between -0.84 and -0.18	bin 2
0.6	between 0.48 and 1.14	bin 4
1.7	between 1.14 and 1.8	bin 5
We get this index using:

python
Copy
Edit
pos_bin = np.digitize(position, position_bins)
So the car's exact position like 0.6 → becomes state 4

🧠 Why Do This?
Because your Q-table can only store a finite number of states.

Imagine storing values for every possible float like 0.12345, 0.12346... 😱

Instead, we say:

"Let's treat all positions between 0.5 and 1.1 as the same state."

Now we have 6 discrete states instead of infinite ones.
'''

position_bin = np.linspace(min_position, max_position, n_bins)


def discretize_position(pos):
    return np.digitize(pos, position_bin)
