from typing import *

class Lecture():
    def __init__(self, day, hour):
        self.day = day
        self.hour = hour

    def getLectureHash(self):
        return self.day+self.hour

class Discipline:
    def __init__(self, name, firstDay, secondDay, startHourFirstDay, startHourSecondDay):
        self.name = name
        self.firstLecture = Lecture(firstDay, startHourFirstDay)
        self.secondLecture = Lecture(secondDay, startHourSecondDay)

class Combinator:
    def __init__(self, disciplines: List[Discipline]):
        self.disciplines = disciplines

    def bicliqueCombinator(self):
        counter = 1
        for i in range (len(self.disciplines)):
            for j in range (i+1,len(self.disciplines)):
                if self.disciplines[i] != self.disciplines[j] and (not self.__areComflictantSubjects(self.disciplines[i],self.disciplines[j])):
                    print(f"•{counter}° possibility: {self.disciplines[i].name} + {self.disciplines[j].name}")

                    print(f"\t{self.disciplines[i].name} info:")
                    print(f"\t\t◦{self.disciplines[i].firstLecture.day} by {self.disciplines[i].firstLecture.hour}")
                    print(f"\t\t◦{self.disciplines[i].secondLecture.day} by {self.disciplines[i].secondLecture.hour}")

                    print(f"\t{self.disciplines[j].name} info:")
                    print(f"\t\t◦{self.disciplines[j].firstLecture.day} by {self.disciplines[j].firstLecture.hour}")
                    print(f"\t\t◦{self.disciplines[j].secondLecture.day} by {self.disciplines[j].secondLecture.hour}")

                    print("-=-=-=-=-=-=-=-=-=-=-=-")
                    counter +=1

    def __areComflictantSubjects(self, firstDiscipline, secondDiscipline):
        firstIds = [firstDiscipline.firstLecture.getLectureHash(), firstDiscipline.secondLecture.getLectureHash()]
        secondIds = [secondDiscipline.firstLecture.getLectureHash(), secondDiscipline.secondLecture.getLectureHash()]
        
        for firstId in firstIds:
            if firstId in secondIds:
                return True
        
        return False

discipline1 = Discipline("Data Structures", "Monday", "Tuesday", "13:30", "15:30")
discipline2 = Discipline("Algorithms", "Wednesday", "Thursday", "13:30", "13:30")
discipline3 = Discipline("Operating Systems", "Monday", "Friday", "15:30", "13:30")
discipline4 = Discipline("Networks", "Tuesday", "Thursday", "15:30", "15:30")
discipline5 = Discipline("Database Systems", "Wednesday", "Friday", "13:30", "15:30")
d6 = discipline5 = Discipline("Photoshop", "Monday", "Tuesday", "15:30", "15:30")
d7 = discipline5 = Discipline("CV1", "Monday", "Tuesday", "13:30", "13:30")

discipline6 = Discipline("Machine Learning", "Monday", "Wednesday", "13:30", "15:30")
discipline7 = Discipline("Artificial Intelligence", "Tuesday", "Friday", "15:30", "15:30")
discipline8 = Discipline("Software Engineering", "Monday", "Tuesday", "13:30", "13:30")
discipline9 = Discipline("Computer Graphics", "Thursday", "Friday", "13:30", "15:30")
discipline10 = Discipline("Cybersecurity", "Wednesday", "Thursday", "15:30", "13:30")

disciplines = [discipline1,discipline2,discipline3,discipline4,discipline5,d6,d7]#,discipline6,discipline7,discipline8,discipline9,discipline10]

myCombinator = Combinator(disciplines)
myCombinator.bicliqueCombinator()