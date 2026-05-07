import pandas as pd
import matplotlib.pyplot as plt

path = r"C:\Users\SUMEDHA KUNDU\OneDrive\Desktop\helpdesk analysis\python\\"

q1 = pd.read_csv(r"C:\Users\SUMEDHA KUNDU\OneDrive\Desktop\helpdesk analysis\data\query1_issue_types.csv")
q2 = pd.read_csv(r"C:\Users\SUMEDHA KUNDU\OneDrive\Desktop\helpdesk analysis\data\query2_resolution_priority.csv")
q3 = pd.read_csv(r"C:\Users\SUMEDHA KUNDU\OneDrive\Desktop\helpdesk analysis\data\query3_monthly_trend.csv")
q5 = pd.read_csv(r"C:\Users\SUMEDHA KUNDU\OneDrive\Desktop\helpdesk analysis\data\query5_status.csv")

# Chart 1 - Issue Types
plt.figure(figsize=(10,5))
plt.bar(q1['issue_type'], q1['total_tickets'], color='steelblue')
plt.title('Ticket Volume by Issue Type', fontsize=14)
plt.xlabel('Issue Type')
plt.ylabel('Total Tickets')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(path + 'chart1_issue_types.png')
plt.close()
print("Chart 1 done!")

# Chart 2 - Resolution by Priority
plt.figure(figsize=(8,5))
plt.bar(q2['priority'], q2['avg_resolution_hours'], color='tomato')
plt.title('Average Resolution Time by Priority (Hours)', fontsize=14)
plt.xlabel('Priority')
plt.ylabel('Avg Hours')
plt.tight_layout()
plt.savefig(path + 'chart2_resolution_priority.png')
plt.close()
print("Chart 2 done!")

# Chart 3 - Monthly Trend
plt.figure(figsize=(12,5))
plt.plot(q3['month'], q3['tickets_opened'], marker='o', color='coral')
plt.title('Monthly Ticket Volume Trend', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Tickets Opened')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig(path + 'chart3_monthly_trend.png')
plt.close()
print("Chart 3 done!")

# Chart 4 - Status Pie
plt.figure(figsize=(8,8))
plt.pie(q5['total_tickets'], labels=q5['status'], autopct='%1.1f%%', startangle=140)
plt.title('Ticket Status Breakdown', fontsize=14)
plt.tight_layout()
plt.savefig(path + 'chart4_status_pie.png')
plt.close()
print("Chart 4 done!")

print("\nALL CHARTS SAVED!")