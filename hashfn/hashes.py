from hash_distribution import plot, distribute
from string import printable

plot(distribute(printable, num_containers=6, hash_function=hash))   #the distribution is uneven, from 6 containers 1 is missing