from multiprocessing import Process,JoinableQueue
import time,random,os
def consumer(q):
   while True:
       res=q.get()
       time.sleep(random.randint(1,3))
       print('%s 吃 %s' %(os.getpid(),res))

       q.task_done() #向q.join()发送一次信号,证明一个数据已经被取走了
def producer(name,q):
   for i in range(3):
       time.sleep(random.randint(1,3))
       res='%s%s' %(name,i)
       q.put(res)
       print('%s 生产了 %s' %(os.getpid(),res))

if __name__ == '__main__':
   q=JoinableQueue()
   #生产者们:即厨师们
   p1=Process(target=producer,args=('包子',q))
   p2=Process(target=producer,args=('骨头',q))
   p3=Process(target=producer,args=('泔水',q))
   #消费者们:即吃货们
   c1=Process(target=consumer,args=(q,))
   c2=Process(target=consumer,args=(q,))
   c1.daemon=True
   c2.daemon=True
   #开始
   p_l=[p1,p2,p3,c1,c2]
   for p in p_l:
       p.start()
   p1.join()
   p2.join()
   p3.join()
   print('主') 
   #主进程等--->p1,p2,p3等---->c1,c2
   #p1,p2,p3结束了,证明c1,c2肯定全都收完了p1,p2,p3发到队列的数据
   #因而c1,c2也没有存在的价值了,应该随着主进程的结束而结束,所以设置成守护进程