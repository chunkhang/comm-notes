#!/usr/bin/env python3

def main():
	lines = []
	with open('data.txt', 'r') as file:
		lines = file.readlines()
		lines = list(filter(lambda x: x != '\n', lines))
		lines = list(map(lambda x: x.strip('\n'), lines))
	with open('README.md', 'w') as file:
		file.write('# Communication Skills Notes\n')
		file.write('\n')
		file.write('Tabulated notes for Communication Skills final examination ' +
			'<br/>\n')
		file.write('<br/>\n')
		file.write('Source: [communication_skill_notes]' +
			'(https://github.com/kw7oe/communication_skill_notes)\n')
		file.write('Data by: Kai Wern <br/>\n')
		file.write('Edited by: Marcus Mu\n')
		file.write('\n')
		file.write('### Table of Contents\n')
		file.write('\n')
		file.write('* [Chapter 1](#chapter-1)\n')
		file.write('* [Chapter 3](#chapter-3)\n')
		file.write('* [Chapter 5](#chapter-5)\n')
		file.write('* [Chapter 6](#chapter-6)\n')
		n = 0
		firstExample = True
		for line in lines:
			if '##' in line:
				file.write('\n\n')
				file.write('<a name="%s"/>' % ('-'.join(line.lower().split()[1:])))
				file.write('\n\n')
				file.write(line+'\n')
				file.write('\n')
				file.write('No | Concept | Definition / Explanation | Example\n')
				file.write('-- | ------- | ------------------------ | -------')
				n = 0
			elif '!' in line:
				n += 1
				firstExample = True
				file.write('\n')
				file.write('%s | <p align="center">**%s**</p> | ' % 
					('0'+str(n) if len(str(n))==1 else str(n), line[2:]))
			elif '@' in line:
				if len(line) <= 2:
					file.write('<p align="center">-</p> | ')
				else:
					file.write('%s | ' % line[2:])
			elif '%' in line:
				if len(line) <= 2:
					file.write('<p align="center">-</p>')
				else:
					if firstExample:
						file.write('<li>%s</li> ' % line[2:])
					else:
						firstExample = False
						file.write('<li>%s</li> ' % line[2:])
	with open('README.md', 'r') as file:
		print(file.read())

if __name__ == '__main__':
	main()