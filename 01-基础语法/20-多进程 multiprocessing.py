import multiprocessing


# 定义一个计算阶乘的函数
def calculate_factorial(number):
    print(f"Process {number}: Calculating factorial of {number}")
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print(f"Process {number}: The factorial of {number} is {factorial}")
    return factorial, number


if __name__ == '__main__':
    # 创建一个进程列表
    processes = []

    # 创建并启动多个进程
    for i in range(1, 5):  # 计算数字1到4的阶乘
        process = multiprocessing.Process(target=calculate_factorial, args=(i,))
        processes.append(process)
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()

    print("All processes have finished.")


    # 创建一个进程池
    with multiprocessing.Pool(multiprocessing.cpu_count() - 1) as pool:  # 可以指定进程数，默认为CPU核心数
        # 创建一个要计算的数字列表
        numbers = list(range(1, 5))  # 计算数字1到4的阶乘

        # 使用pool.map来分配任务到进程池
        results = pool.map(calculate_factorial, numbers)

        # 打印结果
        for result in results:
            factorial, number = result
            print(f"The factorial of {number} is {factorial}")

    print("All pool processes have finished.")
