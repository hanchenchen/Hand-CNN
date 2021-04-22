l = open('./datasets/annotations/oxford_annos.txt', 'r').read().split('\n')
l = ['..' + i[23:] for i in l if i]

test_dev = open('./datasets/oxford_test_annotations.txt', 'w')

test_dev.write('\n'.join(l))

test_dev.close()

print(len(l), l[0])

