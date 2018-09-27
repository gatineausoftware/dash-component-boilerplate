from .IntegrationTests import IntegrationTests
import dash
import dash_html_components as html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from {{cookiecutter.project_slug}} import {{cookiecutter.component_name}} # pylint: disable=no-name-in-module


class Tests(IntegrationTests):
    def test_render_component(self):
        app = dash.Dash(__name__)
        app.layout = html.Div([
            html.Div(id='waitfor'),
            {{cookiecutter.component_name}}(label='Example Component Label')
        ])

        self.startServer(app)

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "waitfor"))
        )

        self.percy_snapshot('Simple Render')
