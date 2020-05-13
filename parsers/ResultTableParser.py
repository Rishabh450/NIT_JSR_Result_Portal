from bs4 import BeautifulSoup
from locators.ProfileLocator import ProfileLocator


class ResultsTableParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def getSemesterStatus(self):
        locator = ProfileLocator.SEM_STATUS
        scores = []
        for score in self.parent.select(locator):
            if score.string is None:
                string = str(score)
                # print(string)
                newScore = BeautifulSoup(string, 'html.parser')
                status = newScore.select_one('td span')
                sem = status.attrs["semester"]
                scores.append(sem)
                scores.append(status.text)

            else:
                scores.append(score.string)

        return scores

    @property
    def getAllSubjects(self):
        locator = ProfileLocator.ALL_SUBJECT_TABLE_IN_SEMESTER
        return self.parent.select(locator)
