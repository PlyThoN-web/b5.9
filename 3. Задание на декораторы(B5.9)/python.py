import time

def time_this(arg = int):
	def wrapper(func):
		def run():
			avg_time = 0
			amount_of_runs = 0
			for _ in range(arg):
				amount_of_runs += 1
				t0 = time.time()
				result = func()
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= arg
			print("Среднее время выполнения за {} запусков: {}".format(amount_of_runs, avg_time))
		return run
	return wrapper

@time_this(10)
def f():
	l = [x for x in range(10**4) if x % 2 == 0]
	return l
f()
