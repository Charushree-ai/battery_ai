import os
import base64
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

def encode_image(image_filename):
    with open(image_filename, 'rb') as f:
        image = f.read()
    return base64.b64encode(image).decode('utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
img_path = os.path.join(BASE_DIR, 'assets/gaston_plante.jpg')
img_src = "data:image/jpeg;base64," + encode_image(img_path)
img_path_wall = os.path.join(BASE_DIR, 'assets/ai_wall.jpg')
img_src_wall = "data:image/jpeg;base64," + encode_image(img_path_wall)

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
                 html.P("Researcher : Charushree K S", style={'textAlign': 'right', 'color': 'white'}),
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

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "value"),
)
def render_tab_content(tab):
    print("hello",tab)
    if tab == "Battery History" or tab =="tab-1":
        return html.Div([
            html.H3("History of Batteries", style={'text-align': 'center', "color": "black"}),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            [
                                html.P(f"Year: {event['Year']}"),
                                html.P(f"{event['Event']}  Type :  {event['Battery_Type']}"),
                                html.Hr(),
                            ]
                        ), width="100vp", style={"textAlign": "center", "color": "black"})
                    for event in battery_discovery_data]
            ),

        ])
    elif tab == "Artificial ageing":
        return html.Div([
            html.Hr(),
            html.Hr(),
            dbc.Row([
                dbc.Col([
                    html.H4("Artificial ageing factors which effect the battery life", style={'color': 'black'}),
                    bar_chart,

                ], width=6),
                dbc.Col(
                    [
                        html.H4("Battery Usage in Different Domains", style={'color': 'black'}),
                        pie_chart,
                    ]
                )
            ])
        ])
    elif tab == "AI":
        return html.Div([
            dbc.Container([
                html.Hr(),
                html.Hr(),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Early Days (Pre-2000s)", style={'background-color': '#B3E0FF'}),
                            dbc.CardBody([
                                html.P("Basic battery monitoring systems used in telecommunications and UPS."),
                                html.P("Simple models and rule-based approaches for battery health estimation."),
                                html.P("Introduction of basic battery management systems in EVs."),
                            ]),
                        ]),
                        width=9)]),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("2000s", style={'background-color': '#B3E0FF'}),
                            dbc.CardBody([
                                html.P(
                                    "Adoption of battery monitoring in aviation, aerospace, and telecommunications."),
                                html.P("Application of SVMs and NNs to battery monitoring."),
                                html.P("Advanced battery management systems in hybrid and electric vehicles."),
                            ]),
                        ]),
                        width=9),
                ]),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("2010s", style={'background-color': '#B3E0FF'}),
                            dbc.CardBody([
                                html.P("Rise of lithium-ion batteries in consumer electronics and renewable energy."),
                                html.P(
                                    "Widespread use of ML in renewable energy applications and industrial batteries."),
                                html.P(
                                    "Integration of ML in EVs for battery health prediction and thermal management."),
                            ]),
                        ]),
                        width=9)]),
                dbc.Row([
                    dbc.Col(
                        dbc.Card([
                            dbc.CardHeader("Recent Advances (2020s and Beyond)", style={'background-color': '#B3E0FF'}),
                            dbc.CardBody([
                                html.P("Continued advancements in AI and ML in various sectors."),
                                html.P(
                                    "Integration of AI and ML in renewable energy, consumer electronics, and industrial batteries."),
                                html.P("Edge computing and IoT for real-time battery monitoring."),
                            ]),
                        ]),
                        width=9),
                ]),
            ]),
        ])
    elif tab == "Self interest":
        return html.Div([html.P("Batteries store power and are widely utilized across various fields"),
                         html.P("To maximize the longevity of a battery, maintenance is essential."),
                         html.P(
                             "Implementing a battery monitoring system is crucial and advantageous to preserving its optimal lifespan"),
                         html.P("Where as Artificial intelligence is considered as the new electricity, "
                                "It is widely used in different fields to find new solutions"),
                         html.P("The usage of ML models has increased the BMS efficieny and performance."
                                " This is an effort to research in this area"),
                         dbc.Row(
                                [
                                dbc.Col([
                                html.H5("In 2020, Studying about battery"),
                                html.Img(src=img_src, style={'width': '350px', 'height': '350px'})], width=6),
                                dbc.Col([
                                html.H5("In 2016, As my wall shows my inclination towards AI and Python"),
                                html.Img(src=img_src_wall, style={'width': '400px', 'height': '300px'})], width=6)
                                ])
                         ], style={'color': 'black'})
if __name__ == "__main__":
    app.run_server(debug=True)
