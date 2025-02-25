# Chess Tournament Manager

## Description
A Python application for managing chess tournaments following the Swiss tournament system. Built with a MVC architecture, this application allows tournament organizers to manage players, tournaments, rounds and generate various reports.

## Features
- Tournament Management:
  - Create new tournaments
  - Set tournament parameters (rounds, time control, description)
  - Track tournament progress
  - Generate Swiss system pairings
- Player Management:
  - Add new players
  - List players registered
- Match Management:
  - Record match results
  - Update player scores
- Reports Generation:
  - Players list (alphabetically)
  - Tournament list and details
  - Tournament players
  - Tournament rounds and matches
- Display Options:
  - Console text format
  - HTML formatted output

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
```bash
git clone https://github.com/fkruklyaramis/OC/tree/main/projet4
cd projet4
```

2. Create a virtual environment:
```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Project Structure
```
projet4/
├── controllers/          # Application logic
│   ├── interface_controller.py
│   ├── player_controller.py
│   ├── report_controller.py
│   └── tournament_controller.py
├── models/              # Data structures and business logic
│   ├── data_manager.py
│   ├── player.py
│   └── tournament.py
├── views/              # User interface
│   ├── interface_view.py
│   ├── player_view.py
│   ├── report_view.py
│   └── tournament_view.py
├── templates/          # HTML templates for reports
│   ├── players_list.html
│   ├── tournaments_list.html
│   ├── tournament_details.html
│   └── tournament_rounds.html
├── data/              # JSON data storage
│   ├── players.json
│   └── tournaments.json
└── main.py            # Application entry point
```

## Usage

### Starting the Application
```bash
python main.py
```

### Main Menu Options
1. Create Tournament
   - Enter tournament details
   - Add players
   - Start rounds
   - Record match results

2. Add Player
   - Enter player name
   - Chess ID
   - Birth date

3. View Reports
   - All players (alphabetically)
   - All tournaments
   - Tournament details by name
   - Tournament players
   - Tournament rounds and matches

4. Exit

## Data Storage
The application uses JSON files for data persistence:
- `players.json`: Stores player information
- `tournaments.json`: Stores tournament data, including rounds and matches

## Dependencies
- Python 3.8+
- Jinja2: Template engine for HTML output
- Rich: Console text formatting and styling

## Architecture
This project follows the MVC (Model-View-Controller) pattern:
- **Models**: Handle data structure and business logic
- **Views**: Manage user interface and data presentation
- **Controllers**: Process user input and coordinate between models and views

## Development
- Written in Python
- Follows PEP 8 style guide
- Implements MVC architecture
- Uses JSON for data persistence
- HTML templates for report generation