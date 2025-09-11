import os
from abc import ABC


class Task(ABC):
    _instances = {}
    requirements = []
    failed = {}
    def __new__(cls):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
    
    def __init__(self):
        assert len(self.requirements) != 0
    
    def check_pass(self):
        fail_result = f"🔴 Task Failed! You got {len(self.failed)-len(self.requirements)} out of {len(self.requirements)}.\nYou Failed on:{[key+".\n" for key in self.failed.keys()]}"
        success_result = f"🟩 Task Completed successfully! You got {len(self.failed)-len(self.requirements)} out of {len(self.requirements)}"
        print(success_result if len(self.failed) == 0 else fail_result)


class Task01(Task):

    requirements = [
        "Environment Created",
        "NumPy installed",
        "Pandas installed",
        "matplotlib installed"
    ]

    def check_env(self):
        try:
            assert os.path.exists("../env")
            self.failed.pop(self.requirements[0], None)
            print("🟩 Passed: Created the Environment Successfully")
        except:
            self.failed[self.requirements[0]] = False
            print("🔴 It seems you haven't created the Environment, ensure you created the environment and it is named: 'env'")

    def check_numpy(self):
        try:
            import numpy
            self.failed.pop(self.requirements[1], None)
            print("🟩 Passed: Installed numpy Successfully")
        except:
            self.failed[self.requirements[1]] = False
            print("🔴 It seems you haven't installed the package: numpy, maybe try activating the environment or installing it via 'pip install'")

    def check_pandas(self):
        try:
            import pandas
            self.failed.pop(self.requirements[2], None)
            print("🟩 Passed: Installed pandas Successfully")
        except:
            self.failed[self.requirements[2]] = False
            print("🔴 It seems you haven't installed the package: pandas, maybe try activating the environment or installing it via 'pip install'")

    def check_matplotlib(self):
        try:
            import matplotlib
            self.failed.pop(self.requirements[3], None)
            print("🟩 Passed: Installed matplotlib Successfully")
        except:
            self.failed[self.requirements[3]] = False
            print("🔴 It seems you haven't installed the package: matplotlib, maybe try activating the environment or installing it via 'pip install'")


class Task02(Task):
    requirements = [
        "'my_vector' Created",
        "'my_matrix' Created",
        "Added 5 to 'my_vector'",
        "Multiplied 'my_matrix' by 2",
        "Added 'another_matrix' to 'my_matrix'",
        "Calculated 'total_earnings'",
        "Answered Question Correctly",
        "Multiplied A and B to get C",
        "Predicted House Prices"
    ]

    def check_my_vector(self, my_vector):
        try:
            import numpy as np
            np.testing.assert_array_equal(np.array([1, 2, 3, 4, 5]), my_vector)
            self.failed.pop(self.requirements[0], None)
            print("🟩 Passed: Created 'my_vector' Successfully")
        except:
            self.failed[self.requirements[0]] = False
            print("🔴 It seems you haven't created 'my_vector' variable successfully, ensure the array only contains the values required and don't change the 'dtype' of the array")

    def check_my_matrix(self, my_matrix):
        try:
            import numpy as np
            np.testing.assert_array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), my_matrix)
            self.failed.pop(self.requirements[1], None)
            print("🟩 Passed: Created 'my_matrix' Successfully")
        except:
            self.failed[self.requirements[1]] = False
            print("🔴 It seems you haven't created 'my_matrix' variable successfully, ensure the array only contains the values required and don't change the 'dtype' of the array")

    def check_added_5(self, my_vector):
        try:
            import numpy as np
            np.testing.assert_array_equal(np.array([1, 2, 3, 4, 5]) + 5, my_vector)
            self.failed.pop(self.requirements[2], None)
            print("🟩 Passed: Added 5 to 'my_vector' Successfully")
        except:
            self.failed[self.requirements[2]] = False
            print("🔴 It seems you haven't made the correct operation to 'my_vector' variable successfully, ensure you made the correct operation with an 'int' and don't change the 'dtype' of the array")

    def check_multiplied_by_2(self, my_matrix):
        try:
            import numpy as np
            np.testing.assert_array_equal(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * 2, my_matrix)
            self.failed.pop(self.requirements[3], None)
            print("🟩 Passed: Multiplied 'my_matrix' by 2 Successfully")
        except:
            self.failed[self.requirements[3]] = False
            print("🔴 It seems you haven't made the correct operation to 'my_matrix' variable successfully, ensure you made the correct operation with an 'int' and don't change the 'dtype' of the array")

    def check_added_matrices(self, result):
        try:
            import numpy as np
            np.testing.assert_array_equal(np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]]) + (np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) * 2), result)
            self.failed.pop(self.requirements[4], None)
            print("🟩 Passed: Added 'another_matrix' to 'my_matrix' Successfully")
        except:
            self.failed[self.requirements[4]] = False
            print("🔴 It seems you haven't made the correct result, ensure you made the correct operation and that you defined 'another_matrix' correctly. Note: Use the latest value of 'my_matrix' and don't redefine it")

    def check_total_earnings(self, total_earnings):
        try:
            import numpy as np
            np.testing.assert_array_equal( np.array([[100, 120, 150, 130], [200, 210, 220, 240], [50, 60, 40, 70]]) + np.array([10, 12, 15, 13]), total_earnings)
            self.failed.pop(self.requirements[5], None)
            print("🟩 Passed: Added 'another_matrix' to 'my_matrix' Successfully")
        except:
            self.failed[self.requirements[5]] = False
            print("🔴 It seems you haven't made the correct result, ensure you made the correct operation and that you haven't altered the original 'sales_data' and 'quarterly_bonus'")

    def check_answer(self, answer):
        try:
            assert answer == (3, 4)
            self.failed.pop(self.requirements[6], None)
            print("🟩 Passed: Correct Answer!")
        except:
            self.failed[self.requirements[6]] = False
            print("🔴 Incorrect, try again!")

    def check_C(self, C):
        try:
            import numpy as np
            A = np.array([[1, 2],
                        [3, 4],
                        [5, 6]])

            B = np.array([[2, 3, 4, 5],
                        [6, 7, 8, 9]])
            np.testing.assert_array_equal(A @ B, C)
            self.failed.pop(self.requirements[7], None)
            print("🟩 Passed: Multiplied A by B Successfully")
        except:
            self.failed[self.requirements[7]] = False
            print("🔴 It seems you haven't made the correct result, ensure you made the correct operation and that you haven't altered the original 'A' and 'B'")

    def check_predicted_prices(self, predicted_prices):
        try:
            import numpy as np
            X = np.array([[1500, 3],
                        [2200, 4],
                        [1200, 2]])
            
            w = np.array([300, 20000]) 
            np.testing.assert_array_equal(X @ w, predicted_prices)
            self.failed.pop(self.requirements[8], None)
            print("🟩 Passed: Predicted House prices Successfully")
        except:
            self.failed[self.requirements[8]] = False
            print("🔴 It seems you haven't made the correct result, ensure you made the correct operation and that you haven't altered the original 'X' and 'w'")


class Task03(Task):
    requirements = [
        "Loaded Titanic dataset",
        "Selected specific columns",
        "Filtered for female passengers",
        "Filtered for 1st class passengers",
        "Filled missing 'Age' values",
        "Created feature matrix X",
        "Created target vector y"
    ]

    def check_data_loaded(self, df):
        try:
            import pandas as pd
            assert isinstance(df, pd.DataFrame)
            assert df.shape == (891, 12)
            assert 'PassengerId' in df.columns
            self.failed.pop(self.requirements[0], None)
            print("🟩 Passed: Loaded the Titanic dataset successfully.")
        except:
            self.failed[self.requirements[0]] = False
            print("🔴 Failed: The DataFrame doesn't seem to be loaded correctly. Ensure you are using pd.read_csv('titanic.csv').")

    def check_column_selection(self, selected_df):
        try:
            import pandas as pd
            assert isinstance(selected_df, pd.DataFrame)
            expected_columns = ['Name', 'Sex', 'Age']
            assert all([col in selected_df.columns for col in expected_columns])
            assert len(selected_df.columns) == len(expected_columns)
            self.failed.pop(self.requirements[1], None)
            print("🟩 Passed: Selected the correct columns successfully.")
        except:
            self.failed[self.requirements[1]] = False
            print("🔴 Failed: The column selection is incorrect. Make sure you are selecting the 'Name', 'Sex', and 'Age' columns into a new DataFrame.")

    def check_female_passengers(self, female_df):
        try:
            import pandas as pd
            original_df = pd.read_csv("titanic.csv")
            expected_df = original_df[original_df['Sex'] == 'female']
            pd.testing.assert_frame_equal(female_df.reset_index(drop=True), expected_df.reset_index(drop=True))
            self.failed.pop(self.requirements[2], None)
            print("🟩 Passed: Filtered for female passengers successfully.")
        except:
            self.failed[self.requirements[2]] = False
            print("🔴 Failed: The filtering for female passengers is incorrect. Use a boolean mask: df[df['Sex'] == 'female'].")

    def check_first_class_passengers(self, first_class_df):
        try:
            import pandas as pd
            original_df = pd.read_csv("titanic.csv")
            expected_df = original_df[original_df['Pclass'] == 1]
            pd.testing.assert_frame_equal(first_class_df.reset_index(drop=True), expected_df.reset_index(drop=True))
            self.failed.pop(self.requirements[3], None)
            print("🟩 Passed: Filtered for 1st class passengers successfully.")
        except:
            self.failed[self.requirements[3]] = False
            print("🔴 Failed: The filtering for 1st class passengers is incorrect. The condition should be df['Pclass'] == 1.")

    def check_age_filled(self, age_series):
        try:
            import pandas as pd
            assert isinstance(age_series, pd.Series)
            assert not age_series.isnull().any(), "There are still missing values in the 'Age' column."
            original_df = pd.read_csv("titanic.csv")
            mean_age = original_df['Age'].mean()
            assert abs(age_series.mean() - mean_age) < 0.01 # Check if the mean is still roughly the same
            self.failed.pop(self.requirements[4], None)
            print("🟩 Passed: Filled missing 'Age' values successfully.")
        except Exception as e:
            self.failed[self.requirements[4]] = False
            print(f"🔴 Failed: The missing 'Age' values were not filled correctly. Hint: Use .fillna() with the mean of the column. Error: {e}")

    def check_X(self, X):
        try:
            import pandas as pd
            assert isinstance(X, pd.DataFrame)
            expected_columns = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
            assert all([col in X.columns for col in expected_columns]), f"Expected columns {expected_columns} not in X."
            assert 'Survived' not in X.columns, "The target variable 'Survived' should not be in X."
            assert X.shape[1] == len(expected_columns)
            self.failed.pop(self.requirements[5], None)
            print("🟩 Passed: Feature matrix 'X' created successfully.")
        except Exception as e:
            self.failed[self.requirements[5]] = False
            print(f"🔴 Failed: The feature matrix 'X' is not correct. It should be a DataFrame containing only the feature columns. Error: {e}")

    def check_y(self, y):
        try:
            import pandas as pd
            assert isinstance(y, pd.Series)
            assert y.name == 'Survived'
            assert not y.isnull().any(), "The target variable 'y' should not have any missing values."
            self.failed.pop(self.requirements[6], None)
            print("🟩 Passed: Target vector 'y' created successfully.")
        except Exception as e:
            self.failed[self.requirements[6]] = False
            print(f"🔴 Failed: The target vector 'y' is not correct. It should be a Pandas Series of the 'Survived' column. Error: {e}")


task01 = Task01()
task02 = Task02()
task03 = Task03()