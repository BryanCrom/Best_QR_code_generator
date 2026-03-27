# Purpose: contains the tests for the view of the best QR code generator application.
# Authors: Bryan Crombach

class TestView:
    """
    Class that contains the tests for the view of the best QR code generator application.
    """

    def test_home_view_initialization(self, setup_gui):
        """
        Test the initialization of the HomeView to ensure that the GUI components are set up correctly.

         assertions:
         - The HomeView window is visible after initialization.

        :param setup_gui: Fixture that sets up the GUI for the tests.
        """
        assert setup_gui.isVisible()
