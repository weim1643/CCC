import sys
import glob
import os

path = sys.argv[1]
input_files = glob.glob(os.path.join(path, '*.in'))
for name in input_files:
    solution_path = os.path.join(path, 'solution.py')
    print(f'running {name}...', end=' ')
    os.system(f'python {solution_path} {name}')
    test_file = name[:-2] + 'test'
    with open(test_file, 'r') as f:
        test_lines = f.readlines()
    out_file = name[:-2] + 'out'
    with open(out_file, 'r') as f:
        out_lines = f.readlines()
    passed = True
    if len(test_lines) != len(out_lines):
        passed = False
    else: 
        for test, out in zip(test_lines, out_lines):
            if test != out:
                passed = False
    if passed:
        print('PASSED')
    else:
        print('FAILED')
