import random
import time
# timer = ExecutionTime()
sample_list = list()
# my_list = [random.randint(1, 888898) for num in
#            range(1, 1000000) if num % 2 == 0]
# print('Finished in {} seconds.'.format(timer.duration()))



class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time
    
    
timer = ExecutionTime()

for i in range(1, 10000000):
    if i % 2 == 0:
        sample_list.append(random.randint(1, 888898))
print('Finished in {} seconds.'.format(timer.duration()))
        
        
        