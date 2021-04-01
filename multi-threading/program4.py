'''
showing performance benifit with threads
correct Main thread waiting for child thread to complete
without timing
'''

import threading as t
import time
def doubles(numbers):
    for n in numbers:
        time.sleep(1)
        print('Double : ',2*n)

def squares(numbers):
    for n in numbers:
        time.sleep(1)
        print('Square : ',n*n)

numbers = [1,2,3,4,5,6]
t1 = t.Thread(target=doubles,args=(numbers,)) #notice the comma
t2 = t.Thread(target=squares,args=(numbers,)) #notice the comma
t1.start()
t2.start()

#main thread has to wait for the child thread to complete
t1.join()
t2.join()

endtime = time.time()
print('Total time taken : ',endtime-begintime)