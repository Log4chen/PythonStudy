在pytest框架中，有如下约束：
所有的单测文件名都需要满足test_*.py格式或*_test.py格式。

在单测文件中，测试类以Test开头，并且不能带有 init 方法(注意：定义class时，需要以T开头，不然pytest是不会去运行该class的)
在单测类中，可以包含一个或多个test_开头的函数。
此时，在执行pytest命令时，会自动从当前目录及子目录中寻找符合上述约束的测试函数来执行。