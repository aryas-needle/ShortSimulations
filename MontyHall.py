import numpy as np
import matplotlib.pyplot as plt
import collections

def montyHall(experiment_number, no_of_doors, change = True):
	'''
	experiment_number(INTEGER) = no of times this test is to be carried out
	no_of_doors(INTEGER) = initial no of doors the participant can choose
	change(BOOLEAN) = if the participant can change his/her initial choice (True = Can)
	'''
	result = []
	not_changing_door_no = no_of_doors
	for _ in range(experiment_number):
		no_of_doors = not_changing_door_no
		#print('\nExperiment starting')
		doors = np.arange(1,not_changing_door_no+1)
		#print('Door: ',doors)
		jackpot_door = np.random.choice(doors)
		#print('Money door: ', jackpot_door)
		prev_door = 0
		while True:
			#Choose a door
			while True:
				chosen = np.random.choice(doors)
				#print('Chosen', chosen)
				if prev_door != chosen:
					#print('Accepted')
					break
			prev_door = chosen
			#Remove a Door
			if no_of_doors > 2:
				#print('Removing')
				while True:
					to_remove = np.random.choice(doors)
					#print('Choosing to delete', to_remove)
					if to_remove != chosen and to_remove != jackpot_door:
						break
				#print('Accepted', to_remove)
				doors = np.delete(doors, to_remove-1)
				#print('Updated door: ', doors)
			else:
				#print('Comparing the last doors')
				#print('Jackpot:',jackpot_door,'chosen: ', chosen)
				result.append(True) if chosen == jackpot_door else result.append(False)
				break
			no_of_doors -= 1
		#print(result[_])
	return result

experiment_number = int(input('Enter the no of test cases to carry: '))
no_of_doors = int(input('Enter the initial number of doors'))
change = input('Do you want to switch places after your chioce repeteadly?(Y/N)')
change = True if change.upper() == 'Y' else False

result = montyHall(experiment_number, no_of_doors, change = change)

counted = collections.Counter(result)


#Plot Section
plt.title('Monty Hall Problem Simulation')

plt.bar(['Won','Lost'], [counted[True],counted[False]], color = ['green','red'])

plt.xlabel('Status')
plt.ylabel('No of wins/lose in '+str(experiment_number)+' tests')


plt.tight_layout()
plt.show()