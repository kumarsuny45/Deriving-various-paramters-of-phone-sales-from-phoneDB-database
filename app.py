import pandas as pd

df = pd.read_csv("device_features (3).csv")

def display_info_by_oem_id(df, oem_id):
    filtered_rows = df[df['oem_id'] == oem_id]
    return filtered_rows[['model', 'manufacturer', 'weight_gram', 'price', 'price_currency']]

while True:
    # Get user input for the OEM ID
    oem_id_input = input("Enter OEM ID (or enter 'exit' to exit): ")

    if oem_id_input.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    # Call the function to search for the given OEM ID
    result = display_info_by_oem_id(df, oem_id_input)

    if not result.empty:
        # Display the information in a more readable format
        print("\nInformation for OEM ID:", oem_id_input)
        print(result.to_string(index=False))
    else:
        print(f"No information found for OEM ID {oem_id_input}.")
import pandas as pd

df = pd.read_csv("device_features (3).csv")

def display_info_by_codename(df, codename):
    filtered_rows = df[df['codename'] == codename]
    result = filtered_rows[['brand', 'model', 'ram_capacity', 'info_added_date', 'market_regions']]

    if not result.empty:
        # Format columns for better readability
        result['ram_capacity'] = result['ram_capacity'].astype(str) + ' GB'
        result['info_added_date'] = pd.to_datetime(result['info_added_date']).dt.strftime('%Y-%m-%d %H:%M:%S')

        # Display formatted result without the index
        print(result.to_string(index=False))
    else:
        print(f"No information found for codename {codename}.")

while True:
    # Get user input for the codename
    codename_input = input("Enter codename (or enter 'exit' to exit): ")

    if codename_input.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    # Call the function to search for the given codename
    display_info_by_codename(df, codename_input)
import pandas as pd

df = pd.read_csv("device_features (3).csv")

def display_info_by_ram_capacity(df, ram_capacity):
    filtered_rows = df[df['ram_capacity'] == ram_capacity]
    return filtered_rows[['oem_id', 'released_date', 'announced_date', 'dimensions', 'device_category']]

while True:
    # Get user input for the RAM capacity
    ram_capacity_input = input("Enter RAM capacity (or enter 'exit' to exit): ")

    # Convert the user input to lowercase before checking 'exit'
    if ram_capacity_input.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    try:
        # Convert the input to an integer for comparison with the DataFrame
        ram_capacity_input = int(ram_capacity_input)

        # Call the function to search for the given RAM capacity
        result = display_info_by_ram_capacity(df, ram_capacity_input)

        if not result.empty:

            print("\nInformation for RAM Capacity:", ram_capacity_input)
            print(result.to_string(index=False))
        else:
            print(f"No information found for RAM Capacity {ram_capacity_input}.")
    except ValueError:
        print("Invalid input. Please enter a numeric RAM capacity or 'exit'.")
import pandas as pd

df = pd.read_csv("device_features (3).csv")

def display_info_by_device_category(df, device_category):
    filtered_rows = df[df['device_category'] == device_category]

    # Select relevant columns
    result = filtered_rows[['model', 'width', 'height', 'dimensions', 'price']]

    # Sort by 'price' in descending order
    result_sorted = result.sort_values(by='price', ascending=False)

    # Format 'dimensions' column for better readability
    result_sorted['dimensions'] = result_sorted['dimensions'].apply(lambda x: f"{x} inches")

    # Format 'price' column for better readability
    result_sorted['price'] = result_sorted['price'].apply(lambda x: f"${x:,.2f}")

    return result_sorted

while True:
    # Get user input for the device category
    device_category_input = input("Enter device_category (or enter 'exit' to exit): ")

    if device_category_input.lower() == 'exit':
        break  # Exit the loop if 'exit' is entered

    # Call the function to search for the given device category
    result = display_info_by_device_category(df, device_category_input)

    if not result.empty:
        # Display formatted result
        print(result.to_string(index=False))
    else:
        print(f"No information found for device_category {device_category_input}.")
import pandas as pd

df = pd.read_csv("device_features (3).csv")

df.columns
  import matplotlib.pyplot as plt

# Count the occurrences of each RAM type in each region
ram_region_counts = df.groupby(['ram_capacity', 'market_regions']).size().unstack(fill_value=0)

# Plot a stacked bar chart
ram_region_counts.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Distribution of RAM Types in Market Regions')
plt.xlabel('RAM Type')
plt.ylabel('Count')
plt.legend(title='Region', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()
  import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Identify the columns representing USB connector type and device category
usb_connector_column = 'usb_connector'
device_category_column = 'device_category'

# Count the occurrences of each USB connector type within each device category
usb_counts = df.groupby([device_category_column, usb_connector_column]).size().unstack(fill_value=0)

# Plot a grouped bar chart
plt.figure(figsize=(14, 8))
usb_counts.plot(kind='bar', stacked=True, colormap='viridis')
plt.title('Number of Devices by USB Connector Type and Device Category')
plt.xlabel('Device Category')
plt.ylabel('Number of Devices')
plt.xticks(rotation=45, ha='right')
plt.legend(title='USB Connector Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Convert 'release_date' to datetime format
df['released_date'] = pd.to_datetime(df['released_date'])

# Extract year and month from 'release_date'
df['year'] = df['released_date'].dt.year
df['month'] = df['released_date'].dt.month

# Filter data for the currency 'GBP'
df_gbp = df[df['price_currency'] == 'GBP']

# Set the plotting style
sns.set(style="whitegrid")

# Create separate charts for each year
years_to_plot = range(2020, 2024)

for year in years_to_plot:
    # Filter data for the specific year
    df_yearly = df_gbp[df_gbp['year'] == year]

    # Plot the monthly average price trends
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='month', y='price', data=df_yearly, ci=None)

    # Set plot title and labels
    plt.title(f'Monthly Average Price Trends in GBP - {year}')
    plt.xlabel('Month')
    plt.ylabel('Average Price (GBP)')

    # Show the plot
    plt.show()
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd



# Count the occurrences of each market region and device category
region_device_counts = df.groupby(['market_regions', 'device_category']).size().unstack(fill_value=0)

# Choose the top 10 regions to display
top_n = 10
top_regions = df['market_regions'].value_counts().head(top_n).index

# Filter the DataFrame for the top 10 regions
top_regions_df = df[df['market_regions'].isin(top_regions)]

# Group the remaining regions into 'Other'
other_sum = df.shape[0] - top_regions_df.shape[0]
other_df = df[~df['market_regions'].isin(top_regions)].copy()
other_df['market_regions'] = 'Other'
top_regions_df = pd.concat([top_regions_df, other_df])


pivot_df = top_regions_df.groupby(['market_regions', 'device_category']).size().unstack(fill_value=0)


colors = sns.color_palette('husl', n_colors=len(pivot_df.columns))

# Plot a stacked bar chart
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(12, 6), color=colors)
plt.title('Distribution of Devices in Top Market Regions and Other')
plt.xlabel('Market Region')
plt.ylabel('Number of Devices')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.legend(title='Device Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt
