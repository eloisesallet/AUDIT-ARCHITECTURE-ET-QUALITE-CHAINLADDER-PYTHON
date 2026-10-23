from pydriller import Repository
import pandas as pd
import matplotlib.pyplot as plt
import collections

repo_url = "https://github.com/casact/chainladder-python"
commit_dates = []
commit_counts = collections.Counter()
files_modified = collections.Counter()

for commit in Repository(repo_url).traverse_commits():
    month_year = commit.author_date.strftime("%Y-%m")
    commit_counts[month_year] += 1
    commit_dates.append(commit.author_date)
    
    for m_file in commit.modified_files:
        if m_file.new_path:
            files_modified[m_file.new_path] += 1

df = pd.DataFrame(commit_dates, columns=['date'])
df['date'] = pd.to_datetime(df['date'], utc=True)

commit_df = df.groupby(df['date'].dt.to_period('M')).size()
commit_df.index = commit_df.index.to_timestamp()

average_commits = commit_df.mean()

# CHART
plt.figure(figsize=(12, 6))
plt.plot(commit_df.index, commit_df.values, marker='o', linestyle='-', color='#004a99', label='Monthly Commits')
plt.axhline(y=average_commits, color='r', linestyle='--', alpha=0.8, label=f'Average ({average_commits:.2f})')

plt.title('Frequency of Commits (2017-2026)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Number of Commits', fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.savefig('commits_chart.png', dpi=300, bbox_inches='tight')

print("COMMIT FREQUENCY PER MONTH")
for period, count in commit_df.items():
    print(f"Month: {period.strftime('%Y-%m')} | Commits: {count}")

# PRINTS
print(f"Average commits per month: {average_commits:.2f}")
print("-" * 30)
print("TOP 10 HOTSPOTS")
for file_path, count in files_modified.most_common(10):
    print(f"File: {file_path:50} | Modifications: {count}")
