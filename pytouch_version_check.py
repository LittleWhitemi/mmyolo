import torch
print(torch.__version__)  #注意是双下划线
print(torch.cuda.is_available())
# cuda是否可用；

print(torch.cuda.device_count())
# 返回gpu数量；

print(torch.cuda.get_device_name(0))
# 返回gpu名字，设备索引默认从0开始；

print(torch.cuda.current_device())
# 返回当前设备索引；