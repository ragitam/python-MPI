from mpi4py import MPI
import time

start = time.time()

comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

n = 1000
pi = 0
dx = 1.0/n
a = 251
lim1 = n/4
lim2 = n/2
lim3 = (3*n)/4

#for i in xrange(n):		
#	x = float(i)/n
#	pi += 4/(1 + x*x)*dx
hasil = comm.reduce(pi, op=MPI.SUM, root=0)

if rank == 0:
	for i in xrange(lim1):
		x = float(i)/n
		pi += 4/(1+ x*x)*dx
if rank == 1:
	for lim1 in xrange(lim2):
		x = float(lim1)/n
		pi += 4/(1+ x*x)*dx
		#print "rank ", rank, "loop ", lim1, " pi : ", pi
if rank == 2:
	i = lim2+1
	for i in xrange(lim3):
		x = float(i)/n
		pi += 4/(1+ x*x)*dx
if rank == 3:
	i = lim3+1
	for i in xrange(n):
		x = float(i)/n
		pi += 4/(1+ x*x)*dx
	print "rank ", rank, " hasil ", pi	
print "hasil dari rank ",rank," adalah ", pi


end = time.time()
print "selesai dalam waktu : ", end - start
comm.Barrier() 
