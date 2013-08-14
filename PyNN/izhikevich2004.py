
"""
Model implementation in PyNN by Vitor Chaud, Andrew Davison and Padraig Gleeson (August 2013).
This is a re-implementation of the models descirbed in the following references to reproduce Fig. 1 of Izhikevich (2004)

Original implementation references:

	Izhikevich E.M. (2004) Which Model to Use for Cortical Spiking Neurons?
	IEEE Transactions on Neural Networks, 15:1063-1070 (special issue on temporal coding)

	Izhikevich E.M. (2003) Simple Model of Spiking Neurons.
	IEEE Transactions on Neural Networks, 14:1569- 1572

	http://www.izhikevich.org/publications/whichmod.htm

"""

#############################################
##
##	VERSION 0.1 - Using PyNN 0.8
##
#############################################


from pyNN.random import RandomDistribution, NumpyRNG
from pyNN.utility import get_script_args, Timer, ProgressBar, init_logging, normalized_filename
import matplotlib.pyplot as plt

simulator_name = get_script_args(1)[0]  

exec("from pyNN.%s import *" % simulator_name)

print("\n")
print "Starting PyNN with simulator: %s"%simulator_name

timer = Timer()


# v represents the membrane potential of the neuron
# u represents a membrane recovery variable
# Synaptic currents or injected dc-currents are delivered via the variable I.



# Dimensionless parameters

# The parameter a describes the time scale of the recovery variable u

# The parameter b describes the sensitivity of the recovery variable
# u to the subthreshold fluctuations of the membrane potential v.

# The parameter c describes the after-spike reset value of the membrane
# potential v caused by the fast high-threshold K+ conductances.

# The parameter d describes after-spike reset of the recovery variable
# u caused by slow high-threshold Na+ and K+ conductances.



#############################################
##	Sub-plot A: Tonic spiking
#############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02	
b = 0.2 	
c = -65.0	
d = 6.0 	

I = 0

v_init = -70
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(10)
neuron.set(i_offset = 14)
run(90)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 1)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(A) Tonic spiking')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 10, 10, 100],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()



#############################################
##	Sub-plot B: Phasic spiking
#############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02	
b = 0.25 	
c = -65.0	
d = 6.0 	

I = 0

v_init = -64
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(20)
neuron.set(i_offset = 0.5)
run(180)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 2)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(B) Phasic spiking')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 20, 20, 200],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()


#############################################
##	Sub-plot C: Tonic bursting
#############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02	
b = 0.2 	
c = -50.0	
d = 2.0 	

I = 0

v_init = -70.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(22)
neuron.set(i_offset = 15.)
run(198)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 3)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(C) Tonic bursting')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 22, 22, 220],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()


#############################################
##	Sub-plot D: Phasic bursting
#############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = 0.25 
c = -55.0
d = 0.05

I = 0

v_init = -64.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(20)
neuron.set(i_offset = 0.6)
run(180)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 4)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(D) Phasic bursting')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 20, 20, 200],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()


#############################################
##	Sub-plot E: Mixed mode
#############################################

timeStep = 0.05

setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = 0.2
c = -55.0
d = 4.0

I = 0

v_init = -70.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(16)
neuron.set(i_offset = 10.0)
run(160 - 16)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')

ax1 = fig.add_subplot(5, 4, 5)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(E) Mixed mode')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 16, 16, 160],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()


#######################################################
##	Sub-plot F: Spike Frequency Adaptation (SFA)
#######################################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.01
b = 0.2
c = -65.0
d = 8.0

I = 0

v_init = -70.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(8.5)
neuron.set(i_offset = 30.0)
run(85 - 8.5)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 6)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(F) SFA')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 8.5, 8.5, 85],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()


############################################
##	Sub-plot G: Class 1 excitable
############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = -0.1
c = -55.0
d = 6.0

I = 0

v_init = -60.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(8.5)
neuron.set(i_offset = 30.0)
run(85 - 8.5)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 7)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(G) Class 1 excitable')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 8.5, 8.5, 85],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()



############################################
##	Sub-plot H: Class 2 excitable
############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.01
b = 0.2
c = -65.0
d = 8.0

I = 0

v_init = -70.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

run(8.5)
neuron.set(i_offset = 30.0)
run(85 - 8.5)

data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 8)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(H) Class 1 excitable')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 8.5, 8.5, 85],[-90, -90,-80, -80]);

plt.show(block=False)
fig.canvas.draw()



#########################################
##	Sub-plot I: Spike latency
#########################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = 0.2
c = -65.0
d = 6.0

I = 0

v_init = -70.0
u_init = b * v_init


neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(10)

neuron.set(i_offset = 7.04)

run(3)

neuron.set(i_offset = 0.0)

run(100 - 13)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 9)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(I) Spike latency')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 10, 10, 13, 13, 100],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



#################################################
##	Sub-plot J: Subthreshold oscillation
#################################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)


a = 0.05
b = 0.26
c = -60.0
d = 0.0

I = 0

v_init = -62.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = 2.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 10)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(J) Subthreshold oscillation')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



####################################
##	Sub-plot K: Resonator
####################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.1
b = 0.26
c = -60.0
d = -1.0

I = 0

v_init = -62.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = 2.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 11)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(K) Resonator')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()


####################################
##	Sub-plot L: Integrator
####################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = -0.1
c = -55.0
d = 6.0

I = 0

v_init = -60.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = 2.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 12)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(L) Integrator')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



######################################
##	Sub-plot M: Rebound spike
######################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.03
b = 0.25
c = -60.0
d = 4.0

I = 0

v_init = -64.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = -15.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 13)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(M) Rebound spike')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-85, -85, -90, -90, -85, -85]);

plt.show(block=False)
fig.canvas.draw()


######################################
##	Sub-plot N: Rebound burst
######################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.03
b = 0.25
c = -52.0
d = 0.0

I = 0

v_init = -64.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = -15.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 14)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(N) Rebound spike')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-85, -85, -90, -90, -85, -85]);

plt.show(block=False)
fig.canvas.draw()



###############################################
##	Sub-plot O: Threshold variability
###############################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.03
b = 0.25
c = -60.0
d = 4.0

I = 0

v_init = -64.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

run(20)

neuron.set(i_offset = -15.0)

run(5)

neuron.set(i_offset = 0.0)

run(200 - 25)


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 15)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(O) Threshold variability')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 20, 20, 25, 25, 200],[-85, -85, -90, -90, -85, -85]);

plt.show(block=False)
fig.canvas.draw()


######################################
##	Sub-plot P: Bistability
######################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)


a = 0.1
b = 0.26
c = -60.0
d = 0.0

I = 0.24

v_init = -61.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

simTime = 300.0/8
run(simTime)
simulatedTime = simTime

neuron.set(i_offset = 1.24)

simTime = 5
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 0.24)

simTime = 216 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 1.24)

simTime = 5
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 0.24)

simTime = 300 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 16)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(P) Bistability')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 300.0/8, 300.0/8, (300.0/8 + 5), (300.0/8 + 5), 216, 216, 221, 221, 300],[-90, -90, -80, -80, -90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



#####################################################
##	Sub-plot Q: Depolarizing after-potential
#####################################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 1.0
b = 0.2
c = -60.0
d = -21.0

I = 0.0

v_init = -70.0
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

simTime = 9
run(simTime)
simulatedTime = simTime

neuron.set(i_offset = 20.0)

simTime = 2
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 0.0)

simTime = 50 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 17)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(Q) DAP')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 9, 9, 11, 11, 50],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



#####################################################
##	Sub-plot R: Accomodation
#####################################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = 0.02
b = 1.0
c = -55.0
d = 4.0

I = 0.0

v_init = -65.0
u_init = -16.0

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}

initialValues = {'u': u_init, 'v': v_init}

cell_type = Izhikevich(**neuronParameters)
neuron = create(cell_type)
neuron.initialize(**initialValues)

neuron.record('v')

simTime = 9
run(simTime)
simulatedTime = simTime

neuron.set(i_offset = 20.0)

simTime = 2
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 0.0)

simTime = 50 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')

ax1 = fig.add_subplot(5, 4, 18)

#plt.xlabel("Time (ms)")
#plt.ylabel("Vm (mV)")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(Q) DAP')

vm = data.filter(name='v')[0]
#plt.plot(vm.times, vm, [0, 9, 9, 11, 11, 50],[-90, -90, -80, -80, -90, -90]);

plt.show(block=False)
fig.canvas.draw()



#####################################################
##	Sub-plot R: Inhibition-induced spiking
#####################################################

timeStep = 0.05
setup(timestep=timeStep, min_delay=0.5)

a = -0.02
b = -1.0
c = -60.0
d = 8.0

I = 80.0

v_init = -63.8
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')

simTime = 50
run(simTime)
simulatedTime = simTime

neuron.set(i_offset = 75.0)

simTime = 250 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 80.0)

simTime = 350 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')
ax1 = fig.add_subplot(5, 4, 19)
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(R) Inhibition-induced spiking')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 50, 50, 250, 250, 350],[-80, -80, -90, -90, -80, -80]);

plt.show(block=False)
fig.canvas.draw()



#####################################################
##	Sub-plot S: Inhibition-induced bursting
#####################################################

timeStep = 0.01
setup(timestep=timeStep, min_delay=0.5)

a = -0.026
b = -1.0
c = -45.0
d = -2.0

I = 80.0

v_init = -63.8
u_init = b * v_init

neuronParameters = 	{
			'a':	a,	
			'b':	b, 	
			'c':	c,	
			'd':	d,
			'i_offset': 	I
			}


initialValues = {'u': u_init, 'v': v_init}


cell_type = Izhikevich(**neuronParameters)


neuron = create(cell_type)

neuron.initialize(**initialValues)

neuron.record('v')
'''
simTime = 50
run(simTime)
simulatedTime = simTime

neuron.set(i_offset = 75.0)

simTime = 250 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime

neuron.set(i_offset = 80.0)

simTime = 350 - simulatedTime
run(simTime)
simulatedTime = simulatedTime + simTime


data = neuron.get_data().segments[0]

plt.ion()
fig = plt.figure(1, facecolor='white')

ax1 = fig.add_subplot(5, 4, 20)

#plt.xlabel("Time (ms)")
#plt.ylabel("Vm (mV)")
ax1.get_xaxis().set_visible(False)
ax1.get_yaxis().set_visible(False)
ax1.spines['left'].set_color('None')
ax1.spines['right'].set_color('None')
ax1.spines['bottom'].set_color('None')
ax1.spines['top'].set_color('None')

ax1.set_title('(S) Inhibition-induced bursting')

vm = data.filter(name='v')[0]
plt.plot(vm.times, vm, [0, 50, 50, 250, 250, 350],[-80, -80, -90, -90, -80, -80]);
'''
plt.show(block=False)
fig.canvas.draw()







raw_input("Simulation finished... Press enter to exit...")


