from time import time as detak
from random import shuffle as kocok
import no05  # mergeSort baru
import no06  # quickSort baru
import no03  # mergeSort dan quickSort awal
k = [i for i in range(1, 6000)]
kocok(k)

merA = k[:]
merB = k[:]
quiA = k[:]
quiB = k[:]

# merge Sort baru
aw = detak(); no05.merge_sort(merB); ak = detak(); print('merge sort baru : %g detik' % (ak-aw))
# Quick Sort baru
aw = detak(); no06.quickSort(quiB); ak = detak(); print('quick sort baru : %g detik' % (ak-aw))

# Merge Sort dan Quick Sort awal
aw = detak(); no03.mergeSort(merA); ak = detak(); print('merge sort awal : %g detik' % (ak-aw))
aw = detak(); no03.quickSort(quiA); ak = detak(); print('quick sort awal : %g detik' % (ak-aw))
