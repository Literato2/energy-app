# Energy Generation Interactive Web App
# Run with: streamlit run energy_app.py

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load data
@st.cache_data
def load_data():
    """Load the energy data from the CSV file"""
    df = pd.read_csv("https://storage.googleapis.com/emb-prod-bkt-publicdata/public-downloads/monthly_full_release_long_format.csv")
    return df

def main():
    st.title("🌍 Interactive Energy Generation Explorer")
    st.markdown("Compare energy generation across countries and sources")
    
    # Load data
    df = load_data()
    
    # Sidebar for selections
    st.sidebar.header("📊 Select Your Data")
    
    # Get unique values
    countries = sorted(df['Area'].unique())
    sources = sorted(df['Variable'].unique())
    
    # Country selection
    st.sidebar.subheader("🌍 Countries")
    selected_countries = st.sidebar.multiselect(
        "Choose countries to compare:",
        options=countries,
        default=['China', 'United States of America'],
        help="Select multiple countries to compare their energy generation"
    )
    
    # Energy source selection
    st.sidebar.subheader("⚡ Energy Sources")
    selected_sources = st.sidebar.multiselect(
        "Choose energy sources:",
        options=sources,
        default=['Solar', 'Nuclear', 'Coal'],
        help="Select energy sources to display on the plot"
    )
    
    # Date range selection
    st.sidebar.subheader("📅 Date Range")
    df['Date'] = pd.to_datetime(df['Date'])
    min_date = df['Date'].min()
    max_date = df['Date'].max()
    
    date_range = st.sidebar.date_input(
        "Select date range:",
        value=(pd.to_datetime('2016-01-01'), max_date),
        min_value=min_date,
        max_value=max_date
    )
    
    # Filter data
    if selected_countries and selected_sources:
        df_filtered = df[
            (df['Area'].isin(selected_countries)) &
            (df['Variable'].isin(selected_sources)) &
            (df['Unit'] == 'TWh') &
            (df['Date'] >= pd.to_datetime(date_range[0])) &
            (df['Date'] <= pd.to_datetime(date_range[1]))
        ].copy()
        
        if not df_filtered.empty:
            # Create interactive plot
            fig = go.Figure()
            
            # Color palette
            colors = ['#e63946', '#a4161a', '#4a90e2', '#1f4e79', '#6c757d', '#adb5bd', 
                     '#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57', '#ff9ff3']
            
            # Add traces for each country-source combination
            for i, country in enumerate(selected_countries):
                for j, source in enumerate(selected_sources):
                    subset = df_filtered[
                        (df_filtered['Area'] == country) &
                        (df_filtered['Variable'] == source)
                    ]
                    
                    if not subset.empty:
                        color_idx = (i * len(selected_sources) + j) % len(colors)
                        fig.add_trace(
                            go.Scatter(
                                x=subset['Date'],
                                y=subset['Value'],
                                mode='lines',
                                name=f'{country} - {source}',
                                line=dict(color=colors[color_idx], width=2),
                                hovertemplate='<b>%{fullData.name}</b><br>' +
                                            'Date: %{x}<br>' +
                                            'Value: %{y:.2f} TWh<extra></extra>'
                            )
                        )
            
            # Update layout
            fig.update_layout(
                title="Interactive Energy Generation Comparison",
                xaxis_title="Date",
                yaxis_title="Generation (TWh)",
                hovermode='x unified',
                legend=dict(
                    orientation="h",
                    yanchor="bottom",
                    y=1.02,
                    xanchor="right",
                    x=1
                ),
                height=600
            )
            
            # Display plot
            st.plotly_chart(fig, use_container_width=True)
            
            # Data summary
            st.subheader("📈 Data Summary")
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.metric("Countries", len(selected_countries))
            with col2:
                st.metric("Energy Sources", len(selected_sources))
            with col3:
                st.metric("Data Points", len(df_filtered))
            
            # Show data table
            st.subheader("📋 Raw Data")
            st.dataframe(df_filtered.sort_values(['Area', 'Variable', 'Date']))
            
        else:
            st.warning("No data available for the selected combination. Try different countries or energy sources.")
    
    else:
        st.info("Please select at least one country and one energy source to see the plot.")
    
    # Additional features
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Quick Stats")
    
    if st.sidebar.button("Show Global Statistics"):
        st.subheader("🌍 Global Energy Statistics")
        
        # Global stats
        global_stats = df[df['Unit'] == 'TWh'].groupby('Variable')['Value'].agg(['mean', 'max', 'min']).round(2)
        st.dataframe(global_stats)
        
        # Top countries by source
        if selected_sources:
            st.subheader("🏆 Top Countries by Energy Source")
            for source in selected_sources[:3]:  # Show top 3 sources
                top_countries = df[
                    (df['Variable'] == source) & 
                    (df['Unit'] == 'TWh')
                ].groupby('Area')['Value'].max().sort_values(ascending=False).head(5)
                
                st.write(f"**{source}:**")
                for country, value in top_countries.items():
                    st.write(f"  • {country}: {value:.2f} TWh")

if __name__ == "__main__":
    main() 