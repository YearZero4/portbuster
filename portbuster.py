import subprocess, sys, subprocess, os
script_name=os.path.basename(__file__)

parameter = sys.argv
allPorts=[]
filter0=[]
portpid=[]

taskname=[]

def task(pidU):
 cmd1='tasklist'
 tasklist = subprocess.run(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.splitlines()
 for i in tasklist:
  if i:
   pid=i.split()[1]
   if pid == pidU:
    name=i.split()[0]
    if name not in taskname:
     taskname.append(name)
     print(f'Nombre del Proceso => {name}, PID => {pidU}')

def kill(port, pid):
 kill=f'taskkill /PID {pid} /F'
 execute = subprocess.run(kill, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
 if execute.stdout:
  print(f'PUERTO => {port} [CERRADO], PID => {pid} [FINALIZO]')

def found():
 cmd1='netstat -ano'
 proceso = subprocess.run(cmd1, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.splitlines()
 for i in enumerate(proceso):
  if i:
   if int(i[0]) > 3:
    if i[1].find('LISTENING') != -1:
     filterx=f'{i[1].split()[1].split(':')[-1]} {i[1].split()[-1]}'
     filter0.append(filterx)
found()


def all():
 for i in filter0:
  port = i.split()[0]
  if port not in allPorts:
   allPorts.append(port)
   portpid.append(i)
 return allPorts

if len(parameter) == 1:
 print(f"""\n AYUDA: Usa los siguientes comandos para ejecutar el script:\n
 python {script_name} -l : Lista todos los puertos en uso.
 python {script_name} -d : Mata todos los procesos que estan usando puertos.
 python {script_name} -p <puerto> : Mata el proceso que esta usando el puerto especificado.
 python {script_name} -f <puerto> : Ver nombre del proceso de un puerto y PID.
 """)
elif parameter[1] == '-l':
 print(all())
elif parameter[1] == '-d':
 all()
 for i in portpid:
  port=i.split()[0]
  process=i.split()[-1]
  try:
   kill(port, process)
  except:
   pass
elif len(parameter) == 3 and parameter[1] == '-p':
 for i in filter0:
  if i.split()[0] == parameter[2]:
   kill(i.split()[0], i.split()[1])
elif len(parameter) == 3 and parameter[1] == '-f':
  for i in filter0:
   if i.split()[0] == parameter[2]:
    task(i.split()[1])
else:
 print('OPCION INVALIDA...')

