#default build suggestion of MPI + OPENMP with gcc on Livermore machines you might have to change the compiler name

SHELL = /bin/sh
.SUFFIXES: .cc .o

LULESH_EXEC = lulesh2.0

MPI_INC = /usr/src/linux-headers-3.8.0-29/include/linux
MPI_LIB = /lib

# Choosing the compiler
INTCOMP = 0
COMPILERNAME = g++
MPICOMPILER = mpig++
ifeq ($(INTCOMP),1)
	COMPILERNAME = icc
	MPICOMPILER = mpiCC
endif

SERCXX = $(COMPILERNAME) -DUSE_MPI=0
MPICXX = $(MPICOMPILER) -DUSE_MPI=1
CXX = $(SERCXX)

# Initial build flags for compile flags
MN = 0
FFP = 0
FB = 0
FI = 0
FSM = 0
FL = 0
F = 0
# Flags specific only to Intel compiler
XH = 0
UR = 0
IP = 0

# Initial additional compile flag
ADDFLAG =

ifeq ($(INTCOMP),0)
	ifeq ($(MN),1)
		ADDFLAG += -march=native
	endif

	ifeq ($(FFP),1)
		ADDFLAG += -fomit-frame-pointer
	endif

	ifeq ($(FB),1)
		ADDFLAG += -floop-block
	endif

	ifeq ($(FI),1)
		ADDFLAG += -floop-interchange
	endif

	ifeq ($(FSM),1)
		ADDFLAG += -floop-strip-mine
	endif

	ifeq ($(FL),1)
		ADDFLAG += -funroll-loops
	endif
	ifeq ($(F),1)
		ADDFLAG += -flto
	endif
endif

ifeq ($(INTCOMP),1)
	ifeq ($(MN),1)
		ADDFLAG += -march=native
	endif

	ifeq ($(XH),1)
		ADDFLAG += -xHost
	endif

	ifeq ($(UR),1)
		ADDFLAG += -unroll
	endif

	ifeq ($(IP),1)
		ADDFLAG += -ipo
	endif
endif



SOURCES2.0 = \
	lulesh.cc \
	lulesh-comm.cc \
	lulesh-viz.cc \
	lulesh-util.cc \
	lulesh-init.cc
OBJECTS2.0 = $(SOURCES2.0:.cc=.o)

#Default build suggestions with OpenMP for g++
#CXXFLAGS = -g -O3 -fopenmp -I. -Wall
#LDFLAGS = -g -O3 -fopenmp
#single thread
#CXXFLAGS = -g -O3 -I. -w
#LDFLAGS = -g -O3

#CXXFLAGS = -g -O3 -fopenmp -I. -w
#LDFLAGS = -g -fopenmp -O3

#Below are reasonable default flags for a serial build
CXXFLAGS = -g -O3 -I. -w $(ADDFLAG)
LDFLAGS = -g -O3 

#common places you might find silo on the Livermore machines.
#SILO_INCDIR = /opt/local/include
#SILO_LIBDIR = /opt/local/lib
#SILO_INCDIR = ./silo/4.9/1.8.10.1/include
#SILO_LIBDIR = ./silo/4.9/1.8.10.1/lib

#If you do not have silo and visit you can get them at:
#silo:  https://wci.llnl.gov/codes/silo/downloads.html
#visit: https://wci.llnl.gov/codes/visit/download.html

#below is and example of how to make with silo, hdf5 to get vizulization by default all this is turned off.  All paths are Livermore specific.
#CXXFLAGS = -g -DVIZ_MESH -I${SILO_INCDIR} -Wall -Wno-pragmas
#LDFLAGS = -g -L${SILO_LIBDIR} -Wl,-rpath -Wl,${SILO_LIBDIR} -lsiloh5 -lhdf5

.cc.o: lulesh.h
	@echo "Building ($(ADDFLAG)) $<"
	$(CXX) -c $(CXXFLAGS) -o $@  $<

all: $(LULESH_EXEC)

#lulesh2.0: $(OBJECTS2.0)
$(LULESH_EXEC): $(OBJECTS2.0)
	@echo "Linking"
	$(CXX) $(OBJECTS2.0) $(LDFLAGS) -lm -o $@

clean:
	/bin/rm -f *.o *~ $(OBJECTS) $(LULESH_EXEC)
	/bin/rm -rf *.dSYM

tar: clean
	cd .. ; tar cvf lulesh-2.0.tar LULESH-2.0 ; mv lulesh-2.0.tar LULESH-2.0

