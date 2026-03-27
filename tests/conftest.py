# Purpose: contains the fixture that sets up the GUI for the tests of the best QR code generator application.
# Authors: Bryan Crombach

import pytest
from PyQt6.QtGui import QImage

from best_qr_code_generator.models.qr_generator import create_qr_code
from best_qr_code_generator.views.HomeView import HomeView


@pytest.fixture
def setup_gui(qtbot):
    """
    Fixture that sets up the GUI for the tests.

    :param qtbot: Pytest-qt bot for simulating user interactions with the GUI.
    """

    window = HomeView()
    qtbot.addWidget(window)
    window.show()
    yield window

@pytest.fixture
def sample_qr_code() -> QImage:
    """
    Fixture to create a sample QR code for testing.

    :return (QImage): A sample QR code image.
    """
    return create_qr_code("google.com")