class SourceCodeGenerator:
    def generate(self, test_result):
        test_targets = {}
        for testcase_result in test_result.testcase_results:
            if not testcase_result.is_passed:
                test_target = testcase_result.name.split(".")[0]
                if test_target not in test_targets:
                    test_targets[test_target] = []
                test_targets[test_target] += [testcase_result]
        for test_target in test_targets:
            testcase_results = test_targets[test_target]
            failed_testcase_prompt = [testcase_result.code + "\n" + testcase_result.stdout for testcase_result in testcase_results]
            return failed_testcase_prompt

        return test_targets