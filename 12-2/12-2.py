def check_report(report):
    desc = False
    asc = False

    for i, x in enumerate(report[:-1]):
        diff = report[i+1] - x

        if diff > 0:
            asc = True
            if diff > 3:
                return 0

        elif diff < 0:
            desc = True
            if diff < -3:
                return 0
        else:
            return 0

        if desc and asc:
            return 0
        
    return 1

if __name__ == "__main__":
    with open('12-2.txt', 'r') as f:
        non_clean_reports = [line.split(' ') for line in f]
        clean_reports = [[int(x.replace('\n', '')) for x in report] for report in non_clean_reports]
        report_safe_list = [check_report(report) for report in clean_reports]

        print("Safe Reports:", sum(report_safe_list))
            

