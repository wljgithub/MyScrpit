import sys,os

def chose_diff():
	s = '''
	enter the difficulty of quizz!
	Easy  		(e)
	Medium 		(m)
	Hard		(h)
		'''
	diff = input(s)

	difficulty=''

	if diff == 'e':
		difficulty ='Easy'
	elif diff =='m':
		difficulty = 'Medium'
	elif diff == 'h':
		difficulty = 'Hard'
	else:
		chose_diff()

	# print(difficulty)
	return difficulty

def returnfiletype():
	t = input(
		'''
	create go file (g)
	create python file (p)
		''')
	filetype = ""

	if t == 'g':
		filetype = "go"
	elif t=='p':
		filetype ='py'

	return filetype
def main(arg):
	#当递归的太多层的时候，返回值就消失了？
	path = arg[1]
	
	diff = chose_diff()

	filename = ''.join(arg[2:]).strip()

	filetype = returnfiletype()

	full_name = r'{}\{}-{}.{}'.format(path,diff,filename,filetype)

	#到时候可以在这里添加一个判断，如果文件以存在则。。。
	codes = '''
package main

import (
	"fmt"
)

func main() {

}
'''
	with open(full_name,'w',encoding='utf-8') as f:
		f.write(codes)

	os.system(full_name)
if __name__ == '__main__':
	main(sys.argv)		
