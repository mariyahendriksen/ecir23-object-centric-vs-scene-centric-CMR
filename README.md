# ecir-23-reproducibility-hendriksen
This is the PyTorch code repository for the ECIR 2023 reproducibility track  TBA

All the commands are to be executed from one folder higher.
0. Download the necessary data.

```bash
wget TBA
unzip TBA
```

After unzipping the folder, put it in the CLIP root folder.
For evaluating X-VLM, we need to have access to the original images from the datasets. We cannot redistribute the images, therefore, we ask you to download the images yourself. The images should be added to the `X-VLM/image` directory. Overall the X-VLM folder should look as follows:

```angular2html
X-VLM/
    data/
        json_splits/
        models/
    images/
        cub/
            001.Black_footed_Albatross/*.jpg
            ...
            174.Palm_Warbler/*.jpg
        fashion200k/
            women/
                dresses/*.jpg
                jackets/*.jpg
                pants/*.jpg
                skirts/*.jpg
                tops/*.jpg
        abo/
            00/*.jpg
            ...
            fe/*.jpg
        mscoco/*.jpg
        flickr30k/*.jpg
```

1. Evaluate model wrt to the dataset type. The evaluation can be done in two ways

```bash
# CLIP evaluation
sh CLIP/jobs/evaluation/evaluate_cub.job
sh CLIP/jobs/evaluation/evaluate_abo.job
sh CLIP/jobs/evaluation/evaluate_fashion200k.job

sh CLIP/jobs/evaluation/evaluate_mscoco.job
sh CLIP/jobs/evaluation/evaluate_flickr30k.job

# X-VLM evaluation
sh X-VLM/jobs/evaluation/evaluate_flickr30k.job 
sh X-VLM/jobs/evaluation/evaluate_cub.job 
sh X-VLM/jobs/evaluation/evaluate_abo.job 
sh X-VLM/jobs/evaluation/evaluate_fashion200k.job 
sh X-VLM/jobs/evaluation/evaluate_mscoco.job 
```

2. Print the results.

```bash
sh CLIP/jobs/postprocessing/results_printer.job
```