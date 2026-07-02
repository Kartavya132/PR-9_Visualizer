import pandas as pd
import numpy as np
import os
from abc import ABC, abstractmethod
from sys import exit


class sales(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def explore_data(self):
        pass

    @abstractmethod
    def clean_data(self):
        pass

    @abstractmethod
    def mathematical_operations(self):
        pass

    @abstractmethod
    def split_data(self):
        pass

    @abstractmethod
    def search_sort_filter(self):
        pass

    @abstractmethod
    def aggregate_functions(self):
        pass

    @abstractmethod
    def statistical_analysis(self):
        pass

    @abstractmethod
    def create_pivot_table(self):
        pass

    @abstractmethod
    def visualize_data(self):
        pass

    @abstractmethod
    def __del__(self):
        pass


class SalesDataAnalzer(sales):

    def __init__(self):
        self.access = True
        self.data = None

    def load_data(self):
        FILE_NAME = input("Enter the name of file : ")
        try:
            path = os.path.abspath(FILE_NAME)
            data = pd.read_csv(path)
            self.data = data
            print("The data is loaded successfully!!")
            return self.data
        except FileNotFoundError:
            self.data = None
            print("There is no such file")
        except FileExistsError:
            self.data = None
            print("There is no such file in dir")
        return None

    def explore_data(self):
        pass

    def clean_data(self):
        pass

    def mathematical_operations(self):
        pass

    def split_data(self):
        pass

    def search_sort_filter(self):
        pass

    def aggregate_functions(self):
        pass

    def statistical_analysis(self):
        pass

    def create_pivot_table(self):
        pass

    def visualize_data(self):
        pass

    def __del__(self):
        pass


def show_menu():
    print("------------------------------------------")
    print("Welcome to data analysis and visualization")
    print("------------------------------------------\n")
    print("The main menu ::")
    print("1. Load dataset")
    print("2. Explore data")
    print("3. Perform Dataframe Operation")
    print("4. Handle missing value")
    print("5. Generate Descriptive Statistics")
    print("6. Data Visualization")
    print("7. Save Visualization")
    print("8. Exit")
    return input("Enter your choice : ")


def main():
    data_structure = SalesDataAnalzer()
    while data_structure.access:
        cho = show_menu()
        match cho:
            case "1":
                data_structure.load_data()
            case "2":
                data_structure.explore_data()
            case "3":
                pass
            case "4":
                pass
            case "5":
                pass
            case "6":
                pass
            case "7":
                pass
            case "8":
                print("Thank you for using this and good bye!!")
                exit()
            case _:
                print("Invalid input")


if __name__ == "__main__":
    main()
