def common_elements():

    krat3 = set()
    krat5 = set()
    for i in range(100):
        if i % 3 == 0:
            krat3.add(i)
        if i % 5 == 0:
            krat5.add(i)
    intersection = krat3.intersection(krat5)
    return intersection

assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")