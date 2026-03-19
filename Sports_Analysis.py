#Need to add question choices through switch case and prolly functions
#Need to remove few # from Q5
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Sports_data.csv")
print("Dataset Preview")
print(df)
#Q1
print("Q1: At which competition level is the chance of winning higher?\n")
total_matches = df.groupby('Match_Level').size()
wins = df[df['Result']=='Win'].groupby('Match_Level').size()
win_percentage= (wins/total_matches)*100
print("Winning percentage of Inter-College level matches is", win_percentage['Inter-college'])
print("Winning percentage of State level matches is", win_percentage['State'])
if win_percentage['Inter-college'] > win_percentage['State']:
    print("\nHence, winning chance is higher at Inter-College level.")
elif win_percentage['Inter-college'] < win_percentage['State']:
    print("\nHence, winning chance is higher at State level.")
else:
    print("Winning chances are equal at both levels")

#Q2
print("\nQ2: Is there a correlation between match duration and winning?\n")
avg_duration = df.groupby('Result')['Duration'].mean()
print("Average match duration for Wins and Losses:",avg_duration)
if avg_duration['Win'] > avg_duration['Loss']:
    print("Hence winning matches tend to last longer.")
elif avg_duration['Win'] < avg_duration['Loss']:
    print("Hence winning matches tend to last shorter.")
else:
    print("Match duration is similar for Wins and Losses.")

#Q3
print("\nQ3: Win-Loss Ratio across competition levels\n")
win = df[df["Result"]=="Win"].groupby('Match_Level').size() 
loss = df[df["Result"]=="Loss"].groupby('Match_Level').size() 
print("Ratio for Inter-College level:\n Win:Loss - ",win['Inter-college'],":",loss['Inter-college'])
print("Ratio for State level:\n Win:Loss - ",win['State'],":",loss['State'])

#Q4
print("\nQ4: Most dominant win based on score margin and full record of that match\n")
wins_only = df[df['Result']=='Win'].copy()
wins_only['Margin'] = wins_only['Score_For']- wins_only['Score_Against']
max_margin= wins_only['Margin'].idxmax()
max_row= wins_only.loc[max_margin]
print("Our largest victory margin was", max_row['Margin'],"points.\n")
print("Full record of this match:")
print("-" * 40)
print(max_row)
print("-" * 40)

#Q5
print("\nQ5: Performance trend overtime\n")
df['Date']= pd.to_datetime(df['Date'],dayfirst=True)
df= df.sort_values('Date')
#finding cumulative wins
wins_so_far = 0
total_so_far = 0
trend_list = []

for i in df['Result']:
    total_so_far = total_so_far + 1
    if i == 'Win':
        wins_so_far= wins_so_far + 1
    current_rate= (wins_so_far/total_so_far)*100
    trend_list.append(current_rate)

df['Win_Rate_Trend'] = trend_list
exact_dates = [d.strftime('%d-%m-%y') for d in df['Date']]
plt.plot(exact_dates,df['Win_Rate_Trend'],marker = 'o',color='blue')
plt.title('Performance Trend')
plt.xlabel('Date of Match')
plt.ylabel('Cumulative win percentage(%)')
plt.grid(True)
plt.xticks(rotation=45)
#plt.savefig('Sports_Performance_Trend.png')
plt.show()
