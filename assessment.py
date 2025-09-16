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
        fail_result = f"🔴 Task Failed! You got {len(self.requirements)-len(self.failed)} out of {len(self.requirements)}.\nYou Failed on:\n{[key+".\n" for key in self.failed.keys()]}"
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


class Task04(Task):
    requirements = [
        "Loaded the dataset",
        "Handled missing bedroom values",
        "Performed one-hot encoding",
        "Created feature matrix X",
        "Created target vector y",
        "Split the data into training and testing sets",
        "Trained the Linear Regression model",
        "Calculated the Mean Absolute Error"
    ]

    def check_data_loaded(self, df):
        try:
            import pandas as pd
            assert isinstance(df, pd.DataFrame)
            assert df.shape == (20640, 10)
            assert 'median_house_value' in df.columns
            self.failed.pop(self.requirements[0], None)
            print("🟩 Passed: Loaded the California Housing dataset successfully.")
        except:
            self.failed[self.requirements[0]] = False
            print("🔴 Failed: The DataFrame does not seem to be loaded correctly. Ensure you use pd.read_csv('california_housing.csv').")

    def check_bedrooms_filled(self, df):
        try:
            assert not df['total_bedrooms'].isnull().any(), "There are still missing values in 'total_bedrooms'."
            assert 455 < df['total_bedrooms'].mean() < 465, "The mean of the 'total_bedrooms' column seems incorrect. Did you use the correct mean after removing outliers to fill the NaNs?"
            self.failed.pop(self.requirements[1], None)
            print("🟩 Passed: Missing 'total_bedrooms' values handled correctly.")
        except Exception as e:
            self.failed[self.requirements[1]] = False
            print(f"🔴 Failed: The missing values in 'total_bedrooms' were not handled correctly. {e}")

    def check_one_hot_encoding(self, df):
        try:
            expected_ohe_cols = ['<1H OCEAN', 'INLAND', 'ISLAND', 'NEAR BAY', 'NEAR OCEAN']
            assert 'ocean_proximity' not in df.columns, "The original 'ocean_proximity' column should be removed."
            assert all([col in df.columns for col in expected_ohe_cols]), "One or more one-hot encoded columns are missing."
            self.failed.pop(self.requirements[2], None)
            print("🟩 Passed: One-hot encoding performed successfully.")
        except Exception as e:
            self.failed[self.requirements[2]] = False
            print(f"🔴 Failed: The one-hot encoding step was not performed correctly. {e}")
            
    def check_X_creation(self, X):
        try:
            import pandas as pd
            assert isinstance(X, pd.DataFrame)
            assert 'median_house_value' not in X.columns, "The target variable 'median_house_value' should not be in X."
            assert X.shape[1] == 13, f"X should have 13 feature columns, but it has {X.shape[1]}."
            self.failed.pop(self.requirements[3], None)
            print("🟩 Passed: Feature matrix 'X' created successfully.")
        except Exception as e:
            self.failed[self.requirements[3]] = False
            print(f"🔴 Failed: The feature matrix 'X' is not correct. {e}")

    def check_y_creation(self, y):
        try:
            import pandas as pd
            assert isinstance(y, pd.Series)
            assert y.name == 'median_house_value', "The target vector y should be the 'median_house_value' Series."
            assert y.shape == (20640,), f"y has an incorrect shape: {y.shape}"
            self.failed.pop(self.requirements[4], None)
            print("🟩 Passed: Target vector 'y' created successfully.")
        except Exception as e:
            self.failed[self.requirements[4]] = False
            print(f"🔴 Failed: The target vector 'y' is not correct. {e}")

    def check_data_split(self, X_train, X_test, y_train, y_test):
        try:
            assert X_train.shape == (16512, 13), f"X_train has incorrect shape: {X_train.shape}"
            assert X_test.shape == (4128, 13), f"X_test has incorrect shape: {X_test.shape}"
            assert y_train.shape == (16512,), f"y_train has incorrect shape: {y_train.shape}"
            assert y_test.shape == (4128,), f"y_test has incorrect shape: {y_test.shape}"
            self.failed.pop(self.requirements[5], None)
            print("🟩 Passed: Data split into training and testing sets successfully.")
        except Exception as e:
            self.failed[self.requirements[5]] = False
            print(f"🔴 Failed: The data split is incorrect. Ensure you used test_size=0.2 and the correct variable order. {e}")

    def check_model_trained(self, model):
        try:
            from sklearn.linear_model import LinearRegression
            from sklearn.exceptions import NotFittedError
            assert isinstance(model, LinearRegression)
            # Check if the model is fitted by accessing an attribute that only exists after fitting
            model.predict([[0]*13])
            self.failed.pop(self.requirements[6], None)
            print("🟩 Passed: Linear Regression model trained successfully.")
        except NotFittedError:
            self.failed[self.requirements[6]] = True
            print("🔴 Failed: The model has been instantiated but not trained. Remember to call the .fit() method.")
        except Exception as e:
            self.failed[self.requirements[6]] = True
            print(f"🔴 Failed: There was an issue with the model training. {e}")

    def check_mae(self, mae_score):
        try:
            assert 45000 < mae_score < 55000, f"The MAE score ({mae_score}) is outside the expected range. Check your data preparation and model training steps."
            self.failed.pop(self.requirements[7], None)
            print(f"🟩 Passed: MAE calculated successfully. Your model is, on average, off by ~${mae_score:,.2f}.")
        except:
            self.failed[self.requirements[7]] = False
            print("🔴 Failed: The MAE calculation is incorrect or the value is unexpected. Ensure you are comparing y_test and your predictions.")


class Task05(Task):
    requirements = [
        "Loaded and cleaned the data",
        "Created feature matrix X and target vector y",
        "Split the data into training and testing sets",
        "Trained the Logistic Regression model",
        "Calculated Logistic Regression accuracy",
        "Trained the K-Nearest Neighbors model",
        "Calculated K-Nearest Neighbors accuracy"
    ]

    def check_data_cleaned(self, df):
        try:
            import pandas as pd
            assert isinstance(df, pd.DataFrame)
            assert df.shape[0] == 889, "The number of rows is incorrect. Did you drop the rows with missing 'Embarked' values?"
            assert df.shape[1] == 11, "The number of columns is incorrect after cleaning and one-hot encoding."
            assert 'PassengerId' not in df.columns, "The 'PassengerId' column should be dropped."
            assert not df.isnull().values.any(), "There are still missing values in the DataFrame."
            self.failed.pop(self.requirements[0], None)
            print("🟩 Passed: Data loaded and cleaned successfully.")
        except Exception as e:
            self.failed[self.requirements[0]] = False
            print(f"🔴 Failed: The data cleaning process was not completed correctly. {e}")

    def check_X_y_creation(self, X, y):
        try:
            import pandas as pd
            assert isinstance(X, pd.DataFrame)
            assert isinstance(y, pd.Series)
            assert 'Survived' not in X.columns, "The target variable 'Survived' should not be in X."
            assert X.shape == (889, 10), f"X has an incorrect shape: {X.shape}. It should be (889, 10)."
            assert y.shape == (889,), f"y has an incorrect shape: {y.shape}."
            assert y.name == 'Survived', "The target vector y should be the 'Survived' Series."
            self.failed.pop(self.requirements[1], None)
            print("🟩 Passed: Feature matrix 'X' and target vector 'y' created successfully.")
        except Exception as e:
            self.failed[self.requirements[1]] = False
            print(f"🔴 Failed: The creation of X and y is incorrect. {e}")

    def check_data_split(self, X_train, X_test, y_train, y_test):
        try:
            assert X_train.shape == (711, 10), f"X_train has incorrect shape: {X_train.shape}"
            assert X_test.shape == (178, 10), f"X_test has incorrect shape: {X_test.shape}"
            assert y_train.shape == (711,), f"y_train has incorrect shape: {y_train.shape}"
            assert y_test.shape == (178,), f"y_test has incorrect shape: {y_test.shape}"
            self.failed.pop(self.requirements[2], None)
            print("🟩 Passed: Data split into training and testing sets successfully.")
        except Exception as e:
            self.failed[self.requirements[2]] = False
            print(f"🔴 Failed: The data split is incorrect. Ensure you used test_size=0.2 and random_state=42. {e}")

    def check_log_reg_trained(self, model):
        try:
            from sklearn.linear_model import LogisticRegression
            from sklearn.exceptions import NotFittedError
            assert isinstance(model, LogisticRegression)
            model.predict([[0]*10]) # Check if fitted
            self.failed.pop(self.requirements[3], None)
            print("🟩 Passed: Logistic Regression model trained successfully.")
        except NotFittedError:
            self.failed[self.requirements[3]] = True
            print("🔴 Failed: The Logistic Regression model has been instantiated but not trained. Remember to call .fit().")
        except Exception as e:
            self.failed[self.requirements[3]] = True
            print(f"🔴 Failed: There was an issue with the Logistic Regression model training. {e}")

    def check_log_reg_accuracy(self, accuracy):
        try:
            assert 0.75 < accuracy < 0.85, f"The accuracy score ({accuracy:.2%}) is outside the expected range (75-85%)."
            self.failed.pop(self.requirements[4], None)
            print(f"🟩 Passed: Logistic Regression accuracy calculated successfully. Accuracy: {accuracy:.2%}")
        except Exception as e:
            self.failed[self.requirements[4]] = False
            print(f"🔴 Failed: The accuracy score calculation for Logistic Regression seems incorrect. {e}")

    def check_knn_trained(self, model):
        try:
            from sklearn.neighbors import KNeighborsClassifier
            from sklearn.exceptions import NotFittedError
            assert isinstance(model, KNeighborsClassifier)
            assert model.n_neighbors == 5, "The number of neighbors (K) should be set to 5."
            model.predict([[0]*10]) # Check if fitted
            self.failed.pop(self.requirements[5], None)
            print("🟩 Passed: K-Nearest Neighbors model trained successfully.")
        except NotFittedError:
            self.failed[self.requirements[5]] = True
            print("🔴 Failed: The KNN model has been instantiated but not trained. Remember to call .fit().")
        except Exception as e:
            self.failed[self.requirements[5]] = True
            print(f"🔴 Failed: There was an issue with the KNN model training. {e}")

    def check_knn_accuracy(self, accuracy):
        try:
            assert 0.65 < accuracy < 0.75, f"The accuracy score ({accuracy:.2%}) is outside the expected range (65-75%)."
            self.failed.pop(self.requirements[6], None)
            print(f"🟩 Passed: KNN accuracy calculated successfully. Accuracy: {accuracy:.2%}")
        except Exception as e:
            self.failed[self.requirements[6]] = False
            print(f"🔴 Failed: The accuracy score calculation for KNN seems incorrect. {e}")


task01 = Task01()
task02 = Task02()
task03 = Task03()
task04 = Task04()
task05 = Task05()