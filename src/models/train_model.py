# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, 'E:/GitHub/hse_workshop_regression/src')

import click
import logging
from pathlib import Path
from dotenv import find_dotenv, load_dotenv
from sklearn.model_selection import train_test_split
import pandas as pd
from catboost import CatBoostRegressor
from sklearn.metrics import mean_absolute_error
import config as cfg
import json 
from utils import *



@click.command()
@click.argument('train_data_filepath', type=click.Path(exists=True))
@click.argument('target_data_filepath', type=click.Path(exists=True))
@click.argument('output_model_filepath', type=click.Path())

def main(train_data_filepath, target_data_filepath, output_model_filepath):

    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    train = pd.read_pickle(train_data_filepath)
    target = pd.read_pickle(target_data_filepath)

    X_train, X_val, y_train, y_val = train_test_split(train, target, train_size=0.8, random_state=228)

    metrics = {}

    model = CatBoostRegressor(iterations = 5000,
                        learning_rate = 0.03,
                        eval_metric = 'MAE',
                        random_seed = 228,
                        use_best_model = True,
                        logging_level = 'Silent',
                        loss_function = 'MAE',
                        od_type = 'Iter',
                        od_wait = 1000,
                        one_hot_max_size = 20,
                        l2_leaf_reg = 50,
                        depth = 6,
                        rsm = 0.6,
                        random_strength = 1,
                        bagging_temperature = 10)

    model.fit(X_train, y_train, eval_set=(X_val, y_val), cat_features=cfg.CAT_COLS)
    save_model(model, output_model_filepath + '/catboost.sav')

    y_pred = model.predict(X_val)
    metrics['MAE'] = mean_absolute_error(y_val, y_pred)

    with open("metrics_catboost.json", "w") as outfile:
        json.dump(metrics, outfile)


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # not used in this stub but often useful for finding various files
    project_dir = Path(__file__).resolve().parents[2]

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main()
