#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import numpy as np
import pandas as pd
import logging

class Common(object):
    """
    ############# method 설명 ###############
    # get_dir_list
    #    - 하위 디렉토리 중 in, out 둘 다 포함하는 디렉토리 list 반환
    #    - 수정 방향: 원하는 디렉토리 list를 input으로 받도록 수정.  
    # load_csv
    #    - csv 파일 로드
    #    - mode: dataframe으로 로드할건지, numpy로 로드할건지 
    # 
    #########################################

    """





    def __init__(self, blank = "", logger_name = ""):
        self.blank = blank
        self.logger_name = logger_name
        self.write_log


    def get_dir_list(self, rootdir):
        """
        # 기능 : in, out 하위 폴더를 포함하는 디렉토리 list 반환
        # input
        #   rootdir : root directory
        # output
        #   dirs : 해당경로에 있는 directory 목록
        """
        for root, dirs, files in os.walk(rootdir):
            if '__pycache__' in dirs:
                dirs.remove('__pycache__')

        # 폴더에 "in", "out" 폴더 있는지 검사. 없으면 에러
        list_dir = []
        for entry in os.listdir(rootdir):
            # file이면 skip
            if os.path.isfile(os.path.join(rootdir, entry)):
                continue
            
            # 하위에 in, out 폴더가 없으면 skip
            filelist_subfoler = os.listdir(os.path.join(rootdir, entry))
            if (not "in" in filelist_subfoler) or (not "out" in filelist_subfoler):
                continue
            
            # in, out 둘중 하나라도 폴더가 아니어도 skip
            if os.path.isfile(os.path.join(rootdir, entry, "in")) or os.path.isfile(os.path.join(rootdir, entry, "out")):
                continue
            
            list_dir.append(os.path.join(rootdir, entry))

        return list_dir

    


    def load_csv(self, path, mode = 0):
        """
        path: csv path
        mode: dataframe 혹은 numpy array
        """
        csv_df = pd.read_csv(path)
        if 1 == mode:
            csv_df = csv_df.values
        return csv_df 


    def write_log(self, msg = "", mode = "i"):
        """
        Log 생성 함수
        - msg: message
        - mode
            . "w" or "W": warning
            . "e" or "E": error
            . etc: 자동으로 "i"로 세팅          
        """

        # 로그 생성
        logger = logging.getLogger(self.logger_name)

        # 로그의 출력 기준 설정
        logger.setLevel(logging.INFO)

        # log 출력 형식
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # log 출력
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # log를 파일에 출력
        file_handler = logging.FileHandler('C:\\Users\\jaewoong29.kim\\Desktop\\Log_python.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        
        if "w" == mode or "W" == mode:
            logger.warn(msg)
        elif "e" == mode or "E" == mode:
            logger.error(msg)
        else:
            logger.info(msg)
        