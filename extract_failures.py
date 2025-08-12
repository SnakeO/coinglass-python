#!/usr/bin/env python3
"""Extract failed test information from test results"""

import subprocess
import re

# Run the test and capture output
result = subprocess.run(['python3', 'tests/test_all_endpoints.py'], 
                       capture_output=True, text=True)

output = result.stdout

# Extract failed tests
failed_tests = []
lines = output.split('\n')
current_test = None
in_test = False

for i, line in enumerate(lines):
    if '### Test #' in line:
        test_num = re.search(r'Test #(\d+)', line)
        if test_num:
            current_test = {'num': test_num.group(1)}
            in_test = True
    elif in_test and '**Endpoint**' in line:
        endpoint = re.search(r'`([^`]+)`', line)
        if endpoint:
            current_test['endpoint'] = endpoint.group(1)
    elif in_test and '**Status**' in line and '❌ FAILED' in line:
        # Look for error in next few lines
        for j in range(i+1, min(i+5, len(lines))):
            if '**Error**' in lines[j]:
                error = re.search(r'`([^`]+)`', lines[j])
                if error:
                    current_test['error'] = error.group(1)
                    failed_tests.append(current_test)
                    break
        in_test = False
    elif in_test and '✅ SUCCESS' in line:
        in_test = False

# Print failed tests
print("Failed Tests:")
print("=" * 80)
for test in failed_tests[:20]:  # Show first 20
    print(f"Test #{test['num']}: {test['endpoint']}")
    print(f"  Error: {test.get('error', 'Unknown')}")
    print()