# Vibe Coding Demo

A fun Cookie Clicker-style game built with Flask! Click your way to fortune and unlock special upgrades.

## Features

- **Click-based gameplay** - Click to earn cookies
- **Upgrades** - Purchase upgrades like Grandma and Robot to boost your production
- **Lucky 67** - Special bonus triggered every 67th click
- **Golden Cookie** - Powerful late-game upgrade
- **Real-time updates** - Cookies per second (CPS) counter

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository** (or download the files):
   ```bash
   git clone <repository-url>
   cd vibecodingdemo
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   ```

3. **Activate the virtual environment**:
   
   **On macOS/Linux:**
   ```bash
   source venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

3. **Start clicking and have fun!**

## Project Structure

```
vibecodingdemo/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Game UI
```

## Dependencies

- **Flask** (3.0.0) - Lightweight Python web framework

## License

Feel free to use and modify this project!

## Contributing

Have ideas to improve the game? Feel free to fork, modify, and submit a pull request!
