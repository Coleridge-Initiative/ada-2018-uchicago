# Packages for UI components
from ipywidgets import *
import ipywidgets as widgets

# Package for database connection
from sqlalchemy import create_engine

# Packages for data manipulation
import pandas as pd
import numpy as np
import geopandas as gpd

# Packages for visualizations
import matplotlib.pyplot as plt
import seaborn as sns

class DashUI:
    def __init__(self, statefp, list_of_metrics, count_qry, change_qry):
        self.engine = create_engine('postgresql://@10.10.2.10/appliedda')
        
        qry = "SELECT countyfp, name, ST_Transform(geom, 102698) geom FROM tl_2016_us_county WHERE statefp = '{}'".format(statefp)
        self.counties = gpd.read_postgis(qry, self.engine, geom_col='geom')
        self.counties['coords'] = self.counties.geometry.apply(lambda x: x.representative_point().coords[0])
        
        self.count_qry = count_qry
        self.change_qry = change_qry
        
        self.metric_dropdown = widgets.Dropdown(
            options=list_of_metrics,
            description='Metric'
        )
        
        self.plot_toggle = widgets.ToggleButtons(
            options=['Count', 'Change'],
            value='Count',
            description='',
            disabled=False,
            button_style='',
            tooltips=['Display absolute counts', 'Display change over time']
        )
        
        options = [(" Q{} {} ".format(qtr, year), (qtr,year)) for year in range(2005,2016) for qtr in range(1,5)]
        self.time_slider = widgets.SelectionSlider(
            options=options,
            description='Quarter',
            disabled=False,
            continuous_update=False,
            layout=Layout(width='60%')
        )
        
        self.time_range_slider = widgets.SelectionRangeSlider(
            options=options,
            index=(0,len(options)-1),
            description='Time Range',
            disabled=False,
            layout=Layout(width='60%')
        )
        self.time_range_slider.layout.visibility = 'hidden'

        self.generate_button = widgets.Button(
            description='Generate Plot',
            disabled=False,
            tooltip='Generate Plot'
        )

        self.panel_items = [
            HBox([self.metric_dropdown]),
            HBox([self.plot_toggle]),
            VBox([self.time_slider, self.time_range_slider]),
            HBox([self.generate_button])
        ]

        self.input_panel = VBox(self.panel_items)
        
        self.output = Output()
        
        def on_value_change(change):
            if change['new'] == 'Count':
                self.time_range_slider.layout.visibility = 'hidden'
                self.time_slider.layout.visibility = 'visible'
            elif change['new'] == 'Change':
                self.time_slider.layout.visibility = 'hidden'
                self.time_range_slider.layout.visibility = 'visible'

        self.plot_toggle.observe(on_value_change, names='value')
        
        def run_query():
            # Get toggle value to determine which plot type to use
            plot_type = self.plot_toggle.value
            
            # Set query for either Count or Change
            if plot_type == 'Count':
                qry = self.count_qry.format(q=self.time_slider.value[0],
                                       y=self.time_slider.value[1])
            elif plot_type == 'Change':
                qry = self.change_qry.format(q0=self.time_range_slider.value[0][0],
                                        y0=self.time_range_slider.value[0][1],
                                        q1=self.time_range_slider.value[1][0],
                                        y1=self.time_range_slider.value[1][1])
        
            # Run the query and return the Dataframe
            return pd.read_sql(qry, self.engine)
    
        def generate_plot(button_obj):
            self.output.clear_output()
            with self.output:
                # Configure plot settings
                sns.set_style('white')
                f, ax = plt.subplots(1, figsize=(6,8))
                ax.axis('off')
                
                # Plot basemap so counties with no data appear hatched
                self.counties.plot(ax=ax, edgecolor='black', color='lightgray', hatch='//')
                
                # Query and merge data with county shapefile
                df = run_query()
                cnty_df = pd.merge(self.counties, df, left_on=['countyfp'], right_on=['cnty'])
                
                # Get metric of interest from dropdown
                metric = self.metric_dropdown.value
                
                # Exception for zero counts
                if self.plot_toggle.value == 'Count':
                    cnty_df = cnty_df[cnty_df[metric] > 0]
                
                # If no counties data, show empty map and return
                if len(cnty_df) == 0:
                    plt.show()
                    return
                
                # Plot county data
                if self.plot_toggle.value == 'Count':
                    colmap = sns.cubehelix_palette(8, start=2.9, rot=0, dark=.1, light=.95, as_cmap=True)
                    cnty_df.plot(metric, ax=ax, legend=True, edgecolor='black', cmap=colmap)
                elif self.plot_toggle.value == 'Change':
                    metric = 'change_in_{}_pct'.format(metric)
                    bound = cnty_df[metric].abs().max()
                    colmap = sns.diverging_palette(10, 150, center='light', as_cmap=True)
                    cnty_df.plot(metric, ax=ax, legend=True, edgecolor='black', cmap=colmap, vmax=bound, vmin=bound*-1)
                
                # Show plot
                plt.show()

        self.generate_button.on_click(generate_plot)
