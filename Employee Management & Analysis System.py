import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect("company.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER,
    join_date TEXT
)
""")

# Insert sample data
employees = [
    (1, "Amit", "IT", 50000, "2023-01-10"),
    (2, "Sneha", "HR", 40000, "2022-05-15"),
    (3, "Rahul", "Finance", 60000, "2023-07-20"),
    (4, "Priya", "IT", 55000, "2021-09-12"),
    (5, "Karan", "HR", 45000, "2022-11-25")
]

cursor.executemany("INSERT OR IGNORE INTO employees VALUES (?, ?, ?, ?, ?)", employees)
conn.commit()

# Fetch data into pandas
df = pd.read_sql_query("SELECT * FROM employees", conn)

print("\nEmployee Data:")
print(df)

# Average salary
print("\nAverage Salary:", df['salary'].mean())

# Department wise average salary
dept_salary = df.groupby('department')['salary'].mean()
print("\nDepartment Wise Salary:")
print(dept_salary)

# Visualization
dept_salary.plot(kind='bar')
plt.title("Average Salary by Department")
plt.show()

conn.close()