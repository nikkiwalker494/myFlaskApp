from datetime import datetime
from flask import template_rendered
from contextlib import contextmanager
from app import create_app

import pytest
import re

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)

@pytest.fixture
def client():
    app = create_app()
    with app.test_client() as client:
        yield client

def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200

def test_home_page_context(client):
    app = client.application
    with captured_templates(app) as templates:
        response = client.get('/')
        template, context = templates[0]
        assert 'date' in context
        date_string = context['date']
        assert re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", date_string)

# def test_home_page_context(client):
#     app = client.application
#     with captured_templates(app) as templates:
#         response = client.get('/')
#         template, context = templates[0]
#         assert 'date' in context

 