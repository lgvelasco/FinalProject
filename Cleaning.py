pulp_fiction = 'Pulp_Fiction.txt'
test = 'Pulp_Fiction_Clean.txt'

fp = open(pulp_fiction, 'r')
ft = open(test, 'w')

for line in fp:
    ft.write(line.lstrip())

fp.close()
ft.close()