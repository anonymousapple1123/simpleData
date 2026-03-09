import sqlite3


def populate_database(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create table if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS your_table_name (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            column1 TEXT,
            column2 INTEGER,
            column3 REAL
        )
    """)

    # Sample data to insert
    sample_data = [
        ("Sample A", 10, 1.23),
        ("Sample B", 15, 2.34),
        ("Sample C", 25, 3.45),
        ("Sample D", 30, 4.56),
    ]

    # Insert sample data
    cursor.executemany(
        """
        INSERT INTO your_table_name (column1, column2, column3) VALUES (?, ?, ?)
    """,
        sample_data,
    )

    # Commit changes and close connection
    connection.commit()
    connection.close()
    print("Sample data added successfully.")


if __name__ == "__main__":
    populate_database("data.db")
