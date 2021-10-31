import futures3
import requests
import time


out = []
CONNECTIONS = 100
TIMEOUT = 5
PARALLEL_REQUESTS = 5
TOTAL_REQUEST_BATCHES = 1000
FREQUENCY = 5

host_name = "http://predictionservicealb-987756931.eu-central-1.elb.amazonaws.com:80/predict"
data = "[[5.7, 2.5, 5.0, 2.0], [1.7, 4.0, 5.0, 1.0]]"


def load_url(url, timeout):
    ans = requests.get(url, timeout=timeout, json=data)
    return ans.json()


for i in range(TOTAL_REQUEST_BATCHES):
    print("Request no.", i)

    time.sleep(1/FREQUENCY)

    with futures3.ThreadPoolExecutor(max_workers=CONNECTIONS) as executor:
        future_to_url = (executor.submit(load_url, host_name, TIMEOUT) for run in range(PARALLEL_REQUESTS))

        for future in futures3.as_completed(future_to_url):
            try:
                data = future.result()
            except Exception as exc:
                data = str(type(exc))
            finally:
                out.append(data)

                print(str(len(out)), end="\r")

    print(out)
