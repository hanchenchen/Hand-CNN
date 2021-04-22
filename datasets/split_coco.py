import random
random.seed(1)

def split_train_val_test(dataset, anno_list):
    anno_list = ['datasets/' + dataset + '/' + dataset + '_images/' + i for i in anno_list]
    random.shuffle(anno_list)
    print('the number of anno_list:', len(anno_list), '(', anno_list[0], '...)')
    train = open(dataset + '/train_annotations.txt', 'w')
    val = open(dataset + '/val_annotations.txt', 'w')
    test_dev = open(dataset + '/test_annotations.txt', 'w')
    train.write('\n'.join(anno_list[:int(len(anno_list) * 0.8)]))
    val.write('\n'.join(anno_list[int(len(anno_list) * 0.8):int(len(anno_list) * 0.9)]))
    test_dev.write('\n'.join(anno_list[int(len(anno_list) * 0.9):]))
    train.close()
    val.close()
    test_dev.close()


dataset = {'COCO-S': {'anno_train': './datasets/COCO-Hand/COCO-Hand-S/COCO-Hand-S_annotations.txt',
                      'imgs': './datasets/COCO-Hand/COCO-Hand-S/COCO-Hand-S_Images/',
                      'prefix': '../COCO-Hand/COCO-Hand-S/COCO-Hand-S_Images/'},
           'COCO-Big': {'anno_train': './datasets/COCO-Hand/COCO-Hand-Big/COCO-Hand-Big_annotations.txt',
                        'imgs': './datasets/COCO-Hand/COCO-Hand-Big/COCO-Hand-Big_Images/',
                        'prefix': '../COCO-Hand/COCO-Hand-S/COCO-Hand-S_Images/'},
           'TV': {'anno_train': './datasets/TV-Hand/train_IDs_tv.txt',
                  'anno_test': './datasets/TV-Hand/test_IDs.txt',
                  'anno_valid': './datasets/TV-Hand/valid_IDs.txt',
                  'imgs': './datasets/TV-Hand/TV-Hand_Images',
                  'prefix': '../TV-Hand/TV-Hand_Images/'}}


def get_list(name, c = '_train'):
    l = open(dataset[name]['anno'+c], 'r').read().split('\n')
    # if l[0].split(',').split('/')
    l = [dataset[name]['prefix'] + i.split('/')[-1] for i in l if i]
    print(l[:10])
    return l



train_list = get_list('COCO-S') + get_list('TV')
val_list = get_list('TV', '_valid')
test_dev_list = get_list('TV', '_test')


random.shuffle(train_list)

train = open('./datasets/train_annotations.txt', 'w')
val = open('./datasets/val_annotations.txt', 'w')
test_dev = open('./datasets/test_annotations.txt', 'w')
train.write('\n'.join(train_list))
val.write('\n'.join(val_list))
test_dev.write('\n'.join(test_dev_list))
train.close()
val.close()
test_dev.close()

print(len(train_list))
print(len(val_list))
print(len(test_dev_list))
# 14930
# 1362
# 4673
