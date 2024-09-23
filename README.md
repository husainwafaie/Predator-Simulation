# Simulation Game

This project is a simulation game built using Python and the Tkinter library. The game involves various types of objects (simultons) that interact with each other in a simulated environment. The objects include predators, prey, and other entities with unique behaviors.

Created by Husain Wafaie as a part of the ICS 33 class at UCI.

<img src="/simulation.jpg" alt="Game Screenshot">

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Files](#files)
- [Classes and Modules](#classes-and-modules)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/husainwafaie/Predator-Simulation.git
    cd Predator-Simulation
    ```

2. **Install dependencies:**
    Ensure you have Python installed. This project uses the Tkinter library, which is included with Python's standard library.

3. **Run the simulation:**
    ```sh
    python script.py
    ```

## Usage

- **Reset:** Resets the simulation.
- **Start:** Starts the simulation.
- **Stop:** Stops the simulation.
- **Step:** Advances the simulation by one step.
- **Object Buttons:** Adds the corresponding object to the simulation.
- **Remove:** Removes the selected object from the simulation.

## Files

- `special.py`: Defines the `Special` class, a predator that can kill prey from a distance.
- `simulton.py`: Defines the `Simulton` base class, which includes location and dimension properties.
- `script.py`: The main script to run the simulation.
- `prey.py`: Defines the `Prey` class, which inherits from `Mobile_Simulton`.
- `hunter.py`: Defines the `Hunter` class, a predator that pursues nearby prey.
- `floater.py`: Defines the `Floater` class, a type of prey that moves randomly.
- `controller.py`: Handles the creation of buttons and canvas, and manages the simulation's main loop.
- `view.py`: Sets up the Tkinter window and layout.
- `mobilesimulton.py`: Defines the `Mobile_Simulton` class, which includes movement capabilities.

## Classes and Modules

### `special.py`
- **Special**: Inherits from `Pulsator` and `Mobile_Simulton`. It can kill prey from a distance using a green laser.

### `simulton.py`
- **Simulton**: Base class for all objects in the simulation. Handles location and dimension properties.

### `prey.py`
- **Prey**: Inherits from `Mobile_Simulton`. Represents prey in the simulation.

### `hunter.py`
- **Hunter**: Inherits from `Pulsator` and `Mobile_Simulton`. Pursues and kills nearby prey.

### `floater.py`
- **Floater**: Inherits from `Prey`. Moves randomly and displays as a red circle.

### `controller.py`
- Functions to create buttons and canvas, and manage the simulation's main loop.

### `view.py`
- Sets up the Tkinter window and layout.

### `mobilesimulton.py`
- **Mobile_Simulton**: Inherits from `Simulton`. Adds movement capabilities, including speed and angle.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Enjoy the simulation game! If you have any questions or issues, feel free to open an issue on GitHub.
