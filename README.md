# ATML_project

## Instructions

Download the Waterbirds Dataset from [here](https://nlp.stanford.edu/data/dro/waterbird_complete95_forest2water2.tar.gz) and uncompress the file.

## Sample Commands

```
# Standard Training (ERM) and score computation.

python3 train_classifier.py --output_dir=output --pretrained_model --num_epochs=100 --weight_decay=1e-3 --batch_size=128 --init_lr=1e-3 --eval_freq=1 --data_dir=waterbird_complete95_forest2water2 --test_wb_dir=waterbird_complete95_forest2water2 --seed=1

# balance domains

python3 balance_groups.py
python3 change_metadata.py

# In wb_data.py, change metadata.csv to new_metadata.csv

# Train on balanced set.

python3 train_classifier.py --output_dir=output --pretrained_model --num_epochs=100 --weight_decay=1e-3 --batch_size=128 --init_lr=1e-3 --eval_freq=1 --data_dir=waterbird_complete95_forest2water2 --test_wb_dir=waterbird_complete95_forest2water2 --seed=1

# Train a model to learn only domain specific features with Adaptive Regularization.

python3 train_classifier_ar.py --output_dir=output --pretrained_model --num_epochs=100 --weight_decay=1e-3 --batch_size=128 --init_lr=1e-3 --eval_freq=1 --data_dir=waterbird_complete95_forest2water2 --test_wb_dir=waterbird_complete95_forest2water2 --seed=1

```
