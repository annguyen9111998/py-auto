class SamplePage():
    name = "a"
    age = "0"
    major = "CS"
    
    def __init__(self):
        super().__init__()

    
    def make_student(self):
        self.student = SamplePage()
        print(self.student)
        print(self.age)
        print(self.major)
        print(self.name)

    def sample(self):
        print('this is sample code')
    
    @classmethod
    def sample_class_method(cls):
        return print('this is sample class method')

    
