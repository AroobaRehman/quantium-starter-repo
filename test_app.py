import pytest
from dash import Dash
from app import app

@pytest.fixture
def dash_app():
    return app

def test_header_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    header = dash_duo.find_element('#app-header')
    assert header is not None
    assert header.text == "Pink Morsel Sales"

def test_graph_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    graph = dash_duo.find_element('#sales-graph')
    assert graph is not None

def test_radio_picker_is_present(dash_duo, dash_app):
    dash_duo.start_server(dash_app)
    radio_group = dash_duo.find_element("#radio-item")
    assert radio_group is not None