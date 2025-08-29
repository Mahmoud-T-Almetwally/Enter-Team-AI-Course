import os
from abc import ABC

class Task(ABC):
    _instances = {}
    got_right = 0
    num_requirements = 0
    def __new__(cls):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    def check_pass(self):
        fail_result = f"🔴 Task Failed! You got {self.got_right} out of {self.num_requirements}"
        success_result = f"🟩 Task Completed successfully! You got {self.got_right} out of {self.num_requirements}"
        print(success_result if self.got_right == self.num_requirements else fail_result)

class Task01(Task):

    num_requirements = 4

    def check_env(self):
        try:
            assert os.path.exists("../env") 
            print("🟩 Passed: Created the Environment Successfully")
            self.got_right += 1
        except:
            print("🔴 It seems you haven't created the Environment, ensure you created the environment and it is named: 'env'")

    def check_numpy(self):
        try:
            import numpy
            print("🟩 Passed: Installed numpy Successfully")
            self.got_right += 1
        except:
            print("🔴 It seems you haven't installed the package: numpy, maybe try activating the environment or installing it via 'pip install'")

    def check_pandas(self):
        try:
            import pandas
            print("🟩 Passed: Installed pandas Successfully")
            self.got_right += 1
        except:
            print("🔴 It seems you haven't installed the package: pandas, maybe try activating the environment or installing it via 'pip install'")

    def check_matplotlib(self):
        try:
            import matplotlib
            print("🟩 Passed: Installed matplotlib Successfully")
            self.got_right += 1
        except:
            print("🔴 It seems you haven't installed the package: matplotlib, maybe try activating the environment or installing it via 'pip install'")

task01 = Task01()