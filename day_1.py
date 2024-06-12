import openpyxl as xl
import re

word_number_dict = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}



def main():
    
    template = r'C:\Users\tyler.hansen\OneDrive - STEPSTONE GROUP LP\Desktop\Repo\Advent of Code\day1.xlsx'
    data_set_new = get_data(template)

    result = data_set_parse(data_set_new)
    
    result

def get_data(template: str):
    wb = xl.open(template, read_only=False)
    ws = wb.active
    for column in ws.iter_cols(min_col=1, values_only=True):
        output = [str(x) for x in column]
        return output
    
        

def data_set_parse(data_set: list[str]) -> list[str]:

    
    for data in data_set:
        if matches:= re.findall(r'(?:(?=(one|two|three|four|five|six|seven|eight|nine)|(\d)))', data):
            first_match = matches[0]
            last_match = matches[-1]
            first_list = list(first_match)
            last_list = list(last_match)
            first_list.extend(last_list)
            first_list.remove('')
            first_list.remove('')
            clean(first_list)
           


def clean(first_list: list[str]) -> list[str]:
    
    new_list = [word_number_dict.get(item, item) for item in first_list]
    addition = new_list[0] + new_list[-1]
    print(addition)

    
            
    
if __name__ == "__main__":
    main()