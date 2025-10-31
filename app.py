import streamlit as st
import uuid
import socket
import requests

st.set_page_config(page_title="VLESS/HY2 节点工具", layout="centered")

st.title("🌐 VLESS/HY2 节点工具")

# 1️⃣ 获取公网 IP
def get_public_ip():
    try:
        ip = requests.get("https://api.ipify.org").text
        return ip
    except:
        return "无法获取公网 IP"

public_ip = get_public_ip()
st.subheader("当前实例公网 IP:")
st.code(public_ip)

# 2️⃣ 检测 TCP 端口
def check_port(host, port):
    try:
        with socket.create_connection((host, port), timeout=2):
            return True
    except:
        return False

st.subheader("端口检测（示例 443）:")
port_status = check_port(public_ip, 443)
st.write(f"TCP 443: {'✅ 可用' if port_status else '❌ 不可用'}")

# 3️⃣ 自动生成随机 VLESS/HY2 节点
st.subheader("随机生成节点链接:")

def generate_vless(ip, port=443):
    node_uuid = str(uuid.uuid4())
    return f"vless://{node_uuid}@{ip}:{port}?encryption=none&security=tls&type=tcp#示例VLESS节点"

def generate_hy2(ip, port=443):
    node_uuid = str(uuid.uuid4())
    return f"hy2://{node_uuid}@{ip}:{port}#示例HY2节点"

vless_link = generate_vless(public_ip)
hy2_link = generate_hy2(public_ip)

st.code(vless_link, language="text")
st.code(hy2_link, language="text")
st.info("⚠️ 注意：这些节点仅演示格式，可用于导入 v2rayN，但 Koyeb 本身无法开放 TCP/UDP 端口。")
