import pandas as pd
import matplotlib.pyplot as plt
from dash import Dash, dcc, html, Input, Output
import io
import base64

# Initialize Dash app
app = Dash(__name__)

# Sample dataset
data = {
    'Player': ['John Doe', 'Jane Smith', 'Alice Brown', 'Tom Lee'],
    'Team': ['Warriors', 'Warriors', 'Tigers', 'Tigers'],
    'Matches Played': [25, 30, 22, 27],
    'Goals Scored': [18, 24, 15, 21],
    'Assists': [9, 12, 8, 11],
    'Win Rate (%)': [80, 85, 70, 75],
    'Season': ['2024', '2024', '2024', '2024'],
}


df = pd.DataFrame(data)

# Helper function to create Matplotlib plots and return as an image
def create_matplotlib_figure(selected_team, selected_metric):
    # Filter data for the selected team
    filtered_df = df[df['Team'] == selected_team]

    # Create the Matplotlib figure
    plt.figure(figsize=(8, 5))
    plt.bar(filtered_df['Player'], filtered_df[selected_metric], color='skyblue')
    plt.title(f'{selected_metric} for {selected_team}', fontsize=16)
    plt.xlabel('Player', fontsize=14)
    plt.ylabel(selected_metric, fontsize=14)
    plt.tight_layout()

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()

    # Encode the image to base64
    encoded_image = base64.b64encode(buf.getvalue()).decode('utf-8')
    buf.close()
    return f"data:image/png;base64,{encoded_image}"

# App layout
app.layout = html.Div([
    html.H1("Sports Performance Dashboard", style={'textAlign': 'center'}),

    html.Label("Select Team:"),
    dcc.Dropdown(
        id='team-dropdown',
        options=[{'label': team, 'value': team} for team in df['Team'].unique()],
        value='Team 1',
        clearable=False
    ),

    html.Label("Select Metric:"),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Matches Played', 'value': 'Matches Played'},
            {'label': 'Goals Scored', 'value': 'Goals Scored'},
            {'label': 'Assists', 'value': 'Assists'},
            {'label': 'Win Rate (%)', 'value': 'Win Rate (%)'}
        ],
        value='Goals Scored',
        clearable=False
    ),

    html.Div(id='output-graph', style={'textAlign': 'center'})
])

# Callback to update graph
@app.callback(
    Output('output-graph', 'children'),
    [Input('team-dropdown', 'value'),
     Input('metric-dropdown', 'value')]
)
def update_graph(selected_team, selected_metric):
    # Generate the Matplotlib figure as an image
    image_src = create_matplotlib_figure(selected_team, selected_metric)

    # Return an HTML <img> tag with the image source
    return html.Img(src=image_src, style={'width': '80%', 'height': 'auto', 'margin-top': '20px'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
