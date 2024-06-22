import datetime
import json

from jsonrunner.result import _TestResult

# 定义用例类型
case_type = {
    0: "passed",
    1: "failure",
    2: "errors",
    3: "skipped"
}


class JSONTestRunner:
    """
    运行测试：生成JSON格式的测试结果
    """

    def __init__(self, output, verbosity=1):
        self.output = output
        self.verbosity = verbosity
        self.start_time = datetime.datetime.now()

    def run(self, test):
        """
        运行测试
        """
        result = _TestResult(self.verbosity)
        test(result)
        case_info = self.test_result(result)

        # 测试结果转JSON
        self.result_to_json(case_info)

        stop_time = datetime.datetime.now()
        print(f"Time Elapsed: {stop_time - self.start_time}")
        return result

    def test_result(self, result):
        """
        解析测试结果
        """
        class_list = []
        sorted_result = self.sort_result(result.result)
        for cid, (cls, cls_results) in enumerate(sorted_result):
            # 统计类下面用例数据
            passed = failure = errors = skipped = 0
            for n, t, e in cls_results:
                if n == 0:
                    passed += 1
                elif n == 1:
                    failure += 1
                elif n == 2:
                    errors += 1
                else:
                    skipped += 1

            # 格式化类的描述信息
            if cls.__module__ == "__main__":
                name = cls.__name__
            else:
                name = "%s.%s" % (cls.__module__, cls.__name__)
            doc = cls.__doc__ and cls.__doc__.split("\n")[0] or ""
            desc = doc and '%s' % doc or name

            cases = []
            for tid, (n, t, e) in enumerate(cls_results):
                case_info = self.generate_case_data(cid, tid, n, t, e)
                cases.append(case_info)

            class_list.append({
                "desc": desc,
                "count": passed + failure + errors + skipped,
                "pass": passed,
                "fail": failure,
                "error": errors,
                "skipped": skipped,
                "cases": cases
            })

        return class_list

    @staticmethod
    def sort_result(result_list):
        """
        unittest运行用例没有特定的顺序，
        这里将测试用例按照测试类分组
        """
        rmap = {}
        classes = []
        for n, t, e in result_list:
            cls = t.__class__
            if not cls in rmap:
                rmap[cls] = []
                classes.append(cls)
            rmap[cls].append((n, t, e))
        r = [(cls, rmap[cls]) for cls in classes]
        return r

    @staticmethod
    def generate_case_data(cid, tid, n, t, e):
        """
        生成测试用例数据
        """
        tid = (n == 0 and "p" or "f") + f"t{cid + 1}.{tid + 1}"
        name = t.id().split('.')[-1]
        doc = t.shortDescription() or ""

        case = {
            "number": tid,
            "name": name,
            "doc": doc,
            "result": case_type.get(n),
            "error": e
        }

        return case

    def result_to_json(self, result):
        """
        测试结果转JSON
        """
        with open(self.output, "w", encoding="utf-8") as f:
            json.dump(result, f)
