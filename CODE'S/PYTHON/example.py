import pandas as pd

# Sample data
data = {
    "Name": ["Amit", "Priya", "Rohan", "Sneha", "Vikram"],
    "Age": [25, 30, 22, 27, 24],
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df.iat[2,2])
