# src/run_cases.py
import numpy as np
from numdiff import f_exp, df_exp, f_sin, df_sin, run_case

# 산출물을 저장소 루트의 /data, /figs에 만들고 싶으면 아래처럼 지정
run_case(f_exp, df_exp, a=1.0,               tag="exp_a1",
         out_dir_data="../data", out_dir_figs="../figs")
run_case(f_sin, df_sin, a=float(np.pi/4.0),  tag="sin_api4",
         out_dir_data="../data", out_dir_figs="../figs")
