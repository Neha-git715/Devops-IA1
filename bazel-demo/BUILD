load("@rules_python//python:defs.bzl", "py_binary", "py_test")

py_binary(
    name = "hello_py",
    srcs = ["hello.py"],
    main = "hello.py",
)

py_test(
    name = "hello_test",
    srcs = ["test_hello.py"],
    deps = [":hello_py"],  # test depends on your binary
)
