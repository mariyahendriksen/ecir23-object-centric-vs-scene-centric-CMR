# ecir-23-reproducibility-hendriksen
This is the PyTorch code repository for the ECIR 2023 reproducibility track  TBA

All the commands are to be executed from one folder higher.
0. Download the necessary data.

```bash
wget TBA
unzip TBA
```
After unzipping the folder, put it in the CLIP root folder.

1. Evaluate model wrt to the dataset type.

```bash
sh CLIP/jobs/evaluation/evaluate_cub.job
sh CLIP/jobs/evaluation/evaluate_abo.job
sh CLIP/jobs/evaluation/evaluate_fashion200k.job

sh CLIP/jobs/evaluation/evaluate_mscoco.job
sh CLIP/jobs/evaluation/evaluate_flickr30k.job
```

2. Print the results.

```bash
sh CLIP/jobs/postprocessing/results_printer.job
```