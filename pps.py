import pandas as pd

def pandas_operations():
    # Creating a DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)

    # Displaying the DataFrame
    print("Original DataFrame:")
    print(df)

    # Basic DataFrame operations
    head_result = df.head(2)  # Get the first 2 rows
    describe_result = df.describe()  # Summary statistics
    transpose_result = df.T  # Transpose the DataFrame

    # Sorting
    sorted_by_age = df.sort_values(by='Age', ascending=False)

    # Selection and Filtering
    age_greater_than_30 = df[df['Age'] > 30]

    # Adding a new column
    df['Salary'] = [60000, 70000, 80000, 90000]

    # Deleting a column
    df = df.drop('City', axis=1)

    # Displaying results
    print("\nDataFrame Operations:")
    print("Head (first 2 rows):")
    print(head_result)

    print("\nDescribe (summary statistics):")
    print(describe_result)

    print("\nTranspose:")
    print(transpose_result)

    print("\nSorting by Age (descending):")
    print(sorted_by_age)

    print("\nSelection and Filtering (Age > 30):")
    print(age_greater_than_30)

    print("\nAdding a new column (Salary) and removing 'City':")
    print(df)

# Correct main guard
if __name__ == "__main__":
    pandas_operations()
