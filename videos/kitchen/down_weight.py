from huggingface_hub import hf_hub_download
import os
os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"

# 在这里填入你的 Token
my_token = "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" 

print("开始下载私有模型...")
hf_hub_download(
    repo_id="Alexhe101/WanxDepth", 
    filename="cktp_new.safetensors", 
    local_dir=".", 
    local_dir_use_symlinks=False,
    token=my_token  # <--- 关键是这一行
)

print("下载完成！")