import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb
import pandas as pd
from PIL import Image


# plot style
sb.set(style="whitegrid")

# import dataset
data = pd.read_csv('HW.txt', sep='\t')

# scatter plot
plt.figure(figsize = (10,6))
sb.scatterplot(data, x='ageYear', y='heightIn', 
               hue='sex', style='sex', s=100, 
               palette={'f': 'red', 'm': 'blue'})
plt.xlabel('Age')
plt.ylabel('Height')
plt.title('Age vs Height by Sex')
plt.legend(title='Sex', labels=['Female','Male'])
plt.savefig('scatter.png')

# show the scatter
img = Image.open('scatter.png')
img.show()

# part b (i) - regression line for males
males = data[data['sex'] == 'm']
sb.lmplot(males, x='ageYear', y='heightIn', ci = 95,
          markers='o', line_kws={'color': 'green'}, scatter_kws={'alpha': 0.6})
plt.title('Regression Line Males')         
plt.xlabel('Age')
plt.ylabel('Height')
plt.savefig('sctMale.png')

# part b (ii) - reg line for females
females = data[data['sex'] == 'f']
sb.lmplot(females, x='ageYear', y='heightIn', ci = 95,
          markers='o', line_kws={'color': 'yellow'}, scatter_kws={'alpha': 0.6})
plt.title('Regression Line Females')         
plt.xlabel('Age')
plt.ylabel('Height')
plt.savefig('sctFemale.png')

# part b (iii) - reg line for all
sb.lmplot(data, x='ageYear', y='heightIn', ci = 95,
          markers='o', line_kws={'color': 'brown'}, scatter_kws={'alpha': 0.6})
plt.title('Regression Line All')         
plt.xlabel('Age')
plt.ylabel('Height')
plt.savefig('sctAll.png')

# show all scatters:
imgM = Image.open('sctMale.png')
imgF = Image.open('sctFemale.png')
imgAll = Image.open('sctAll.png')
imgM.show()
imgF.show()
imgAll.show()
