import plotly.express as px
import plotly.io as pio
import os

def iris_plot():
  # Generate a nice 2D scatter plot
  df = px.data.iris()
  fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                   size='petal_length', hover_data=['petal_width'])
  return fig

def tip_plot():
  # Another set of 2D plots
  df = px.data.tips()
  fig = px.scatter(df, x="total_bill", y="tip", color="smoker", facet_col="sex", facet_row="time")
  return fig

def demo1():
  fig = iris_plot()

  # Generate HTML
  html = pio.to_html(fig, include_plotlyjs='cdn')

  # Save HTML to the docs directory
  html_file = os.path.join('docs', 'index.html')
  with open(html_file, 'w') as f:
    f.write(html)

def demo2():
  fig1 =  iris_plot()
  fig2 = tip_plot()

  # Get the base HTML for each plot
  fig1_html = pio.to_html(fig1, include_plotlyjs='cdn', full_html=False)
  fig2_html = pio.to_html(fig2, include_plotlyjs='cdn', full_html=False)

  # Wrap the individual plots in the rest of the HTML
  page_html = f'''<html>
          <head>
          <title>Demo of plotly in Github pages</title>
          </head>
          <body>
              <h1>First plot</h1>
              {fig1_html}
              <h1>Second plot</h1>
              {fig2_html}
          </body>
      </html>
  '''

  # Write the HTML into the file system
  html_dir = os.path.join('docs', 'demo2')
  os.makedirs(html_dir, exist_ok=True)
  html_file = os.path.join(html_dir, 'index.html')
  with open(html_file, 'w') as f:
    f.write(page_html)


if __name__ == '__main__':
  demo1()
  demo2()

# Make sure docs/index.html is tracked, then commit a push.
# The html should be available at <github-id>.github.io/<repo>
