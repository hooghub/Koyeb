import streamlit as st
import requests
import random
import socket

st.set_page_config(page_title="VLESS/HY2 节点工具", layout="centered")

st.title("🌐 VLESS / HY2 节点工具")

# 自动获取公网 IP
def get_public_ip():
    try:
        return requests.get("https://api.ipify.org").text
    except:
        return "获取失败"

ip = get_public_ip()
st.write(f"**公网 IP:** {ip}")

# 随机端口示例
port = random.randint(10000, 65000)
st.write(f"**端口:** {port}")

# 检测 TCP 端口是否开放
def check_port(ip, port):
    try:
        with socket.create_connection((ip, port), timeout=2):
            return "✅ 可用"
    except:
        return "❌ 不可用"

status = check_port(ip, port)
st.write(f"**端口状态:** {status}")

# 随机 UUID 生成 VLESS / HY2 链接
import uuid
node_uuid = str(uuid.uuid4())

vless_link = f"vless://{node_uuid}@{ip}:{port}?encryption=none&security=tls&type=tcp#示例VLESS节点"
hy2_link = f"hy2://{node_uuid}@{ip}:{port}#示例HY2节点"

st.write("**VLESS 链接:**")
st.code(vless_link, language="text")

st.write("**HY2 链接:**")
st.code(hy2_link, language="text")
