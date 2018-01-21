# Add .d to Make's recognized suffixes.
SUFFIXES += .d

# compiler flags
CXXFLAGS =	-O3 -g -Wall -fmessage-length=0 -std=c++11 -fopenmp

#include paths
INCLUDE_DIRS = -I./src -I/usr/lib/petsc/include/ -I/usr/lib/openmpi/include/

# libraries
LIBS = -L/usr/lib/petscdir/3.7.3/x86_64-linux-gnu-real/lib  -lpetsc_real -llapack -lblas

# project directories
SRC_DIR = ./src
OBJ_DIR = ./build
DEP_DIR = ./depend

# examples directories
EXAMPLE_DIR = ./examples
EXAMPLE_BUILD_DIR = ./examples/build

# project sources
SRC_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$(SRC_FILES))

# project dependencies
DEP_FILES:=$(patsubst $(SRC_DIR)/%.cpp,$(DEP_DIR)/%.d,$(SRC_FILES))


# examples sources
EXAMPLES = $(wildcard $(EXAMPLE_DIR)/*.c)

# example objects
OBJS = $(wildcard $(EXAMPLE_BUILD_DIR)/*.o)


# phony targets
.PHONY: clean

NO_DEPS := clean

heaving: $(EXAMPLE_BUILD_DIR)/heaving.o program
	@echo "link " $< 
	g++ $(CXXFLAGS) -o $(EXAMPLE_DIR)/$@ $< $(OBJ_FILES) $(LIBS)


# build airfoil example executable
airfoil: $(EXAMPLE_BUILD_DIR)/airfoil.o program
	@echo "link airfoil"
	g++ $(CXXFLAGS) -o $(EXAMPLE_DIR)/$@ $< $(OBJ_FILES) $(LIBS)


# build airfoil example object
#$(EXAMPLE_BUILD_DIR)/airfoil.o: $(EXAMPLE_DIR)/airfoil.cpp
$(EXAMPLE_BUILD_DIR)/%.o: $(EXAMPLE_DIR)/%.cpp
	@echo "compile airfoil"
	g++ $(CXXFLAGS) $(INCLUDE_DIRS) -c -o $@ $<

# the program build just objects to be linked to the examples
program: $(OBJ_FILES)
	@echo "Program files"
	@echo $(SRC_FILES)
	@echo $(OBJ_FILES)

# build program objects
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp $(DEP_DIR)/%.d
	g++ $(CXXFLAGS) $(INCLUDE_DIRS) -c -o $@ $<


# -MM dependencies excluding system deps
# -MT ovveride target dependency, otherwise it would be *.o
# -MF file to write the dependency to
$(DEP_DIR)/%.d: $(SRC_DIR)/%.cpp
	$(CXX) $(CXXFLAGS) -MM -MT $(OBJ_DIR)/$(patsubst %.cpp,%.o,$(notdir $<)) $< -MF $@
#	$(CXX) $(CXXFLAGS) -MM -MT $(patsubst $(SRC_DIR)/%,$(OBJ_DIR)/%,$(patsubst %.cpp,%.o,$<)) $< -MF $@
#	$(CXX) $(CXXFLAGS) -MM -MT '$(patsubst $(SRC_DIR)/%.cpp,$(OBJ_DIR)/%.o,$<)' $< -MF $@

# create depenency files
depend:	$(DEP_FILES)
	@echo "make dependencies"

#Don't create dependencies when we're cleaning, for instance
ifeq (0, $(words $(findstring $(MAKECMDGOALS), $(NO_DEPS))))
    #Chances are, these files don't exist.  GMake will create them and
    #clean up automatically afterwards
    -include $(DEP_FILES)
endif

# clean everything
clean:
	@echo "remove examples"
	rm -f $(EXAMPLE_DIR)/airfoil
	@echo "remove example objects"
	rm -f $(OBJS)
	@echo "remove project objects"
	rm -f $(OBJ_FILES)
	@echo "remove dependencies"
	rm -f $(DEP_FILES)
