class Student:
    def __init__(self, student_id: int, first_name: str,last_name: str):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.exam_scores = []

    def add_score(self, score):
        while True:
            if 0 < score <= 100:
                self.exam_scores.append(score)
                return self.exam_scores
            else:
                print("ocenka vishe 100 ballov")
                score = int(input("vvedi ocenku: "))


    def show_scores(self):
        my_string = ", ".join(map(str,self.exam_scores))
        print(my_string)

    def score_average(self):
        if self.exam_scores != 0:
            summa = sum(self.exam_scores)
            len_o = len(self.exam_scores)
            average = summa / len_o
            return f'average score is {average}'
        else:
            print(f' Student {self.first_name} {self.last_name} has not yet passed any exams')

    def course_passed(self):
        if sum(self.exam_scores) > 60:
            return True
        else:
            return False

student_1 =  Student(1,"John","Doe")
student_1.add_score(100)
student_1.add_score(95)
student_1.show_scores()
print(student_1.score_average())
print(student_1.course_passed())
student_2 =  Student(2,"Linda","Jones")
student_2.add_score(25)
student_2.add_score(65)
student_2.add_score(80)
student_2.add_score(75)
student_2.show_scores()
print(student_2.score_average())
print(student_2.course_passed())
