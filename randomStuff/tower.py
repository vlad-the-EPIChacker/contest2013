def TowerOfHanoi(n, fro, to, aux):
    if n == 1:
        print "Move disk 1 from rod", fro, "to rod", to
        return
    TowerOfHanoi(n - 1, fro, aux, to)
    print "Move disk", n, "from rod", fro, "to rod", to
    TowerOfHanoi(n - 1, aux, to, fro)


TowerOfHanoi(4, 'A', 'C', 'B')
print ''
TowerOfHanoi(10, 'A', 'C', 'B')
print ''
TowerOfHanoi(1, 'A', 'C', 'B')