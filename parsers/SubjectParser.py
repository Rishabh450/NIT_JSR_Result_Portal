from bs4 import BeautifulSoup
from locators.ProfileLocator import ProfileLocator


class SubjectParser:
    def __init__(self,parent):
        self.parent = parent

    @property
    def getSubjectDetails(self):
        locator = ProfileLocator.SUBJECT_DETAILS
        return self.parent.select(locator)
