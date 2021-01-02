import sys, datetime,os,json

writepathtodo='todo.txt'
writepathdone='done.txt'
def help():
	print("Usage :-\n$ ./todo add \"todo item\"  # Add a new todo\n$ ./todo ls               # Show remaining todos\n$ ./todo del NUMBER       # Delete a todo\n$ ./todo done NUMBER      # Complete a todo\n$ ./todo help             # Show usage\n$ ./todo report           # Statistics\n",end="")

def report():
	try:
		fileDoneRead = open(writepathdone,"r")
		fileTodoRead = open(writepathtodo,"r")
		done = fileDoneRead.read().split('\n')
		todo = fileTodoRead.read().split('\n')
		pending = 0
		completed = 0
		for i in todo:
			if i:
				pending+=1
		for i in done:
			if i:
				completed+=1
		print('{} Pending : {} Completed : {}'.format(datetime.datetime.now().strftime('%Y-%m-%d'),pending,completed))
	finally:
		fileDoneRead.close()
		fileTodoRead.close()
def add(val):
	try:
		fileTodoRead = open(writepathtodo,"r")
		todo = fileTodoRead.read().split('\n')
		fileTodoWrite = open(writepathtodo,"w")
		todo.append(val)
		fileTodoWrite.write('\n'.join(todo))
		print('Added todo: "{}"'.format(val))
	finally:
		fileTodoRead.close()
		fileTodoWrite.close()
def ls():
	try:
		seeRev=[]
		fileTodoRead = open(writepathtodo,"r")
		todo = fileTodoRead.read().split('\n')
		for i in todo:
			if i:
				seeRev.append(i)
		i=len(seeRev)-1
		if(i==-1):
			print('There are no pending todos!')
			return
		while(i>=0):
			print('[{}] {}'.format(i+1,seeRev[i]))
			i-=1
	finally:
		fileTodoRead.close()
def done(val):
	try:
		fileDoneRead = open(writepathdone,"r")
		fileTodoRead = open(writepathtodo,"r")
		done = fileDoneRead.read().split('\n')
		todo = fileTodoRead.read().split('\n')
		fileTodoWrite = open(writepathtodo,"w")
		fileDoneWrite = open(writepathdone,"w")
		
		if int(val)<1:
			print('Error: todo #{} does not exist.'.format(val))
			return
		
		todo.pop(int(val))
		done.append('x {} {}'.format(datetime.datetime.now().strftime('%Y-%m-%d'),val))
		fileTodoWrite.write('\n'.join(todo))
		fileDoneWrite.write('\n'.join(done))
		print('Marked todo #{} as done.'.format(val))
	except IndexError:
		print('Error: todo #{} does not exist.'.format(val))
	finally:
		fileDoneRead.close()
		fileTodoRead.close()


def dele(val):
	try:
		seeRev=[]
		fileTodoRead = open(writepathtodo,"r")
		todo = fileTodoRead.read().split('\n')
		fileTodoWrite = open(writepathtodo,"w")
		if(todo==['']):
			print('There are no pending todos!')
			return
		if int(val)<1:
			print('Error: todo #{} does not exist. Nothing deleted.'.format(val))
			return
		todo.pop(int(val))
		print('Deleted todo #{}'.format(val))
		
	except IndexError:
		print('Error: todo #{} does not exist. Nothing deleted.'.format(val))
	finally:
		fileTodoWrite.write('\n'.join(todo))
		fileTodoWrite.close()
		fileTodoRead.close()



def main(argv):
	try:
		if(os.path.exists(writepathdone)):
			file1 = open(writepathdone,"r")
		else:
			file1 = open(writepathdone,"w")
		if(os.path.exists(writepathtodo)):
			file2 = open(writepathtodo,"r")
		else:
			file2 = open(writepathtodo,"w")
	finally:
		file1.close()
		file2.close()
	if(argv==[]):
		help()
	else:
		opt=argv[0]
		if(opt=="help"):
			help()
		elif(opt=="report"):
			report()
		elif(opt=="add"):
			if(len(argv)!=2):
				print('Error: Missing todo string. Nothing added!')
			else:
				add(argv[1])
		elif(opt=="ls"):
			ls()
		elif(opt=="done"):
			if(len(argv)!=2):
				print('Error: Missing NUMBER for marking todo as done.')
			else:
				done(argv[1])
		elif(opt=="del"):
			if(len(argv)!=2):
				print('Error: Missing NUMBER for deleting todo.')
			else:
				dele(argv[1])
if __name__ == "__main__":
   main(sys.argv[1:])