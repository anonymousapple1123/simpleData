import sys
from database import Database
from analysis import DataAnalyzer

def main():
    # Initialize database
    db = Database('data.db')
    
    # Get data from the database
    data = db.fetch_data('SELECT * FROM your_table_name')
    
    # Analyze the data
    analyzer = DataAnalyzer(data)
    
    # Perform analysis and print results
    results = analyzer.perform_analysis()
    print(results)

if __name__ == '__main__':
    main()

