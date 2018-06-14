Given two integers n and k, return all possible combinations of k numbers out of 1 2 3 ... n.

Make sure the combinations are sorted.

To elaborate,

Within every entry, elements should be sorted. [1, 4] is a valid entry while [4, 1] is not.
Entries should be sorted within themselves.
Example :
If n = 4 and k = 2, a solution is:

[
  [1,2],
  [1,3],
  [1,4],
  [2,3],
  [2,4],
  [3,4],
]

class Solution:
    # @param n : integer
    # @param k : integer
    # @return a list of list of integers
	b=[]
	def combine(self, n, k):
		if(k>n):
			return []
		if(k==0):
		    k=n
		return self.generate_comb(n,k,1)
		
	def generate_comb(self,n,k,start):
		if(k==1):
			return [[x] for x in xrange(start,n+1)]
		else:
			a=[]
			temp=[]
			for i in xrange(start,n+1):
				a=self.generate_comb(n,k-1,i+1)
				
				for j in xrange(0,len(a)):
					
					a[j].append(i)
					a[j].sort()
				for x in a:
					temp.append(x)
			
			return temp

