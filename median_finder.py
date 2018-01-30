import heapq

def find_med(l):
	max_heap, min_heap = [], [] #Heaps for maintaining the median, the max heap will be implemented by having the values be negated making the min_heap implementation return the largest negative
	median = -1
	for n in l: # O(n) loop over the list
		if len(min_heap) == len(max_heap): # Given a balanced list, whichever side gets the element will contain the new median
			if n > median:
				heapq.heappush(min_heap, n)
				median = min_heap[0]
			else:
				heapq.heappush(max_heap, n*-1)
				median = max_heap[0]*-1
		elif len(min_heap) > len(max_heap): # If unbalanced then once an element is inserted the new median is both top elements / 2
			if n > median:
				heapq.heappush(max_heap, heapq.heappop(min_heap)*-1)
				heapq.heappush(min_heap, n)
			else:
				heapq.heappush(max_heap, n*-1)
			median = (max_heap[0]*-1 + min_heap[0]) / 2
		else: # Same as previous case, but with more elements below the median than above
			if n < median:
				heapq.heappush(min_heap, heapq.heappop(max_heap)*-1)
				heapq.heappush(max_heap, n*-1)
			else:
				heapq.heappush(min_heap, n)
			median = ((max_heap[0]*-1) + min_heap[0]) / 2


	return median


print(find_med([4,2]))
print("Try with your own space separated input: ")
l = input().split()
l = list(int(x) for x in l)
print(find_med(l))