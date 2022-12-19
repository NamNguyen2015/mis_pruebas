#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 12:33:58 2022

@author: namnguyen
"""

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid, GridOptionsBuilder, GridUpdateMode


df = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
#grid_table = AgGrid(df, editable=True)
#new_df = grid_return['data']
# =============================================================================
#
#
# def generate_agrid(df):
#     gb = GridOptionsBuilder.from_dataframe(df)
#     gb.configure_selection(selection_mode="multiple", use_checkbox=True)
#     gridoptions = gb.build()
#
#     grid_response = AgGrid(
#         df,
#         height=200,
#         gridOptions=gridoptions,
#         update_mode=GridUpdateMode.MANUAL,
#         editable=True
#     )
#     selected = grid_response['selected_rows']
#
#     # Show the selected row.
#     if selected:
#         st.write('selected')
#         st.dataframe(selected)
#
#     return grid_response
#
# =============================================================================

def add_row(grid_table):
    df = pd.DataFrame(grid_table['data'])

    new_row = [['', '']]
    df_empty = pd.DataFrame(new_row, columns=df.columns)
    df = pd.concat([df, df_empty], axis=0, ignore_index=True)

    # Save new df to sample.csv.
    df.to_csv('sample.csv', index=False)


def get_data():
    """Reads sample.csv and return a dataframe."""
    return pd.read_csv('sample.csv')


if __name__ == '__main__':
    df = get_data()
    #grid_response = generate_agrid(df)
    grid_response = AgGrid(df,editable=True,update_mode=GridUpdateMode.MANUAL, use_checkbox=True)

    st.sidebar.button("Add row", on_click=add_row, args=[grid_response])
