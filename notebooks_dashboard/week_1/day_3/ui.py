from ipywidgets import *
import ipywidgets as widgets

class DashUI:
    def __init__(self, list_of_metrics):
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