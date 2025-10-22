# run_cases.py  (루트)
import numpy as np
from numdiff import f_exp, df_exp, f_sin, df_sin, run_case

# 산출물을 루트의 /data, /figs 폴더에 저장
run_case(f_exp, df_exp, a=1.0, tag="exp_a1", out_dir_data="data", out_dir_figs="figs")
run_case(f_sin, df_sin, a=float(np.pi/4), tag="sin_api4", out_dir_data="data", out_dir_figs="figs")
