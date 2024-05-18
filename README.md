# Learn-unittest-class

## 前言

`unittest` 作为Python标准库中的单元测试框架，仍然可以满足我们的绝大部分单元测试相关工作，虽然，`pytest`
正在变得更加流行。 `unittest`仍未过时，或者到了要被抛弃的地步，很多时候我们觉得`unittest`
不是太好用，一方面是因为对它不是足够了解，另一方面它的生态（第三方扩展插件）比较糟糕。

本课程希望深入和全面的介绍 `unittest`的使用，以及教你如何开发 `unittest` 扩展插件，来满足单元测试/自动化测试相关工作。

## PyUnit、unittest 和 unittest2

* unitest 发展轨迹：

`PyUnit` -> `unittest` -> `unittest2` -> `unittest`（now）

### PyUnit

PyUnit是最早的Python单元测试框架，其灵感来源于JUnit（Java中的一个单元测试框架）。 由Steve
Purcell开发，并成为Python社区的一个非官方标准。PyUnit 不再作为一个独立的框架存在。它的功能和设计思想已经完全融入了 unittest
模块。

### unittest

unittest是Python标准库中的单元测试框架，实际上是对PyUnit的标准化和集成。在`Python 2.1`
中首次引入，作为标准库的一部分，以后Python的每个版本都内置了unittest。
它提供了丰富的测试功能，包括测试用例（TestCase）、测试套件（TestSuite）、测试加载器（TestLoader）、测试运行器（TestRunner）和各种断言方法。

__主要变化和改进__

* 组织结构：unittest模块的结构更加清晰，便于扩展和使用。

* 改进的断言方法：unittest引入了更多的断言方法，如assertEqual、assertTrue等，方便测试编写。

* 测试发现：支持自动发现测试用例的机制，使得测试组织更加灵活。

* 测试夹具（Fixture）：支持setUp和tearDown方法，用于在测试前后进行初始化和清理工作。

### unittest2

unittest2是unittest的增强版，主要用于提供在较旧版本Python中引入的unittest功能。其目标是为还没有升级到新版本Python的用户提供最新的unittest功能。在`Python 2.7`
和`Python 3.2`中，unittest模块进行了重大改进和增强，这些改进也被包含在unittest2中。

__主要变化和改进__

* 改进的测试发现机制：更加智能和灵活的测试用例发现功能。

* 更强大的断言方法：添加了更多断言方法，比如assertIs、assertIsNone、assertIn等。

* 基于类的setUpClass和tearDownClass方法：用于在整个测试类开始前和结束后执行一些初始化和清理工作。

* 基于方法的setUpModule和tearDownModule方法：用于在整个测试模块开始前和结束后执行一些初始化和清理工作。

* 测试跳过和预期失败：引入了@unittest.skip装饰器和相关功能，用于标记跳过的测试和预期会失败的测试。

### 总结

* PyUnit 是早期的单元测试框架，启发了后来的unittest。

* unittest 是Python标准库中的单元测试框架，基于PyUnit，提供了更丰富和标准化的测试功能。

* unittest2 是unittest的增强版，主要为了提供在较旧版本Python中引入新功能的支持，但随着Python 2.7和Python
  3.2之后的版本逐渐成为主流，unittest2的使用也逐渐减少。

因此，PyUnit、unittest和unittest2基本上是同一个框架的不同演进阶段，而unittest成为了现在Python标准库中的正式单元测试框架。

## unittest 优势

* `标准库集成`：unittest 是 Python 标准库的一部分，安装 Python 时默认可用，不需要额外安装。

* `面向对象的设计`：通过继承 `unittest.TestCase` 组织测试代码，结构清晰，便于扩展和维护。

* `丰富的断言方法`：提供了多种断言方法，方便进行各种类型的测试检查。

## 有哪些库基于unittest

### django `TestCase`

Django 提供的 TestCase 类继承自 unittest.TestCase，并进行了扩展以支持 Django 应用的测试。

```python
from django.test import TestCase


class IndexPageTest(TestCase):
    """
    测试index登录首页
    """

    def test_index_page_renders_index_template(self):
        """
        断言是否用给定的index.html模版响应
        :return:
        """
        response = self.client.get('/index/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
```

* 优势：内置对 Django ORM、视图和模板的支持，可以方便地测试 Django 应用的各个方面。

### Flask-Testing

```python
from urllib import request
from flask import Flask
from flask_testing import LiveServerTestCase


class MyTest(LiveServerTestCase):

    def create_app(self):
        app = Flask(__name__)
        app.config['TESTING'] = True
        # Default port is 5000
        app.config['LIVESERVER_PORT'] = 8943
        # Default timeout is 5 seconds
        app.config['LIVESERVER_TIMEOUT'] = 10
        return app

    def test_server_is_up_and_running(self):
        response = request.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)

```

* 优势：提供了对 Flask 应用的全面测试支持，包括视图测试和上下文管理。

### Testify

Testify 是由 Yelp 开发的一个测试框架，旨在替代 unittest，提供更强大的功能。

```python
from testify import *


class AdditionTestCase(TestCase):

    @class_setup
    def init_the_variable(self):
        self.variable = 0

    @setup
    def increment_the_variable(self):
        self.variable += 1

    def test_the_variable(self):
        assert_equal(self.variable, 1)

    @suite('disabled', reason='ticket #123, not equal to 2 places')
    def test_broken(self):
        # raises 'AssertionError: 1 !~= 1.01'
        assert_almost_equal(1, 1.01, threshold=2)

    @teardown
    def decrement_the_variable(self):
        self.variable -= 1

    @class_teardown
    def get_rid_of_the_variable(self):
        self.variable = None


if __name__ == "__main__":
    run()
```

* 优势：提供了更直观的测试 API 和强大的测试功能，如分布式测试和并行执行。

### nose2

nose2 是 nose 的继任者，旨在提供一个扩展性强、易于使用的测试框架。 nose2将unittest扩展，使测试更加方便。

```python
import unittest
from nose2.tools import params


class TestStrings(unittest.TestCase):
    def test_upper(self):
        self.assertEqual("spam".upper(), "SPAM")


@params("Sir Bedevere", "Miss Islington", "Duck")
def test_is_knight(value):
    assert value.startswith('Sir')
```

* 优势：提供了自动化发现和运行测试用例的功能，支持丰富的插件和扩展。

* 运行

```shell
> nose2 -v
```

### Seldom

seldom 是基于unittest 的自动化测试框架。

````python
import seldom


class YouTest(seldom.TestCase):

    def test_case(self):
        """a simple test case """
        self.assertEqual(1 + 1, 2)


if __name__ == '__main__':
    seldom.main()
````

* 优势：seldom是一个全功能测试框架，支持 Web/App/API测试等。

## unittest 基础

unittest官方文档： https://docs.python.org/3/library/unittest.html

在unittest文档中有四个重要的概念： Test Case、Test Suite、Test Runner和Test Fixture。只有理解了这几个概念，才能理解单元测试的基本特征。

* Test Case

Test Case是最小的测试单元，用于检查特定输入集合的特定返回值。unittest提供了`TestCase`基类，我们创建的测试类需要继承该基类，它可以用来创建新的测试用例。

* Test Suite

测试套件是测试用例、测试套件或两者的集合，用于组装一组要运行的测试。unittest提供了`TestSuite`类来创建测试套件。

* Test Runner

Test Runner是一个组件，用于协调测试的执行并向用户提供结果。Test
Runner可以使用图形界面、文本界面或返回特殊值来展示执行测试的结果。unittest提供了`TextTestRunner`类运行测试用例。

* Test Fixture

Test
Fixture代表执行一个或多个测试所需的环境准备，以及关联的清理动作。例如，创建临时或代理数据库、目录，或启动服务器进程。unittest中提供了`setUp()`/`tearDown()`、`setUpClass()`/`tearDownClass()`
等方法来完成这些操作。

### 第一个测试用例

* 计算器

实现一个`Calculator` 计算器类，`add()` 方法用于参数的加法计算。

```python
# calculator.py

class Calculator:
    """
    计算器
    """

    def __init__(self, *args):
        self.args = args

    def add(self):
        """
        加法运算
        """
        return sum(self.args)
```

* 测试计算器

通过`unittest` 编写`Calculator`类的测试用例。

```python
# test_calculator.py
import unittest

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    # 用例前置动作
    def setUp(self):
        print("test start")

    # 用例后置动作
    def tearDown(self):
        print("test end")

    def test_add_one(self):
        c = Calculator(2)
        result = c.add()
        self.assertEqual(result, 2)

    def test_add_two(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)

    def test_add_three(self):
        c = Calculator(3, 5)
        result = c.add()
        self.assertEqual(result, 8)


if __name__ == '__main__':
    # 创建测试套件
    suit = unittest.TestSuite()
    suit.addTest(TestCalculator("test_add_one"))
    suit.addTest(TestCalculator("test_add_two"))
    suit.addTest(TestCalculator("test_add_three"))

    # 创建测试运行器
    runner = unittest.TextTestRunner()
    runner.run(suit)
```

* 运行测试

```bash
python test_calculator.py

test start
test end
.test start
test end
.test start
test end
.
----------------------------------------------------------------------
Ran 3 tests in 0.001s

OK
```


### 命令行工具

####  unitest 命令使用

unittest模块可以从命令行中使用，来运行来自模块、类甚至单个测试方法的测试。

```bash
python -m unittest test_module1 test_module2
python -m unittest test_module.TestClass
python -m unittest test_module.TestClass.test_method
```
> `python -m` 以脚本形式运行库模块.

可以传入包含任何组合模块名称和完全限定的类或方法名称的列表。

测试模块也可以通过文件路径指定：

```bash
python -m unittest tests/test_something.py
```

这样可以让你使用shell文件名自动补全来指定测试模块。指定的文件仍然必须可以作为一个模块进行导入。路径会被转换成模块名，去掉‘.py’并将路径分隔符转换为‘.’。

通过传入`-v` 选项 来运行更详细的测试:

```bash
python -m unittest -v test_module
```

当不带参数执行时，会启用`Test Discovery`（后面会介绍 `discovery()` 方法）:

```bash
python -m unittest
```


### unitest 命令选项

获取所有命令行选项的列表:

```bash
python -m unittest -h

usage: python.exe -m unittest [-h] [-v] [-q] [--locals] [-f] [-c] [-b] [-k TESTNAMEPATTERNS] [tests ...]

positional arguments:
  tests                a list of any number of test modules, classes and test methods.

options:
  -h, --help           show this help message and exit
  -v, --verbose        Verbose output
  -q, --quiet          Quiet output
  --locals             Show local variables in tracebacks
  -f, --failfast       Stop on first fail or error
  -c, --catch          Catch Ctrl-C and display results so far
  -b, --buffer         Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS  Only run tests which match the given substring

Examples:
  python.exe -m unittest test_module               - run tests from test_module
  python.exe -m unittest module.TestClass          - run tests from module.TestClass
  python.exe -m unittest module.Class.test_method  - run specified test method
  python.exe -m unittest path/to/test_file.py      - run tests from test_file.py

usage: python.exe -m unittest discover [-h] [-v] [-q] [--locals] [-f] [-c] [-b] [-k TESTNAMEPATTERNS] [-s START]
                                       [-p PATTERN] [-t TOP]

options:
  -h, --help            show this help message and exit
  -v, --verbose         Verbose output
  -q, --quiet           Quiet output
  --locals              Show local variables in tracebacks
  -f, --failfast        Stop on first fail or error
  -c, --catch           Catch Ctrl-C and display results so far
  -b, --buffer          Buffer stdout and stderr during tests
  -k TESTNAMEPATTERNS   Only run tests which match the given substring
  -s START, --start-directory START
                        Directory to start discovery ('.' default)
  -p PATTERN, --pattern PATTERN
                        Pattern to match tests ('test*.py' default)
  -t TOP, --top-level-directory TOP
                        Top level directory of project (defaults to start directory)

For test discovery all test modules must be importable from the top level directory of the project.
```

__重要选项说明__

* `-b` / `--buffer` : 测试运行期间，标准输出和标准错误流会被缓冲。通过测试时的输出会被丢弃，测试失败或出错时，输出会被正常回显，并添加到失败消息中。

```bash
python -m unittest -b
```

* `-c` / `--catch` : 测试运行期间按`Control + C` 会等待当前测试结束，然后报告到目前为止的所有结果。第二次按`Control + C` 会引发正常的 KeyboardInterrupt 异常。

```bash
python -m unittest -c
```

* `-f`/ `--failfast`：在出现第一个错误或失败时停止测试运行。

```bash
 python -m unittest -f
```

* `-k`：只运行与模式或子字符串匹配的测试方法和类。可以多次使用此选项，这样所有与给定模式中的任何一个匹配的测试用例都会被包括进来。

例如，`-k foo` 会匹配`foo_tests.SomeTest.test_something`，`bar_tests.SomeTest.test_foo`，但不会匹配`bar_tests.FooTest.test_something`。

```bash
python -m unittest -k cal
```

* `--durations N` 显示N个最慢的测试用例（N=0表示全部）(python 3.12 新增)。

```bash
python -m unittest --durations 2
```

* `-v`，`--verbose` : 详细的输出。

```bash
python -m unittest -v
```

__测试发现__

Unittest支持简单的测试查找。为了与测试查找兼容，所有的测试文件必须是从项目的顶级目录中导入的模块或包（这意味着它们的文件名必须是有效的标识符）。

测试发现在`TestLoader.discover()`中实现，但也可以从命令行使用。基本的命令行用法是:

发现子命令有以下选项：

* `-s`，`--start-directory`： 开始查找的目录（默认为`.`）

* `-p`，`--pattern` 匹配测试文件的模式（默认为`test*.py`）

* `-t`，`--top-level-directory`: 项目的顶层目录（默认为开始目录）

`-s`，`-p`和`-t`选项可以按照这个顺序作为位置参数传入。以下两个命令行是等效的：

```bash
python -m unittest discover -s project_directory  -p "*_test.py"
python -m unittest discover project_directory  "*_test.py"
```

除了作为路径外，还可以传入包名作为开始目录，例如`myproject.subpackage.test`。提供的包名将被导入，其在文件系统上的位置将被用作开始目录。
