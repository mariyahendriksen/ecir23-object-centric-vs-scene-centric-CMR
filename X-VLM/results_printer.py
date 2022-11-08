import pickle
import os

root = 'X-VLM/data/models'
datasets = ['coco', 'f30k', 'cub', 'fashion200k', 'abo']

dataset_key_to_names = {
    'abo': 'Amazon Berkley Objects',
    'coco': 'MS COCO',
    'cub': 'CUB-200',
    'f30k': 'Flickr30k',
    'fashion200k': 'Fashion200k'
}

def ranks_to_recalls(ranks):
    import numpy as np
    r1 = 100.0 * len(np.where(ranks < 1)[0]) / len(ranks)
    r5 = 100.0 * len(np.where(ranks < 5)[0]) / len(ranks)
    r10 = 100.0 * len(np.where(ranks < 10)[0]) / len(ranks)

    return r1, r5, r10

i2t = 'eval_ranks_i2t.pkl'
t2i = 'eval_ranks_t2i.pkl'

for dataset in datasets:
    # generate paths
    path_i2t = os.path.join(root, dataset, i2t)
    path_t2i = os.path.join(root, dataset, t2i)

    # print(f'{path_i2t} exists?', os.path.exists(path_i2t))
    # print(f'{path_t2i} exists?', os.path.exists(path_t2i))

    # load info from paths
    with open(path_i2t, 'rb') as f:
        task = 'Image-to-text retrieval'
        # print(path_i2t)
        ranks = pickle.load(f)
        tr1, tr5, tr10 = ranks_to_recalls(ranks)
    
    with open(path_t2i, 'rb') as f:
        task = 'Text-to-image retrieval'
        # print(path_i2t)
        ranks = pickle.load(f)
        ir1, ir5, ir10 = ranks_to_recalls(ranks)
    
    tr_mean = (tr1 + tr5 + tr10) / 3
    ir_mean = (ir1 + ir5 + ir10) / 3
    r_mean = (tr_mean + ir_mean) / 2

    print(f"""
    Dataset: {dataset_key_to_names[dataset]}
    Task: Text-to-image retrieval
    Recall@1: {ir1}
    Recall@5: {ir5}
    Recall@10: {ir10}
    Task: Image-to-text retrieval
    Recall@1: {tr1}
    Recall@5: {tr5}
    Recall@10: {tr10}
    """)