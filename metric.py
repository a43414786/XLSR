#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 03:55:47 2021

@author: changxin
"""

import torch
from torch import Tensor

class PSNR(torch.nn.MSELoss):
    def __init__(self,max = 1.) -> None:
        super().__init__()
        self.max = max
    
    def forward(self, input: Tensor, target: Tensor) -> Tensor:
        mse = super().forward(input, target)
        if(mse == 0):return 100
        return 20 * torch.log10(self.max /  torch.sqrt(mse))

class RGB2YCbCr(torch.nn.Module):
    def __init__(self) -> None:
        super().__init__()
    def forward(self, input: Tensor) -> Tensor:
        if(len(input.shape) == 3):
            return input[0] * 0.257 + input[1] * 0.504 + input[2] * 0.098 + (1/16)
        if(len(input.shape) == 4):
            return input[0,0] * 0.257 + input[0,1] * 0.504 + input[0,2] * 0.098 + (1/16)

def cal_psnr(x, y):
    '''
    Parameters
    ----------
    x, y are two tensors has the same shape (1, C, H, W)

    Returns
    -------
    score : PSNR.
    '''
    x = RGB2YCbCr()(x).unsqueeze(0).unsqueeze(0)
    y = RGB2YCbCr()(y).unsqueeze(0).unsqueeze(0)
    mse = torch.mean((x - y) ** 2, dim=[1, 2, 3])
    score = - 10 * torch.log10(mse)
    return score