
All the commands are to be executed from one folder higher.
0. Download the necessary data.

```bash
wget TBA
unzip TBA
```
After unzipping the folder, put it in the CLIP root folder.

Install the dependancies:

```bash
pip install -r requirements.txt
```


1. Evaluate model wrt to the dataset type.

```bash
sh X-VLM/jobs/evaluation/evaluate_cub.job
sh CLIP/jobs/evaluation/evaluate_abo.job
sh CLIP/jobs/evaluation/evaluate_fashion200k.job

sh CLIP/jobs/evaluation/evaluate_mscoco.job
sh CLIP/jobs/evaluation/evaluate_flickr30k.job
```

2. Print the results.

```bash
sh CLIP/jobs/postprocessing/results_printer.job
```