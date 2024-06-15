import random
import time

# Load proxies from a file
def load_proxies(file_path='proxies.txt'):
    with open(file_path, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

# Save the current proxy to a file
def save_current_proxy(proxy, file_path='current_proxy.txt'):
    with open(file_path, 'w') as file:
        file.write(proxy)

def rotate_proxy(proxies):
    return random.choice(proxies)

def main():
    proxies = load_proxies()
    while True:
        current_proxy = rotate_proxy(proxies)
        save_current_proxy(current_proxy)
        print(f"Current Proxy: {current_proxy}")
        time.sleep(60)  # Change proxy every 60 seconds

if __name__ == '__main__':
    main()
