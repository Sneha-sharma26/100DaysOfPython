## asyncio => Asynchronous IO
import time 

# # 1. the below code will take 3 sec each to run each function & we cann't perform another func before the execution ends
def func1():
    time.sleep(3)
    print('func1')
    
def func2():
    time.sleep(3)
    print('func2')
    
func1()
func2()

# # 2. To run these func concurrently
import asyncio
import requests

async def func1():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.canva.com%2Fdesktop-wallpapers%2Ftemplates%2Fcute%2F&psig=AOvVaw1RtSGYpoxODaYCtqd6Z0IQ&ust=1740162998171000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJDzpOTy0osDFQAAAAAdAAAAABAJ"
    response = requests.get(url)
    open("picture1.jpg", 'wb').write(response.content)
    print('func1')
    
async def func2():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.canva.com%2Fdesktop-wallpapers%2Ftemplates%2Fcute%2F&psig=AOvVaw1RtSGYpoxODaYCtqd6Z0IQ&ust=1740162998171000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJDzpOTy0osDFQAAAAAdAAAAABAJ"
    response = requests.get(url)
    open("picture2.jpg", 'wb').write(response.content)
    print('func2')
    
async def func3():
    url = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.canva.com%2Fdesktop-wallpapers%2Ftemplates%2Fcute%2F&psig=AOvVaw1RtSGYpoxODaYCtqd6Z0IQ&ust=1740162998171000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJDzpOTy0osDFQAAAAAdAAAAABAJ"
    response = requests.get(url)
    open("picture3.jpg", 'wb').write(response.content)
    print('func1')

async def main():  
    L = await asyncio.gather(
        func1(),
        func2(),
        func3()
    )
    print(L)
asyncio.run(main())  # this is downloading the image (ek sath)