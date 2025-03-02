import sys
from itertools import groupby


class Printer:
    def __init__(self, file: list[str]) -> None:
        self.file = file

    def result(self) -> list[str]:
        total_part1 = 0
        total_part2 = 0
        
        directory, instructions = [
            list(element) for i, element in groupby(self.file, key=bool) if i
        ]

        directory_int = self.parse_directory(directory)

        instructions_int = self.parse_instructions(instructions)

        for instruction in instructions_int:
            if self.check_directory(directory_int, instruction):
                total_part1 += self.middle_element(instruction)
            else:
                total_part2 += self.check_directory_part_2(directory_int, instruction)
                

        return total_part1, total_part2
    
    def check_directory(self, directory: list[list[int]], instruction: list[int]) -> bool:
        
        res = True
        try:
            for i in range(len(instruction) - 1):
                if instruction[i+1] not in directory[instruction[i]]:
                    res = False
                    break
        except KeyError:
            res = False
        
        return res
    
    def check_directory_part_2(self, directory_int: dict[int: list[int]], instruction: list[int]) -> list[int]:
        
        present = []
        absent = []

        for element in instruction:
            if element in directory_int:
                present.append(element)
            else:
                absent.append(element)

        present.sort(key=lambda x: directory_int[x])
        
        new_list = present+absent

        final_list = self.reshuffle_directory(directory_int, new_list)

        return self.middle_element(final_list)
    
    
    def reshuffle_directory(self, directory: dict[int: list[int]], instruction: list[int]) -> list[int]:
        
        sorted = False
   
        while not sorted:
            sorted = True
            for i in range(len(instruction) - 1):
                if instruction[i+1] not in directory[instruction[i]]:
                    sorted = False
                    instruction[i], instruction[i+1]  = instruction[i+1], instruction[i]
                    
        
        return instruction
                    
    
    def middle_element(self, instruction: list[int]) -> int:
        n = len(instruction)

        return instruction[n // 2]


    def transform_str_int(self, input: list[str]) -> list[list[int]]:
        for i, element in enumerate(input):
            input[i] = [int(x) for x in element]

        return input

    def parse_directory(self, directory: list[str]) -> dict[int: list[int]]:
        x = [element.split("|") for element in directory]

        parsed_directory = self.transform_str_int(x)

        directory_instructions = self.transform_list_list_dict(parsed_directory)

        return directory_instructions
    
    def transform_list_list_dict(self, parsed_directory: list[list[int]]) -> dict[int: list[int]]:
        res = {}
        
        for directory in parsed_directory:
            key = directory[0]
            values = directory[1:]
            if key in res:
                res[key].extend(values)
            else:
                res[key] = values

        return res

    def parse_instructions(self, instructions: list[str]) -> list[list[int]]:
        x = [element.split(",") for element in instructions]

        parsed_instructions = self.transform_str_int(x)

        return parsed_instructions


def main(filename: str) -> None:
    with open(filename) as output:
        file = output.read().splitlines()

        result = Printer(file)

        part_1, part_2 = result.result()

        print(f'Part 1: {part_1}')

        print(f'Part 2: {part_2}')


main(sys.argv[1])
