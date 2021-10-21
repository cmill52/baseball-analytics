import pandas as pd
import numpy as np
import seaborn as sns

class LukeJacksonVisualizations():
  def __init__(self):
    self.df = pd.read_csv(r'\Users\Cmiller\Downloads\savant_data.csv')
    
  def stuff_visualization(self):
    return sns.scatterplot(
      data = self.df,
      x = 'velocity',
      y = 'spin_rate',
      hue = 'player_name'
      )
