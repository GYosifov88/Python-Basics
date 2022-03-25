pool_total_in_litres = int(input())
first_pipe_debit = int(input())
second_pipe_debit = int(input())
hours_worker_missing = float(input())


total_first_pipe = first_pipe_debit * hours_worker_missing
total_second_pipe = second_pipe_debit * hours_worker_missing
total_two_pipes = total_first_pipe + total_second_pipe
percent_first_pipe = (total_first_pipe / total_two_pipes) * 100
percent_second_pipe = (total_second_pipe / total_two_pipes) * 100
percent_full =  (total_two_pipes / pool_total_in_litres) * 100

difference = abs(pool_total_in_litres - total_two_pipes)
if pool_total_in_litres >= total_two_pipes:
    print (f"The pool is {percent_full:.2f}% full. Pipe 1: {percent_first_pipe:.2f}%. Pipe 2: {percent_second_pipe:.2f}%.")
else:
    print (f"For {hours_worker_missing} hours the pool overflows with {difference:.2f} liters.")