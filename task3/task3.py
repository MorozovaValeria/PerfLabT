import json

def rep_file(tests, values):
    report = []
    for tests_d in tests:
        value_rep = values_compare(tests_d['id'], values)
        if 'values' not in tests_d.keys():
            report.append({'id': tests_d['id'],
                            'title': tests_d['title'],
                            'value': value_rep})
        else:
            report.append({'id': tests_d['id'],
                            'title': tests_d['title'],
                            'value': value_rep,
                            'values': rep_file(tests_d['values'], values)})
    return report

def values_compare(test_id, values):
    value = ''
    for values_d in values:
        if values_d['id'] == test_id:
            value = values_d['value']
            break
    return value

tests_input = input()
values_input = input()
report_input = input()

with open(values_input, 'r') as file_v, open(tests_input, 'r') as file_t:
    load_values = json.load(file_v)['values']
    load_tests = json.load(file_t)['tests']

rep = rep_file(load_tests, load_values)

with open(report_input, 'w') as rep_inp:
    rep_inp.writelines(json.dumps({"tests": rep}, indent=3))