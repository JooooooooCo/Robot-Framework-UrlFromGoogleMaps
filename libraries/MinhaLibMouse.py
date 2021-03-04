import pywinauto
"""Lib para controle de mouse e teclado de acordo com pywinauto - Somente Windows"""

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def my_mouse(
        self,
        locator: str = None,
        x: int = 0,
        y: int = 0,
        off_x: int = 0,
        off_y: int = 0,
        image: str = None,
        method: str = "locator",
        ctype: str = "click",
    ) -> None:
        """Mouse click `locator`, `coordinates`, or `image`

        When using method `locator`,`image` or `ocr` mouse is clicked by default at
        center coordinates.

        Click types are:

        - `click` normal left button mouse click
        - `double`
        - `right`

        :param locator: element locator on active window
        :param x: coordinate x on desktop
        :param y: coordinate y on desktop
        :param off_x: offset x (used for locator and image clicks)
        :param off_y: offset y (used for locator and image clicks)
        :param image: image to click on desktop
        :param method: one of the available methods to mouse click, default "locator"
        :param ctype: type of mouse click
        """
        self.logger.info("Mouse click: %s", locator)

        if method == "locator":
            element, _ = self.find_element(locator)
            if element and len(element) == 1:
                x, y = self.get_element_center(element[0])
                self.click_type(x + off_x, y + off_y, ctype)
            else:
                raise ValueError(f"Could not find unique element for '{locator}'")
        elif method == "coordinates":
            self.mouse_click_coords(x, y, ctype)
        elif method == "image":
            self.mouse_click_image(image, off_x, off_y, ctype)

    def click_type(
        self, x: int = None, y: int = None, click_type: str = "click"
    ) -> None:
        """Mouse click on coordinates x and y.

        Default click type is `click` meaning `left`

        :param x: horizontal coordinate for click, defaults to None
        :param y: vertical coordinate for click, defaults to None
        :param click_type: "click", "right" or "double", defaults to "click"
        :raises ValueError: if coordinates are not valid
        """
        self.logger.info("Click type '%s' at (%s, %s)", click_type, x, y)
        if (x is None and y is None) or (x < 0 or y < 0):
            raise ValueError(f"Can't click on given coordinates: ({x}, {y})")
        if click_type == "click":
            pywinauto.mouse.click(coords=(x, y))
        elif click_type == "double":
            pywinauto.mouse.double_click(coords=(x, y))
        elif click_type == "right":
            pywinauto.mouse.right_click(coords=(x, y))