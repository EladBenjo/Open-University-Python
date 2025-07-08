"""
@Project: mmn_16

@Description : Data preperation, analysis and visualization.

@ID : 206014698
@Author: Elad Benjo
@semester : 2025a
"""

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


def validate_df(df, required_columns=None):
    """
    Validates that the input is a non-empty DataFrame with required columns.
    param: df: Pandas DataFrame
    param: required_columns: List of columns that must exist
    :return: bool: True if df is instance of DataFrame and is not empty and all the requiered columns exist, else False.
    """
    if not isinstance(df, pd.DataFrame):
        print("Error: Input is not a pandas DataFrame.")
        return False
    if df.empty:
        print("Error: DataFrame is empty.")
        return False
    if required_columns:
        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            print(f"Error: Missing required columns: {missing}")
            return False
    return True


def ensure_csv_extension(filename):
    """
    Ensures the filename ends with '.csv'. If not, adds the extension.

    :param:
        filename (str): The file name or path.

    :return:
        str: File name ending with '.csv'.
    """
    if not filename.lower().endswith('.csv'):
        filename += '.csv'
    return filename


def load_data(filename):
    """
    Loads data from a CSV file into a pandas DataFrame.
    Handles invalid file names, missing files, and other errors.

    :param:
        filename (str): Path to the CSV file.

    :return:
        pd.DataFrame: DataFrame with loaded data, or None if failed.
    """
    filename = ensure_csv_extension(filename)
    try:
        df = pd.read_csv(filename)
        return df
    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except pd.errors.ParserError:
        print("Error: Failed to parse the CSV file.")
    except OSError:
        print("Error: Invalid file name or file path.")
    except Exception as e:
        print(f"Error: {e}")
    return None


def mask_data(df):
    """
    Filters the DataFrame to include only rows where 'Close Approach Date'
    is from a given date onwards.

    :param df: Pandas:
        df (pd.DataFrame): The input DataFrame.

    :return:
        pd.DataFrame: Filtered DataFrame or None if invalid input.
    """
    given_date = pd.Timestamp('2000-01-01')

    # 1. Using external method 'valida_df' to validate df and 'Close Approach Date' column
    if not validate_df(df, ['Close Approach Date']):
        return None

    # 2. Convert the column to datetime
    try:
        df['Close Approach Date'] = pd.to_datetime(df['Close Approach Date'], errors='coerce')
    except Exception as e:
        print(f"Error: Could not convert 'Close Approach Date' to datetime. {e}")
        return None

    # 3. Filter only dates >= 2000-01-01
    mask = df['Close Approach Date'] >= pd.Timestamp(given_date)
    filtered_df = df[mask].copy()

    # 4. Check if result is empty
    if filtered_df.empty:
        print("Warning: No data from year 2000 and onwards.")
        return filtered_df

    return filtered_df


def data_details(df):
    """
    Filters the DataFrame to remove given columns
    :param: df(pd.DataFrame): The input DataFrame
    :return: tuple holding the number of rows, columns, and a list of the remaining columns name None in case of empty
     or invalid df
    """
    given_columns = ['Orbiting Body', 'Neo Reference ID', 'Equinox']
    if validate_df(df):
        df.drop(given_columns, axis=1, errors='ignore', inplace=True)
        n_rows, n_cols = df.shape
        col_names = list(df.columns)
        return n_rows, n_cols, col_names
    return None


def max_absolut_magnitude(df):
    """
    Find the closet astroid to earth by 'Absolute Magnitude' and return its name and it 'Absolute Magnitude' value
    :param: df (pd.DataFrame): The input DataFrame
    :return: tuple holding the name (str) of the nearest astroid to earth and the value of its absolute magnitude (int)
    """
    requiered_columns = ['Absolute Magnitude', 'Name']
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, requiered_columns):
        return None

    # Find the row with the maximum Absolute Magnitude
    idx_max = df['Absolute Magnitude'].idxmax()
    asteroid_name = df.at[idx_max, 'Name']
    max_magnitude = df.at[idx_max, 'Absolute Magnitude']
    return asteroid_name, max_magnitude


def closest_to_earth(df):
    """
    Find the closest astroid to earth by km and return its name
    :param: df (pd.DataFrame): The input DataFrame
    :return: str name of the closet astroid to earth
    """
    requiered_columns = ['Miss Dist.(kilometers)', 'Name']
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, requiered_columns):
        return None

    # get the id of the min Miss Dist(km) and return the coresponding astroid name
    idx_min = df['Miss Dist.(kilometers)'].idxmin()
    return df.at[idx_min, 'Name']


def common_orbit(df):
    """
    Create a dictionary with key 'Orbit ID' and value number of asteroids in this orbit
    :param: df (pd.DataFrame): The input DataFrame
    :return: dict with key 'Orbit ID' and value number of asteroids in this orbit
    """
    requiered_columns = ['Orbit ID']
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, requiered_columns):
        return None

    # Count occurrences of each Orbit ID
    orbit_counts = df['Orbit ID'].value_counts().to_dict()
    return orbit_counts


def min_max_diameter(df):
    """
    Count how many astroids have a max diameter greater than the average max diameter in the df.
    :param: df (pd.DataFrame): The input DataFrame
    :return: int count of how many astroids have a max diameter greater than the average max diameter in the df
    """
    column = 'Est Dia in KM(max)'
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, [column]):
        return None
    # Calculate the mean of max diameter in the data frame
    mean_max_diameter = df[column].mean()
    # The bool expression will return 1 for each time it is greater than the mean
    count = (df['Est Dia in KM(max)'] > mean_max_diameter).sum()
    return int(count)


def plt_hist_diameter(df):
    """
    Plot a histogram of the number of astroids with their mean diameter in km.
    Mean diameter will be the average between 'Est Dia in KM(min)' and 'Est Dia in KM(max)'.
    Histogram has 100 bins.
    :param: df (pd.DataFrame): The input DataFrame
    :return: None
    """
    requierd_column = ['Est Dia in KM(min)', 'Est Dia in KM(max)']
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, requierd_column):
        return None

    # Calculate the mean diameter for each record
    mean_diameter = (df['Est Dia in KM(min)'] + df['Est Dia in KM(max)']) / 2

    # Plot histogram
    plt.hist(mean_diameter, bins=100, color='steelblue', edgecolor='black')
    plt.xlabel('Mean Diameter (km)')
    plt.ylabel('Number of Astroids')
    plt.title('Histogram of Asteroid Count by Mean Diameter (km)')
    plt.grid(True)
    plt.show()


def plt_hist_common_orbit(df):
    """
    Plot a histogram of the number of astroid with their according orbit intersection.
    Histogram has 10 bins.
    :param: df (pd.DataFrame): The input DataFrame
    :return: None
    """
    requierd_column = 'Minimum Orbit Intersection'
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, [requierd_column]):
        return None

    # Calculate range
    values = df[requierd_column].dropna()
    min_val = values.min()
    max_val = values.max()

    # Plot histogram
    plt.hist(values, bins=10, range=(min_val, max_val), color='steelblue', edgecolor='black')
    plt.xlabel('Minimum Orbit Intersection')
    plt.ylabel('Number of Asteroids')
    plt.title('Histogram of Asteroids by Their Minimum Orbit Intersection')
    plt.grid(True)
    plt.show()


def plt_pie_hazard(df):
    """
    Plot a pie chart of the percentage of astroids that are classified as hazardous and the ones that aer not.
    :param: df (pd.DataFrame): The input DataFrame
    :return: None
    """
    requierd_column = 'Hazardous'
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, [requierd_column]):
        return None

    # Count the hazardous and non hazardous
    counts = df[requierd_column].value_counts(dropna=False)
    labels = counts.index.astype(str)
    sizes = counts.values

    # Plot pie chart
    plt.figure(figsize=(7, 7))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title('Percentage of Hazardous and Non-Hazardous Asteroids')
    plt.axis('equal')
    plt.show()


def plt_linear_motion_magnitude(df):
    """
    Plot a scatter plot and a simple linear regression to examine the relationship between the proximity of an asteroid
    to earth and its movement speed.
    Note: There is a positive linear relation between the two variables; although the scatterplot looks very dense and
    somewhat messy, the r-value indicates a moderate linear association. Combined with a very low p-value, this means
    the relationship is statistically significant.
    However, the large dispersion of data points around the regression line shows that the miss distance only explains
    a small portion of the variance in velocity. In other words, despite the statistical significance, most of the
    variation in speed is not accounted for by miss distance alone. Therefore, while the correlation exists, it is not
    strong enough to allow for accurate prediction or reliable explanation of asteroid velocity based solely on miss
    distance.
    :param: df (pd.DataFrame): The input DataFrame
    :return: None
    """
    requierd_column = ['Miss Dist.(kilometers)', 'Miles per hour']
    if not validate_df(df, requierd_column):
        return None

    # Get the actual series
    x = df['Miss Dist.(kilometers)']
    y = df['Miles per hour']

    # Remove NaN
    mask = x.notna() & y.notna()
    x = x[mask]
    y = y[mask]

    # Linear regression
    a, b, r_value, p_value, std_err = stats.linregress(x, y)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, alpha=0.6, label='Data points')
    plt.plot(x, a * x + b, color='red', label=f'Linear Regression (r={r_value:.2f}, r^2={r_value*r_value:.2f})'
                                              f'\np < 0.05: {0.05>p_value}')
    plt.xlabel('Miss Distance (kilometers)')
    plt.ylabel('Velocity (Miles per hour)')
    plt.title('Linear Regression: Miss Distance vs. Velocity')
    plt.legend()
    plt.grid(True)
    plt.show()
