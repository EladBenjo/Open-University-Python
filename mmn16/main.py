"""
@Project: mmn_16

@Description : main for mmn_16 written with Chat-GPT for testing

@ID : 206014698
@Author: Elad Benjo
@semester : 2025a
"""

# main.py
import nasa_asteroid_ds as nasads


def main():
    # 1. Load the data
    df = nasads.load_data('nasa.csv')
    if df is None:
        print("Could not load data, exiting.")
        return

    # 2. Data Cleaning - keep only asteroids from year 2000 onwards
    df = nasads.mask_data(df)
    if df is None or df.empty:
        print("No data available after filtering by date, exiting.")
        return

    # 3. Remove specific columns and show table details
    details = nasads.data_details(df)
    print("Table details after removing columns:", details)

    # 4. Maximum absolute magnitude
    result = nasads.max_absolut_magnitude(df)
    print("Asteroid with max absolute magnitude:", result)

    # 5. Closest asteroid to earth (by km)
    closest = nasads.closest_to_earth(df)
    print("Name of closest asteroid to earth:", closest)

    # 6. Most common orbits
    orbit_dict = nasads.common_orbit(df)
    print("Number of asteroids per Orbit ID:", dict(list(orbit_dict.items())))

    # 7. How many have max diameter above average
    count = nasads.min_max_diameter(df)
    print("Number of asteroids with max diameter above average:", count)

    # 8. Plots:
    print("\nPresenting plots (close each plot to see the next):")

    nasads.plt_hist_diameter(df)
    nasads.plt_hist_common_orbit(df)
    nasads.plt_pie_hazard(df)
    nasads.plt_linear_motion_magnitude(df)


if __name__ == "__main__":
    main()
