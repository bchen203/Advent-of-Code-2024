
def is_monotonically_increasing(report_: list):
    if len(report_) == 1:
        return True
    elif len(report_) == 2:
        return report_[0] < report_[1]
    elif len(report_) == 3:
        return report_[0] < report_[1] < report_[2]
    else:
        # print(list[1:-1])
        return is_monotonically_increasing(report_[1:-1]) and report_[0] < report_[1] and report_[-2] < report_[-1]

def is_monotonically_decreasing(report_: list):
    if len(report_) == 1:
        return True
    elif len(report_) == 2:
        return report_[0] > report_[1]
    elif len(report_) == 3:
        return report_[0] > report_[1] > report_[2]
    else:
        # print(list[1:-1])
        return is_monotonically_decreasing(report_[1:-1]) and report_[0] > report_[1] and report_[-2] > report_[-1]

def is_increasing_by_3(report_: list):
    for i in range(len(report_) - 1):
        if report_[i] > report_[i + 1] or report_[i + 1] - report_[i] > 3:
            return False
    return True

def is_decreasing_by_3(report_: list):
    for i in range(len(report_) - 1):
        if report_[i] < report_[i + 1] or report_[i] - report_[i + 1] > 3:
            return False
    return True

def is_safe(report_: list):
    if is_monotonically_increasing(report_):
        if is_increasing_by_3(report_):
            return True
    elif is_monotonically_decreasing(report_):
        if is_decreasing_by_3(report_):
            return True
    return False

with open("../Input/Day_2.txt", "r") as file:
    lines = file.readlines()

reports = []
for line in lines:
    temp = line.split()
    report = [int(num) for num in temp]
    reports.append(report)

# Part 1 Solution
total_safe_reports = 0
for report in reports:
    if is_safe(report):
        total_safe_reports += 1

print(f"total safe reports: {total_safe_reports}")

# Part 2 Solution
total_safe_reports_with_dampen = 0
for report in reports:
    if is_safe(report):
        total_safe_reports_with_dampen += 1
    else: # not only increasing or decreasing
        for i in range(len(report)):
            temp = report[:i] + report[i + 1:]
            if is_safe(temp):
                total_safe_reports_with_dampen += 1
                break

print(f"total safe report w/ dampens: {total_safe_reports_with_dampen}")