import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

battery_discovery_data = [
    {"Year": 1800, "Event": "Alessandro Volta invents the Voltaic Pile", "Battery_Type": "[Zn-Cu]"},
    {"Year": 1836, "Event": "John F. Daniell invents the Daniell Cell", "Battery_Type": "[Zn-Cu]"},
    {"Year": 1859, "Event": "Gaston Plante invents the lead-acid battery", "Battery_Type": "[Pb]"},
    {"Year": 1866, "Event": "Georges Leclanché invents the Leclanche cell", "Battery_Type": "[Zn-MnO2]"},
    {"Year": 1887, "Event": "Carl Gassner invents the dry cell battery", "Battery_Type": "[Zn-MnO2]"},
    {"Year": 1899, "Event": "Waldemar Jungner develops the nickel-cadmium (NiCd) battery", "Battery_Type": "[Ni-Cd]"},
    {"Year": 1949, "Event": "John Goodenough invents the lithium battery cathode", "Battery_Type": "[Li]"},
    {"Year": 1971, "Event": "Stanley Whittingham develops the first lithium-ion battery", "Battery_Type": "[Li]"},
]

# Data for the pie chart
domains = ["Consumer Electronics", "Electric Vehicles", "Renewable Energy", "Aerospace", "Industrial", "Other"]
battery_usage = [40, 25, 20, 5, 8, 2]  # Example percentages (you can adjust these)

# Create the pie chart
pie_chart = dcc.Graph(
    figure={
        "data": [
            go.Pie(
                labels=domains,
                values=battery_usage,
                hole=0.4,
                hoverinfo="label+percent",
                textinfo="value",
                marker={"colors": ['#FFA07A', '#7B68EE', '#87CEEB', '#FFD700', '#32CD32', '#D3D3D3']},
            ),
        ],
        "layout": go.Layout(title="Usage of Batteries in Different Domains"),
    },
)

factors = ["Temperature", "Charge/Discharge Cycles", "Depth of Discharge", "Current", "Chemistry"]
impact_scores = [90, 80, 70, 60, 50]  # Example impact scores (you can adjust these)

# Create the bar chart
bar_chart = dcc.Graph(
    figure={
        "data": [
            go.Bar(
                x=factors,
                y=impact_scores,
                marker_color=['#FFA07A', '#7B68EE', '#87CEEB', '#FFD700', '#32CD32'],
            ),
        ],
        "layout": go.Layout(
            title="Artificial ageing factors which effect the battery life",
            xaxis={"title": "Factors"},
            yaxis={"title": "Score"},
        ),
    },
)

app.layout = html.Div(
    [
        dbc.Row([html.H1("BATTERIES"),
                 html.P("Research : Charushree K S", style={'textAlign': 'right', 'color': 'white'}),
                 html.P("Contact : charudalu@gmail.com", style={'textAlign': 'right', 'color': 'white'})
                 #  dcc.Markdown('''
                 #         Researcher [Charushree K S](https://www.linkedin.com/in/k-s-charushree).
                 #     ''', style={'textAlign':'right','color':'white'})
                 ],
                style={'background-color': '#0CAFFF', "textAlign": "center", "height": "16vh", 'border': '3px',
                       'padding': '10px', 'color': 'white'}),
        dbc.Row(
            [
                dbc.Col(
                    dcc.Tabs(id="tabs", value="tab-1", children=[
                        dcc.Tab(label="Battery History", value="Battery History",
                                style={'background-color': '#B3E0FF', "height": "25vh", "color": "white",
                                       'width': '465px'}),
                        dcc.Tab(label="Artificial ageing", value="Artificial ageing",
                                style={'background-color': '#B3E0FF', "height": "25vh", "color": "white",
                                       'width': '465px'}),
                        dcc.Tab(label="AI in battery monitoring system", value="AI",
                                style={'background-color': '#B3E0FF', "height": "25vh", "color": "white",
                                       'width': '465px'}),
                        dcc.Tab(label="Self interest", value="Self interest",
                                style={'background-color': '#B3E0FF', "height": "25vh", "color": "white",
                                       'width': '465px'})
                    ], vertical=True
                             ), width=3, style={'background-color': '#B3E0FF', "height": "100vh", "color": "white"}),
                dbc.Col(html.Div(id="tab-content"),
                        style={'background-color': '#E6F7FF', "height": "100vh", "color": "white"}),
            ]
        )
    ],
    style={"height": "100vh"}
)


if __name__ == "__main__":
    app.run_server(debug=True)
