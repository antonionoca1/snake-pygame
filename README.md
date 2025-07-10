# Snake Game (Pygame)

A classic 2D Snake game implemented in Python using the Pygame library, designed with domain-driven principles for readability and maintainability.

## Features
- Simple start screen to begin the game
- Snake moves continuously in four cardinal directions (Up, Down, Left, Right)
- Single food item appears randomly on the grid-based board
- Snake grows by one segment when food is consumed
- Real-time display of the player's current score
- Responsive UI adapts to different screen sizes (desktop and mobile)
- Arrow keys for direction control
- Game ends if the snake's head hits the board boundaries or its own body
- "Game Over" screen displays final score and restart option

## Getting Started

### Prerequisites
- Python 3.12 or higher
- [Pygame](https://www.pygame.org/)

Install dependencies:
```bash
pip install -r requirements.txt
```

### Running the Game
To start the game, use the provided batch script:
```bash
run.bat
```

### Running Tests
To run all unit tests:
```bash
test.bat
```

## Project Structure
- `domain.py` — Core domain logic (snake, food, grid, etc.)
- `game.py` — Game loop and state management
- `drawing.py` — Rendering and UI
- `input.py` — Input handling
- `main.py` — Entry point
- `tests/` — Unit tests for domain, drawing, and game logic
- `run.bat` — Launches the game
- `test.bat` — Runs all tests

## Controls
- Arrow keys: Change snake direction

## License
This project is for educational purposes.
