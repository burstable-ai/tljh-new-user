from setuptools import setup

setup(
    name="cb_new_user",
    entry_points={"tljh": ["new_user = cb_new_user"]},
    py_modules=["cb_new_user"],
)