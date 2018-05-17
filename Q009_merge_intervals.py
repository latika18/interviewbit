Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Given intervals [1,3],[6,9] insert and merge [2,5] would result in [1,5],[6,9].

Example 2:

Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] would result in [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

def insert( intervals, new_interval):
    count = 0
    status = False
    final_interval = []
    k = len(intervals)
    for i in range(k):
        print "set " , i, intervals[i]
##        pdb.set_trace()
        ## if new interval lesser than given interval
        if min(new_interval) < min(intervals[i]) and max(new_interval) < min(intervals[i]):
            status = False
            break 
        
        ## if new interval falls under given interval
        if min(new_interval) >= min(intervals[i]) and max(new_interval)<= max(intervals[i]):
            status = True
            break 

        ## if new interval overlaps given interval    
        elif min(new_interval) <= min(intervals[i]) and max(new_interval)>= max(intervals[i]):
            intervals.remove(intervals[i])
            status = True
            intervals.insert(i, new_interval)
            
            
            
        ## part of new interval overlaps with left part of given interval
        elif min(new_interval) <= max(intervals[i]) and min(new_interval) >= min(intervals[i]):
            intervals[i][1]  = max(new_interval)
            new_interval = intervals[i] 
            status = True

        ## part of new interval overlaps with right part of given interval
        elif max(new_interval) > min(intervals[i])and max(new_interval) <= max(intervals[i]):
            print "a"
            new_interval[1]  = max(intervals[i])
            intervals.remove(intervals[i])
            status = True
            intervals.insert(i, new_interval)
        print intervals[i]

        
               
    if not status:
        intervals.append(new_interval)
    
    for elem in intervals:
        if elem not in final_interval:
            final_interval.append(elem)
    
    
    return final_interval 

print insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,9])

##print insert([[1,2],[3,6]],[8,10])
       

