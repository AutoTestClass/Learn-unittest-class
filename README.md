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
