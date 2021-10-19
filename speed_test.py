# speed test using Python

import speedtest

s= speedtest.Speedtest()

download= s.download()
upload = s.upload()

download_mbps = round(download/10**6,2)
upload_mbps= round(upload/10**6,2)

print(f"Download speed is: {download_mbps} Mbps")
print(f"Upload speed is: {upload_mbps} Mbps")
