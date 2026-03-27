# Purpose: contains the tests for the controller of the best QR code generator application.
# Authors: Bryan Crombach

from best_qr_code_generator.controllers.controller import on_enter


class TestController:
    """
    Class that contains the tests for the controller of the best QR code generator application.
    """

    def test_on_enter(self, setup_gui):
        """
        Test the on_enter controller function.

        assertions:
        - The save button is enabled after calling the on_enter function.
        - The image widget contains a valid pixmap after calling the on_enter function.
        - The pixmap in the image widget has a width greater than 0 after calling the on_enter function.
        - The pixmap in the image widget has a height greater than 0 after calling the on_enter function.

        :param setup_gui: Fixture that sets up the GUI for the tests.
        """
        on_enter("google.com", setup_gui.rect.image, setup_gui.save_button)

        assert setup_gui.save_button.isEnabled()
        assert setup_gui.rect.image.pixmap() is not None
        assert not setup_gui.rect.image.pixmap().isNull()
        assert setup_gui.rect.image.pixmap().size().width() > 0
        assert setup_gui.rect.image.pixmap().size().height() > 0
