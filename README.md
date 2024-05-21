# Learn-unittest-class

* 课程大纲

![](/images/unittest.png)

## 前言

`unittest` 作为Python标准库中的单元测试框架，仍然可以满足我们的绝大部分单元测试相关工作，虽然，`pytest`
正在变得更加流行。 `unittest`仍未过时，或者到了要被抛弃的地步，很多时候我们觉得`unittest`
不是太好用，一方面是因为对它不是足够了解，另一方面它的生态（第三方扩展插件）比较糟糕。

本课程希望深入和全面的介绍 `unittest`的使用，以及教你如何开发 `unittest` 扩展插件，来满足单元测试/自动化测试相关工作。

## PyUnit、unittest 和 unittest2

* unitest 发展轨迹：

![](./images/histroy.png)

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

### django TestCase

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

👉 [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

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

#### unitest 命令使用

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

* `-c` / `--catch` : 测试运行期间按`Control + C` 会等待当前测试结束，然后报告到目前为止的所有结果。第二次按`Control + C`
  会引发正常的 KeyboardInterrupt 异常。

```bash
python -m unittest -c
```

* `-f`/ `--failfast`：在出现第一个错误或失败时停止测试运行。

```bash
 python -m unittest -f
```

* `-k`：只运行与模式或子字符串匹配的测试方法和类。可以多次使用此选项，这样所有与给定模式中的任何一个匹配的测试用例都会被包括进来。

例如，`-k foo` 会匹配`foo_tests.SomeTest.test_something`，`bar_tests.SomeTest.test_foo`
，但不会匹配`bar_tests.FooTest.test_something`。

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

### 断言方法

> unittest的断言方法非常丰富，除了简单的 相等、包含，还有 类型、异常、警告、日志的断言。

TestCase类提供了几种断言方法来检查并报告失败。以下表格列出了最常用的方法（更多断言方法请参见下表）：

| Method                      | Checks that          | New in |
|-----------------------------|----------------------|--------|
| `assertEqual(a, b)`         | a == b               |        |
| `assertNotEqual(a, b)`      | a != b               |        |
| `assertTrue(x)`             | bool(x) is True      |        |
| `assertFalse(x)`            | bool(x) is False     |        |
| `assertIs(a, b)`            | a is b               | 3.1    |
| `assertIsNot(a, b)`         | a is not b           | 3.1    |
| `assertIsNone(x)`           | x is None            | 3.1    |
| `assertIsNotNone(x)`        | x is not None        | 3.1    |
| `assertIn(a, b)`            | a in b               | 3.1    |
| `assertNotIn(a, b)`         | a not in b           | 3.1    |
| `assertIsInstance(a, b)`    | isinstance(a, b)     | 3.2    |
| `assertNotIsInstance(a, b)` | not isinstance(a, b) | 3.2    |

还可以使用以下方法检查异常、警告和日志消息的生成:

| Method                                          | Checks that                                                          | New in |
|-------------------------------------------------|----------------------------------------------------------------------|--------|
| `assertRaises(exc, fun, *args, **kwds)`         | `fun(*args, **kwds)` raises `exc`                                    |        |
| `assertRaisesRegex(exc, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises `exc` and the message matches regex `r`  | 3.1    |
| `assertWarns(warn, fun, *args, **kwds)`         | `fun(*args, **kwds)` raises `warn`                                   | 3.2    |
| `assertWarnsRegex(warn, r, fun, *args, **kwds)` | `fun(*args, **kwds)` raises `warn` and the message matches regex `r` | 3.2    |
| `assertLogs(logger, level)`                     | The `with` block logs on `logger` with minimum `level`               | 3.4    |
| `assertNoLogs(logger, level)`                   | The `with` block does not log on `logger` with minimum `level`       | 3.10   |

还有其他方法可以用来执行更具体的检查，比如：

| Method                       | Checks                                                                            | New in |
|------------------------------|-----------------------------------------------------------------------------------|--------|
| `assertAlmostEqual(a, b)`    | `round(a - b, 7) == 0`                                                            |        |
| `assertNotAlmostEqual(a, b)` | `round(a - b, 7) != 0`                                                            |        |
| `assertGreater(a, b)`        | `a > b`                                                                           | 3.1    |
| `assertGreaterEqual(a, b)`   | `a >= b`                                                                          | 3.1    |
| `assertLess(a, b)`           | `a < b`                                                                           | 3.1    |
| `assertLessEqual(a, b)`      | `a <= b`                                                                          | 3.1    |
| `assertRegex(s, r)`          | `r.search(s)`                                                                     | 3.1    |
| `assertNotRegex(s, r)`       | `not r.search(s)`                                                                 | 3.2    |
| `assertCountEqual(a, b)`     | `a` and `b` have the same elements in the same number, regardless of their order. | 3.2    |

__assertEqual()__

`assertEqual()` 自动使用的特定类型方法列表如下表所示。请注意，通常不需要直接调用这些方法。

| Method                        | Checks              | New in |
|-------------------------------|---------------------|--------|
| `assertMultiLineEqual(a, b)`	 | strings             | 3.1    |
| `assertSequenceEqual(a, b)`	  | sequences	          | 3.1    |
| `assertListEqual(a, b)`	      | lists	              | 3.1    |
| `assertTupleEqual(a, b)`	     | tuples	             | 3.1    |
| `assertSetEqual(a, b)`	       | sets or frozensets	 | 3.1    |
| `assertDictEqual(a, b)`	      | dicts	              | 3.1    |

### Fixtrue

Fixtures的概念前面有过简单的介绍，我们可以形象地把它看作夹心饼干外层的两片饼干，这两片饼干就是setUp/tearDown，中间的奶油就是测试用例。

![](/images/test_fixture.png)

类和模块级别的固定装置是在`TestSuite`中实现的。当测试套件遇到来自新类的测试时，会调用上一个类的`tearDownClass()`
（如果有的话），然后调用新类的`setUpClass()`。

类似地，如果一个测试来自前一个测试的不同模块，则会运行前一个模块的`tearDownModule`，然后运行新模块的`setUpModule`。

__setUp and tearDown__

* `setUp`

准备测试装置的方法。这个方法会在调用测试方法之前立即被调用；除了AssertionError或SkipTest之外，此方法引发的任何异常都将被视为错误而不是测试失败。默认实现什么也不做。

* `tearDwon`

测试方法被调用并记录结果后立即调用的方法。即使测试方法引发异常，也会调用此方法，因此子类中的实现可能需要特别小心地检查内部状态。此方法将仅在setUp()
成功时调用，而不管测试方法的结果如何。默认实现不执行任何操作。

```python
import unittest


class Test(unittest.TestCase):

    def setUp(self) -> None:
        print("before")

    def test_case(self):
        print("this is case")

    def tearDown(self) -> None:
        print("after")


if __name__ == '__main__':
    unittest.main()
```

__setUpClass and tearDownClass__

这些必须被实现为类方法。

```python
import unittest


class SomeWork():

    def init_env(self):
        print("初始化环境")

    def clear_env(self):
        print("清理环境配置")


class Test(unittest.TestCase):
    some_work = None

    @classmethod
    def setUpClass(cls):
        cls.some_work = SomeWork()
        cls.some_work.init_env()

    def test_case(self):
        print("this is case")

    @classmethod
    def tearDownClass(cls):
        cls.some_work.clear_env()


if __name__ == '__main__':
    unittest.main()
```

__setUpModule and tearDownModule__

这些应该作为函数来实现。

```python
import unittest


def setUpModule():
    print("all module case before")


def tearDownModule():
    print("all module case after")


class Test(unittest.TestCase):

    def test_case(self):
        print("this is case")


if __name__ == '__main__':
    unittest.main()
```

### Skipping test and expected failure

#### 基本使用

unittest支持跳过单个测试方法甚至整个测试类。此外，它还支持将测试标记为“预期失败”，即一个有问题并将失败的测试，但不应计入TestResult的失败。

* `unittest.skip(reason)`

无条件地跳过装饰的测试，需要说明跳过测试的原因。

* `unittest.skipIf(condition, reason)`

如果条件为真，则跳过装饰的测试。

* `unittest.skipUnless(condition, reason)`

当条件为真时，执行装饰的测试。

* `unittest.expectedFailure()`

不管执行结果是否失败，都将测试标记为失败。

__基本的跳过示例__

```python
import sys
import unittest

__version__ = 0


def element_is_exists() -> bool:
    """
    element is exists
    :return: 
    """
    return False


class MyTestCase(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(__version__ < 3, "not supported in this library version")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if element_is_exists():
            self.skipTest("external resource not available")
        # test code that depends on the external resource
        pass
```

__跳过测试类__

```python
import unittest


@unittest.skip("showing class skipping")
class MySkippedTestCase(unittest.TestCase):
    def test_not_run(self):
        pass
```

__预期用例失败__

```python
import unittest


class ExpectedFailureTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
```

跳过的测试不会运行`setUp()`或`tearDown()`。跳过的类不会运行`setUpClass()`或`tearDownClass()`
。跳过的模块不会运行`setUpModule()`或`tearDownModule()`。

#### 自己封装skip

制作自己的跳过装饰器很容易，只需制作一个在希望跳过测试时调用skip()的装饰器即可。这个装饰器会跳过测试，除非传递的对象具有特定属性。

```python
import unittest


def skipUnlessHasattr(obj, attr):
    """
    自定义 skipUnlessHasattr 装饰器
    :param obj:
    :param attr:
    :return:
    """
    if hasattr(obj, attr):
        return lambda func: func
    return unittest.skip("{!r} doesn't have {!r}".format(obj, attr))


#
class ExampleClass:
    """
    示例类，包含一些属性
    """

    def __init__(self):
        self.some_attribute = 'value'


class MyTestCase(unittest.TestCase):

    @skipUnlessHasattr(ExampleClass(), 'some_attribute')
    def test_with_attribute(self):
        self.assertTrue(True)

    @skipUnlessHasattr(ExampleClass(), 'missing_attribute')
    def test_without_attribute(self):
        self.assertTrue(True)


# 运行测试
if __name__ == '__main__':
    unittest.main()
```

### 测试发现 discover

`discover()`是unittest非常重要的一个方法，用于实现测试发现。

```python
import unittest

unittest.defaultTestLoader.discover(start_dir, pattern='test*.py', top_level_dir=None)
```

__参数说明__

* `test_dir`: 指定测试目录。
* `pattern`: 指定查找用例的规则。
* `top_level_dir`: 指定项目顶层目录。

从指定的起始目录递归查找所有测试模块，返回一个包含它们的TestSuite对象。只会加载与模式匹配的测试文件（使用类似shell的模式匹配）。只有可导入的模块名称（即有效的Python标识符）才会被加载。

__所有测试模块必须从项目的顶层可导入。如果起始目录不是顶层目录，则必须单独指定`top_level_dir`。__

如果导入模块失败，例如由于语法错误，则这将被记录为单个错误，发现将继续。如果导入失败是因为引发了SkipTest，则将其记录为跳过而不是错误。

如果发现一个包（包含一个名为__init__.py的文件的目录），将检查该包是否有load_tests函数。如果存在，则将调用package.load_tests(
loader, tests, pattern)。测试发现会确保在调用期间只检查一次包是否包含测试，即使load_tests函数本身调用loader.discover。

如果load_tests存在，则发现不会递归进入该包，load_tests负责加载包中的所有测试。

模式故意不存储为loader属性，以便包可以继续自行发现。

top_level_dir被内部存储，并用作对discover()的任何嵌套调用的默认值。也就是说，如果一个包的load_tests调用loader.discover()
，则不需要传递此参数。

start_dir可以是一个点分隔的模块名称，也可以是一个目录。

#### 为什么要设置 top_level_dir ?

假设你的项目结构如下：

```
my_project/
├── top_level_dir/
│   ├── __init__.py
│   ├── main_module.py
│   └── tests/
│       ├── __init__.py
│       ├── test_module1.py
│       └── test_module2.py
└── run_tests.py
```

1. 顶层目录是 `top_level_dir`:

main_module.py 和 tests 文件夹位于 top_level_dir 中。测试文件 test_module1.py 和 test_module2.py 位于 top_level_dir/tests
中。

2. 导入路径设置：

要从项目的顶层导入 test_module1 和 test_module2，它们的路径将是 top_level_dir.tests.test_module1 和
top_level_dir.tests.test_module2。

__使用 discover 方法__

如果你在 run_tests.py 中运行测试，并且 run_tests.py 位于 my_project 目录下，则需要指定 top_level_dir，因为 start_dir
并不是项目的顶层目录。

```python
import unittest

if __name__ == '__main__':
    # 指定测试开始的目录为 `top_level_dir/tests`
    start_dir = 'top_level_dir/tests'
    # 指定顶层目录为 `top_level_dir`
    top_level_dir = 'top_level_dir'

    loader = unittest.TestLoader()
    suite = loader.discover(start_dir=start_dir, pattern='test*.py', top_level_dir=top_level_dir)

    runner = unittest.TextTestRunner()
    runner.run(suite)
```

在这个例子中：

start_dir 是 `top_level_dir/tests`，它不是项目的顶层目录。因此，我们必须指定 top_level_dir 为 `top_level_dir`。这样，unittest
会正确地将 top_level_dir 作为项目的顶层目录，然后在 top_level_dir/tests 目录中查找匹配 pattern='test*.py' 的测试模块。

__当你不指定 top_level_dir 时，unittest 会尝试从 start_dir 的父目录开始导入模块。如果 start_dir
不是项目的顶层目录，就会导致模块导入错误。例如，它可能会找不到 top_level_dir.tests.test_module1，因为它没有在正确的路径下查找。__
