
def clearContent(grid):
    newGrid = []
    for cont in grid:
        if cont == '无':
            break
        newGrid.append(cont)
    return newGrid


class Entries():
    Entries_id = 0
    Entries_name = ''
    Entries_school = ''
    Entries_classifed = ''
    Entries_author = []
    Entries_teacher = []
    Entries_award = ''

    def __init__(self, id, name, school, classifed, author, teacher:list, award):
        self.Entries_id = str(int(id))
        self.Entries_name = name
        if self.Entries_name[0] == '《' and self.Entries_name[-1] == '》':
            self.Entries_name = self.Entries_name[1:-1]     # 修正作品名加书名号的形式
        self.Entries_school = school
        self.Entries_classifed = classifed
        self.Entries_author = clearContent(author)
        self.Entries_teacher = clearContent(teacher)
        self.Entries_award = award[0]


