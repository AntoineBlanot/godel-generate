import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file', type=str, help='File to clean')
args = parser.parse_args()

with open(args.file, 'r') as f:
    data = f.read().split('\n')

cleaned_data = []
for i in range(len(data)):
    d = data[i]
    print(str(i) + ') ' + d)
    i = ''
    while i not in ['y', 'n']:
        i = input('Do you want to keep that data (y/n): ')
    if i == 'y':
        cleaned_data.append(d + '\n')

clean_file = 'clean_' + args.file
with open(clean_file, 'w') as f:
    f.writelines(cleaned_data)

print('Clean data has been saved in {} with {} examples ({} removed).'.format(clean_file, len(cleaned_data), len(data) - len(cleaned_data)))