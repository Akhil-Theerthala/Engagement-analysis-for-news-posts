import pandas as pd
import os

DIR = '.'
save_dir = '../'
files = os.listdir(DIR)

columns = ['id', 'page_id', 'name',
           'message', 'description', 'caption',
           'post_type', 'status_type', 'likes_count',
           'comments_count', 'shares_count', 'love_count',
           'wow_count', 'haha_count', 'sad_count',
           'thankful_count', 'angry_count', 'link',
           'picture', 'posted_at']

df = pd.DataFrame(columns=columns)

for f in files:
    if f.split('.')[-1] != 'py':
        temp = pd.read_csv(os.path.join(DIR, f), encoding='utf-16')
        temp['source'] = f.split('.')[0]
        df = pd.concat([df, temp], axis=0)

df.to_csv(save_dir + 'news_data.csv', encoding='utf-8')
