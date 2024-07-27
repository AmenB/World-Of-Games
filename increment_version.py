import re
import sys

version_file = 'VERSION.txt'

def get_current_version():
    try:
        with open(version_file, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        return '01'

def increment_version(version):
    match = re.match(r'(\d+)', version)
    if match:
        number = int(match.group(1))
        return f'{number + 1:02}'
    return '01'

def update_version_file(version):
    with open(version_file, 'w') as file:
        file.write(version)

if __name__ == '__main__':
    current_version = get_current_version()
    new_version = increment_version(current_version)
    update_version_file(new_version)
    print(new_version)