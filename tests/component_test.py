# Purpose: contains the tests for the components of the best QR code generator application.
# Authors: Bryan Crombach
from PyQt6.QtCore import Qt
from unittest.mock import patch


class TestComponents:
    """
    Test the components of the application.
    """

    def test_rect(self, setup_gui):
        """
        Test the Rect component to ensure it is initialized correctly and has valid dimensions.

        assertions:
        - The Rect component's rect attribute is not None.
        - The Rect component's rect has a width greater than 0.
        - The Rect component's rect has a height greater than 0.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.rect is not None
        assert setup_gui.rect.width() > 0
        assert setup_gui.rect.height() > 0
        assert setup_gui.rect.width() == setup_gui.rect.height()

        assert setup_gui.rect.get_image_widget() is not None

    def test_title(self, setup_gui):
        """
        Test the Title component to ensure it is initialized correctly.

        assertions:
        - The Title component's title attribute is not None.
        - The Title component's title text is not empty.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.title is not None
        assert setup_gui.title.text() != ""

    def test_qr_image(self, setup_gui, sample_qr_code):
        """
        Test the QRImage component to ensure it is initialized correctly.

        assertions:
        - The QRImage component's image attribute is not None.
        - The QRImage component's image has a width greater than 0.
        - The QRImage component's image has a height greater than 0.
        - The QRImage component's image is square (i.e., width equals height).
        - The initial QRImage component's image pixmap is not None.
        - The initial QRImage component's image pixmap is null (i.e., it does not contain valid image data).
        - The initial QRImage component's image pixmap has a width of 0.
        - The initial QRImage component's image pixmap has a height of 0.
        - The QRImage component's get_pixmap method returns a non-None value.

        - After setting the pixmap of the QRImage component to a sample QR code, the pixmap is not null and has valid dimensions.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.rect.image is not None
        assert setup_gui.rect.image.width() > 0
        assert setup_gui.rect.image.height() > 0
        assert setup_gui.rect.image.width() == setup_gui.rect.image.width()

        assert setup_gui.rect.image.pixmap() is not None
        assert setup_gui.rect.image.pixmap().isNull()
        assert setup_gui.rect.image.pixmap().size().width() == 0
        assert setup_gui.rect.image.pixmap().size().height() == 0

        assert setup_gui.rect.image.get_pixmap() is not None

        # change the pixmap of the image widget to the sample QR code and check if it is set correctly
        setup_gui.rect.image.set_pixmap(sample_qr_code)

        assert setup_gui.rect.image.pixmap() is not None
        assert not setup_gui.rect.image.pixmap().isNull()
        assert setup_gui.rect.image.pixmap().size().width() > 0
        assert setup_gui.rect.image.pixmap().size().height() > 0
        assert (
            setup_gui.rect.image.pixmap().size().width()
            == setup_gui.rect.image.pixmap().size().height()
        )

    def test_input_field(self, qtbot, setup_gui):
        """
        Test the InputField component to ensure it is initialized correctly.

        assertions:
        - The InputField component's input_field attribute is not None.
        - The InputField component's input_field text is empty by default.
        - The InputField component's input_field has a non-empty placeholder text.
        - After simulating user input, the InputField component's input_field text is updated correctly
        - After clearing the InputField component's input_field, the text is empty again.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.input_field is not None
        assert setup_gui.input_field.text() == ""
        assert setup_gui.input_field.placeholderText() != ""

        qtbot.keyClicks(setup_gui.input_field, "google.com")
        assert setup_gui.input_field.text() == "google.com"

        setup_gui.input_field.clear()
        assert setup_gui.input_field.text() == ""

    def test_save_button(self, qtbot, setup_gui):
        """
        Test the SaveButton component to ensure it is initialized correctly.

        assertions:
        - The SaveButton component's save_button attribute is not None.
        - The SaveButton component's save_button is disabled by default.
        - After simulating a click on the EnterButton component, the save_button is enabled.
        - After simulating a click on the SaveButton component, a file dialog is opened to save the generated QR code.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.save_button is not None
        assert not setup_gui.save_button.isEnabled()

        qtbot.mouseClick(setup_gui.enter_button, Qt.MouseButton.LeftButton)
        assert setup_gui.save_button.isEnabled()

        with patch(
            "best_qr_code_generator.views.components.SaveButton.QFileDialog.getSaveFileName"
        ) as mock_dialog:
            mock_dialog.return_value = ("test.png", "PNG Files (*.png)")
            qtbot.mouseClick(setup_gui.save_button, Qt.MouseButton.LeftButton)
            assert mock_dialog.called

    def test_enter_button(self, qtbot, setup_gui):
        """
        Test the EnterButton component to ensure it is initialized correctly.

        assertions:
        - The EnterButton component's enter_button attribute is not None.
        - After simulating a click on the EnterButton component, the QR code is generated and displayed in the Rect component's image widget.
        - After simulating a click on the EnterButton component, the SaveButton component is enabled.

        :param setup_gui: fixture that sets up the GUI for the tests.
        """
        assert setup_gui.enter_button is not None

        qtbot.keyClicks(setup_gui.input_field, "google.com")
        qtbot.mouseClick(setup_gui.enter_button, Qt.MouseButton.LeftButton)

        assert not setup_gui.rect.image.pixmap().isNull()
        assert setup_gui.rect.image.pixmap().size().width() > 0
        assert setup_gui.rect.image.pixmap().size().height() > 0
        assert (
            setup_gui.rect.image.pixmap().size().width()
            == setup_gui.rect.image.pixmap().size().height()
        )

        assert setup_gui.save_button.isEnabled()
