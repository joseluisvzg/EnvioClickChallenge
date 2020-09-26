class DataSet():
	def __init__(self):
		self.data = []

	def order_data(self):
		"""
			Order dataset in a iterative way (instead of recursive way in order to avoid stack overflow on large datasets)
		"""
		queue = []
		queue.append(self.data)
		while len(queue) > 0:
			siblings = queue.pop()
			self.order_siblings(siblings)
			for sibling in siblings:
				childs = sibling.childs
				if len(childs) > 0:
					queue.append(childs)

	def order_siblings(self, data_list):
		"""
			Order a subset list by level + priority using merge sort algorithm
		"""
		self.mergeSort(data_list)

	def show(self):
		"""
			Dataset traversal in depth first search mode
		"""
		queue = [(data, 0) for data in self.data[::-1]]
		while len(queue) > 0:
			data, depth = queue.pop()
			print("{}{} (level:{} and priority:{})".format('\t'*depth, data.name, data.level, data.priority))
			for child in data.childs[::-1]:
				queue.append((child, depth+1))

	def addData(self, new_data):
		"""
			Append new Data element/s into dataset
		"""
		self.data.extend(new_data)
		self.order_data()

	def mergeSort(self, a):
		"""
			Merge sort algorithm
		"""
		current_size = 1
		while current_size < len(a): # -1
		    left = 0
		    while left < len(a)-1:  
		        mid = min((left + current_size - 1),(len(a)-1)) 
		        right = ((2 * current_size + left - 1,  
		                len(a) - 1)[2 * current_size  
		                    + left - 1 > len(a)-1])
		        self.merge(a, left, mid, right)  
		        left = left + current_size*2
		    current_size = 2 * current_size  

	def merge(self, a, l, m, r):  
		"""
			Merge sort customized (order by level + priority)
		"""
		n1 = m - l + 1
		n2 = r - m  
		L = [0] * n1  
		R = [0] * n2  

		for i in range(0, n1):  
		    L[i] = a[l + i]  

		for i in range(0, n2):  
		    R[i] = a[m + i + 1]  
		i, j, k = 0, 0, l  

		while i < n1 and j < n2:  
		    if L[i].numeric_level + L[i].numeric_priority > R[j].numeric_level + R[j].numeric_priority:  
		        a[k] = R[j]  
		        j += 1
		    else:  
		        a[k] = L[i]  
		        i += 1
		    k += 1

		while i < n1:  
		    a[k] = L[i]  
		    i += 1
		    k += 1

		while j < n2:  
		    a[k] = R[j]  
		    j += 1
		    k += 1