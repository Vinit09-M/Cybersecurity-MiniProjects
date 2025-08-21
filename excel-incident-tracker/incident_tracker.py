from openpyxl import Workbook
from datetime import datetime

# Create a workbook and select active sheet
wb = Workbook()
ws = wb.active
ws.title = "Incidents"

# Add headers
headers = ["Date", "Incident Type", "Severity", "Status", "Description", "Assigned To"]
ws.append(headers)

# Example incidents (you can add more)
incidents = [
    ["2025-08-21", "Phishing Email", "High", "Open", "User received suspicious email", "Alice"],
    ["2025-08-20", "Malware Detected", "Medium", "Closed", "Malware quarantined on laptop", "Bob"],
    ["2025-08-19", "Unauthorized Login Attempt", "Low", "Investigating", "Multiple failed logins", "Charlie"]
]

for inc in incidents:
    ws.append(inc)

# Auto-fit column widths (basic)
for col in ws.columns:
    max_length = 0
    col_letter = col[0].column_letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    ws.column_dimensions[col_letter].width = max_length + 2

# Save file
file_name = "cyber_incidents.xlsx"
wb.save(file_name)
print(f"Excel file '{file_name}' created successfully!")
