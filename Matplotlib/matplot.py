
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917, 31991, 27076, 26549, 21955, 20937, 18591, 15288, 13123, 11254, 8659]

explode=[0,0,0,0.1,0,0,0,0,0,0,0,0,0,0,0]

labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']

plt.pie(slices, labels=labels, explode=explode,shadow=True,
autopct='%1.1f%%',wedgeprops={'edgecolor': 'black'})

plt.title("Pie chart")
plt.tight_layout()
plt.show()