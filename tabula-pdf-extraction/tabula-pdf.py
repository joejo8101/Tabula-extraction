# from tabula import read_pdf
# import re

# # Specify the path to your file
# file = '/home/user/Documents/Test_Data.pdf'

# # Read your PDF file with tabula
# tables = read_pdf(file, pages="all", multiple_tables=True)
# print("TABLES", tables)
# # Dictionary to store the field values
# field_values = {}

# # Field labels and their corresponding text to match
# field_labels = {
#     'name_address_employer': r'Name and address of the Employer/Specified Bank\n(.+?)\n',
#     'name_address_employee': r'Name and address of the Employee/Specified senior citizen\n(.+?)\n',
#     'pan_deductor': r'PAN of the Deductor\n([A-Z0-9]{10})',
#     'tan_deductor': r'TAN of the Deductor\n([A-Z0-9]{10})',
#     'pan_employee': r'PAN of the Employee/Specified senior citizen\n(.+?)\n',
#     'assessment_year': r'Assessment Year\n(\d{4}-\d{2})',
#     'salary_17_1': r'Salary as per provisions contained in section 17\(1\)\(a\) ([\d,.]+)',
#     'value_perquisites_17_2': r'Value of perquisites under section 17\(2\)[\s\S]*?\d{1,3},\d{1,3},\d{1,3}[\s\S]*?([\d,.]+)',
#     'profits_lieu_17_3': r'Profits in lieu of salary under section 17\(3\)[\s\S]*?\d{1,3},\d{1,3},\d{1,3}[\s\S]*?([\d,.]+)',
#     'total_salary': r'Total\s*([\d,.]+)',
#     'salary_from_other': r'Reported total amount of salary received from other employer\(s\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'travel_concession_10_5': r'Travel concession or assistance under section 10\(5\)\(a\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'gratuity_10_10': r'Death-cum-retirement gratuity under section 10\(10\)\(b\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'pension_commuted_10_10a': r'Commuted value of pension under section 10\(10A\)\(c\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'leave_encashment_10_1aa': r'Cash equivalent of leave salary encashment under section 10\(10AA\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'house_rent_hra_10_13a': r'House rent allowance under section 10\(13A\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'any_other_exemption_10': r'Total amount of any other exemption under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_any_other_exemption_10': r'Total amount of exemption claimed under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_exemptions_10': r'Total amount of exemption claimed under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_salary_current_employer': r'Total amount of salary received from current employer(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'standard_deduction_16_ia': r'Standard deduction under section 16\(ia\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'entertainment_allowance_16_ii': r'Entertainment allowance under section 16\(ii\)\(a\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_on_employment_16_iii': r'Tax on employment under section 16\(iii\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_deduction': r'Total amount of deductions under section 16(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'income_house_property': r'Income \(or admissible loss\) from house property reported by employee offered for TDS(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'income_other_sources': r'Income under the head Other Sources offered for TDS(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_other_income': r'Total of amount deductible under any other provision\(s\) of Chapter VI-A(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'gross_total_income': r'Gross total income \(6\+8\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_80c': r'Total Deduction in respect of life insurance premia, contributions to provident fund etc\. under section 80C(?:[\s\S]+?Gross Amount Deductible Amount\n([\d,.]+)|: Not found)',
#     'deduction_80ccc': r'Deduction in respect of contribution to certain pension funds under section 80CCC(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_pension_80ccd_1': r'Deduction in respect of contribution by taxpayer to pension scheme under section 80CCD \(1\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_total_80c_ccc_ccd_1': r'Total deduction under section 80C, 80CCC and 80CCD\(1\)\(c\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_pension_80ccd_1b': r'Deduction in respect of amount paid/deposited to notified pension scheme under section 80CCD \(1B\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_employer_pension_80ccd_2': r'Deduction in respect of contribution by Employer to pension scheme under section 80CCD \(2\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_health_insurance_80d': r'Deduction in respect of health insurance premia under section 80D(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_education_loan_80e': r'Deduction in respect of interest on loan taken for higher education under section 80E(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_donations_80g': r'Deduction in respect of interest on deposits in savings account under section 80TTA(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_interest_savings_80tta': r'Deduction in respect of interest on loan taken for higher education under section 80E(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_any_other_vi_a': r'Total of amount deductible under any other provision\(s\) of Chapter VI-A(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_total_any_other_vi_a': r'Total Deduction in respect of donations to certain funds, charitable institutions, etc. under section 80G(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_aggregate_vi_a': r'Deduction in respect of contribution by Employer to pension scheme under section 80CCD \(2\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_taxable_income': r'Total taxable income \(6\+8\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_on_total_income': r'Tax on total income(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'rebate_section_87a': r'Rebate under section 87A, if applicable(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'surcharge': r'Surcharge(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'health_education_cess': r'Health and education cess(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_payable': r'Tax payable(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'relief_section_89': r'Less: Relief under section 89 \(attach details\)(?:[\s\S]+?: Not found)',
#     'net_tax_payable': r'Net tax payable \(17-18\)(?:[\s\S]+?\n([\d,.]+)|: Not found)'
# }

# # Iterate over each table
# # Iterate over each table
# for table in tables:
#     for key, value in field_labels.items():
#         # Iterate over each row in the table
#         for row in table.iterrows():
#             # Check if the value exists in the row
#             if re.search(value, str(row[1])):
#                 # Get the corresponding field value using regex match
#                 match = re.search(value, str(row[1]))
#                 field_value = match.group(1)  # Extract the matched value from the regex match
#                 # Store the field value in the dictionary
#                 field_values[key] = field_value
#                 break

# # Print the field values
# for key, value in field_values.items():
#     print("HI",f"{key}: {value}")
# import cv2
# import pytesseract
# from pdf2image import convert_from_path
# import numpy as np
# # # Field labels and their corresponding text to match

# field_labels = {
#     'name_address_employer': r'Name and address of the Employer/Specified Bank\n(.+?)\n',
#     'name_address_employee': r'Name and address of the Employee/Specified senior citizen\n(.+?)\n',
#     'pan_deductor': r'PAN of the Deductor\n([A-Z0-9]{10})',
#     'tan_deductor': r'TAN of the Deductor\n([A-Z0-9]{10})',
#     'pan_employee': r'PAN of the Employee/Specified senior citizen\n(.+?)\n',
#     'assessment_year': r'Assessment Year\n(\d{4}-\d{2})',
#     'salary_17_1': r'Salary as per provisions contained in section 17\(1\)\(a\) ([\d,.]+)',
#     'value_perquisites_17_2': r'Value of perquisites under section 17\(2\)[\s\S]*?\d{1,3},\d{1,3},\d{1,3}[\s\S]*?([\d,.]+)',
#     'profits_lieu_17_3': r'Profits in lieu of salary under section 17\(3\)[\s\S]*?\d{1,3},\d{1,3},\d{1,3}[\s\S]*?([\d,.]+)',
#     'total_salary': r'Total\s*([\d,.]+)',
#     'salary_from_other': r'Reported total amount of salary received from other employer\(s\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'travel_concession_10_5': r'Travel concession or assistance under section 10\(5\)\(a\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'gratuity_10_10': r'Death-cum-retirement gratuity under section 10\(10\)\(b\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'pension_commuted_10_10a': r'Commuted value of pension under section 10\(10A\)\(c\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'leave_encashment_10_1aa': r'Cash equivalent of leave salary encashment under section 10\(10AA\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'house_rent_hra_10_13a': r'House rent allowance under section 10\(13A\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'any_other_exemption_10': r'Total amount of any other exemption under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_any_other_exemption_10': r'Total amount of exemption claimed under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_exemptions_10': r'Total amount of exemption claimed under section 10(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_salary_current_employer': r'Total amount of salary received from current employer(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'standard_deduction_16_ia': r'Standard deduction under section 16\(ia\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'entertainment_allowance_16_ii': r'Entertainment allowance under section 16\(ii\)\(a\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_on_employment_16_iii': r'Tax on employment under section 16\(iii\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_deduction': r'Total amount of deductions under section 16(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'income_house_property': r'Income \(or admissible loss\) from house property reported by employee offered for TDS(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'income_other_sources': r'Income under the head Other Sources offered for TDS(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_other_income': r'Total of amount deductible under any other provision\(s\) of Chapter VI-A(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'gross_total_income': r'Gross total income \(6\+8\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_80c': r'Total Deduction in respect of life insurance premia, contributions to provident fund etc\. under section 80C(?:[\s\S]+?Gross Amount Deductible Amount\n([\d,.]+)|: Not found)',
#     'deduction_80ccc': r'Deduction in respect of contribution to certain pension funds under section 80CCC(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_pension_80ccd_1': r'Deduction in respect of contribution by taxpayer to pension scheme under section 80CCD \(1\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_total_80c_ccc_ccd_1': r'Total deduction under section 80C, 80CCC and 80CCD\(1\)\(c\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_pension_80ccd_1b': r'Deduction in respect of amount paid/deposited to notified pension scheme under section 80CCD \(1B\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_employer_pension_80ccd_2': r'Deduction in respect of contribution by Employer to pension scheme under section 80CCD \(2\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_health_insurance_80d': r'Deduction in respect of health insurance premia under section 80D(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_education_loan_80e': r'Deduction in respect of interest on loan taken for higher education under section 80E(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_donations_80g': r'Deduction in respect of interest on deposits in savings account under section 80TTA(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_interest_savings_80tta': r'Deduction in respect of interest on loan taken for higher education under section 80E(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_any_other_vi_a': r'Total of amount deductible under any other provision\(s\) of Chapter VI-A(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_total_any_other_vi_a': r'Total Deduction in respect of donations to certain funds, charitable institutions, etc. under section 80G(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'deduction_aggregate_vi_a': r'Deduction in respect of contribution by Employer to pension scheme under section 80CCD \(2\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'total_taxable_income': r'Total taxable income \(6\+8\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_on_total_income': r'Tax on total income(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'rebate_section_87a': r'Rebate under section 87A, if applicable(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'surcharge': r'Surcharge(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'health_education_cess': r'Health and education cess(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'tax_payable': r'Tax payable(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'net_tax_payable': r'Net tax payable \(17-18\)(?:[\s\S]+?\n([\d,.]+)|: Not found)',
#     'relief_section_89': r'Less: Relief under section 89 \(attach details\)(?:[\s\S]+?: Not found)'

# }

# # Step 1: Convert PDF to images
# pdf_path = '/home/user/Documents/Test_Data.pdf'
# images = convert_from_path(pdf_path)

# # Step 2: Extract text from each page using Pytesseract
# for i, image in enumerate(images):
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     text = pytesseract.image_to_string(image)
#     print(f"Page {i+1}:\n{text}\n")


# import cv2
# import pytesseract
# from pdf2image import convert_from_path
# import numpy as np
# import re

# # Step 1: Convert PDF to images
# pdf_path = '/home/user/Documents/Test_Data.pdf'
# images = convert_from_path(pdf_path)

# # Step 2: Initialize the data dictionary
# data_dict = {}

# # Step 3: Extract text from each page using Pytesseract
# for i, image in enumerate(images):
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     text = pytesseract.image_to_string(image)

#     # Step 4: Extract values using regular expressions or string manipulation
#     pan_employee_match = re.search(r'PAN of the Employee/Specified senior citizen\n(\w+)', text)
#     if pan_employee_match:
#         data_dict['pan_employee'] = pan_employee_match.group(1)

#     assessment_year_match = re.search(r'Assessment Year:\s+(\d{4}-\d{2})', text)
#     if assessment_year_match:
#         data_dict['assessment_year'] = assessment_year_match.group(1)

#     salary_17_1_match = re.search(r'Salary as per provisions contained in section 17\(1\)\s+([\d.]+)', text)
#     if salary_17_1_match:
#         data_dict['salary_17_1'] = float(salary_17_1_match.group(1))

#     value_prerequisites_17_2_match = re.search(r'Value of perquisites under section 17\(2\)\s+([\d.]+)', text)
#     if value_prerequisites_17_2_match:
#         data_dict['value_prerequisites_17_2'] = float(value_prerequisites_17_2_match.group(1))

#     profits_in_lieu_17_3_match = re.search(r'Profits in lieu of salary under section 17\(3\)\s+([\d.]+)', text)
#     if profits_in_lieu_17_3_match:
#         data_dict['profits_in_lieu_17_3'] = float(profits_in_lieu_17_3_match.group(1))

#     # Continue extracting other fields in a similar manner for each page

#     # Step 5: Print the extracted values for the current page
#     print(f"Page {i+1}:\n{text}\n")
#     print("Extracted Values:")
#     for key, value in data_dict.items():
#         print(f"{key}: {value}")
#     print("\n")

# # Step 6: Print the final populated dictionary
# print("Populated Dictionary:")
# print(data_dict)
# import cv2
# import pytesseract
# from pdf2image import convert_from_path
# import numpy as np
# import re

# # Step 1: Convert PDF to images
# pdf_path = '/home/user/Documents/Test--Data.pdf'
# images = convert_from_path(pdf_path)

# # Step 2: Initialize the data dictionary
# data_dict = {}

# # Step 3: Define the mapping of patterns to Django model field names
# pattern_mapping = {
#     'pan_deductor': r'PAN of the Deductor\s+(\w+)',
#     'tan_deductor': r'TAN of the Deductor\s+(\w+)',
#     'pan_employee': r'PAN of the Employee/Specified senior citizen\s+(\w+)',
#     # 'pan_employee': r'PAN of the Employee/Specified senior citizen\n(\w+)',
#     'assessment_year': r'Assessment Year:\s+(\d{4}-\d{2})',
#     'salary_17_1': r'Salary as per provisions contained in section 17\(1\)\s+([\d.]+)',
#     'value_prerequisites_17_2': r'Value of perquisites under section 17\(2\)\s+([\d.]+)',
#     'profits_in_lieu_17_3': r'Profits in lieu of salary under section 17\(3\)\s+([\d.]+)',
#     # Add more field names and patterns as needed
# }

# # Swap keys and values in the pattern_mapping dictionary
# pattern_mapping = {value: key for key, value in pattern_mapping.items()}

# # Step 4: Extract text from each page using Pytesseract
# for i, image in enumerate(images):
#     image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
#     text = pytesseract.image_to_string(image)

#     # Step 5: Extract values using pattern mapping
#     for pattern, field_name in pattern_mapping.items():
#         match = re.search(pattern, text)
#         if match:
#             data_dict[field_name] = match.group(1)

#     # Step 6: Print the extracted values for the current page
#     print(f"Page {i+1}:\n{text}\n")
#     print("Extracted Values:")
#     for key, value in data_dict.items():
#         print(f"{key}: {value}")
#     print("\n")

# # Step 7: Print the final populated dictionary
# print("Populated Dictionary:")
# print(data_dict)


# import cv2
# from pdf2image import convert_from_path
# import pytesseract
# import numpy as np

# # Convert PDF pages to images
# pdf_path = '/home/user/Documents/Test_Data.pdf'
# images = convert_from_path(pdf_path)

# # Iterate over the images and perform OCR using OpenCV
# for i, image in enumerate(images):
#     # Convert the image to grayscale
#     gray = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)

#     # Apply thresholding or other preprocessing techniques if needed
#     # gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#     # Apply OCR using OpenCV
#     text = pytesseract.image_to_string(gray)

#     # Print the extracted text
#     print(f"Page {i+1}:\n{text}\n")

# import textract
# import codecs

# path = '/home/user/Documents/Test_Data.pdf'

# textract_text = textract.process(path)
# #convert bytes to string
# textract_str_text = codecs.decode(textract_text)

# print("TEXT", textract_str_text)


from tabula import read_pdf
from tabulate import tabulate
import re
import PyPDF2

# Initialize the dictionary with field names as keys and None as values
data_dict = {
    'name_address_employer': None,
    'name_address_employee': None,
    'pan_deductor': None,
    'tan_deductor': None,
    'pan_employee': None,
    'assessment_year': None,
    'salary_17_1': None,
    'value_prerequisites_17_2': None,
    'profits_in_lieu_17_3': None,
    'total_salary': None,
    'salary_from_other': None,
    'travel_concession_10_5': None,
    'gratuity_10_10': None,
    'pension_commuted_10_10a': None,
    'leave_encashment_10_1aa': None,
    'house_rent_hra_10_13a': None,
    'any_other_exemption_10': None,
    'total_any_other_exemption_10': None,
    'total_exemptions_10': None,
    'total_salary_current_employer': None,
    'standard_deduction_16_ia': None,
    'entertainment_allowance_16_ii': None,
    'tax_on_employment_16_iii': None,
    'total_deduction': None,
    'income_house_property': None,
    'income_other_sources': None,
    'total_other_income': None,
    'gross_total_income': None,
    'deduction_80c': None,
    'deduction_80ccc': None,
    'deduction_pension_80ccd_1': None,
    'deduction_total_80c_ccc_ccd_1': None,
    'deduction_pension_80ccd_1b': None,
    'deduction_employer_pension_80ccd_2': None,
    'deduction_health_insurance_80d': None,
    'deduction_education_loan_80e': None,
    'deduction_donations_80g': None,
    'deduction_interest_savings_80tta': None,
    'deduction_any_other_vi_a': None,
    'deduction_total_any_other_vi_a': None,
    'deduction_aggregate_vi_a': None,
    'total_taxable_income': None,
    'tax_on_total_income': None,
    'rebate_87a': None,
    'surcharge': None,
    'health_edu_cess': None,
    'tax_payable': None,
    'relief_89': None,
    'net_tax_payable': None,
}

search_patterns = {
    'name_address_employer': r'Name and address of the Employer/Specified Bank\n([\s\S]+?)Name and address of the Employee/Specified senior citizen',
    'name_address_employee': r'Name and address of the Employee/Specified senior citizen\n([\s\S]+?)PAN of the Deductor',
    'pan_deductor': r'PAN of the Deductor\n([A-Z0-9]{10})',
    'tan_deductor': r'TAN of the Deductor\n([A-Z0-9]{10})',
    'pan_employee': r'PAN of the Employee/Specified senior citizen\n(.+?)\n',
    'assessment_year': r'Assessment Year\n(\d{4}-\d{2})',
    'salary_17_1': r'Salary as per provisions contained in section 17\(1\)\s+nan\s+([\d,]+)',
    'total_salary': r'Total\s+nan\s+nan\s+nan\s+([\d,]+)',
    'salary_from_other': r'Reported total amount of salary received from other employer\(s\)\s+nan\s+nan\s+nan\s+([\d,]+)',
    'travel_concession_10_5': r'Travel concession or assistance under section 10\(5\)\s+nan\s+([\d,]+)',
    'gratuity_10_10': r'Death-cum-retirement gratuity under section 10\(10\)\s+nan\s+([\d,]+)',
    'pension_commuted_10_10a': r'Commuted value of pension under section 10\(10A\)\s+nan\s+([\d,]+)',
    'house_rent_hra_10_13a': r'House rent allowance under section 10\(13A\)\s+nan\s+([\d,]+)',
    'any_other_exemption_10': r'Total amount of any other exemption under section 10\s+([\d,]+)',
    'standard_deduction_16_ia': r'Standard deduction under section 16\(ia\)\s+([\d,]+)',
    'entertainment_allowance_16_ii': r'Entertainment allowance under section 16\(ii\)\s+([\d,]+)',
    'tax_on_employment_16_iii': r'Tax on employment under section 16\(iii\)\s+([\d,]+)',
    'income_other_sources': r'Income under the head Other Sources offered for TDS\s+([\d,]+)',
    'total_other_income': r'Total amount of other income reported by the employee\s+nan\s+([\d,]+)',
    'gross_total_income': r'Gross total income \(6\+8\)\s+nan\s+([\d,]+)',
    'deduction_pension_80ccd_1': r'Deduction in respect of contribution by taxpayer to pension\s+scheme under section 80CCD \(1\)\s+([\d,]+)',
    'deduction_total_80c_ccc_ccd_1': r'Total deduction under section 80C, 80CCC and 80CCD\(1\)\s+([\d,]+)',
    'deduction_pension_80ccd_1b': r'Deductions in respect of amount paid/deposited to notified\s+pension scheme under section 80CCD \(1B\)\s+([\d,]+)',
    'deduction_health_insurance_80d': r'Deduction in respect of health insurance premia under section\s+80D\s+([\d,]+)',
    'deduction_education_loan_80e': r'Deduction in respect of interest on loan taken for higher\s+education under section 80E\s+([\d,]+)',
    'total_taxable_income': r'Total taxable income \(9-11\)\s+([\d,]+)',
    'tax_on_total_income': r'Tax on total income\s+([\d,]+)',
    'rebate_87a': r'Rebate under section 87A, if applicable\s+([\d,]+)',
    'surcharge': r'Surcharge, wherever applicable\s+([\d,]+)',
    'health_edu_cess': r'Health and education cess\s+([\d,]+)',
    'tax_payable': r'Tax payable \(13\+15\+16-14\)\s+([\d,]+)',
    'relief_89': r'Less: Relief under section 89 \(attach details\)\s+([\d,]+)',
    'net_tax_payable': r'Net tax payable \(17-18\)\s+([\d,]+)',

    'value_prerequisites_17_2': r'Value of perquisites under section 17\(2\) \(as per Form No\. 12BA,\s+wherever applicable\)\s+nan\s+([\d,.]+)',
    'profits_in_lieu_17_3': r'Profits in lieu of salary under section 17\(3\) \(as per Form No\. 12BA,\s+wherever applicable\)\s+nan\s+([\d,.]+)',
    'leave_encashment_10_1aa': r'Cash equivalent of leave salary encashment under section 10\(1AA\)\s+nan\s+([\d,.]+)',
    'total_any_other_exemption_10': r'Total amount of any other exemption under section 10\s+([\d,.]+)',
    'total_exemptions_10': r'Total amount of exemptions under section 10\s+nan\s+([\d,.]+)',
    'total_salary_current_employer': r'Total amount of salary received from current employer\s+nan\s+([\d,.]+)',
    'total_deduction': r'Total amount of deductions under section 16\s+nan\s+([\d,.]+)',
    'income_house_property': r'Income \(or admissible loss\) from house property reported by\s+([\d,.]+)',
    'total_other_income': r'Total amount of other income reported by the employee\s+nan\s+([\d,.]+)',
    'deduction_80c': r'\(a\) Deduction in respect of life insurance premia, contributions to\s+([\d,.]+)',
    'deduction_80ccc': r'\(b\) Deduction in respect of contribution to certain pension funds\s+([\d,.]+)',
    'deduction_employer_pension_80ccd_2': r'Deduction in respect of contribution by Employer to\s+pension\s+scheme under section 80CCD \(2\)\s+([\d,.]+)',
    'deduction_donations_80g': r'Deduction in respect of donations to certain funds, charitable institutions, etc\. under section 80G\s+([\d,.]+)',
    'deduction_interest_savings_80tta': r'Deduction in respect of interest on deposits in savings account under section 80TTA\s+([\d,.]+)',
    'deduction_any_other_vi_a': r'Amount Deductible under any other provision \(s\) of Chapter VI-A\s+nan\s+nan\s+nan\s+([\d,.]+)',
    'deduction_total_any_other_vi_a': r'Total of amount deductible under any other provision\(s\) of Chapter VI-A\s+([\d,.]+)',
    'deduction_aggregate_vi_a': r'Aggregate of deductible amount under Chapter VI-A\s+([\d,.]+)',
}

pdf_path = '/home/user/Documents/Test_Data.pdf'

# Open the PDF file
with open(pdf_path, "rb") as f:
    reader = PyPDF2.PdfReader(f)

    # Extract text from each page of the PDF
    extracted_text = ""
    for page in reader.pages:
        extracted_text += page.extract_text()

    # print("EXTRACTED TEXT", extracted_text)

    # Iterate over the search_patterns dictionary
    for field, pattern in search_patterns.items():
        match = re.search(pattern, extracted_text, re.IGNORECASE)
        if match:
            value = match.group(1).replace(',', '')
            try:
                data_dict[field] = match.group(1).strip()
            except ValueError:
                pass

# Reads table from PDF file
df_list = read_pdf(pdf_path, pages="all")

# Convert each DataFrame to a list of lists
table_data = [df.values.tolist() for df in df_list]

# Print the tabulated tables
for data in table_data:
    # print(tabulate(data))
    # print()
    table_text = '\n'.join(' '.join(str(cell) for cell in row) for row in data)

    # Search for the patterns and extract the values
    for field, pattern in search_patterns.items():
        if data_dict[field] is not None:
            continue  # Skip fields already extracted using PdfReader

        match = re.search(pattern, table_text, re.IGNORECASE)
        if match:
            value = match.group(1).replace(',', '')
            try:
                data_dict[field] = float(value)
            except ValueError:
                pass

# Print the dictionary
for key, value in data_dict.items():
    print(f"{key}: {value}")