import pandas as pd
import argparse
import os 
import json


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--work-dir", type=str, required=False, default="D:/emergencyhack/")
    args = parser.parse_args()
    return args


def load_dtypes_json(work_dir):
    with open(os.path.join(work_dir, 'dtypes.json'), 'r') as json_file:
        dtypes = json.load(json_file)
    return dtypes


def date_parser():
    return lambda x: pd.to_datetime(x, format='%Y-%m-%d')


def main():
    args = parse_args()
    work_dir = args.work_dir
    dtypes = load_dtypes_json(work_dir)
    work_dir = os.path.join(work_dir, '2_track', 'track_2_package')
    print(work_dir)
    custom_date_parser = date_parser()
    train_hist = pd.read_csv(
        os.path.join(work_dir, 'train.csv'),
        dtype=dtypes['train'],
        parse_dates=['date'], 
        date_parser=custom_date_parser
    )
    years = [
        1989,
        1993,
        1997,
        2001,
        2003,
        2004,
        2005,
        2012,
        2013
    ]
    train_hist[(~train_hist['year'].isin(years))&(~train_hist['month'].isin([7, 8, 9, 10]))].to_csv(os.path.join(work_dir, 'cutoff_train.csv'), index=False)


if __name__ == "__main__":
    main()