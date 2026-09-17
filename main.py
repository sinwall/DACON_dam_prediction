# # 팔당댐 홍수 안전운영에 따른 한강 수위예측 AI 경진대회
# # 팀명 : 쿠마리코지카후원회동남지부장
#
#
# # 개발 환경 정보
#
# 프로세서	Intel(R) Core(TM) i7-10700K CPU @ 3.80GHz   3.80 GHz
# 설치된 RAM	64.0GB(63.6GB 사용 가능)
# 시스템 종류	64비트 운영 체제, x64 기반 프로세서
# 에디션	Windows 10 Home
# 버전	21H2
# OS 빌드	19044.1889
#
# # 파이썬 및 라이브러리 버전
#
# Python == 3.8.6
# NumPy == 1.20.3
# Pandas == 1.4.3
# requests == 2.25.1
# lightgbm == 3.3.2
#
#
# # 외부 데이터 정보 및 출처
#
# 1. 댐 관측소 제원 (출처: OpenAPI, http://api.hrfco.go.kr/{api_key}/dam/info.xml, api_key는 코드 본문에 포함된 것으로 사용 가능)
# 경로: /data/OpenAPI/dmobs.json
#
# 2. 강수량 관측소 제원 (출처: OpenAPI, http://api.hrfco.go.kr/{api_key}/rainfall/info.xml)
# 경로: /data/OpenAPI/rfobs.json
#
# 3. 수위 관측소 제원 (출처: OpenAPI, http://api.hrfco.go.kr/{api_key}/waterlevel/info.xml)
# 경로: /data/OpenAPI/wlobs.json
#
# 4. 코드 가독성을 높이기 위해 별도로 분리한 텍스트 (출처: 직접 작성)
# 경로: /data/_positive_importances.txt, /data/_rfobscds.txt, /data/_unimportant_feature_names.txt, /data/_useless_feature_names.txt, /data/_wlobscds.txt
#

from time import sleep, time
import requests
import os
import pandas as pd
import json
import numpy as np
import lightgbm as lgbm

##### OpenAPI를 이용한 데이터 수집 시작 #####

# 데이터 경로 지정 : 실험용에서와 제출용에서 데이터 경로가 다름
# _input_path = '../data'
_input_path = '/data'

# 한강홍수통제소 OpenAPI 인증키
api_key = '97D5425D-C330-49D5-A048-11D7B089DD91'

# 수위 관측소 데이터 읽어들이기
file = open(f'{_input_path}/OpenAPI/wlobs.json', 'r', encoding='utf8')
wlobs = json.load(file)
file.close()
for item in wlobs['content']:
    # 서울 경기 관측소 정보만 활용
    if not (item['addr'].startswith('서울특별시') or item['addr'].startswith('경기도')):
        continue
    wlobscd = item['wlobscd']
    site = f'{_input_path}/OpenAPI/wl_fw/{wlobscd}'
    if not os.path.isdir(site):
        os.mkdir(site)
    for yr in range(2012, 2022 + 1):
        for mo in range(1, 12 + 1):
            tic = time()

            if yr == 2022 and mo == 8:
                break
            if mo in [1, 3, 5, 7, 8, 10, 12]:
                dd = 31
            elif mo in [4, 6, 9, 11]:
                dd = 30
            elif mo == 2 and yr % 4 == 0:
                dd = 29
            else:
                dd = 28
            # 일 단위로 데이터를 내려받음
            url = f'http://api.hrfco.go.kr/{api_key}/waterlevel/list/10M/{wlobscd}/{yr}{mo:0>2}010000/{yr}{mo:0>2}{dd}2350.json'
            response = requests.get(url)
            response_json = response.json()
            if not (200 <= response.status_code < 300):
                print(response.status_code, wlobscd, yr, mo)
            df = pd.DataFrame(response_json['content'])[['ymdhm', 'wl', 'fw']]
            df = df.rename(columns={'wl': f'wl_{wlobscd}', 'fw': f'fw_{wlobscd}'})
            df['ymdhm'] = pd.to_datetime(df['ymdhm'])
            df.to_csv(f'{site}/wl_fw_{yr}{mo:0>2}.csv', index=False)

            toc = time()

            sleep(max(0.1 - (toc - tic), 0))

# 강수량 관측소 데이터 읽어들이기
file = open(f'{_input_path}/OpenAPI/rfobs.json', 'r', encoding='utf8')
rfobs = json.load(file)
file.close()
for item in rfobs['content']:
    if not (item['addr'].startswith('서울특별시') or item['addr'].startswith('경기도')):
        continue
    rfobscd = item['rfobscd']
    site = f'{_input_path}/OpenAPI/rf/{rfobscd}'
    if not os.path.isdir(site):
        os.mkdir(site)

    for yr in range(2012, 2022 + 1):
        for mo in range(1, 12 + 1):
            tic = time()

            if yr == 2022 and mo == 8:
                break
            if mo in [1, 3, 5, 7, 8, 10, 12]:
                dd = 31
            elif mo in [4, 6, 9, 11]:
                dd = 30
            elif mo == 2 and yr % 4 == 0:
                dd = 29
            else:
                dd = 28
            url = f'http://api.hrfco.go.kr/{api_key}/rainfall/list/10M/{rfobscd}/{yr}{mo:0>2}010000/{yr}{mo:0>2}{dd}2350.json'
            response = requests.get(url)
            response_json = response.json()
            if not (200 <= response.status_code < 300):
                print(response.status_code, rfobscd, yr, mo)
            df = pd.DataFrame(response_json['content'])[['ymdhm', 'rf']]
            df = df.rename(columns={'rf': f'rf_{rfobscd}'})
            df['ymdhm'] = pd.to_datetime(df['ymdhm'])
            df.to_csv(f'{site}/rf_{yr}{mo:0>2}.csv', index=False)

            toc = time()

            sleep(max(0.1 - (toc - tic), 0))

# 댐 데이터 읽어들이기
file = open(f'{_input_path}/OpenAPI/dmobs.json', 'r', encoding='utf8')
dmobs = json.load(file)
file.close()
for item in dmobs['content']:
    if item is None or item['dmobscd'] != '1017310':
        continue
    dmobscd = item['dmobscd']
    site = f'{_input_path}/OpenAPI/dm/{dmobscd}'
    if not os.path.isdir(site):
        os.mkdir(site)

    for yr in range(2012, 2022 + 1):
        for mo in range(1, 12 + 1):
            tic = time()

            if yr == 2022 and mo == 8:
                break
            if mo in [1, 3, 5, 7, 8, 10, 12]:
                dd = 31
            elif mo in [4, 6, 9, 11]:
                dd = 30
            elif mo == 2 and yr % 4 == 0:
                dd = 29
            else:
                dd = 28
            url = f'http://api.hrfco.go.kr/{api_key}/dam/list/10M/{dmobscd}/{yr}{mo:0>2}010000/{yr}{mo:0>2}{dd}2350.json'
            response = requests.get(url)
            response_json = response.json()
            if not (200 <= response.status_code < 300):
                print(response.status_code, dmobscd, yr, mo)
            df = pd.DataFrame(response_json['content'])[['ymdhm', 'swl', 'inf', 'sfw', 'ecpc', 'tototf']]
            #             df = df.rename(columns={'rf': f'rf_{rfobscd}'})
            df['ymdhm'] = pd.to_datetime(df['ymdhm'])
            df.to_csv(f'{site}/dm_{yr}{mo:0>2}.csv', index=False)

            toc = time()

            sleep(max(0.1 - (toc - tic), 0))

# 바다누리 해양정보 서비스 OpenAPI 인증키
api_key = 'Kr6Ya7xOQiHbhBifm21nTg=='

# 조위 데이터를 수집할 관측소
tobs = [
    {'obs_post_id': 'DT_0032',
     'obs_post_name': '강화대교'},
    {'obs_post_id': 'DT_0044',
     'obs_post_name': '영종대교'}
]
shutdown = False
obs_last_req_cnt = 20000
for item in tobs:
    obs_post_id = item['obs_post_id']
    site = f'{_input_path}/OpenAPI/tide_level/{obs_post_id}'
    if not os.path.isdir(site):
        os.mkdir(site)

    for yr in range(2012, 2022 + 1):
        for mo in range(1, 12 + 1):

            if yr == 2022 and mo == 8:
                break
            if mo in [1, 3, 5, 7, 8, 10, 12]:
                dd = 31
            elif mo in [4, 6, 9, 11]:
                dd = 30
            elif mo == 2 and yr % 4 == 0:
                dd = 29
            else:
                dd = 28
            for day in range(1, dd + 1):
                if shutdown:
                    continue
                url = f'http://www.khoa.go.kr/api/oceangrid/tideObs/search.do?ServiceKey={api_key}&ObsCode={obs_post_id}&Date={yr}{mo:0>2}{day:0>2}&ResultType=json'
                response = requests.get(url)
                response_json = response.json()
                if not (200 <= response.status_code < 300):
                    # print(response.status_code, obs_post_id, yr, mo, day)
                    continue
                if 'data' not in response_json['result']:
                    # print(response_json, obs_post_id, yr, mo, day)
                    obs_last_req_cnt -= 1
                    # print(obs_last_req_cnt)
                    continue
                if 'meta' in response_json['result']:
                    obs_last_req_cnt = int(response_json['result']['meta']['obs_last_req_cnt'].split('/')[0])
                    # print(obs_last_req_cnt)
                if obs_last_req_cnt < 10:
                    shutdown = True
                df = pd.DataFrame(response_json['result']['data'])[['record_time', 'tide_level']]
                df = df.rename(columns={'record_time': 'ymdhm', 'tide_level': f'tide_level_{obs_post_id}'})
                df['ymdhm'] = pd.to_datetime(df['ymdhm'])
                df.to_csv(f'{site}/tide_level_{yr}{mo:0>2}{day:0>2}.csv', index=False)

# 이상 일 단위로 데이터를 저장하였으나, 입출력 편의를 위해 다시 합칠 것

# 데이터 편집 일자, 큰 의미는 없습니다
date = 20220822

# 댐 데이터 합치기
for dmobscd in os.listdir(f'{_input_path}/OpenAPI/dm/'):
    df_dm = []
    for file_name in sorted(os.listdir(f'{_input_path}/OpenAPI/dm/{dmobscd}')):
        file_path = f'{_input_path}/OpenAPI/dm/{dmobscd}/{file_name}'
        df_dm.append(pd.read_csv(file_path, parse_dates=['ymdhm']).iloc[::-1])
    df_dm = pd.concat(df_dm, axis=0, ignore_index=True)
    df_dm.to_csv(f'{_input_path}/OpenAPI_merged/dm_{date}.csv', index=False)

# 수위 데이터 합치기
for wlobscd in os.listdir(f'{_input_path}/OpenAPI/wl_fw/'):
    df_wl = []
    for file_name in sorted(os.listdir(f'{_input_path}/OpenAPI/wl_fw/{wlobscd}')):
        file_path = f'{_input_path}/OpenAPI/wl_fw/{wlobscd}/{file_name}'
        df_wl.append(pd.read_csv(file_path, parse_dates=['ymdhm']).iloc[::-1])
    df_wl = pd.concat(df_wl, axis=0, ignore_index=True)
    df_wl.to_csv(f'{_input_path}/OpenAPI_merged/wl_{wlobscd}_{date}.csv', index=False)

# 강수량 데이터 합치기
for rfobscd in os.listdir(f'{_input_path}/OpenAPI/rf/'):
    df_rf = []
    for file_name in sorted(os.listdir(f'{_input_path}/OpenAPI/rf/{rfobscd}')):
        file_path = f'{_input_path}/OpenAPI/rf/{rfobscd}/{file_name}'
        df_rf.append(pd.read_csv(file_path, parse_dates=['ymdhm']).iloc[::-1])
    df_rf = pd.concat(df_rf, axis=0, ignore_index=True)
    df_rf.to_csv(f'{_input_path}/OpenAPI_merged/rf_{rfobscd}_{date}.csv', index=False)

# 조위 데이터 합치기
for obs_post_id in os.listdir(f'{_input_path}/OpenAPI/tide_level'):
    df_tide = []
    for file_name in sorted(os.listdir(f'{_input_path}/OpenAPI/tide_level/{obs_post_id}')):
        file_path = f'{_input_path}/OpenAPI/tide_level/{obs_post_id}/{file_name}'
        df_tide.append(pd.read_csv(file_path, parse_dates=['ymdhm']))
    df_tide = pd.concat(df_tide, axis=0, ignore_index=True)
    df_tide.to_csv(f'{_input_path}/OpenAPI_merged/tide_level_{obs_post_id}_{date}.csv', index=False)

##### OpenAPI 데이터 수집 및 정리 작업 끝 #####

##### 모형 구성 및 예측 시작 #####

# OpenAPI로 추출한 데이터들 중 사용할 수위 및 강수량 관측소 코드를 불러오기
with open(f'{_input_path}/_wlobscds.txt', 'r') as file:
    _wlobscds = eval(file.read())
with open(f'{_input_path}/_rfobscds.txt', 'r') as file:
    _rfobscds = eval(file.read())
# 이후에 추출할 특성들 중 사용할 것과 사용하지 않을 것들의 이름을 불러오기
with open(f'{_input_path}/_positive_importances.txt', 'r') as file:
    _positive_importances = eval(file.read())
with open(f'{_input_path}/_useless_feature_names.txt', 'r') as file:
    _useless_feature_names = eval(file.read())
with open(f'{_input_path}/_unimportant_feature_names.txt', 'r') as file:
    _unimportant_feature_names = eval(file.read())



def load_data(data_type):
    '''
    대회에서 공식적으로 제공된 데이터를 불러옵니다.
    '''
    dataset_path = f'{_input_path}/{data_type}_data'
    dfs = []
    for file_name in sorted(os.listdir(f'{dataset_path}/')):
        if not file_name.endswith('.csv'):
            continue
        df = pd.read_csv(f'{dataset_path}/{file_name}', parse_dates=['ymdhm'])
        dfs.append(df)
    return pd.concat(dfs, axis=0, ignore_index=True)


def load_extended_data():
    '''
    한강홍수통제소 및 바다누리 해양정보 서비스에서 OpenAPI로 추출한 데이터를 불러옵니다.
    '''
    wlobscds, rfobscds = _wlobscds, _rfobscds
    obs_post_ids = ['DT_0032', 'DT_0044']

    date = 20220822

    # 댐 정보 불러오기
    df_dm = pd.read_csv(
        f'{_input_path}/OpenAPI_merged/dm_{date}.csv',
        parse_dates=['ymdhm'],
        na_values=[' ', '##########'])

    # 수위 정보 불러오기
    df_wl = []
    for wlobscd in wlobscds:
        if f'wl_{wlobscd}' in _useless_feature_names + _unimportant_feature_names and f'fw_{wlobscd}' in _useless_feature_names + _unimportant_feature_names:
            continue
        df_wl.append(pd.read_csv(
            f'{_input_path}/OpenAPI_merged/wl_{wlobscd}_{date}.csv',
            na_values=[' ', '##########'])
        )
    df_wl = pd.concat(df_wl, axis=1).drop(columns=['ymdhm'])

    # 강수량 정보 불러오기
    df_rf = []
    for rfobscd in rfobscds:
        if f'rf_{rfobscd}' in _useless_feature_names + _unimportant_feature_names:
            continue
        df_rf.append(pd.read_csv(
            f'{_input_path}/OpenAPI_merged/rf_{rfobscd}_{date}.csv',
            na_values=[' ', '##########'])
        )
    df_rf = pd.concat(df_rf, axis=1).drop(columns=['ymdhm'])

    # 조위 정보 불러오기
    df_tide = []
    for obs_post_id in obs_post_ids:
        df = pd.read_csv(f'{_input_path}/OpenAPI_merged/tide_level_{obs_post_id}_{date}.csv', parse_dates=['ymdhm'])
        df = df.drop_duplicates()
        df = df.set_index('ymdhm', drop=True)
        # 조위 데이터는 불규칙하게 기록되어 있으므로 10분 간격의 기록으로 변환
        # 데이터 누출을 방지하기 위해 forward fill 방법을 사용
        df = df.reindex(df.index.ceil('10min').drop_duplicates(), method='ffill')
        df = df.reindex(pd.date_range(pd.Timestamp(2012, 1, 1), pd.Timestamp(2022, 7, 31, 23, 50), freq='10min'))
        df = df.reset_index(drop=True)
        df_tide.append(df)
    df_tide = pd.concat(df_tide, axis=1)

    # 불러온 데이터들 합치기
    df = pd.concat([df_dm, df_wl, df_tide, df_rf], axis=1)
    df = df.drop(columns=list(set(_useless_feature_names + _unimportant_feature_names) & set(df.columns)))
    for name in df.columns:
        if name == 'ymdhm':
            continue
        df[name] = df[name].astype(np.float32)
    return df


def cleanup(df):
    '''
    데이터의 오류를 보정합니다.
    '''
    time = df['ymdhm']

    # 강수량이 음수로 기록된 경우 0으로 바꿈
    for col_name in df.columns:
        if col_name.startswith('rf_'):
            df[col_name] = np.clip(df[col_name], 0, None)
    return df


def features_for_learning(df):
    '''
    불러온 데이터로부터 학습에 사용할 설명변수들을 추출합니다.
    '''
    removed_features = ['ymdhm', 'fw_1018680']
    usable_features = [name for name in df.columns if name not in removed_features]
    time = df['ymdhm']
    result = dict()
    # 변수들의 값으로부터 특성을 추출하면서 pd.Series.shift() 를 적용하는데,
    # 이는 특정 시점의 수위를 예측할 때 10분 전까지의 관측값만을 사용하도록 함
    for name in usable_features:
        for i in range(1, 6 + 1):
            # 여러 변수들의 값 자체 혹은 값 변화량의 10분 전, 20분 전, ... , 60분 전 값을 활용
            result[f'{name}_s{i}'] = df[name].shift(i)
            result[f'{name}_diff1_s{i}'] = df[name].diff(1).shift(i)
            result[f'{name}_diff2_s{i}'] = df[name].diff(2).shift(i)
        for i in [6, 12]:
            # 여러 변수들의 1시간/2시간 구간 내 통계량을 활용
            result[f'{name}_roll{i}_mean'] = df[name].rolling(i).agg('mean').shift(1)
            result[f'{name}_roll{i}_median'] = df[name].rolling(i).agg('median').shift(1)
            result[f'{name}_roll{i}_std'] = df[name].rolling(i).agg('std').shift(1)

    # 연도
    result['yr'] = time.dt.year

    # 조석 주기를 활용
    # [아래에 실수가 있으나] 12시간 25분 및 삭망월 29.53일을 사용
    elapsed_index = (time - time.iloc[0]).dt.total_seconds() // 600
    pi = np.pi
    _tide_period = 12 + 25 / 60
    _lunar_period = 29.53 * 24 / 2
    result['tide_period_cos'] = np.cos((2 * pi / _tide_period) * elapsed_index)
    result['tide_period_sin'] = np.sin((2 * pi / _tide_period) * elapsed_index)
    result['lunar_period_cos'] = np.cos((2 * pi / _lunar_period) * elapsed_index)
    result['lunar_period_sin'] = np.sin((2 * pi / _lunar_period) * elapsed_index)

    result = pd.DataFrame(result)[sorted(set(_positive_importances) & set(result.keys()))]
    for name in result.columns:
        result[name] = result[name].astype(np.float32)
    return result


def labels_for_learning(df):
    '''
    불러온 데이터로부터 학습에 사용할 반응변수들을 추출합니다.
    '''
    return df[['wl_1018662', 'wl_1018680', 'wl_1018683', 'wl_1019630']]


def submit(Y_pred):
    '''
    예측한 수치를 제출하기 위한 파일로 만듭니다.
    '''
    df = pd.read_csv(f'{_input_path}/sample_submission.csv')
    df['wl_1018662'] = Y_pred[:, 0]
    df['wl_1018680'] = Y_pred[:, 1]
    df['wl_1018683'] = Y_pred[:, 2]
    df['wl_1019630'] = Y_pred[:, 3]
    df.to_csv(f'./submission.csv', index=False)


#     df.to_csv(f'../output/submission.csv', index=False)

def competition_metric(Y_true, Y_pred):
    '''
    실제값과 예측값을 바탕으로 대회 평가 점수를 산출합니다.
    '''
    l2_mean = np.mean(np.square(Y_true - Y_pred), axis=0)
    r_sq = 1 - (l2_mean / np.var(Y_true, axis=0))
    if np.isnan(r_sq).any() or (r_sq <= 0).any():
        return 999.
    return np.mean(np.sqrt(l2_mean) / r_sq)


class MyLGBM():
    '''
    Light GBM으로 다변수 시계열 값을 예측하는 클래스로, scikit-learn식의 API를 참고하였습니다.
    '''

    def __init__(self, params):
        self.params = params

    def fit(self, X, Y):
        '''
        분류기를 훈련합니다.
        '''
        self.boosters = []
        for _, y in Y.iteritems():
            booster = lgbm.train(
                self.params,
                lgbm.Dataset(X, y),
            )
            self.boosters.append(booster)
        return self

    def predict(self, X):
        '''
        분류기를 통해 예측합니다.
        '''
        return np.stack([booster.predict(X) for booster in self.boosters], axis=1)


class Adapter():
    '''
    대회에서 제공된 데이터와 OpenAPI로 구한 데이터의 단위 차이를 보정하는 클래스
    '''

    def __init__(self):
        pass

    def fit(self, X, Y):
        self.xs, self.ys = [], []
        for i in range(X.shape[1]):
            x, y = X.iloc[:, i], Y.iloc[:, i]
            x, y = x[~x.duplicated()], y[~x.duplicated()]
            mask_notna = ~np.isnan(x) & ~np.isnan(y)
            x, y = x[mask_notna], y[mask_notna]
            self.xs.append(x.iloc[x.argsort()])
            self.ys.append(y.iloc[y.argsort()])
        return self

    def transform(self, X):
        result = np.empty_like(X)
        for i in range(X.shape[1]):
            result[:, i] = np.interp(X[:, i], self.xs[i], self.ys[i])
        return result


# OpenAPI로 추출한 방대한 데이터셋 로드
df = load_extended_data()

# 대회에서 제공된 데이터 로드
df_old = pd.merge(load_data('water'), load_data('rf'), on='ymdhm')
df_old = df_old.set_index('ymdhm', drop=True)
df_old = df_old.reindex(pd.date_range(pd.Timestamp(2012, 1, 1), pd.Timestamp(2022, 7, 31, 23, 50), freq='10min'))
df_old = df_old.reset_index().rename(columns={'index': 'ymdhm'})

# 데이터셋을 청소
df = cleanup(df)

# 학습에 사용할 특성들 추출
df_features = features_for_learning(df)

# 예측해야 할 4개 교량의 수위 데이터 추출
df_labels = labels_for_learning(df_old)

# 학습에 사용할 타겟 추출
df_interms = labels_for_learning(df)

# 제출과 무관하게 성능 시험을 위한 훈련 및 시험 데이터 구분
# 이하에서 *_train, *_test은 제출과 무관한 훈련 및 시험 데이터를 의미
mask_train = (df['ymdhm'] < pd.Timestamp(2021, 6, 1))
mask_test = (df['ymdhm'] >= pd.Timestamp(2021, 6, 1)) & (df['ymdhm'] < pd.Timestamp(2021, 7, 19))
# 제출을 위한 훈련 및 시험 데이터 구분
# 이하에서 *_train_final, *_test_final은 제출을 위한 훈련 및 시험 데이터를 의미
mask_train_final = (df['ymdhm'] < pd.Timestamp(2022, 6, 1))
mask_test_final = (df['ymdhm'] >= pd.Timestamp(2022, 6, 1)) & (df['ymdhm'] < pd.Timestamp(2022, 7, 19))

# X_*는 학습용 특성들, Y_*는 대회에서 제공한 타겟
# I_*는 OpenAPI로 추출한 타겟을 의미
# Y_*와 I_*는 같은 관측소의 자료라도 단위 탓인지 다른 값을 가짐
X_train, Y_train = df_features[mask_train], df_labels[mask_train]
X_test, Y_test = df_features[mask_test], df_labels[mask_test]

X_train_final, Y_train_final = df_features[mask_train_final], df_labels[mask_train_final]
X_test_final = df_features[mask_test_final]

I_train, I_test = df_interms[mask_train], df_interms[mask_test]
I_train_final = df_interms[mask_train_final]

# 분류기 MyLGBM에 사용할 하이퍼패러매터로, 래핑된 LightGBM의 하이퍼패러매터로 사용됨
params = {
    'max_depth': -1,
    'num_leaves': 48,
    'num_iterations': 364,
    'learning_rate': 9.641e-2,
    'force_row_wise': True,
    'random_state': 42,
    'deterministic': True,

    'verbosity': -1,
}

# I_*의 데이터 수가 Y_*의 데이터 수보다 많으므로,
# 우선 X_*로부터 I_*를 예측하는 모델 생성
model = MyLGBM(params)
model.fit(X_train, I_train)

# 이후 I_*로부터 Y_*로 단위를 변환하도록 함
adapter = Adapter().fit(I_train, Y_train)
I_recon, I_pred = model.predict(X_train), model.predict(X_test)
Y_recon, Y_pred = adapter.transform(I_recon), adapter.transform(I_pred)
print(competition_metric(Y_train, Y_recon))
print(competition_metric(Y_test, Y_pred))

# 0.8215447499112705
# 0.8001409238529582

# 스태킹: 앞에서 훈련한 분류기의 예측을 다시 특성으로 사용하여 두 번째 모델을 학습함
# 두 번째 모델에 사용할 특성들
_lower_features = []
for col_name in df_features.columns:
    use = False
    for name in df_old.columns:
        if name in col_name:
            use = True
    if use:
        _lower_features.append(col_name)

# 첫 번째 모델의 예측 결과를 특성에 포함시킴
XX_train = np.concatenate([X_train[_lower_features].values, Y_recon], axis=1)
XX_test = np.concatenate([X_test[_lower_features].values, Y_pred], axis=1)

# 두 번째 LightGBM 모델의 하이퍼패러매터
lower_params = {
    'max_depth': -1,
    'num_leaves': 48,
    'num_iterations': 234,
    'learning_rate': 8.66621e-3,
    'force_row_wise': True,
    'random_state': 42,
    'deterministic': True,

    'verbosity': -1,
}

# 두 번째 모델 훈련
lower_model = MyLGBM(lower_params)
lower_model.fit(XX_train, pd.DataFrame(Y_train.values - Y_recon))
print(competition_metric(Y_train, Y_recon + lower_model.predict(XX_train)))
print(competition_metric(Y_test, Y_pred + lower_model.predict(XX_test)))

# 0.8096651756348624
# 0.7966187467037728

# 앞의 과정들을 훈련 데이터 전체에 대하여 적용
# 즉, 2022년 6월 이전까지의 데이터를 사용해 훈련하여, 2022년 6월 1일부터 7월 18일까지의 값을 예측
model.fit(X_train_final, I_train_final)
adapter = Adapter().fit(I_train_final, Y_train_final)
Y_recon_final = adapter.transform(model.predict(X_train_final))
Y_pred_final = adapter.transform(model.predict(X_test_final))

XX_train_final = np.concatenate([X_train_final[_lower_features].values, Y_recon_final], axis=1)
XX_test_final = np.concatenate([X_test_final[_lower_features].values, Y_pred_final], axis=1)
lower_model.fit(XX_train_final, pd.DataFrame(Y_train_final.values - Y_recon_final))

# 작업 디렉토리에 'submission.csv'라는 이름으로 예측 결과를 생성함
submit(Y_pred_final + lower_model.predict(XX_test_final))

