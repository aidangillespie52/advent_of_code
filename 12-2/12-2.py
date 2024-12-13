def check_report(report):
    # Keeps track of whether the list is ascending or descending
    desc = False
    asc = False

    for i, x in enumerate(report[:-1]):
        diff = report[i+1] - x

        if diff > 0:
            asc = True
            # If the difference is over limit return False
            if diff > 3:
                return 0

        elif diff < 0:
            desc = True
            # If the difference is over limit return False
            if diff < -3:
                return 0
        else:
            return 0

        # If both then we return False because it has to be strictly one or the other
        if desc and asc:
            return 0
    
    # If we never encountered a condition that the report is False then must be True
    return 1

def check_report_dampen(report):
    # Iterate through each number in the report and remove it and see if it returns True
    for i in range(len(report)):
        report_copy = report.copy()
        report_copy.pop(i)    # Remove element from list
        safe = check_report(report_copy)
        if safe:    return 1
    
    # If none of them returned True then we return False
    return 0
        

if __name__ == "__main__":
    with open('12-2.txt', 'r') as f:
        # Remove \n from numbers and convert to int
        non_clean_reports = [line.split(' ') for line in f]
        clean_reports = [[int(x.replace('\n', '')) for x in report] for report in non_clean_reports]

        report_safe_list = [check_report(report) for report in clean_reports]
        report_safe_list_dampen = [check_report_dampen(report) for report in clean_reports]

        print("Safe Reports:", sum(report_safe_list))
        print("Dampened Safe Reports:", sum(report_safe_list_dampen))
            

