import random
random.seed(1)
dataset_path = 'COCO-Hand-S'
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


origin_anno = open(dataset_path + '/COCO-Hand-S_annotations.txt', 'r').read()
origin_anno = origin_anno.split('\n')
print(origin_anno[:10], len(origin_anno))

split_train_val_test(dataset_path, origin_anno)
