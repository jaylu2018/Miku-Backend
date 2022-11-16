import locale
import paramiko


def datetime_fmt():
    locale.setlocale(locale.LC_CTYPE, 'zh_CN.UTF-8')
    return '%Y-%m-%d %H:%M:%S'


if __name__ == '__main__':
    private_key = paramiko.RSAKey.from_private_key_file(
        '/Users/luyh/PycharmProjects/djangoProject/Miku/utils/common/id_rsa')
    # 创建SSH对象
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # 连接服务器
    ssh.connect(hostname='192.168.40.7', port=22, username='luyh', password='lyh@0101!!')
    # 执行命令
    stdin, stdout, stderr = ssh.exec_command('df -h')
    res, err = stdout.read(), stderr.read()

    # 获取命令结果
    result = res if res else err
    print(result)
