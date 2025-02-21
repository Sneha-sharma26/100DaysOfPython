import multiprocessing
import requests

# def downloadFile(url, name):
#     print("started downloading")
#     response = requests.get(url)
#     open(f"file{name}.jpg", 'wb').write(response.content)
#     print("finished downloading")

# url = 'https://pixabay.com/photos/ice-curtain-icicle-ice-formations-16558/'
# # download the given image's link one by one
# for i in range(2):
#     downloadFile(url, i)   # this will download the given image's link one by one

# # using Multiprocessing  
# if __name__ == '__main__':
#     pros = []
#     for i in range(2):
#         downloadFile(url, i)   # this will download the given image's link one by one
#         # for multiprocessing
#         p = multiprocessing.Process(target=downloadFile, args=[url,i])
#         p.start()
#         pros.append(p)
    
#     for p in pros:
#         p.join()

        
#----------- Another way ----------#

# using ProcessPoolExecutor()
from concurrent.futures import ProcessPoolExecutor

def downloadFile(url, name):
    print("started downloading")
    response = requests.get(url)
    open(f"file{name}.jpg", 'wb').write(response.content)
    print("finished downloading")

url = 'https://pixabay.com/photos/ice-curtain-icicle-ice-formations-16558/'
if __name__ == '__main__':
    with ProcessPoolExecutor() as executor:
        l1 = [url for i in range(3)]
        l2 = [i for i in range(3)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)