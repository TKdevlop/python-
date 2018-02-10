#multi processing  # it allows to launching sperate pyhton process that not nessary talk to eachother
#it allow
# its max out your cpu core your usage
# each multi pyhton program is a process

import multiprocessing

def spawn(num,num2):
    print("spanned")

if__name__=="__main__":
    for i range(50):
         p=multiprocessing.Process(target=spawn, args=(i,i+1))
           p.start()
          p.join()
 
