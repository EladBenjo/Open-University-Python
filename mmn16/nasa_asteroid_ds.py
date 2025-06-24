"""
@Project: mmn_16

@Description : Data preperation, analysis and visualization.

@ID : 206014698
@Author: Elad Benjo
@semester : 2025a
"""

import pandas as pd


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
    Count how many astroids have a max diameter greater than the average max diameter in the df
    :param: (pd.DataFrame): The input DataFrame
    :return: int count of how many astroids have a max diameter greater than the average max diameter in the df
    """
    requiered_columns = ['Est Dia in KM(max)']
    # Validate df is DataFrame and is not empty and needed columns exist
    if not validate_df(df, requiered_columns):
        return None
    mean_max_diameter = df['Est Dia in KM(max)'].mean()
    mask = df['Est Dia in KM(max)'] > mean_max_diameter
    greater_than_mean_count = mask.sum()
    return int(greater_than_mean_count)
