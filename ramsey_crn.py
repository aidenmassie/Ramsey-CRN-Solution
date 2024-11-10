import itertools

def NumbersAreValid(numbers, n):
    numbers_dict = dict()

    for number in numbers:
        if not number in numbers_dict:
            numbers_dict[number] = 1
        else:
            numbers_dict[number] += 1
    
    species_count = numbers_dict.values()
    species_count_record = dict()
    
    for count in species_count:
        if not count in species_count_record:
            species_count_record[count] = 1
        else:
            species_count_record[count] += 1
    
    for count_record in species_count_record:
        if count_record >= n:
            return True
    
    return False

def CheckNumbers(configuration, n):
    new_configuration = [configuration]
    rules = list(itertools.combinations(range(0, len(configuration)), 2))

    for number in new_configuration:
        if NumbersAreValid(number, n):
            for rule in rules:
                number_copy = number.copy()

                if number_copy[rule[0]] > 0 and number_copy[rule[1]] > 0:
                    number_copy[rule[0]] -= 1
                    number_copy[rule[1]] -= 1
                    number_copy.sort(reverse=True)

                    if not number_copy in new_configuration:
                        new_configuration.append(number_copy)
        else:
            return number

    return []

def RamseyCRN(n):
    if n <= 2:
        return n
    else:
        configuration = [n]*n

        while True:
            checker = CheckNumbers(configuration, n)
            if not checker:
                break
            else:
                re_add = 0
                configuration = checker

                for number in configuration:
                    if number == n:
                        re_add += 1
                
                configuration += [n]*(n-re_add)
                configuration.sort(reverse=True)
        
        return len(configuration)

if __name__=="__main__":
    n = int(input('Enter a number: '))
    print(RamseyCRN(n))