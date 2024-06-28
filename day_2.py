import openpyxl as xl
import re


def main():
    
    template = r'C:\Users\tyler.hansen\OneDrive - STEPSTONE GROUP LP\Desktop\Repo\Advent of Code\day2.xlsx'
    data_set_new = get_data(template)

    clean_list(data_set_new)


def get_data(template: str):
    wb = xl.open(template, read_only=False)
    ws = wb.active
    for column in ws.iter_cols(min_col=1, values_only=True):
        output = [str(x) for x in column]
        return output
    

def clean_list(data_set_new: list[str]) -> list[str]:
    new_list = []
    delimiters = [": ", "; ", ", "]
    for data in data_set_new:
        new_list = re.split(r'(: |; |, )', data)
        final_list = [item for item in new_list if item not in delimiters]
        parse_list(final_list)
    

def parse_list(final_list: list[str]) -> list[str]:
    unique_list = []

    matches = re.findall(r'(\d* red|\d* blue|\d* green)', str(final_list))
    for match in matches:
        number, color = match.split(" ")
        int_number = int(number)
        if color == 'red' and int_number > 12:
            unique_list.append(final_list[0])
        elif color == 'green' and int_number > 13:
            unique_list.append(final_list[0])
        elif color == 'blue' and int_number > 14:
            unique_list.append(final_list[0])
        else:
            pass
    check_list = [item for item in final_list if item not in unique_list]
    print(check_list[0])
    
            



if __name__ == "__main__":
    main()