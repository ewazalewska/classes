class Project:
    def __init__(self, building, localization, inwestor, authors):
        self.building = building
        self.localization = localization
        self.inwestor = inwestor,
        self.authors = authors

dom = Project('house', 'Lublin', 'Narkiewicz', 'zespół 1')
print(dom.building)