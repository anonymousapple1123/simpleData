import pandas as pd

class DataAnalyzer:
    def __init__(self, data):
        self.data = pd.DataFrame(data, columns=['Column1', 'Column2', 'Column3'])

    def perform_analysis(self):
        # Replace with the analysis you want to perform
        summary = self.data.describe()
        return summary

