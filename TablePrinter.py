print("Prajwal BR\nUSN:1AY24AI083\nSec:O")
def print_table(data, headers=None, align=None, title=None):
    """
    Prints a formatted table from 2D list data.
    
    Args:
        data: List of lists containing table data (rows x columns)
        headers: List of column headers (optional)
        align: List of alignment characters ('l', 'c', 'r') for each column (optional)
        title: Table title (optional)
    """
    if not data:
        print("No data to display")
        return

    # Determine column widths
    col_widths = []
    num_cols = len(data[0])
    
    working_data = data + [headers] if headers else data
    
    for col in range(num_cols):
        max_width = max(len(str(row[col])) for row in working_data)
        col_widths.append(max_width)
    
    if not align:
        align = ['l'] * num_cols  
    elif len(align) != num_cols:
        align = (align * num_cols)[:num_cols]  
    
    if title:
        total_width = sum(col_widths) + 3 * (len(col_widths) - 1)
        print(f"\n{title.center(total_width)}")
    
    if headers:
        header_row = []
        for i, header in enumerate(headers):
            if align[i] == 'l':
                header_row.append(str(header).ljust(col_widths[i]))
            elif align[i] == 'c':
                header_row.append(str(header).center(col_widths[i]))
            else:
                header_row.append(str(header).rjust(col_widths[i]))
        print(" | ".join(header_row))
        print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))
    
    for row in data:
        formatted_row = []
        for i, cell in enumerate(row):
            if align[i] == 'l':
                formatted_row.append(str(cell).ljust(col_widths[i]))
            elif align[i] == 'c':
                formatted_row.append(str(cell).center(col_widths[i]))
            else:
                formatted_row.append(str(cell).rjust(col_widths[i]))
        print(" | ".join(formatted_row))


if __name__ == "__main__":
    inventory = [
        ["Apples", 25, 1.99],
        ["Oranges", 40, 2.49],
        ["Bananas", 30, 0.99],
        ["Grapes", 15, 3.99],
        ["Mangoes", 10, 4.49]
    ]
    
    print("\nFruit Inventory:")
    print_table(
        data=inventory,
        headers=["Fruit", "Quantity", "Price"],
        align=['l', 'r', 'r'],
        title="Current Inventory Status"
    )
    
    employee_data = [
        ["John Smith", "Sales", 5, 45000],
        ["Sarah Johnson", "Marketing", 3, 52000],
        ["Mike Brown", "IT", 7, 68000],
        ["Emily Davis", "HR", 2, 48000]
    ]
    
    print("\nEmployee Directory:")
    print_table(
        data=employee_data,
        headers=["Name", "Department", "Years", "Salary"],
        align=['l', 'l', 'c', 'r'],
        title="Company Employees"
    )
