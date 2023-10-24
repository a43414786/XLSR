import os
import glob
from PIL import Image


class buildDataset():
    def __init__(self,datasetName,src_path,SR_rate) -> None:
        
        target_hr_root = os.path.join(datasetName,datasetName + '_HR')
        target_lr_root = os.path.join(datasetName,datasetName + '_LR', f'X{SR_rate}')
        
        if(os.path.exists(datasetName)):
            os.remove(datasetName)
        os.makedirs(target_hr_root)
        os.makedirs(target_lr_root)
        
        image_paths = glob.glob(os.path.join(src_path, '*.png'))
        image_names = os.listdir(src_path)
        if(os.path.exists(src_path + f'x{SR_rate}')):
            pass
        for idx in range(len(image_paths)):
            img_path = image_paths[idx]
            hr_name = image_names[idx]
            lr_name = image_names[idx][:-4] + f'x{SR_rate}.png'
            
            HR = Image.open(img_path)
            LR = HR.resize((HR.size[0]//SR_rate, HR.size[1]//SR_rate), Image.BICUBIC)  
            LR_w, LR_h = LR.size
            HR_w, HR_h = HR.size
            if(LR_w * SR_rate != HR_w or LR_h * SR_rate != HR_h):
                HR = HR.resize((LR_w * SR_rate,LR_h * SR_rate,), Image.BICUBIC)  
                
            
            HR.save(os.path.join(target_hr_root,hr_name))
            LR.save(os.path.join(target_lr_root,lr_name))
            
            print(idx,end='\r')
     
if __name__ == '__main__':
    src_path = r'C:\Users\dic\Desktop\YS-Huang\Research\XCAT\dataset\valid'
    bd = buildDataset('DIV2K_valid',src_path=src_path,SR_rate=2)
    