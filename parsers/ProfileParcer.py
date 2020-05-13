from bs4 import BeautifulSoup

from locators.ProfileStructure import ProfileStructure


class ProfileParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def getDetails(self):
        locator = ProfileStructure.STRUCTURE
        details = self.parent.select(locator)
        return details
