# Definition for an interval.
#class Interval:
    #def __init__(self, s=0, e=0):
        #self.start = s
        #self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        count = 0
        status = False
        final_interval = []
        #new_interval = (min(new_interval.new_interval),max(new_interval.new_interval))
        interval = [[v.start, v.end] for v in intervals]
        new_int = [new_interval.start, new_interval.end]
        #new_low, new_high = min(*new_interval), max(*new_interval)
    # ...
    
        
        k = len(interval)
        for i in range(k):
        
      
        ## if new interval lesser than given interval
            if min(new_int) < min(interval[i]) and max(new_int) < min(interval[i]):
                status = False
                break 
        
        ## if new interval falls under given interval
            elif min(new_int) >= min(interval[i]) and max(new_int)<= max(interval[i]):
                status = True
                break 

        ## if new interval overlaps given interval    
            elif min(new_int) <= min(interval[i]) and max(new_int)>= max(interval[i]):
                interval.remove(interval[i])
                status = True
                interval.insert(i, new_int)
            
            
            
        ## part of new interval overlaps with left part of given interval
            elif min(new_int) <= max(interval[i]) and min(new_int) >= min(interval[i]):
                interval[i][1]  = max(new_int)
                new_int = interval[i] 
                status = True

        ## part of new interval overlaps with right part of given interval
            elif max(new_int) > min(interval[i])and max(new_int) <= max(interval[i]):
            
                new_int[1]  = max(interval[i])
                interval.remove(interval[i])
                status = True
                interval.insert(i, new_int)
        
            count += 1
               
        if not status:
            interval.insert(count,new_int)
    
        for elem in interval:
            if elem not in final_interval:
                final_interval.append(elem)
    
    
        return [Interval(l, h) for l, h in final_interval]
         
