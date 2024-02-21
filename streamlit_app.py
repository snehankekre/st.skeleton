import time

import numpy as np
import pandas as pd
import streamlit as st

with st.expander("Show code"):
    st.code("""
    import time

    import numpy as np
    import pandas as pd
    import streamlit as st

    # Placeholder for the get_census_data_from_database function
    def get_census_data_from_database(year):
        # Simulating a delay to mimic data fetching
        time.sleep(1)  # Simulating a delay
        # Generating a sample dataframe based on the selected year
        return pd.DataFrame(
            np.random.rand(10, 4),
            columns=[f'{year}_Data_{i}' for i in range(4)]
        )

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("New behavior")
        st.caption("Using `st.skeleton`")
        # Draw UI
        st.write("Census Data")
        # Assuming st.skeleton is integrated and accepts a height parameter
        census_data_placeholder = st.skeleton(height=400)  # Using the new st.skeleton command

        year = st.selectbox("Select Year", options=[2022, 2023, 2024])

        # Get data from source, this could take some time
        census_dataframe = get_census_data_from_database(year)

        # Replace the skeleton animation with the actual data
        # Assuming the placeholder object returned by st.skeleton behaves like st.empty()
        census_data_placeholder.dataframe(census_dataframe)

    with col2:
        st.subheader("Current behavior")
        st.caption("Using `st.empty`")
        # Draw UI
        st.write("Census Data")
        census_data_placeholder = st.empty()  # Using the current st.empty command

        year = st.selectbox("Select Year", options=[2022, 2023, 2024], key="old")

        # Get data from source, this could take some time
        census_dataframe = get_census_data_from_database(year)

        # Replace the skeleton animation with the actual data
        # Assuming the placeholder object returned by st.skeleton behaves like st.empty()
        census_data_placeholder.dataframe(census_dataframe)
    """)

# Placeholder for the get_census_data_from_database function
def get_census_data_from_database(year):
    # Simulating a delay to mimic data fetching
    time.sleep(1)  # Simulating a delay
    # Generating a sample dataframe based on the selected year
    return pd.DataFrame(
        np.random.rand(10, 4),
        columns=[f'{year}_Data_{i}' for i in range(4)]
    )

col1, col2 = st.columns(2)

with col1:
    st.subheader("New behavior")
    st.caption("Using `st.skeleton`")
    # Draw UI
    st.write("Census Data")
    # Assuming st.skeleton is integrated and accepts a height parameter
    census_data_placeholder = st.skeleton(height=400)  # Using the new st.skeleton command

    year = st.selectbox("Select Year", options=[2022, 2023, 2024])

    # Get data from source, this could take some time
    census_dataframe = get_census_data_from_database(year)

    # Replace the skeleton animation with the actual data
    # Assuming the placeholder object returned by st.skeleton behaves like st.empty()
    census_data_placeholder.dataframe(census_dataframe)

with col2:
    st.subheader("Current behavior")
    st.caption("Using `st.empty`")
    # Draw UI
    st.write("Census Data")
    census_data_placeholder = st.empty()  # Using the current st.empty command

    year = st.selectbox("Select Year", options=[2022, 2023, 2024], key="old")

    # Get data from source, this could take some time
    census_dataframe = get_census_data_from_database(year)

    # Replace the skeleton animation with the actual data
    # Assuming the placeholder object returned by st.skeleton behaves like st.empty()
    census_data_placeholder.dataframe(census_dataframe)


