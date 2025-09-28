load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
    name = "hello_py",
    srcs = ["hello.py"],
    main = "hello.py",
)

py_test(
    name = "test_hello",
    srcs = ["test_hello.py"],
    deps = [":hello_py"],
)
