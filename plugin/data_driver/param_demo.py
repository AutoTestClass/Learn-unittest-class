import inspect
import json
import warnings
from functools import wraps

import openpyxl
from parameterized.parameterized import default_doc_func
from parameterized.parameterized import default_name_func
from parameterized.parameterized import delete_patches_if_need
from parameterized.parameterized import parameterized
from parameterized.parameterized import reapply_patches_if_need
from parameterized.parameterized import skip_on_empty_helper

from .conversion import check_data


def read_json_file(file_path: str) -> list:
    """
    读取JSON文件
    :param file_path:
    :return:
    """
    with open(file_path, encoding="utf8") as f:
        data = json.load(f)
        print(data)

    return data


def read_excel_file(file_path: str, sheet_name=None, start_line: int = 1) -> list:
    """
    读取excel文件
    :param file_path:
    :param sheet_name:
    :param start_line:
    :return:
    """
    wb = openpyxl.load_workbook(file_path)
    if sheet_name is None:
        sheet_name = "Sheet1"

    try:
        # 获取指定的sheet标签页
        sheet = wb[sheet_name]

        # 读取数据sheet_name
        data_list = []
        for row in sheet.iter_rows(min_row=start_line, values_only=True):
            line = []
            for cell in row:
                line.append(cell)
            data_list.append(line)
    except KeyError:
        raise ValueError(f"Sheet '{sheet_name}' not found in the Excel file.")

    # 关闭Excel文件
    wb.close()

    return data_list


def file_data(file_path: str, sheet_name=None, start_line: int = 1):
    file_type = file_path.split(".")[-1]

    if file_type == "json":
        file_data = read_json_file(file_path)

    elif file_type == "xlsx":
        file_data = read_excel_file(file_path)

    else:
        raise TypeError("不支持文件类型")

    return data(file_data)


def data(input, name_func=None, doc_func=None, skip_on_empty=False,
         namespace=None, **legacy):
    """ A "brute force" method of parameterizing test cases. Creates new
        test cases and injects them into the namespace that the wrapped
        function is being defined in. Useful for parameterizing tests in
        subclasses of 'UnitTest', where Nose test generators don't work.

        :param input: An iterable of values to pass to the test function.
        :param name_func: A function that takes a single argument (the
            value from the input iterable) and returns a string to use as
            the name of the test case. If not provided, the name of the
            test case will be the name of the test function with the
            parameter value appended.
        :param doc_func: A function that takes a single argument (the
            value from the input iterable) and returns a string to use as
            the docstring of the test case. If not provided, the docstring
            of the test case will be the docstring of the test function.
        :param skip_on_empty: If True, the test will be skipped if the
            input iterable is empty. If False, a ValueError will be raised
            if the input iterable is empty.
        :param namespace: The namespace (dict-like) to inject the test cases
            into. If not provided, the namespace of the test function will
            be used.

        >>> @parameterized.expand([("foo", 1, 2)])
        ... def test_add1(name, input, expected):
        ...     actual = add1(input)
        ...     assert_equal(actual, expected)
        ...
        >>> locals()
        ... test_add1_foo_0: <function ...> ...
        >>>
        """

    input = check_data(input)

    if "testcase_func_name" in legacy:
        warnings.warn("testcase_func_name= is deprecated; use name_func=",
                      DeprecationWarning, stacklevel=2)
        if not name_func:
            name_func = legacy["testcase_func_name"]

    if "testcase_func_doc" in legacy:
        warnings.warn("testcase_func_doc= is deprecated; use doc_func=",
                      DeprecationWarning, stacklevel=2)
        if not doc_func:
            doc_func = legacy["testcase_func_doc"]

    doc_func = doc_func or default_doc_func
    name_func = name_func or default_name_func

    def parameterized_expand_wrapper(f, instance=None):
        frame_locals = namespace
        if frame_locals is None:
            frame_locals = inspect.currentframe().f_back.f_locals

        parameters = parameterized.input_as_callable(input)()

        if not parameters:
            if not skip_on_empty:
                raise ValueError(
                    "Parameters iterable is empty (hint: use "
                    "`parameterized.expand([], skip_on_empty=True)` to skip "
                    "this test when the input is empty)"
                )
            return wraps(f)(skip_on_empty_helper)

        digits = len(str(len(parameters) - 1))
        for num, p in enumerate(parameters):
            name = name_func(f, "{num:0>{digits}}".format(digits=digits, num=num), p)
            # If the original function has patches applied by 'mock.patch',
            # re-construct all patches on the just former decoration layer
            # of param_as_standalone_func so as not to share
            # patch objects between new functions
            nf = reapply_patches_if_need(f)
            frame_locals[name] = parameterized.param_as_standalone_func(p, nf, name)
            frame_locals[name].__doc__ = doc_func(f, num, p)

        # Delete original patches to prevent new function from evaluating
        # original patching object as well as re-constructed patches.
        delete_patches_if_need(f)

        f.__test__ = False

    return parameterized_expand_wrapper
