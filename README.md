# Sports-Analytics

GROUP MEMBERS
NEEL JOGANI 
KEVIL VEKARIYA
FENIL PATEL
HARSH SONI
MANAV PATEL

# Sports Performance Dashboard

This project is a **Dash** web application that visualizes player performance metrics for sports teams. Users can interactively explore different teams and metrics using dropdown menus, and the corresponding bar charts are dynamically generated and displayed.

## Features

- Interactive dashboard with dropdowns to select:
  - Team
  - Performance metric (e.g., Matches Played, Goals Scored, Assists, Win Rate)
- Dynamic bar chart visualization for the selected team's players.
- Easy-to-use interface built with Python libraries:
  - **Pandas** for data handling.
  - **Matplotlib** for data visualization.
  - **Dash** for building the interactive web app.

## How It Works

1. The app uses a sample dataset of player statistics, including:
   - Player names, teams, matches played, goals scored, assists, and win rates.
2. When a team and metric are selected, the app filters the data and generates a bar chart using Matplotlib.
3. The bar chart is encoded as a Base64 image and rendered on the web page.

## Requirements

To run this project, you need Python and the following libraries:
- `dash`
- `pandas`
- `matplotlib`

Install the dependencies using:
```bash
pip install dash pandas matplotlib

