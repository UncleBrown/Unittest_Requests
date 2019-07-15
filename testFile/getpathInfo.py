#获取项目绝对路径
import os

def get_path():
    
    #获取当前文件路径
    #real_path=os.path.realpath(__file__)
    
    #获取当前文件所在绝对路径
    path = os.path.split(os.path.realpath(__file__))[0] #os.path.split将路径与文件名分开，返回列表
    return path

if __name__ == "__main__":
    #print(f"当前文件所在路径：{get_path()[0]}")
    print(f"当前文件所在目录：{get_path()}")