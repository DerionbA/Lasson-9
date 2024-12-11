class student:
    grade = 10
    name = "Derion"

    def intro(self):
        print("hi i am a student")


    def detail(self): 
        print("my name is ", self.name)
        print("i am in grade", self.grade)

ob = student()
ob.intro()
ob.detail()