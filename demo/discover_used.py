import unittest

if __name__ == '__main__':
    # 指定测试开始的目录为 `top_level_dir/tests`
    start_dir = 'top_level_dir/tests'
    # 指定顶层目录为 `top_level_dir`
    top_level_dir = 'top_level_dir'

    suite = unittest.defaultTestLoader.discover(
        start_dir=start_dir,
        pattern='test*.py',
        top_level_dir=top_level_dir
    )

    runner = unittest.TextTestRunner()
    runner.run(suite)
