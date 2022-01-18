# python-plot-sharing
A demo for sharing plotly plots via github pages.

The file, `share_plot.py` contains two demos for sharing plots
on github pages.

1. `demo1()` uses plotly generate all the HTML and publishes it the root.
See it here [https://wehi-researchcomputing.github.io/python-plot-sharing/](https://wehi-researchcomputing.github.io/python-plot-sharing/)
2. `demo2()` shows how you can wrap several plots in your own HTML. See it here
 [https://wehi-researchcomputing.github.io/python-plot-sharing/demo2](https://wehi-researchcomputing.github.io/python-plot-sharing/demo2)

Limitations of this technique are:

* The only ability to interact is what is provided by the plotly
javascript front end. Specifically, there is no server to recalculate based on
user input.
* Plots are public even if your repo is not. (Although github
seems to be offering a paid service where you have some control.)

