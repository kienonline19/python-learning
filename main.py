import openpyxl


def protect_excel_sheets(file_path, password):
    # Load the workbook
    workbook = openpyxl.load_workbook(file_path)

    # Iterate through all sheets
    for sheet in workbook.sheetnames:
        # Select the sheet
        worksheet = workbook[sheet]

        # Protect the sheet
        worksheet.protection.sheet = True
        worksheet.protection.password = password

        # Optional: Set specific protection options
        worksheet.protection.enable()

    # Save the workbook
    workbook.save(file_path)
    print(f"All sheets in {file_path} have been protected.")


# Usage example
file_path = 'Book1.xlsx'
password = '12345'
protect_excel_sheets(file_path, password)
